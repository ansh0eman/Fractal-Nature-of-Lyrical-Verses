# -*- coding: utf-8 -*-
"""Lyrics_Extraction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nCSwLLVLxI3in0Djj-XwUmptQRxiaGUi
"""

GENIUS_API_TOKEN='aMk3NwEa55ORwS_dlsYrV7HlNrZzegtdxSHj11Bo6_RlqEeCYLXgC0U2aiV0kCgP'

import lyricsgenius
import pandas as pd
import re

# Replace 'your_access_token_here' with your Genius API token
genius = lyricsgenius.Genius(GENIUS_API_TOKEN, timeout=5, retries=3)

# Define the artist's name
artist_name = input("Input artist you want lyrics for: ")  # Replace with the artist you want

# Function to clean the lyrics
def clean_lyrics(lyrics):
    # Remove unwanted sections
    lyrics = re.sub(r'^\d+ ContributorsTranslations.*? Lyrics', '', lyrics, flags=re.DOTALL)
    lyrics = re.sub(r'\d+Embed$', '', lyrics, flags=re.DOTALL)
    lyrics = re.sub(r'\[.*?\]', '', lyrics)  # Remove content in brackets (e.g., [Verse 1])
    lyrics = lyrics.strip()
    return lyrics

max_songs = int(input("Enter max numbers of songs: "))

# Get the artist object
artist = genius.search_artist(artist_name, max_songs=max_songs)  # You can increase max_songs as needed

# Initialize a list to hold the song data
songs_data = []

# Loop through each song by the artist
for song in artist.songs:
    song_title = song.title
    song_lyrics = clean_lyrics(song.lyrics)

    # Append song data to the list
    songs_data.append([artist_name, song_title, song_lyrics])

# Create a DataFrame from the collected data
df = pd.DataFrame(songs_data, columns=['Artist', 'Song', 'Lyrics'])

# Apply the cleaning function to all rows in the 'Lyrics' column
df['Lyrics'] = df['Lyrics'].apply(clean_lyrics)

pd.set_option('display.max_rows', None)

df.head()

# Save the DataFrame to a CSV file
csv_filename = f"{artist_name.replace(' ', '_')}_lyrics.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"Lyrics saved successfully to {csv_filename}.")

