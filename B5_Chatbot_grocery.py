import random    #Imports the random module to use functions like random.choice() for selecting random responses.

def chatbot():    #Defines a function named chatbot(), which encapsulates all the chatbot logic.
    print("Welcome to our Grocery Store Chatbot!")
    print("To end the chat, type 'exit' or 'bye'")
#Prints a welcome message and a note to the user on how to exit the chatbot.

    greetings = ["Hello! How can I assist you today?", "Hi there! Need help with groceries?", "Hey! I'm here to help you."]
    delivery = ["Your order is on the way!", "Delivery usually takes 3-5 business days.", "Same-day delivery is available in select areas."]
    return_policy = ["You can return unopened items within 7 days.", "Returns accepted within 7 days of purchase."]
    refund = ["Your refund will be processed within 7 days.", "Refunds are initiated once the returned item is received."]
    pricing = ["Please mention the product name to get the price.", "Let me know which item you want the price for."]
    item_prices = {
        "milk": "Milk is 30rs per liter.",
        "eggs": "A dozen eggs cost 80rs.",
        "rice": "Rice is 50rs per kg."
    }
    store_info = {
        "timing": "Our store is open from 8 AM to 10 PM every day.",
        "location": "We are located at XYZ Market, Main Street, City.",
        "payment": "We accept cash, credit/debit cards, and UPI payments."
    }
    issue = ["For any query, contact 24389.", "You can also visit our help center at www.help.com."]
    unknown = ["Sorry, I didn't understand that. Can you rephrase?", "I'm not sure I got that. Could you clarify?"]
#Initializes lists and dictionaries containing preset responses for different user queries such as greetings, delivery info, return policy, item prices, etc.

    while True:   #Starts an infinite loop that runs until the user types "exit" or "bye".
        user_input = input("You: ").lower()  #Takes input from the user and converts it to lowercase for easier keyword matching.

        if user_input in ['exit', 'bye']:
            print("Bot: Thank you for shopping with us! Have a great day!")
            break
        #If the user types "exit" or "bye", it thanks them and breaks the loop (ends the chat).
        elif any(word in user_input for word in ['hi', 'hello', 'hey']):
            print("Bot:", random.choice(greetings))
        elif "delivery" in user_input or "shipping" in user_input:
            print("Bot:", random.choice(delivery))   # Checks for keywords "delivery" or "shipping" and provides delivery info.
        elif "return" in user_input or "exchange" in user_input:
            print("Bot:", random.choice(return_policy))  #Checks for return/exchange-related keywords and gives return policy details.
        elif "refund" in user_input:
            print("Bot:", random.choice(refund))   #Responds to refund-related queries.
        elif any(item in user_input for item in item_prices):
            for item in item_prices:
                if item in user_input:
                    print("Bot:", item_prices[item])
                    break
                #Checks if the input contains any item name in item_prices dictionary and prints its price.
        elif "price" in user_input or "cost" in user_input:
            print("Bot:", random.choice(pricing))  #Responds when the user asks for "price" or "cost" without specifying the item.
        elif "timing" in user_input or "hours" in user_input:
            print("Bot:", store_info["timing"])  # Replies with store timing when "timing" or "hours" is mentioned.
        elif "location" in user_input or "address" in user_input or "store" in user_input:
            print("Bot:", store_info["location"])  #Replies with store location info when "location" or "address" is mentioned.
        elif "payment" in user_input:
            print("Bot:", store_info["payment"])  # Replies with payment method details.
        elif "issue" in user_input or "problem" in user_input:
            print("Bot:", random.choice(issue))  # Responds to problem/issue-related keywords.
        elif "thank" in user_input:
            print("Bot: You're welcome!") # Replies politely if the user says thank you.
        else:
            print("Bot:", random.choice(unknown))  #Handles unknown inputs by printing a generic clarification message.

# Run the chatbot
chatbot()  #Calls the chatbot function to start the program.

# Input:
# You: hi
# Output:
# Bot: Hello! How can I assist you today?

# Input:
# You: what is the price of milk
# Output:
# Bot: Milk is 30rs per liter.

# Input:
# You: where is your store
# Output:
# Bot: We are located at XYZ Market, Main Street, City.

# Input:
# You: exit
# Output:
# Bot: Thank you for shopping with us! Have a great day!
