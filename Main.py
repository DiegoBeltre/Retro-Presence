from time import sleep, time
from pypresence import Presence
from Capture import get_frame_hash
from imghash import build_library, find_best_match

CLIENT_ID = "1519389749364654212"

THRESHOLDS = {
    "MATCH": 35,            
    "CONFIDENCE_MAX": 80,  
    "CONFIRMATIONS": 3,    
    "STREAK_OVERRIDE": 8   
}

ASSET_KEYS = {
    "RESIDENT_EVIL_4": "re4",
    "Final_Fantasy_X": "ffx",
    "Destroy_All_Humans": "destroy",
    "Fatal_Frame": "fatal1",
    "Fatal_Frame_2": "fatal2",
    "Fatal_Frame_3": "fatal3",
    "Metal_Gear_Solid_3": "mgs3",
}

def get_console(name):
    return name.split("111")[1] if "111" in name else "Unknown"

def normalize_game_name(name):
    base_name = name.split("111")[0] if "111" in name else name
    return base_name.replace("_", " ").replace("!", "").strip().title()

def get_asset_key(name):
    base_name = name.split("111")[0] if "111" in name else name
    return ASSET_KEYS.get(base_name, "ps2_logo")

class PresenceTracker:
    def __init__(self, client_id):
        self.rpc = Presence(client_id)
        self.rpc.connect()
        print("Discord Rich Presence connected successfully.")
        
        self.current_game = None
        self.candidate_game = None
        self.candidate_count = 0
        
        self.last_best_pick = None
        self.best_pick_streak = 0
        self.start_time = int(time())

    def update_streak(self, game):
        """Tracks how many times in a row a game gets the #1 spot."""
        if game == self.last_best_pick:
            self.best_pick_streak += 1
        else:
            self.last_best_pick = game
            self.best_pick_streak = 1
        return self.best_pick_streak

    def reset_streak(self):
        self.last_best_pick = None
        self.best_pick_streak = 0

    def process_frame(self, game, score):
        """Evaluates the image-matching results against filters and streaks."""
        streak = self.update_streak(game)

        if score > THRESHOLDS["CONFIDENCE_MAX"]:
            print(f"Extreme low confidence ({score} > {THRESHOLDS['CONFIDENCE_MAX']}) - ignoring frame")
            self.reset_streak()
            return

        is_strict_match = score <= THRESHOLDS["MATCH"]
        is_streak_exception = streak >= THRESHOLDS["STREAK_OVERRIDE"]

        if is_strict_match or is_streak_exception:
            if is_streak_exception and not is_strict_match:
                print(f"-> Streak Exception Triggered! '{game}' picked {streak}x in a row (Score: {score})")
            
            self._update_candidate(game)
        else:
            print(f"Building streak: {streak}/{THRESHOLDS['STREAK_OVERRIDE']}s (Score: {score})")

    def _update_candidate(self, game):
        """Tracks game stability confirmations before pushing an update to Discord."""
        if game == self.candidate_game:
            self.candidate_count += 1
        else:
            self.candidate_game = game
            self.candidate_count = 1

        if self.candidate_count >= THRESHOLDS["CONFIRMATIONS"] and game != self.current_game:
            self.current_game = game
            self.start_time = int(time())
            
            display_name = normalize_game_name(self.current_game)
            console = get_console(self.current_game)
            asset_key = get_asset_key(self.current_game)

            self.rpc.update(
                details=display_name,
                state=console,
                start=self.start_time,
                large_image=asset_key,
                large_text=display_name
            )
            print(f"Discord Updated: {display_name} ({console})")

def main():
    library = build_library()
    tracker = PresenceTracker(CLIENT_ID)
    print("PYpresence initialized. Processing media frames...")

    while True:
        try:

            frame_hashes = get_frame_hash()
            game, score = find_best_match(frame_hashes, library)
            print(f"Detected: {game} | Score: {score}")

            tracker.process_frame(game, score)
            sleep(1)
            
        except Exception as e:
            print(f"Error occurred loop side: {e}")
            sleep(5)

if __name__ == "__main__":
    main()
