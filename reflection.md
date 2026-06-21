# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |

|1|Hint returns "Go Higher!"|Hint returned "Go Lower!"|Incorrect Hint|

|Entered 30 , Secret: 40|Hint returns "Go Higher!"|Hint returned "Go Lower!"|Incorrect Hint|

|Clicked "New Game" after winning|New Game prompt disappears after clicking|New Game prompt stayed|New Game prompt not disappearing|

|Clicked "New Game" after Game Over|Game Over message disappears after clicking|Game Over message stayed|Game Over prompt not disappearing|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude correctly fixed the incorrect hints error, which I verified through pytest and running the game in streamlit.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When attempting to fix the history not appending the submitted guesses correctly, Claude suggested moving the Developer Debug window to the bottom, so it would refresh after submitting. However, I knew this would mess up the placement of the Developer Debug window. To get past this, the top Developer Debug window is a placeholder, and its data (including history) is updated after submitting. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Through manual testing while running the game

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the hints in pytest, and it showed the correct hints were being returned.

- Did AI help you design or understand any tests? How?
Claude helped design the hint tests, as well as tests for string vs. int guesses.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would say Streamlit runs top to bottom
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Looking through the code manually to find where potential bugs occur

- What is one thing you would do differently next time you work with AI on a coding task?
Document more

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project helped me feel that I was using AI assistance in a systematic and comepetent way, rather than shooting in the dark.
