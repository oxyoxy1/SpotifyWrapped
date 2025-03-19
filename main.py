import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import requests
from PIL import Image, ImageTk
import io
import math

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Spotify API credentials
CLIENT_ID = "b9153b4c3cf34932b67c7ddc94c59d29"
CLIENT_SECRET = "c1ed8e3d77984db992b4686d98790d04"
REDIRECT_URI = "http://127.0.0.1:8888/callback/"

# Scopes required for reading user data and creating/modifying playlists
SCOPE = "user-library-read user-top-read playlist-modify-public playlist-modify-private"

# Authenticate with Spotify
logger.info("Authenticating with Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))
logger.info("Authentication successful.")

# Get the current user's ID
user_id = sp.current_user()["id"]
logger.debug(f"Fetched current user ID: {user_id}")

# Tkinter: Create a window to prompt the user for the playlist length
def prompt_user_for_playlist_length():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    playlist_length = simpledialog.askinteger("Playlist Length", "How many tracks would you like in your playlist?", minvalue=1, maxvalue=50)
    root.destroy()  # Close the window after input
    return playlist_length

# Prompt user for playlist length using the GUI
playlist_length = prompt_user_for_playlist_length()
if not playlist_length:
    logger.error("No valid input for playlist length.")
    exit()

# Fetch top tracks (limited to the desired length)
logger.info(f"Fetching top {playlist_length} tracks...")
top_tracks = sp.current_user_top_tracks(limit=playlist_length, time_range="short_term")
logger.debug(f"Top tracks response: {top_tracks}")

if not top_tracks['items']:
    logger.warning("No top tracks found. Try listening to more music on Spotify.")
    exit()

# Create a new playlist
playlist_name = "My Replay"
playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
logger.info(f"Created playlist: {playlist_name}")

# Get track URIs from top tracks (using URIs instead of IDs)
track_uris = [track["uri"] for track in top_tracks["items"]]

# Log track URIs for debugging
logger.debug(f"Track URIs: {track_uris}")

# Add the selected top tracks to the playlist
logger.info(f"Adding {len(track_uris)} top tracks to the playlist...")
sp.playlist_add_items(playlist["id"], track_uris)
logger.info(f"Added {len(track_uris)} top tracks to the playlist.")

# Visualizer: Display the track names and popularity as a bar chart
track_names = [track["name"] for track in top_tracks["items"]]
track_popularity = [track["popularity"] for track in top_tracks["items"]]  # Popularity is from 0 to 100

# Create a bar chart with improved styling
plt.figure(figsize=(10, 6))
plt.barh(track_names, track_popularity, color='skyblue')
plt.xlabel('Popularity')
plt.title('Top Tracks by Popularity')
plt.tight_layout()  # Ensure everything fits nicely
plt.show()

# Display album artwork in a Tkinter window
def display_album_art(top_tracks):
    root = tk.Tk()
    root.title("Top Tracks Album Art")

    # Calculate the number of rows and columns for the grid layout
    columns = 5  # Set a fixed number of columns
    rows = math.ceil(len(top_tracks['items']) / columns)  # Adjust rows based on number of items

    for idx, track in enumerate(top_tracks['items']):
        # Fetch the image URL for the album art
        album_image_url = track['album']['images'][0]['url']
        
        # Fetch the image using requests
        response = requests.get(album_image_url)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        
        # Scale the image size based on the number of tracks
        img_size = 150 if playlist_length <= 10 else 100  # Adjust the image size dynamically
        img = img.resize((img_size, img_size), Image.Resampling.LANCZOS)  # Resize the image for display
        
        # Convert image to Tkinter-compatible format
        img_tk = ImageTk.PhotoImage(img)

        # Create a label to display the image
        label = tk.Label(root, image=img_tk)
        label.image = img_tk  # Keep a reference to the image to prevent garbage collection
        
        # Place the image in the grid
        label.grid(row=idx // columns, column=idx % columns, padx=10, pady=10)

    root.mainloop()

# Call the function to display album art
display_album_art(top_tracks)

# Print Playlist Link
logger.info(f"Your personalized playlist is ready! Listen here: {playlist['external_urls']['spotify']}")
