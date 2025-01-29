import streamlit as st
import time
import random
# Define trivia questions and answers
QUESTIONS = [
    {"question": "URL stands for", "options": ["Unit Resource Load", "Uniform Read Locator", "Uniform Resource Locator", "Unit Resource Locator"], "answer": "Uniform Resource Locator"},
    {"question": "IVR stands for", "options": ["Interest Voice Record", "Interactive Voice Response", "Interactive Voice Record", "Interesting Voice Report"], "answer": "Interactive Voice Response"},
    {"question": "POD stands for", "options": ["Product Oriented Delivery", "Product Oriented Department", "Primary Oriented Device", "Product Oriented Development"], "answer": "Product Oriented Delivery"},
    {"question": "RCA stands for", "options": ["Route Cause Anomaly", "Random Care Analysis", "Root Cause Analysis", "Random Cause Analysis"], "answer": "Root Cause Analysis"},
    {"question": "MVP stands for", "options": ["Minimum Viable Product", "Maximum Viable Product", "Minimum Visible Product", "Minimum Variable Price"], "answer": "Minimum Viable Product"},
    {"question": "PDI stands for", "options": ["Price Demand Id", "Product Demand Ideas", "Product Diverse Ideas", "Product Discovery Ideas"], "answer": "Product Discovery Ideas"},
    {"question": "KPI stands for", "options": ["Key Program Indicator", "Key Progress Indicator", "Key Performance Indicator", "Key Preference Indicator"], "answer": "Key Performance Indicator"},
    {"question": "SSO stands for", "options": ["Simple Sign On", "Sample Sign On", "Single Sign One", "Single Sign On"], "answer": "Single Sign On"},
    {"question": "IDA stands for", "options": ["Interesting Document Analysis", "Intelligent Document Automation", "Inverse Document Analysis", "Intelligent Diverse Automation"], "answer": "Intelligent Document Automation"},
    {"question": "DISA stands for", "options": ["Dormant Intelligence Switch Architecture", "Device Intelligence Service Architecture", "Document Intelligence Solution Architecture", "Document Intelligence Solution Analysis"], "answer": "Document Intelligence Solution Architecture"}
]

random.shuffle(QUESTIONS)

def main():
    st.set_page_config(page_title="Trivia Game", layout="centered")
    st.title("🎉 Welcome to the Trivia Game! 🎉")

    # User identification for multiplayer support
    username = st.text_input("Enter your name to start:")
    if not username:
        st.warning("Please enter your name to begin.")
        st.stop()

    # Initialize session state variables per user
    if 'user_sessions' not in st.session_state:
        st.session_state.user_sessions = {}

    if username not in st.session_state.user_sessions:
        st.session_state.user_sessions[username] = {
            'current_question': 0,
            'score': 0,
            'time_left': 20,
            'start_time': time.time(),
            'asked_questions': set(),
            'last_answer_correct': None
        }

    user_data = st.session_state.user_sessions[username]

    # Timer logic
    time_elapsed = time.time() - user_data['start_time']
    user_data['time_left'] = max(0, 20 - int(time_elapsed))

    if user_data['time_left'] == 0:
        st.warning(f"⏰ Time's up, {username}! The game is over.")
        st.markdown(f"### Final Score: {'⭐' * user_data['score']} {'🍏' * (len(QUESTIONS) - user_data['score'])}")
        st.stop()

    st.markdown(f"## ⏳ Time left: {user_data['time_left']} seconds")
    st.markdown(f"### Score: {'⭐' * user_data['score']} {'🍏' * (user_data['current_question'] - user_data['score'])}")

    # Ensure question is not repeated
    if user_data['current_question'] < len(QUESTIONS):
        question = QUESTIONS[user_data['current_question']]
        while question['question'] in user_data['asked_questions']:
            user_data['current_question'] += 1
            if user_data['current_question'] >= len(QUESTIONS):
                break
            question = QUESTIONS[user_data['current_question']]

        if user_data['current_question'] < len(QUESTIONS):
            user_data['asked_questions'].add(question['question'])
            st.markdown(f"### {user_data['current_question'] + 1}. {question['question']}")

            # Display options as buttons
            for option in question['options']:
                button_key = f"{username}_q{user_data['current_question']}_option_{option}"
                if st.button(option, key=button_key):
                    if option == question['answer']:
                        user_data['score'] += 1
                        user_data['last_answer_correct'] = True
                    else:
                        user_data['last_answer_correct'] = False
                    user_data['start_time'] = time.time()
                    st.experimental_rerun()

            # Show correct or incorrect message before rerun
            if user_data['last_answer_correct'] is not None:
                if user_data['last_answer_correct']:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! The correct answer was {question['answer']}.")
                time.sleep(1.5)  # Wait before rerun
                user_data['current_question'] += 1
                user_data['last_answer_correct'] = None
                st.experimental_rerun()

    else:
        st.balloons()
        st.markdown(f"### 🎉 Game Over! Your final score is {'⭐' * user_data['score']} {'🍏' * (len(QUESTIONS) - user_data['score'])}")
        st.markdown("#### 🔄 Click Restart to play again!")
        if st.button("Restart"):
            del st.session_state.user_sessions[username]
            st.experimental_rerun()
        st.stop()

if __name__ == "__main__":
    main()

