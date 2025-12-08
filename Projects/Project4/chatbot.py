#Rule Based Python Ai Chat Bot:


import datetime
import time

#Time Based Greeting


name = input("Swagat Ha, Enter Your Name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning :" , name)

elif 11 <= presentHour <= 17:
    print("Good AfterNoon :" , name)

elif 17 <= presentHour <= 20 :
    print("Good Evening :" , name)

else:
    print("Good Night :" , name)



print("Namaste Welcome To Rule Based Chatbot ! ")
print("You Can Ask Me Basic Questions, Type 'Bye' to exit from the bot : ")

# Chatbot Memory Creation
responses = {
    'hello' : "Hii, Welcome , How Can I Help You😊", 
    "how are you" : "I Am Good , How About You😁",
    "who are you" : "I Am A Smart Ai Chatbot",
    "motivate me" : "Keep Going. Every Bug Of Your Project Makes You A Better Developer",
    "happy" : "Great To Hear That",
    "sad" : "No Pain, No Gain",
    "What is my name" : f"Your Name Is {name} Sir "
}

#function to get response of chatbot

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am Not Able To Answer That . I Am In Learning Phase 😊"


#Take User Input
while True:
    user_input = input("Please ask your question ? ")
    reply = getResponseBot(userQuestion= user_input)
    print("Bot Response : " , reply)

    if "bye" in user_input.lower():
        break

