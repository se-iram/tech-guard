import streamlit as st
from utils.schedule_utils import save_schedule


def page_add_track():
    st.title("📝 Add a New Focus Track")
    st.subheader("Start tracking your dream with daily focus!")

    track = st.text_input("🧠 What's your focus area? (e.g., DSA, Networking)", key="input_track")
    dream = st.text_input("🌟 What's your dream for this track?", key="input_dream")
    focus_time = st.time_input("⏰ What time do you want to study daily?", key="input_time")
    duration_minutes = st.slider("⏳ Session duration (in minutes)", min_value=1, max_value=360, value=60)
    duration = round(duration_minutes / 60, 2)
    if st.button("📏 Save My Track"):
        if track and dream:
            save_schedule(track, dream, str(focus_time), duration)
            st.success("✅ Track saved!")
            st.session_state.page = "🎯 Focus Session"
            st.rerun()
        else:
            st.warning("⚠️ Please complete all fields before saving.")
