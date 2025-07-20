# 🧠 Kaun Banega Crorepati - Python CLI Quiz Game

A command-line quiz game inspired by the iconic Indian TV show *Kaun Banega Crorepati (KBC)* — built entirely in Python!  
Answer 20 tech and general knowledge questions, climb the money ladder, and see how far you can go! 💸

---

## 🎮 Features

- ✅ 20 curated questions (Tech + General Knowledge)
- 📈 Progressive prize money system
- ❌ Wrong answer ends the game
- 💸 Retain earned money if eliminated
- 🔁 Smart input validation & restart option
- ⌛ Realistic delay between prompts using `time.sleep()`
- 🖥️ Fully CLI-based, no external libraries required

---

## 🎬 Game Flow (as shown in demo video)

1. Shows the code structure
2. Answers 2–3 questions correctly
3. Gives a wrong input → gets the option to restart
4. Plays again → gives a wrong answer → retains money earned till last correct question

---

## 🧾 How It Works

The quiz is powered by a structured list of questions in Python. Each question is represented as a list with the following format:

```python
[
    "Question text",
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    CorrectOptionIndex
]
Example of a question:-
["What is the capital of Japan?", "Tokyo", "Seoul", "Osaka", "Kyoto", 1]

