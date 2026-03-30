# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 is designed to suggest songs from a small catalog based on a user's preferred genre, mood, and energy level. It assumes the user has a single dominant taste profile — one favorite genre, one mood, and a target energy level — and ranks songs that best match those preferences. This system is built for classroom exploration only and is not intended for real-world music platforms or production use.

---

## 3. How the Model Works

VibeFinder 1.0 works by comparing each song in the catalog against a user's taste profile and assigning a score based on how well they match. Every song gets points for matching the user's favorite genre (+2.0), matching the user's preferred mood (+1.0), and having an energy level close to the user's target (up to +1.0 depending on how similar the energy is). If the user enjoys acoustic music and the song is highly acoustic, it gets a small bonus of +0.5 points. Once every song has been scored, the system sorts them from highest to lowest and returns the top results. Think of it like a judge scoring contestants — the song that matches the most preferences wins.

---

## 4. Data

The catalog contains 18 songs stored in `data/songs.csv`. The starter dataset had 10 songs, and 8 additional songs were added to improve genre and mood diversity. Genres represented include pop, lofi, rock, ambient, jazz, synthwave, indie pop, R&B, electronic, classical, country, and hip-hop. Moods include happy, chill, intense, relaxed, focused, moody, energetic, and sad. Each song has numerical features for energy, tempo, valence, danceability, and acousticness on a 0.0–1.0 scale. Notable gaps include no metal, no Latin music, no songs with lyrics-based mood tags, and most genres have only one or two representatives which limits variety for users with niche tastes.

---

## 5. Strengths

VibeFinder 1.0 works best for users with a clear, strong genre preference — for example, a dedicated lofi listener or a rock fan will consistently see their preferred genre at the top of results. The scoring logic is fully transparent: every recommendation comes with a written explanation of exactly why it ranked where it did, which makes it easy to understand and debug. The acoustic bonus also adds a useful layer of personalization for users who specifically enjoy acoustic music, rewarding songs that are both acoustically rich and match other preferences.

---

## 6. Limitations and Bias

The most significant bias in this system is that genre is worth +2.0 points — the highest single weight — which means songs that match the user's genre will almost always dominate the top results, even if their mood or energy is a poor fit. For example, a "Deep Intense Rock" user will always see the two rock songs ranked first, leaving little room for songs from other genres that might actually match the vibe better. The dataset itself also introduces bias: with 18 songs, some genres like lofi and pop have multiple entries while others like classical and country have only one, meaning users who prefer underrepresented genres will receive lower-quality recommendations. When we ran the weight shift experiment — halving genre and doubling energy — songs with matching energy from different genres became much more competitive, showing how sensitive the ranking is to weight choices. Finally, the system has no diversity logic, so it can recommend multiple songs from the same artist or genre back-to-back without any penalty.

---

## 7. Evaluation

Three distinct user profiles were tested: "High-Energy Pop" (genre: pop, mood: happy, energy: 0.9), "Chill Lofi" (genre: lofi, mood: chill, energy: 0.3, likes_acoustic: True), and "Deep Intense Rock" (genre: rock, mood: intense, energy: 0.95). For each profile, the top 5 recommendations were reviewed to see if they matched musical intuition. The results were mostly accurate — the Chill Lofi profile correctly surfaced acoustic lofi songs at the top, and the Deep Intense Rock profile put the two heaviest rock songs first. One interesting finding was that for the Deep Intense Rock profile, Gym Hero (a pop song) ranked #3 purely because of its intense mood and high energy, even though it shares nothing else with rock. A weight shift experiment was also run — halving genre weight from +2.0 to +1.0 and doubling energy weight — which caused songs with matching energy but different genres to become significantly more competitive, confirming that genre dominates the ranking under the original weights.

---

## 8. Future Work

First, a diversity penalty would prevent the same genre or artist from dominating every recommendation, making the results feel more varied and less like a filter bubble. Second, additional features like tempo range preferences, valence (positivity), and danceability could be incorporated into the user profile to capture a more complete picture of musical taste. Third, the system could be extended to support multiple scoring modes — for example a "Mood-First" mode or an "Energy-Focused" mode — so users can switch strategies depending on what they are looking for.

---

## 9. Personal Reflection

My biggest learning moment during this project was understanding how to assign weighted scores to specific song attributes and use those scores to drive real recommendations. It made the concept of a recommender system feel concrete and tangible rather than abstract. Using AI tools helped guide me through the process step by step, though I found it important to double-check the AI along the way to make sure no steps were skipped or rushed. What surprised me most was how much a recommendation system can accomplish using just simple single numerical values — the idea that a song's entire "vibe" can be captured and compared using a handful of decimals between 0.0 and 1.0 was unexpectedly powerful. If I were to extend this project, I would evolve it into a machine learning model that learns from user feedback over time rather than relying on manually assigned weights.
