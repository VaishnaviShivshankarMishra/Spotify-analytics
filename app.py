import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Spotify Analytics", layout="wide")
st.title("🎵 Spotify 2023 Analytics")

# Connect to database
conn = sqlite3.connect("spotify.db")

# Queries
top_artists = pd.read_sql("""
    SELECT artists_name, COUNT(*) as track_count
    FROM tracks
    GROUP BY artists_name
    ORDER BY track_count DESC
    LIMIT 10
""", conn)

avg_danceability = pd.read_sql("""
    SELECT released_year, AVG(danceability_percent) AS avg_danceability
    FROM tracks
    GROUP BY released_year
    ORDER BY released_year
""", conn)

conn.close()

# Display
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Top Artists")
    st.dataframe(top_artists)

with col2:
    st.subheader("💃 Average Danceability")
    st.dataframe(avg_danceability)
