from utils.schedule_utils import load_all_tracks
import streamlit as st
from utils.progress_utils import get_today_progress, get_streak
import json


def page_track_history():
    st.title("📋 Track History")
    tracks = load_all_tracks()

    if not tracks:
        st.warning("⚠️ No tracks found.")
        return

    if "track_to_delete_index" in st.session_state:
        del_index = st.session_state.track_to_delete_index
        if 0 <= del_index < len(tracks):
            deleted_track = tracks[del_index]
            deleted_id = deleted_track.get("id")

            if deleted_id:
                keys_to_remove = [key for key in st.session_state.keys() if deleted_id in key]
                for key in keys_to_remove:
                    del st.session_state[key]

            tracks.pop(del_index)
            with open("data/tracks.json", "w") as f:
                json.dump(tracks, f, indent=2)

            st.success("✅ Track deleted successfully.")

        del st.session_state.track_to_delete_index
        st.rerun()

    for i, track in enumerate(tracks):
        st.markdown(f"**Track:** {track['track']}")
        st.markdown(f"**Dream:** {track['dream']}")
        st.markdown(f"**Time:** {track['time']} | ⏳ {track['duration']} minutes")

        today_done = get_today_progress(track["id"])
        total_target = int(track["duration"])
        percent = int((today_done / total_target) * 100) if total_target else 0

        st.progress(min(percent, 100))
        st.markdown(f"**📅 Today:** {today_done} / {total_target} minutes")

        streak = get_streak(track["id"])
        st.markdown(f"🔥 **Streak:** {streak} day(s)")

        col1, _ = st.columns([1, 4])
        with col1:
            if st.button("🗑️ Delete", key=f"del_{i}"):
                st.session_state.track_to_delete_index = i
                st.rerun()

        st.markdown("---")
