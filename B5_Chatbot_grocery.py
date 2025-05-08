import streamlit as st

bot_name = "Grocery Buddy"

# Rule-based knowledge base
if 'knowledge_base' not in st.session_state:
    st.session_state.knowledge_base = {
        "hello": [f"Hello! I'm {bot_name}. How can I assist you with your groceries today?"],
        "hi": [f"Hi there! I'm {bot_name}. Need help with your grocery needs?"],
        "hey": [f"Hey! I'm {bot_name}. What can I help you with?"],
        "delivery": ["Your order is on the way!", "Delivery usually takes 3-5 business days.", "Same-day delivery is available in select areas."],
        "shipping": ["Your order is on the way!", "Delivery usually takes 3-5 business days.", "Same-day delivery is available in select areas."],
        "return": ["You can return unopened items within 7 days.", "Returns accepted within 7 days of purchase."],
        "exchange": ["You can return unopened items within 7 days.", "Returns accepted within 7 days of purchase."],
        "refund": ["Your refund will be processed within 7 days.", "Refunds are initiated once the returned item is received."],
        "price of milk": ["Milk is 30rs per liter."],
        "price of eggs": ["A dozen eggs cost 80rs."],
        "price of rice": ["Rice is 50rs per kg."],
        "timing": ["Our store is open from 8 AM to 10 PM every day."],
        "hours": ["Our store is open from 8 AM to 10 PM every day."],
        "location": ["We are located at XYZ Market, Main Street, City."],
        "address": ["We are located at XYZ Market, Main Street, City."],
        "payment": ["We accept cash, credit/debit cards, and UPI payments."],
        "issue": ["For any query, contact 24389.", "You can also visit our help center at www.help.com."],
        "problem": ["For any query, contact 24389.", "You can also visit our help center at www.help.com."],
        "thank you": ["You're welcome!"]
    }

# Title
st.title("🛒 Grocery Store Rule-Based Chatbot")

# Input box
user_input = st.text_input("Enter your grocery query here:")

# Button row
col1, col2 = st.columns([1, 0.1])
with col1:
    ask = st.button("Ask")
with col2:
    quit = st.button("Quit")

# Logic
if ask and user_input:
    key = user_input.lower()
    if key in st.session_state.knowledge_base:
        for response in st.session_state.knowledge_base[key]:
            st.write(response)
    else:
        st.warning("Question not present in the knowledge base.")
        st.session_state['new_question'] = key

if 'new_question' in st.session_state and st.session_state['new_question']:
    st.info("You can add an answer for: " + st.session_state['new_question'])
    new_answer = st.text_input("Enter answer:", key="answer_input")
    if st.button("Add answer"):
        if new_answer:
            st.session_state.knowledge_base[st.session_state['new_question']] = [new_answer]
            st.success("Answer added to knowledge base!")
            st.session_state['new_question'] = ""  # Reset

if quit:
    st.write("👋 Thank you for using Grocery Buddy!")
