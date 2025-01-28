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
            background-color: #fffc5;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .question-card {
            background: white;
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
        .options {
            color: #4169e1;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(page_title="Trivia Game", layout="centered")
    custom_style()

    st.title("🎉 Welcome to the Trivia Game! 🎉")

    # Initialize session state variables
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'time_left' not in st.session_state:
        st.session_state.time_left = 60
    if 'answered' not in st.session_state:
        st.session_state.answered = False

    # Timer logic
    if st.session_state.time_left > 0:
        timer_placeholder = st.empty()
        with timer_placeholder:
            st.markdown(f"<div class='timer'>⏳ Time left: {st.session_state.time_left} seconds</div>", unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.time_left -= 1
        timer_placeholder.empty()
    else:
        st.warning("⏰ Time's up! The game is over.")
        st.markdown(f"<div class='score'>Your final score is {st.session_state.score}.</div>", unsafe_allow_html=True)
        return

    # Display current question
    question = QUESTIONS[st.session_state.current_question]
    st.markdown(f"<div class='question-card'><strong>Question {st.session_state.current_question + 1}: </strong>{question['question']}</div>", unsafe_allow_html=True)

    # Display options
    selected_option = st.radio(
        "Choose your answer:", 
        [f"<span class='options'>{opt}</span>" for opt in question['options']],
        format_func=lambda x: x,  # Ensures proper rendering
        key=f"q{st.session_state.current_question}"
    )

    # Submit button
    if st.button("Submit"):
        if not st.session_state.answered:
            st.session_state.answered = True
            if selected_option.strip() == question['answer']:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer was {question['answer']}.")
            
            # Proceed to next question or end game
            if st.session_state.current_question < len(QUESTIONS) - 1:
                st.session_state.current_question += 1
                st.session_state.answered = False
            else:
                st.balloons()
                st.markdown(f"<div class='score'>🎉 You've completed the game! Your final score is {st.session_state.score}.</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score'>Score: {st.session_state.score}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='timer'>⏳ Time left: {st.session_state.time_left} seconds</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
