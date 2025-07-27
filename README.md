# TrackGuard — Stay Consistent. Stay Closer to Your Dream.

> A soulful AI-powered productivity & emotional support tool for students who want to stay consistent, focused, and emotionally grounded in their learning journey.

![Image](https://github.com/user-attachments/assets/24cffee3-ff34-4fab-9402-7f1c678bbc42)

---

## Why We Built This

In today’s world, AI can automate tasks — but what about the messy emotional moments students face while learning? The moments of doubt, distraction, burnout, and fear?

**TrackGuard** is more than a productivity tool — it’s a **calm companion** for learners. Built with empathy and intention, it helps students:

- Set consistent learning goals
- Stay on track with smart reminders
- Rebuild motivation when feeling lost
- Reflect on their journey and purpose
- Feel emotionally supported, not just optimized

We believe that **human intelligence + emotional resilience** is what keeps a learner moving — and that’s what AI should support.

---

## 🌟 Key Features

| Feature | Description |
|--------|-------------|
| ➕ **Add New Track** | Users can add learning tracks (e.g., DSA, Networking) with daily time and session duration. |
| 🎯 **Focus Session Timer** | Visual focus timer to stay committed for each session. Tracks time per learning goal. |
| 🧠 **Daily Reminder Popup** | Notifies users when it's time to study, even if they're on another page. |
| 📋 **Track History** | View all added tracks, delete them, and track daily progress + streaks. |
| 🔥 **Streak Counter** | Shows daily progress and study streaks per track. |
| 💬 **Motivation Room** (✨ Unique) | A calming space with: <br> - Welcome prompt <br> - Reflection input <br> - Gemini-generated voice response from a mentor <br> - A mini mental exercise guide |
| 🗣️ **Gemini Voice Mentor** | Users share their feelings, and receive a calm, 1-minute motivational voice reply (via Gemini + TTS). |
| 🧘 **Mental Exercises** | Personalized, bullet-style mindfulness tasks to build clarity and regain focus. |
| 💾 **Local Progress Tracking** | All sessions are logged in JSON files, tracking per-track progress securely. |

---

## 💡 Technologies Used

| Tech | Purpose |
|------|--------|
| **Python** | Core logic |
| **Streamlit** | Frontend web UI |
| **Google Gemini API** | Motivational voice and exercises |
| **gTTS** | Text-to-speech for mentor replies |
| **dotenv** | Secure key loading |
| **JSON (local)** | Tracks & progress storage |
| **uuid** | Unique track ID management |

---

## 🧪 How It Works

### 1. Add a Learning Track
User defines:
- The subject area (e.g., DSA)
- Their long-term dream (e.g., become a software engineer)
- A daily study time
- Session duration

### 2. Get Smart Reminders
If a track’s scheduled time is within ±10 minutes, a popup appears encouraging them to start their focus session.

### 3. Focus Timer + Session Logging
- Visual countdown
- Session logged upon completion (in `progress.json`)
- Progress bar and streak are updated

### 4. Motivation Room
If a student feels lost:
- They can enter the 💬 **Motivation Room**
- A calming message welcomes them
- They write about their struggle
- Gemini replies with a **1-minute mentor voice message**
- A mental exercise is shown below
- User is encouraged to return to their focus session

---

## 📸 Screenshots

![Image](https://github.com/user-attachments/assets/cdac90f9-08c0-44ce-9c58-cf5408e2b184)
![Image](https://github.com/user-attachments/assets/c47dd96b-e089-40d6-9405-32f07eb2726a)
![Image](https://github.com/user-attachments/assets/24cffee3-ff34-4fab-9402-7f1c678bbc42)
![Image](https://github.com/user-attachments/assets/3143050e-1b49-4df7-bce7-565fa884f56e)

---

## 🚀 Getting Started (Local)

1. **Clone the repo**
```bash
git clone https://github.com/your-username/trackguard.git
cd trackguard
# create virtual environment
python -m venv venv
source venv/bin/activate
# install dependencies
pip install -r requirements.txt
# create .env file
GOOGLE_API_KEY=your_gemini_api_key_here
# run the app
streamlit run app.py
```
## Folder Structure
TrackGuard/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   ├── tracks.json
│   ├── progress.json
│   └── audio/          ← generated voice files
│
├── pages/
│   ├── add_track_page.py
│   ├── focus_session_page.py
│   ├── motivation_room_page.py
│   └── track_history_page.py
│
└── utils/
    ├── schedule_utils.py
    ├── progress_utils.py
    ├── motivation.py
    ├── motivation_gemini.py
    ├── motivation_voice.py
    └── popup_reminder.py

---

## Track Submitted To
Push the Limits - Beyond Automation

We went beyond task automation and built a vibe-based student support system where AI supports the emotional side of human learning, helping students regain confidence, clarity, and consistency.

---

## Made for CS Girlies Hackathon
“Build something unmistakably human.”

---

## Author
- Iram Hameed
- Role: Solo developer
