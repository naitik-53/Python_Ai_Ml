#This Is My 2nd Project Of Python

#This Is A Chat Bot Ai Which Replies According To Your Mood
#Multi Keywords Per Mood
#Random Reply
#Case-insensitive detection
#Fall back Smart Reply

import random
user_input = input("How are you feeling today? ").lower()

#Defining Keywords And Replies For Different Moods
happy_keywords = ["happy", "joyful", "elated", "cheerful", "content"]
sad_keywords = ["sad", "unhappy", "down", "dejected", "blue"]
angry_keywords = ["angry", "mad", "furious", "irate", "annoyed"]
tired_keywords = ["tired", "exhausted", "weary", "fatigued", "drained"]

happy_replies = ["That's great to hear! Keep smiling!😍", "Happiness looks good on you!", "Yay! Spread the joy!"]

sad_replies = ["I'm sorry to hear that. I'm here for you.", "It's okay to feel sad sometimes. Take your time.", "Sending you positive vibes!"]

angry_replies = ["Take a deep breath. It's going to be okay.", "Try to stay calm. I'm here to help.", "Let's find a way to cool down together."]

tired_replies = ["Make sure to get some rest!", "It's important to take care of yourself.", "Maybe a short nap will help recharge you."]

if any(keyword in user_input for keyword in happy_keywords):
    print(random.choice(happy_replies))

elif any(keyword in user_input for keyword in sad_keywords):
    print(random.choice(sad_replies))

elif any(keyword in user_input for keyword in angry_keywords):
    print(random.choice(angry_replies))

elif any(keyword in user_input for keyword in tired_keywords):
    print(random.choice(tired_replies))

else:
    fallback_replies = [
        "I'm not sure how you're feeling, but I'm here to listen!",
        "Tell me more about your day.",
        "I'm here for you, no matter what!"
    ]
    print(random.choice(fallback_replies))



#------End Of The Program--------


