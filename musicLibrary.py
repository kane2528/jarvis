import webbrowser

# Dictionary of songs
music = {
    "skyfall": "https://www.youtube.com/watch?v=H6ven_YN_nI",
    "bye-bye": "https://www.youtube.com/watch?v=salLotdGa88"
}

def openYouTubeHome():
    """Open YouTube homepage in the default web browser"""
    webbrowser.open("https://www.youtube.com/")
    print("Opening YouTube homepage")
    
def playYouTubeSong(song_name):
    """Play a specific song from YouTube"""
    url = music.get(song_name.lower())
    if url:
        webbrowser.open(url)
        print(f"Playing '{song_name}' from {url}")
    else:
        print(f"Song '{song_name}' not found.")
        print("Sorry, I don't have that song in my library.")

def stopMusic():
    """Stopping music isn't applicable when using a web browser to play YouTube"""
    print("Stopping music is not applicable for web browser playback")
