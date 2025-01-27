import streamlit as st
import random
import time

# Questions and answers
questions = [
{"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Jane Austen"], "answer": "William Shakespeare"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "N2"], "answer": "H2O"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which country invented pizza?", "options": ["France", "Italy", "USA", "Greece"], "answer": "Italy"},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "answer": "Leonardo da Vinci"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Whale Shark", "Blue Whale", "Giraffe"], "answer": "Blue Whale"},
    {"question": "What is the square root of 64?", "options": ["6", "8", "10", "12"], "answer": "8"},
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

            if st.button("Submit", key=f"submit{player_state['current_question']}"):
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
