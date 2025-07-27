import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

fallback_quotes = {
    "DSA": [
        "Every problem you solve sharpens your mind! 🧠",
        "DSA mastery is your ladder to greatness!",
        "One step closer to cracking coding interviews!"
    ],
    "Networking": [
        "Every packet you understand connects you to your dream.",
        "You’re one step closer to becoming a Networking Pro!",
        "Routing your way to success!"
    ],
    "AI": [
        "You’re training your brain just like a model trains on data!",
        "One session today = smarter model tomorrow.",
        "Your mind is your most powerful neural network."
    ],
    "default": [
        "You did great! Keep going, your dream is real.",
        "Your effort today plants the seed for tomorrow’s success!",
        "Stay consistent. You're becoming unstoppable! 💪"
    ]
}

def get_quote(track):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        prompt = f"Motivate me to study {track}. Return just one short motivational quote."
        print(f"🔍 Generating quote for track: {track}")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini API failed: {e}")
        return random.choice(fallback_quotes.get(track, fallback_quotes["default"]))
