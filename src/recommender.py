from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []

    print(f"Loading songs from {csv_path}...")

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    print(f"Loaded songs: {len(songs)}")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a weighted score and reasons for one song against user preferences."""
    score = 0.0
    reasons: List[str] = []
    
    # Genre match: +2.0 if song genre == favorite genre
    user_genre = str(user_prefs.get("genre", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    if user_genre and song_genre == user_genre:
        score += 1.0
        reasons.append("genre match (+2.0)")
    
    # Mood match: +1.5 if song mood == favorite mood
    user_mood = str(user_prefs.get("mood", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    if user_mood and song_mood == user_mood:
        score += 1.5
        reasons.append("mood match (+1.5)")
    
    # Energy closeness (target = 0.40)
    song_energy = float(song.get("energy", 0.5))
    energy_diff = abs(song_energy - 0.40)
    if energy_diff <= 0.10:
        score += 3.0
        reasons.append("energy closeness (+1.5)")
    elif energy_diff <= 0.20:
        score += 0.8
        reasons.append("energy closeness (+0.8)")
    
    # Tempo closeness (target = 78)
    song_tempo = float(song.get("tempo_bpm", 80))
    tempo_diff = abs(song_tempo - 78)
    if tempo_diff <= 8:
        score += 1.2
        reasons.append("tempo closeness (+1.2)")
    elif tempo_diff <= 15:
        score += 0.6
        reasons.append("tempo closeness (+0.6)")
    
    # Valence closeness (target = 0.60)
    song_valence = float(song.get("valence", 0.5))
    valence_diff = abs(song_valence - 0.60)
    if valence_diff <= 0.10:
        score += 0.8
        reasons.append("valence closeness (+0.8)")
    elif valence_diff <= 0.20:
        score += 0.4
        reasons.append("valence closeness (+0.4)")
    
    # Danceability closeness (target = 0.60)
    song_danceability = float(song.get("danceability", 0.5))
    danceability_diff = abs(song_danceability - 0.60)
    if danceability_diff <= 0.10:
        score += 0.8
        reasons.append("danceability closeness (+0.8)")
    elif danceability_diff <= 0.20:
        score += 0.4
        reasons.append("danceability closeness (+0.4)")
    
    # Acousticness closeness (target = 0.80)
    song_acousticness = float(song.get("acousticness", 0.5))
    acousticness_diff = abs(song_acousticness - 0.80)
    if acousticness_diff <= 0.10:
        score += 1.2
        reasons.append("acousticness closeness (+1.2)")
    elif acousticness_diff <= 0.20:
        score += 0.6
        reasons.append("acousticness closeness (+0.6)")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by score with human-readable explanations."""
    scored_songs = [
        (
            song,
            score,
            "; ".join(reasons) if reasons else "No strong feature matches",
        )
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked[:k]
