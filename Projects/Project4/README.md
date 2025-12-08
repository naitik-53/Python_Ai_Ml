🧠 Rule-Based Python Chatbot

A simple beginner-friendly rule-based chatbot made using Python.
This bot replies to basic questions using predefined rules (dictionary lookup).
It also greets the user based on the current time.

🚀 Features

⏰ Time-based greeting (Morning, Afternoon, Evening, Night)

👤 User name detection

🤖 Simple rule-based responses

🔁 Chat loop enabled (Ask unlimited questions)

❌ Type bye to exit

📌 How It Works

Program asks your name

It checks current system hour and greets you

You can ask questions like:

hello

how are you

who are you

motivate me

what is my name

The bot looks for keywords in a dictionary and returns the matching response

If no match is found → bot says it is still learning

Type bye → program ends

🛠️ Requirements

Python 3.x
(No external libraries required)

▶️ How to Run

Save the file as chatbot.py

Run the code in terminal:

python chatbot.py


Start chatting with the bot!

🧩 Code Overview
1. Time-Based Greeting

Uses datetime module to detect current hour and greet the user.

2. Dictionary-Based Memory

All responses are stored in a Python dictionary:

responses = {
    "hello": "Hi! Welcome!",
    "how are you": "I am good!",
    ...
}

3. Rule-Matching System

The bot checks if any key (like "hello") is present inside your question.

4. Infinite Chat Loop

Keeps taking input until user types "bye".

📷 Example Output
Swagat Ha, Enter Your Name : Aman
Good Evening: Aman
Namaste! Welcome To The Rule-Based Chatbot!
You can ask me basic questions. Type 'bye' to exit.

Please ask your question? hello
Bot Response: Hi! Welcome!

Please ask your question? bye
Goodbye! Have a great day 😊

📝 Future Improvements (Optional)

Add more responses

Add voice input/output

Add GUI (Tkinter)

Add AI/ML features

Add user emotion tracking

👍 Author

Made by a beginner learning Python and AI 😄
Keep coding… every line makes you better!