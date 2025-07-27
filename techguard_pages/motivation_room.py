import streamlit as st
from utils.motivation_gemini import get_motivation_reply
from utils.motivation_voice import play_voice


def page_motivation_room():
    st.title("🧘 Motivation Room")
    st.markdown("### ✨ Welcome to your calming space")
    st.markdown("Take a deep breath. This is your time to reflect, recharge, and remember why you started. 💖")
    st.markdown("---")

    st.markdown("✍️ **Why did you start this journey?**\nReflect below:")
    user_input = st.text_area("", placeholder="Write here…")

    if st.button("📤 Share with Mentor"):
        if user_input:
            with st.spinner("Connecting with your mentor..."):
                voice_text, exercise_text = get_motivation_reply(user_input)

                # 🎧 Play voice message
                play_voice(voice_text)

            # ✅ Visually appealing mini-exercise
            if exercise_text:
                exercise_steps = [step.strip("•*- ") for step in exercise_text.split("\n") if step.strip()]
                styled_steps = "<br>".join([f"✅ {step}" for step in exercise_steps])

                st.markdown(
                    f"""
                    <div style="
                        background-color: #eafaf1;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
                        font-size: 17px;
                        color: #1b4332;">
                        🧘‍♀️ <strong>Mini Exercise:</strong><br><br>
                        {styled_steps}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
