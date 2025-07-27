import streamlit as st
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# import all techguard_pages
from techguard_pages.add_track import page_add_track
from techguard_pages.focus_session import page_focus_session
from techguard_pages.track_history import page_track_history
from techguard_pages.motivation_room import page_motivation_room

# import utilities
from utils.schedule_utils import load_all_tracks, get_upcoming_tracks
from utils.popup_reminder import render_focus_popup

# app configuration
st.set_page_config(page_title="TrackGuard", page_icon="🎯", layout="centered")

# initialize session state defaults
if "page" not in st.session_state:
    st.session_state.page = "➕ Add New Track"

if "selected_track_index" not in st.session_state:
    st.session_state.selected_track_index = 0

if "show_popup" not in st.session_state:
    st.session_state.show_popup = True

# Load user tracks
tracks = load_all_tracks()
upcoming_tracks = get_upcoming_tracks(tracks)

# Show focus session popup reminder if focus time is near
if upcoming_tracks and st.session_state.show_popup:
    render_focus_popup(tracks, upcoming_tracks)

# Sidebar Navigation
st.sidebar.title("🛍️ Navigation")
page = st.sidebar.radio("Go to", ["➕ Add New Track", "🎯 Focus Session", "📋 Track History", "💬 Motivation Room"],
                         index=["➕ Add New Track", "🎯 Focus Session", "📋 Track History", "💬 Motivation Room"].index(st.session_state.page))
st.session_state.page = page


# Main page rendering
if st.session_state.page == "➕ Add New Track":
    page_add_track()
elif st.session_state.page == "🎯 Focus Session":
    page_focus_session()
elif st.session_state.page == "📋 Track History":
    page_track_history()
elif st.session_state.page == "💬 Motivation Room":
    page_motivation_room()
