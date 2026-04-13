# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

MusiChooser 1.0

---

## 2. Intended Use

This is a model that suggests 5 songs from a small catalog based on a user's profile. The profile itself has mood, genre, and energy level. 
---

## 3. How It Works (Short Explanation)

It looks at various features of a song (i.e. danceability, energy) and compares it to the profile of the user's presumed feature preferences. The lower the difference between what the user usually likes and what the song has, the higher the song recommendation. It is all done by a reward system. The more rewards for a lower difference, the higher the number for recommendation.

---

## 4. Data

At the moment, there are 17 songs in the dataset. They reflect a wide array of songs of all genres and moods. A slightly higher portion of the songs lean towards lofi, and the dataset may reflect a college student who is studying at the library frequently, but otherwise it is a balanced dataset.
---

## 5. Strengths  

The recommender works best when a user has a clear favorite genre or mood and the catalog includes songs near their target values. By combining exact genre and mood matches with features like energy, tempo, valence, danceability, and acousticness, it produces consistent results. It excels with simple profiles like “happy pop with moderate energy” or “chill lofi with low energy” making the top picks feel intuitive.

---

## 6. Limitations and Bias 

The recommender is limited by a small catalog and a few hand-picked features, so it can’t capture lyrics, artist history, or complex taste patterns. Common genres and moods get favored, making some tastes easier to serve. Fixed weights can overemphasize exact matches, missing songs that are similar in vibe but not identical, which can make results feel narrow for nuanced listeners.

---

## 7. Evaluation  

I tested intense-sad, happy EDM, and moody pop listening user profiles. I looked at the scores each time the weights were changed. It was surprising to see that even though the energy weight was doubled and the genre weight was halved, the scores were relatively similar, around a max of 1.5 in difference. It defintely gets to prioritize genre, especially lofi ones that are more prevalant in the dataset.


---

## 8. Future Work  

If I kept improving this recommender, I’d let users tweak more preferences like tempo, artist familiarity, or new vs familiar songs. I’d add simple explanations for each recommendation, like “matches your mood” or “fits your favorite genre.” To keep things diverse, I’d slightly shuffle top results so one style doesn’t dominate. Finally, I’d support more complex tastes, like “sad but energetic,” by adjusting weights based on context.

---

## 9. Personal Reflection  

A few sentences about your experience.  

I was surprised at how much genre could dominate results, even when I adjusted other factors like energy, showing how the dataset itself shapes recommendations. It made me realize that music apps balance user preferences, catalog makeup, and scoring choices, so even small algorithm tweaks can change what people hear.
