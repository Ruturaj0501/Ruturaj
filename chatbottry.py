import random
import re

response={
    "greet":["Hello how can i help you","how can i assist you ","i am thre to help you"],
    "bye":["have a nice day","see yo soon","byy"],
    "product":["we have phones,laptps,watche,ltablet ad other accesories"],
    "help":["i acn help you i product details,order status"],
    "order_response":["sure,ente the order number"],
    "default":["I cant undertans whta re trying to say type again"]


}

def check_status(order_num):
    status=["is placed successfully","has been shipped","out fordelivery","will delevr shortly","sorry for late will delbevry yu rder very quickly"]
    return f"order{order_num} {random.choice(status)}"

def get_response(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hii" in user_input:
        return random.choice(response["greet"])
    elif "help" in user_input:
        return random.choice(response["help"])
    elif "product" in user_input or "products" in user_input:
        return random.choice(response["product"])
    elif "bye" in user_input:
        return random.choice(response["bye"])
    elif "mobiles" in user_input:
        return "we have samsung s25,iphone 12,13,14,16, mi redmi note 7,8,9"
    elif "laptops" in user_input:
        return "we have hp,dell, moottorola,lenovo, asus"
    
    if "order" in user_input:
        order_number=re.findall(r'\d+',user_input)
        if order_number:
            return check_status(order_number[0])
        else:
            return random.choice(response["order_response"])
    return random.choice(response["default"])


def chat():
    print("Chatbot i am here to help you type bye to exit")
    while True:
        user_input=input("You :")
        if "bye" in user_input.lower():
            print("Chatbot ", random.choice(response["bye"]))
            break
        print("chatbot",get_response(user_input))

if __name__=="__main__":
    chat()

