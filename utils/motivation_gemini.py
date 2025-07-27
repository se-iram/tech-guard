import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_motivation_reply(user_input):
    try:
        # Generate short mentor voice message
        voice_prompt = (
            "You are a calm, wise mentor helping a demotivated student. Based on the student's message below, "
            "speak to them for about one minute in a supportive and encouraging tone. Give meaningful advice, relate to their journey, "
            "and motivate them to continue working towards their dream.\n\n"
            f"Student: {user_input}\nMentor:"
        )

        voice_response = model.generate_content(voice_prompt)
        voice_text = voice_response.text.strip()

        # Generate calming mental exercise as bullet points
        exercise_prompt = (
            "Give a short mental exercise in 5 to 7 bullet points that helps students regain focus and calm. "
            "Only return the bullet points, no intro or explanation."
        )

        exercise_response = model.generate_content(exercise_prompt)
        exercise_text = exercise_response.text.strip()

        return voice_text, exercise_text
    except Exception as e:
        return f"❌ Gemini failed to respond: {e}", ""
