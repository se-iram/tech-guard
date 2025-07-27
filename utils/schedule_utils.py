import json
import os
from datetime import datetime, timedelta
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACK_FILE = os.path.join(BASE_DIR, "data", "tracks.json")


def load_all_tracks():
    if not os.path.exists(TRACK_FILE):
        return []
    with open(TRACK_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_schedule(track, dream, time, duration):
    new_track = {
        "id": str(uuid.uuid4()),  # 🆕 generate unique ID
        "track": track,
        "dream": dream,
        "time": time,
        "duration": duration
    }

    tracks = load_all_tracks()
    tracks.append(new_track)

    with open("data/tracks.json", "w") as f:
        json.dump(tracks, f, indent=2)


def is_focus_time_now(saved_time_str, window_minutes=10):
    """Check if the current time is within the focus window."""
    try:
        # Parse the saved time (e.g., '15:00:00')
        saved_time = datetime.strptime(saved_time_str, "%H:%M:%S").time()
        now = datetime.now().time()

        # Convert both to datetime objects for comparison
        now_dt = datetime.combine(datetime.today(), now)
        focus_dt = datetime.combine(datetime.today(), saved_time)

        lower_bound = (focus_dt - timedelta(minutes=window_minutes)).time()
        upper_bound = (focus_dt + timedelta(minutes=window_minutes)).time()

        return lower_bound <= now <= upper_bound
    except:
        return False


def get_upcoming_tracks(tracks, window_minutes=10):
    now = datetime.now().time()
    upcoming = []

    def time_to_minutes(t):
        return t.hour * 60 + t.minute

    now_min = time_to_minutes(now)

    for track in tracks:
        try:
            scheduled_time = datetime.strptime(track["time"], "%H:%M:%S").time()
        except ValueError:
            continue  # skip if time format is wrong

        track_min = time_to_minutes(scheduled_time)
        if abs(now_min - track_min) <= window_minutes:
            upcoming.append(track)

    return upcoming