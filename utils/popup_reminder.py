import streamlit as st

def render_focus_popup(tracks, upcoming_tracks):
    st.markdown("""
        <style>
        .popup-box {
            position: relative;
            background-color: #f9f9f9;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .popup-close {
            position: absolute;
            top: 10px;
            right: 20px;
            color: red;
            font-weight: bold;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="popup-box">', unsafe_allow_html=True)
    st.markdown("### 🔔 It's your focus time!")
    options = [f"{t['track']} — {t['dream']}" for t in upcoming_tracks]
    selected = st.selectbox("Choose a track to focus now:", options, key="popup_select")
    selected_index = options.index(selected)

    if st.button("🖐️ Go to Focus Session", key="popup_go"):
        track_to_focus = upcoming_tracks[selected_index]
        for idx, t in enumerate(tracks):
            if t["track"] == track_to_focus["track"]:
                st.session_state.selected_track_index = idx
                st.session_state.page = "🎯 Focus Session"
                st.session_state.show_popup = False
                st.rerun()

    if st.button("❌ Close", key="popup_close"):
        st.session_state.show_popup = False
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
