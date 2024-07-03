import tkinter as tk
from tkinter import scrolledtext, messagebox
import random


responses = {
    'greet': ["Hello! How can I assist you today?", 
              "Hi there! How can I help you today?", 
              "Hey! What's up?"],
    'bot_name': ["I'm your assistant bot!", 
                 "You can call me ChatBot.", 
                 "I am a chatbot, here to help."],
    'age': ["I'm ageless!", 
            "I don't have an age, I'm a bot.", 
            "I was created recently, but I'm here to stay!"],
    'weather': ["I can't provide real-time weather updates. You can check a weather website for that.", 
                "I'm sorry, I'm not equipped to give weather information."],
    'time': ["I don't wear a watch, but it's always a good time to chat!", 
             "The time? It's time to chat with you!"],
    'date': ["Today's date is [insert current date].", 
             "It's [insert current date]."],
    'goodbye': ["Goodbye! Have a great day!", 
                "See you later!"],
    'thanks': ["You're welcome!", 
               "No problem!", 
               "My pleasure!"],
    'help': ["I'm here to help you. Ask me anything!", 
             "How can I assist you today?", 
             "What do you need help with?"],
    'creator': ["I was created by Aditya sant.", 
                "I'm a product of artificial intelligence technology.",
                "My creator is aditya sant."],
    'joke': ["Why don't skeletons fight each other? They don't have the guts!",
             "Parallel lines have so much in common. It’s a shame they’ll never meet.",
             "I used to play piano by ear, but now I use my hands."],
    'music': ["I enjoy all types of music! What's your favorite genre?",
              "Music is a great way to relax and unwind.",
              "Listening to music can improve your mood."],
    'movies': ["What's your favorite movie genre?",
               "Movies are a great source of entertainment.",
               "I love watching movies too!"],
    'food': ["I'm a chatbot, so I don't eat, but I can help you find recipes!",
             "Food brings people together. What's your favorite dish?",
             "Exploring different cuisines is always exciting!"],
    'interests': ["I'm interested in technology, artificial intelligence, and chatting with you!",
                  "I love learning new things and helping others.",
                  "My interests include chatting, answering questions, and assisting users."],
    'default': ["I'm not sure how to respond to that. Can you ask something else?", 
                "Could you please rephrase that?", 
                "I didn't catch that. Could you ask again?"],
}


def get_response(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey", "hola", "greetings"]):
        return random.choice(responses['greet'])
    elif "your name" in user_input:
        return random.choice(responses['bot_name'])
    elif "how old are you" in user_input:
        return random.choice(responses['age'])
    elif "weather" in user_input:
        return random.choice(responses['weather'])
    elif "time" in user_input:
        return random.choice(responses['time'])
    elif "date" in user_input:
        return random.choice(responses['date'])
    elif any(goodbye in user_input for goodbye in ["bye", "goodbye", "see you", "take care"]):
        return random.choice(responses['goodbye'])
    elif any(thanks in user_input for thanks in ["thank you", "thanks", "appreciate"]):
        return random.choice(responses['thanks'])
    elif "help" in user_input:
        return random.choice(responses['help'])
    elif "creator" in user_input:
        return random.choice(responses['creator'])
    elif "joke" in user_input:
        return random.choice(responses['joke'])
    elif "music" in user_input:
        return random.choice(responses['music'])
    elif "movies" in user_input:
        return random.choice(responses['movies'])
    elif "food" in user_input:
        return random.choice(responses['food'])
    elif any(interest in user_input for interest in ["interest", "hobby", "like"]):
        return random.choice(responses['interests'])
    else:
        return random.choice(responses['default'])


def send():
    user_input = entry.get()
    if user_input.strip() != "":
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, "You: " + user_input + "\n", "user")
        response = get_response(user_input)
        chatbox.insert(tk.END, "Bot: " + response + "\n", "bot")
        chatbox.config(state=tk.DISABLED)
        entry.delete(0, tk.END)


def clear_chat():
    chatbox.config(state=tk.NORMAL)
    chatbox.delete('1.0', tk.END)
    chatbox.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Rule-Based Chatbot")
root.geometry("600x400")
root.configure(bg="grey")


title_label = tk.Label(root, text="Chat with Bot", font=("Arial", 20, "bold"), bg="#E8E8E8", fg="#333333")
title_label.pack(pady=10)


chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="white", fg="#333333", font=("Arial", 12))
chatbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chatbox.tag_config("user", foreground="blue")
chatbox.tag_config("bot", foreground="red")


entry_frame = tk.Frame(root, bg="#333333")
entry_frame.pack(padx=10, pady=5, fill=tk.X, expand=True)

entry = tk.Entry(entry_frame, width=60, font=("Arial", 14), bd=2, relief=tk.GROOVE)
entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)


send_button = tk.Button(entry_frame, text="Send", command=send, bg="green", fg="white", font=("Arial", 14, "bold"), relief=tk.RAISED)
send_button.pack(side=tk.LEFT, padx=5, pady=5)


clear_button = tk.Button(root, text="Clear Chat", command=clear_chat, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
clear_button.pack(pady=5)


def show_about():
    messagebox.showinfo("About Chatbot", "This is a rule-based chatbot implemented using Python and tkinter.\n\nCreated by Aditya sant")


about_button = tk.Button(root, text="About", command=show_about, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
about_button.pack(pady=5)


root.mainloop()
