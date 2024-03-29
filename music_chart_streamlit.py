import pandas as pd 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
sns.set_style('dark')
music_data = pd.read_csv('spotify-2023.csv', encoding='latin1')
music_data_df = pd.DataFrame(music_data) 
key1 = 'unique_key_1'
key2 = 'unique_key_2'
key3 = 'unique_key_3'
key4 = 'unique_key_4'

st.set_page_config(layout="wide", page_title="2023 Music Insights - Streaming Platforms", page_icon=":musical_note:")
# Title and Description
st.title(':notes: 2023 Music Insights - Streaming Platforms')
st.markdown(
    """
    Explore the top songs across various music platforms throughout 2023! :headphones:
    
    Get insights into the most streamed tracks on **Spotify, Apple Music, Shazam, and Deezer.**

    Discover rankings, top artists, and the latest music trends from leading platforms, all in one place!
    """
)
#Most Listening song
def cr_most_listening_sort():
    most_listening_sort = music_data_df.sort_values(by='streams', ascending=False)
    most_listening_sort['rank'] = range(1, len(most_listening_sort) + 1)
    column_to_display = ['rank','track_name','artist(s)_name','streams']
    return most_listening_sort[column_to_display].head(10).reset_index(drop=True)

st.title('Most Listening Songs in 2023 :musical_note:')
result_most_listening = cr_most_listening_sort()
st.dataframe(result_most_listening, use_container_width=True)

#Top Artist(s)
def cr_top_artists():
    top_artists = music_data_df.groupby('artist(s)_name')['streams'].sum().reset_index()
    top_artists = top_artists.sort_values(by='streams', ascending=False)
    top_artists['rank'] = range(1, len(top_artists) + 1)
    columns_to_display = ['rank','artist(s)_name', 'streams']
    return top_artists[columns_to_display].head(10).reset_index(drop=True)

st.title('Top Artist in 2023 :microphone:')
result_top_artists= cr_top_artists()
st.dataframe(result_top_artists, use_container_width=True)
#Most listening song by platform
def get_platform_logo(platform):
    logos = {
        'Spotify': 'https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg',
        'Apple': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Apple_Music_logo.png',
        'Deezer': 'https://upload.wikimedia.org/wikipedia/commons/d/db/Deezer_logo.svg',
        'Shazam': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Shazam_logo.svg'
        # Add logo URLs for each platform
    }
    return logos.get(platform, '')

def cr_most_listening_platform(data, platform):
    data_filtered = data[data[f'in_{platform.lower()}_charts'] != 0]
    most_listening_sort = data_filtered.sort_values(by=f'in_{platform.lower()}_charts', ascending=True)
    most_listening_sort['rank'] = range(1, len(most_listening_sort) + 1)
    columns_to_display = ['rank', 'track_name', 'artist(s)_name']
    return most_listening_sort[columns_to_display].head(10).reset_index(drop=True)

st.title('Most Listening Songs by Platform in 2023 :iphone:')
platform_choice = st.selectbox('Choose Platform', ['Spotify', 'Apple', 'Deezer', 'Shazam'], key=key1)
if platform_choice:
    result = cr_most_listening_platform(music_data_df, platform_choice)    
    platform_logo = get_platform_logo(platform_choice)
    st.image(platform_logo, caption=platform_choice, width=100)
    st.dataframe(result, use_container_width=True)

#Top Artist(s) by platform
def cr_top_artists_platform(data, platform):
    data_filtered = data[data[f'in_{platform.lower()}_charts'] != 0]
    top_artists = data_filtered.groupby('artist(s)_name')[f'in_{platform.lower()}_charts'].sum().reset_index()
    top_artists = top_artists.sort_values(by=f'in_{platform.lower()}_charts', ascending=False)
    top_artists['rank'] = range(1, len(top_artists) + 1)
    columns_to_display = ['rank','artist(s)_name']
    return top_artists[columns_to_display].head(10).reset_index(drop=True)

st.title('Top Artist by Platform in 2023 :iphone:')
platform_choice = st.selectbox('Choose Platform', ['Spotify', 'Apple', 'Deezer', 'Shazam'], key=key2)
if platform_choice:
    result = cr_top_artists_platform(music_data_df, platform_choice)    
    platform_logo = get_platform_logo(platform_choice)
    st.image(platform_logo, caption=platform_choice, width=100)
    st.dataframe(result, use_container_width=True)

#Most Listening songs by released year
def cr_music_data_filter(year):
    filtered_data = music_data_df[music_data_df['released_year'] == year]
    most_listening_sort = filtered_data.sort_values(by='streams', ascending=False)
    most_listening_sort['rank'] = range(1, len(most_listening_sort) + 1)
    columns_to_display = ['rank','track_name', 'artist(s)_name', 'streams']
    return most_listening_sort[columns_to_display].head(10).reset_index(drop=True)

st.title('Most listening song by released year in 2023 :calendar:')
unique_years = sorted(music_data_df['released_year'].unique(), reverse=True)
selected_year = st.selectbox('Choose Year', unique_years, key=key3)
result_most_listening_byyear = cr_music_data_filter(selected_year)
st.dataframe(result_most_listening_byyear, use_container_width=True)

#Top artists by released year
def cr_music_data_filter(year):
    filtered_data = music_data_df[music_data_df['released_year'] == year]
    most_listening_year = filtered_data.groupby(['released_year','artist(s)_name'])['streams'].sum().reset_index()
    most_listening_year = most_listening_year.sort_values(by='streams', ascending=False)
    most_listening_year['rank'] = range(1, len(most_listening_year) + 1)
    columns_to_display = ['rank', 'artist(s)_name', 'streams']
    return most_listening_year[columns_to_display].head(10).reset_index(drop=True)

st.title('Top Artists by Year of Song Release in 2023 :calendar:')
unique_years = sorted(music_data_df['released_year'].unique(), reverse=True)
selected_year = st.selectbox('Choose Year', unique_years, key=key4)
result_top_artists_year = cr_music_data_filter(selected_year)
st.dataframe(result_top_artists_year, use_container_width=True)

st.write("---")
st.write("©Anasvbbas ")
