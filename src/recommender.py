from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Scores and ranks all songs for a user, returning the top k."""
        def score(song: Song) -> float:
            s = 0.0
            if song.genre.lower() == user.favorite_genre.lower():
                s += 2.0
            if song.mood.lower() == user.favorite_mood.lower():
                s += 1.0
            s += 1 - abs(song.energy - user.target_energy)
            if user.likes_acoustic and song.acousticness > 0.6:
                s += 0.5
            return s

        return sorted(self.songs, key=score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a plain-language explanation of why a song was recommended."""
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match (+2.0)")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match (+1.0)")
        energy_sim = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"energy similarity (+{energy_sim:.2f})")
        if user.likes_acoustic and song.acousticness > 0.6:
            reasons.append("acoustic bonus (+0.5)")
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dictionaries."""
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Scores a single song against user preferences and returns (score, reasons)."""
    score = 0.0
    reasons = []

    if song['genre'].lower() == user_prefs['genre'].lower():
        score += 2.0
        reasons.append('genre match (+2.0)')

    if song['mood'].lower() == user_prefs['mood'].lower():
        score += 1.0
        reasons.append('mood match (+1.0)')

    energy_similarity = 1 - abs(song['energy'] - user_prefs['energy'])
    score += energy_similarity
    reasons.append(f'energy similarity (+{energy_similarity:.2f})')

    if user_prefs.get('likes_acoustic') and song['acousticness'] > 0.6:
        score += 0.5
        reasons.append('acoustic bonus (+0.5)')

    return score, ', '.join(reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs, sorts by score descending, and returns the top k results."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
