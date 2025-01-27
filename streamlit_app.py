import streamlit as st
import random
import time

# Questions and answers
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
    {"question": "DISA stands for", "options": ["Dormant Intelligence Switch Architecture", "Device Intelligence Service Architecture", "Document Intelligence Solution Architecture", "Document Intelligence Solution Analysis"], "answer": "Document Intelligence Solution Architecture"},
]
# Shuffle questions to add variety
random.shuffle(QUESTIONS)

def main():
    st.title("Trivia Game")
    
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
        with st.empty():
            for i in range(st.session_state.time_left, -1, -1):
                st.session_state.time_left = i
                time.sleep(1)
    else:
        st.warning("Time's up! The game is over.")
        st.write(f"Your final score is {st.session_state.score}.")
        return

    # Display current question
    question = QUESTIONS[st.session_state.current_question]
    st.write(f"**Question {st.session_state.current_question + 1}:** {question['question']}")

    # Display options
    selected_option = st.radio("Choose your answer:", question['options'])

    # Submit button
    if st.button("Submit"):
        if not st.session_state.answered:
            st.session_state.answered = True
            if selected_option == question['answer']:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! The correct answer was {question['answer']}.")
            
            # Proceed to next question or end game
            if st.session_state.current_question < len(QUESTIONS) - 1:
                st.session_state.current_question += 1
                st.session_state.answered = False
            else:
                st.success("You've completed the game!")
                st.write(f"Your final score is {st.session_state.score}.")

    st.write(f"Score: {st.session_state.score}")
    st.write(f"Time left: {st.session_state.time_left} seconds")

if __name__ == "__main__":
    main()
