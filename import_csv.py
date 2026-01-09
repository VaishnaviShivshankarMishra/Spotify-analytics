import sqlite3
import pandas as pd

try:
    df = pd.read_csv(
        "data/spotify-2023.csv",
        encoding="latin1",
        on_bad_lines="skip"
    )
except Exception as e:
    print("Error loading CSV:", e)
    exit(1)

# Rename columns
df = df.rename(columns={
    "artist(s)_name": "artists_name",
    "danceability_%": "danceability_percent",
    "valence_%": "valence_percent",
    "energy_%": "energy_percent",
    "acousticness_%": "acousticness_percent",
    "instrumentalness_%": "instrumentalness_percent",
    "liveness_%": "liveness_percent",
    "speechiness_%": "speechiness_percent"
})

# Save to SQLite
conn = sqlite3.connect("spotify.db")
df.to_sql("tracks", conn, if_exists="replace", index=False)
conn.close()

print("✅ CSV imported successfully with Latin-1 encoding")
