import json
import os
from datetime import datetime, timedelta

PROGRESS_FILE = "data/progress.json"

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return []
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def log_session(track_id, duration):
    progress = load_progress()
    today = datetime.now().strftime("%Y-%m-%d")

    # Check if already logged for today for this track
    for entry in progress:
        if entry["track_id"] == track_id and entry["date"] == today:
            return  # Don't log twice

    progress.append({
        "track_id": track_id,
        "date": today,
        "duration": duration
    })

    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def get_today_progress(track_id):
    today = datetime.now().strftime("%Y-%m-%d")
    progress = load_progress()
    for entry in progress:
        if entry["track_id"] == track_id and entry["date"] == today:
            return entry["duration"]
    return 0

def get_streak(track_id):
    progress = load_progress()
    # Collect all dates where this track had > 0 duration
    date_set = {
        entry["date"]
        for entry in progress
        if entry["track_id"] == track_id and entry["duration"] > 0
    }

    if not date_set:
        return 0

    streak = 0
    today = datetime.now().date()

    while True:
        date_str = today.strftime("%Y-%m-%d")
        if date_str in date_set:
            streak += 1
            today -= timedelta(days=1)
        else:
            break

    return streak
