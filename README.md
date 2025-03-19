## Spotify Replay Playlist Generator

This Python project allows users to generate a personalized Spotify playlist based on their most played tracks. The program fetches the top tracks from the user's Spotify account, creates a new playlist, and adds the selected tracks. It also provides a visual representation of the popularity of these tracks and displays album art for each of them in an aesthetically pleasing Tkinter window.

# Features
- **Spotify Authentication**: The program authenticates with Spotify using OAuth and accesses the user's top tracks.
- **Playlist Generation**: The program allows the user to create a playlist of their most played songs and adds them automatically to a new playlist.
- **Visualization**: The program creates a bar chart to visually represent the popularity of the user's top tracks.
- **Album Art Display**: The program fetches and displays the album art for the top tracks in a Tkinter window, adjusting the layout based on the number of tracks.
- **Custom Playlist Length**: Users can specify the number of tracks they want in their playlist through a simple graphical user interface (GUI) prompt.

# Requirements
- Python 3.6+
- Spotipy library (for Spotify API access)
- Matplotlib (for visualizing track popularity)
- Tkinter (for the GUI prompt and album art display)
- Pillow (for handling and displaying album art)

You can install the required dependencies using the following command:
```bash
pip install spotipy matplotlib pillow
```
# Setup
## Spotify Developer Application:
To use the Spotify API, you need to create a Spotify Developer Application and get your Client ID and Client Secret.
Visit Spotify Developer Dashboard to create an application and get the necessary credentials.

## Authentication:
Replace the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI with your own credentials in the script.

# Run the Script:
Once the dependencies are installed and the credentials are set up, run the script:
```bash
python main.py
```
The script will prompt you to log in to your Spotify account in the browser, and it will use the redirected token to fetch your top tracks.

# How It Works
User Prompt: The program will ask you to specify how many tracks you want in your playlist through a Tkinter-based GUI.
Fetching Top Tracks: The program fetches the user's top tracks using Spotify's Web API, limited to the specified number of tracks.
Playlist Creation: The program creates a new playlist for the user and adds the selected tracks to it.
Track Popularity Chart: The program generates a bar chart displaying the popularity of each track.
Album Art Display: The program fetches and displays the album artwork for each track in a Tkinter window, arranging them in a grid layout based on the number of tracks.

# Screenshots
## Playlist Length Prompt:

## Top Tracks Popularity Chart:

## Album Art Display:

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
This project uses the Spotipy library for accessing Spotify's API.
Album art is fetched via requests and displayed using the Pillow library.
Matplotlib is used to create the bar chart visualizing the track popularity.
Contributing
Feel free to fork the repository, make improvements, and submit pull requests. If you encounter any issues or have suggestions for new features, please create an issue on GitHub.

Enjoy your personalized Spotify playlist and visual experience!
