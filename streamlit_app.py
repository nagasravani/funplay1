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

def custom_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #6699cc;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .question-card {
            background: orange;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .timer {
            font-size: 1.5rem;
            font-weight: bold;
            color: #f44336;
        }
        .score {
            font-size: 1.2rem;
            font-weight: bold;
            color: #4caf50;
        }
        .option-button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 15px;
            margin: 5px;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
        }
        .option-button:hover {
            background-color: #0056b3;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(page_title="Trivia Game", layout="centered")
    custom_style()

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
            'asked_questions': set()
        }

    user_data = st.session_state.user_sessions[username]

    # Timer logic
    time_elapsed = time.time() - user_data['start_time']
    user_data['time_left'] = max(0, 20 - int(time_elapsed))

    if user_data['time_left'] == 0:
        st.warning(f"⏰ Time's up, {username}! The game is over.")
        st.markdown(f"<div class='score'>Your final score is {user_data['score']}.</div>", unsafe_allow_html=True)
        st.stop()

    timer_placeholder = st.empty()
    with timer_placeholder:
        st.markdown(f"<div class='timer'>⏳ Time left: {user_data['time_left']} seconds</div>", unsafe_allow_html=True)

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
            st.markdown(f"<div class='question-card'><strong>Question {user_data['current_question'] + 1}: </strong>{question['question']}</div>", unsafe_allow_html=True)

            # Display options as buttons
            col1, col2 = st.columns(2)
            for i, option in enumerate(question['options']):
                with col1 if i % 2 == 0 else col2:
                    if st.button(option, key=f"{username}_q{user_data['current_question']}_option{i}", use_container_width=True):
                        if option == question['answer']:
                            st.success("✅ Correct!")
                            user_data['score'] += 1
                            st.markdown(f"<div class='score'>Your updated score is {user_data['score']}!</div>", unsafe_allow_html=True)
                        else:
                            st.error(f"❌ Wrong! The correct answer was {question['answer']}.")

                        if user_data['current_question'] < len(QUESTIONS) - 1:
                            user_data['current_question'] += 1
                            user_data['start_time'] = time.time()
                            st.experimental_rerun()
                        else:
                            st.balloons()
                            st.markdown(f"<div class='score'>🎉 You've completed the game, {username}! Your final score is {user_data['score']}.</div>", unsafe_allow_html=True)
                            st.stop()

    st.markdown(f"<div class='score'>Score: {user_data['score']}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
