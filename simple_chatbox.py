import nltk
from nltk.chat.util import Chat, reflections #natural language toolkit

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],

    [
        r"hi|hey|hello",
        ["Hello", "Hey there!",]
    ],

    [
        r"what is your name?",
        ["I am a chatbox created by OP. You can call me AbhiAI",]
    ],

    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great today! How can I assist you?"]
    ],

    [
        r"sorry (.*)",
        ["It's okay, no problem!", "No worries, how can I assist you?",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Glad to hear that! How can I assist you today?",]
    ],
    [
        r"(.*) (location|city) ?",
        ["Im in the cloud, but Im here to help you anywhere!",]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye! It was nice talking to you."]
    ],
]

# Default reflections
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

#Creating the chatbox

chatbox = Chat(pairs, reflections)

def chat():
    print("Hi! I am a simple chatbox. Type 'quit' to exit. ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye")
            break
        response = chatbox.respond(user_input)
        print("Bot:", response)

#Running the chat function

if __name__ == "__main__":
    chat()