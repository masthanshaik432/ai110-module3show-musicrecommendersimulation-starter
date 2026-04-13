"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


EDGE_CASE_PROFILES = [
    {
        "name": "Intense Sad",
        "prefs": {"genre": "rock", "mood": "sad", "energy": 1.0},
    },
    {
        "name": "Happy EDM",
        "prefs": {"genre": "edm", "mood": "happy", "energy": 1.0},
    },
    {
        "name": "Ultra Chill Acoustic",
        "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.0},
    },
    {
        "name": "Genre Unknown Focused",
        "prefs": {"genre": "classical", "mood": "focused", "energy": 0.3},
    },
    {
        "name": "Moody Pop",
        "prefs": {"genre": "pop", "mood": "moody", "energy": 0.5},
    },
]


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile in EDGE_CASE_PROFILES:
        name = profile["name"]
        user_prefs = profile["prefs"]
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== Profile: {name} ===")
        print(f"Preferences: {user_prefs}\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
