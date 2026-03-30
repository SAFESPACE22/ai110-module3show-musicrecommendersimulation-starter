# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music platforms like Spotify and YouTube use a combination of collaborative filtering (recommending songs that similar users enjoyed) and content-based filtering (matching songs to a user's taste based on audio features like genre, mood, and energy). At scale, these systems process millions of data points skips, replays, playlist adds to continuously refine predictions. My version is a simplified content-based recommender that prioritizes three core features: **genre**, **mood**, and **energy level**. It scores each song in a small catalog against a user's taste profile and returns the highest-scoring tracks, making its reasoning transparent and easy to trace.

**Song features used:**
- `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`

**UserProfile stores:**
- `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

**Scoring logic (Algorithm Recipe):**
- +2.0 points if the song's genre matches the user's favorite genre
- +1.0 point if the song's mood matches the user's favorite mood
- Up to +1.0 point based on energy similarity: `1 - abs(song_energy - target_energy)`
- +0.5 points if the user likes acoustic songs and the song has high acousticness (> 0.6)
- Maximum possible score: 4.5 points

**How recommendations are chosen:**
- Input: User preference dictionary (genre, mood, energy, likes_acoustic)
- Process: Every song in the catalog is scored using the Algorithm Recipe above
- Output: Songs sorted highest to lowest score — the top `k` results are returned

**Known potential bias:**
- Because genre is worth the most points (+2.0), songs that match the user's genre will almost always rank higher even if their mood or energy is a poor fit. This could create a "filter bubble" where the user only ever sees one genre dominating their recommendations.

**Data Flow Diagram:**

```mermaid
flowchart TD
    A[data/songs.csv] --> B[load_songs: Read all songs into a list]
    B --> C[User Preference Profile\ngenre, mood, energy, likes_acoustic]
    C --> D{For each song in catalog...}
    D --> E[score_song: Apply Algorithm Recipe\n+2.0 genre match\n+1.0 mood match\n+0.0-1.0 energy similarity\n+0.5 acoustic bonus]
    E --> F[Assign numeric score to song]
    F --> D
    D --> G[All songs scored]
    G --> H[Sort songs highest score to lowest]
    H --> I[Return Top K Recommendations\nwith score and reasons]
```

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Terminal Output

![Terminal Output](screenshots/terminal_output.png)

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

