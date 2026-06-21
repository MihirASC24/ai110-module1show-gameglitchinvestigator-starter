# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
To challenge the player to guess a secret number with hints

- [X] Detail which bugs you found.
Incorrect hints, failing to refresh screen, incorrect secret range

- [X] Explain what fixes you applied.
Corrected hint logic, corrected secret logic

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters guess of 90
2. Game returns "Too High!"
3. User guesses 60 -> "Too Low"
4. Score updates after each guess
5. User enters [secret] -> Correct guess, game ends

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
tests/test_game_logic.py::test_winning_guess PASSED                               [ 10%]
tests/test_game_logic.py::test_guess_too_high PASSED                              [ 20%]
tests/test_game_logic.py::test_guess_too_low PASSED                               [ 30%]
tests/test_game_logic.py::test_string_secret_win[50_0] PASSED                     [ 40%]
tests/test_game_logic.py::test_string_secret_win[50_1] PASSED                     [ 50%]
tests/test_game_logic.py::test_string_secret_too_high[50_0] PASSED                [ 60%]
tests/test_game_logic.py::test_string_secret_too_high[50_1] PASSED                [ 70%]
tests/test_game_logic.py::test_string_secret_too_low[50_0] PASSED                 [ 80%]
tests/test_game_logic.py::test_string_secret_too_low[50_1] PASSED                 [ 90%]
tests/test_game_logic.py::test_string_guess_matches_int_secret PASSED             [100%]

================================== 10 passed in 0.02s ===================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
