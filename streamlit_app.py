import streamlit as st
import random
import time

# Questions and answers
questions = [
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
random.shuffle(questions)

# Game state
if "players" not in st.session_state:
    st.session_state.players = {}

# Main function to run the game
def main():
    # Initialize player session
    player_id = st.text_input("Enter your name to start the game:")
    if player_id and player_id not in st.session_state.players:
        st.session_state.players[player_id] = {
            "score": 0,
            "current_question": 0,
            "start_time": time.time(),
        }

    if player_id and player_id in st.session_state.players:
        player_state = st.session_state.players[player_id]

        # Timer
        elapsed_time = time.time() - player_state["start_time"]
        remaining_time = 60 - elapsed_time
        if remaining_time <= 0:
            st.write(f"### Time's up, {player_id}! The game is over!")
            st.write(f"Your final score is: {player_state['score']}/{len(questions)} 🎉")
            if player_state['score'] == len(questions):
                st.write("🎉🎉🎉 Perfect score! Excellent! 🎉🎉🎉")
            elif player_state['score'] >= 7:
                st.write("😊😊 Great job! 😊😊")
            elif player_state['score'] >= 4:
                st.write("🙂 Keep practicing! 🙂")
            else:
                st.write("😔 Better luck next time! 😔")
            st.stop()

        st.write(f"**Time Remaining:** {int(remaining_time)} seconds")

        # Display question
        if player_state["current_question"] < len(questions):
            question = questions[player_state["current_question"]]
            st.write(f"**Question {player_state['current_question'] + 1}:** {question['question']}")

            options = question["options"]
            user_answer = st.radio("Select your answer:", options, key=f"q{player_state['current_question']}")

            if st.button("Next", key=f"next{player_state['current_question']}"):
                if user_answer == question["answer"]:
                    st.success("Correct!")
                    player_state["score"] += 1
                else:
                    st.error(f"Wrong! The correct answer is: {question['answer']}")

                player_state["current_question"] += 1
        else:
            st.write(f"### Game Over! {player_id}, your final score is: {player_state['score']}/{len(questions)} 🎉")
            if player_state['score'] == len(questions):
                st.write("🎉🎉🎉 Perfect score! Excellent! 🎉🎉🎉")
            elif player_state['score'] >= 7:
                st.write("😊😊 Great job! 😊😊")
            elif player_state['score'] >= 4:
                st.write("🙂 Keep practicing! 🙂")
            else:
                st.write("😔 Better luck next time! 😔")

            # Restart game option
            if st.button("Play Again"):
                st.session_state.players[player_id] = {
                    "score": 0,
                    "current_question": 0,
                    "start_time": time.time(),
                }

if __name__ == "__main__":
    main()
