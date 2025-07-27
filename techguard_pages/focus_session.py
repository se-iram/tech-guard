import streamlit as st
from utils.schedule_utils import load_all_tracks
import time
from utils.progress_utils import log_session
from utils.motivation import get_quote


def page_focus_session():
    tracks = load_all_tracks()

    if not tracks:
        st.warning("⚠️ No tracks found. Please add one first.")
        return

    st.title("🎯 Focus Session")
    track_names = [f"{t['track']} — {t['dream']}" for t in tracks]

    if st.session_state.get("selected_track_index", 0) >= len(track_names):
        st.session_state.selected_track_index = 0

    selected = st.selectbox(
        "Select a track", track_names, index=st.session_state.selected_track_index
    )
    st.session_state.selected_track_index = track_names.index(selected)

    active = tracks[st.session_state.selected_track_index]

    st.markdown(f"### 🧠 Track: {active['track']}")
    st.markdown(f"💭 **Dream:** {active['dream']}")
    st.markdown(f"🕒 **Daily Time:** {active['time']}")
    st.markdown(f"📚 **Duration:** {active['duration']} minute(s)")

    track_id = active["id"]
    timer_key = f"timer_{track_id}"
    start_key = f"start_time_{track_id}"
    total_key = f"total_seconds_{track_id}"

    if timer_key not in st.session_state:
        st.session_state[timer_key] = False

    if st.session_state[timer_key] and all(
        k in st.session_state for k in [start_key, total_key]
    ):
        elapsed_time = int(time.time() - st.session_state[start_key])
        remaining_time = st.session_state[total_key] - elapsed_time

        if remaining_time > 0:
            hours, rem = divmod(remaining_time, 3600)
            minutes, seconds = divmod(rem, 60)
            st.markdown(f"### ⏳ `{hours:02}:{minutes:02}:{seconds:02}`")
            time.sleep(1)
            st.rerun()
        elif elapsed_time < st.session_state[total_key] + 2:
            st.session_state[timer_key] = False
            st.success("🎉 Focus session complete!")
            st.balloons()

            completed_minutes = int(active['duration'])
            log_session(active["id"], completed_minutes)

            quote = get_quote(active["track"])
            st.markdown(f"💡 *{quote}*")
        else:
            st.session_state[timer_key] = False
    else:
        if st.button("▶️ Start Focus Timer"):
            st.session_state[timer_key] = True
            st.session_state[start_key] = time.time()
            st.session_state[total_key] = int(active['duration']) * 60
            st.rerun()
