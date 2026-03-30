"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from recommender import load_songs, recommend_songs


def main() -> None:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    songs = load_songs(os.path.join(base_dir, "data", "songs.csv")) 

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9, "likes_acoustic": False},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3, "likes_acoustic": True},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95, "likes_acoustic": False},
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n{'='*50}")
        print(f"Profile: {profile_name}")
        print(f"{'='*50}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
