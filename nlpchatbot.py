import nltk
from nltk.chat.util import Chat, reflections

# Simple clean keyword-response pairs
pairs = [
    ['hello', ['Hello! How can I help you today?']],
    ['hi', ['Hi there! How can I assist you?']],
    ['hey', ['Hey! What can I do for you?']],
    ['order', ['To place an order, please go to our shop section.']],
    ['refund', ['You can request a refund from the "My Orders" page.']],
    ['return', ['Returns can be initiated via the "My Orders" section.']],
    ['delivery', ['Your order will be delivered within 3-5 business days.']],
    ['shipping', ['Shipping typically takes 3-5 business days.']],
    ['price', ['Prices are listed with each product on our website.']],
    ['bye', ['Thank you! Have a nice day.']],
    ['exit', ['Goodbye! Feel free to come back anytime.']],
    ['quit', ['Session ended. Take care!']],
    ['default', ["I'm sorry, I didn't understand that. Can you rephrase?"]]
]

# Chat logic using keyword matching
def simple_chatbot():
    print("🛒 Welcome to ShopBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['bye', 'exit', 'quit']:
            print("Bot:", get_response(user_input))
            break
        print("Bot:", get_response(user_input))

# Response generator
def get_response(user_input):
    for key, responses in pairs:
        if key in user_input:
            return responses[0]
    return [r for k, r in pairs if k == 'default'][0]

simple_chatbot()
