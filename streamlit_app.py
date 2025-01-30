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
    st.markdown("""
        <style>
            .title { text-align: center; color: #FF5733; font-size: 36px; font-weight: bold; }
            .question { color: #FF9900; font-size: 24px; font-weight: bold; padding: 10px; }
            .option-button { background-color: #FFFFFF; color: #000000; font-size: 18px; padding: 10px; margin: 5px; border-radius: 10px; width: 100%; text-align: center; }
            .option-button:hover { background-color: #00CC66; color: white; }
            .score { color: #FFD700; font-size: 20px; }
            .timer { color: #FF0000; font-size: 18px; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🎉 Welcome to the Trivia Game! 🎉</div>", unsafe_allow_html=True)
    
    username = st.text_input("Enter your name to start:")
    if not username:
        st.warning("Please enter your name to begin.")
        st.stop()

    if 'user_sessions' not in st.session_state:
        st.session_state.user_sessions = {}

    if username not in st.session_state.user_sessions:
        st.session_state.user_sessions[username] = {
            'current_question': 0,
            'score': 0,
            'asked_questions': set(),
            'selected_option': None,
            'show_answer': False,
            'time_left': 60
        }

    user_data = st.session_state.user_sessions[username]
    st.markdown(f"<div class='score'>Score: {'⭐' * user_data['score']} {'🍏' * (user_data['current_question'] - user_data['score'])}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown(f"<div class='timer'>⏳ Time Left: {user_data['time_left']} sec</div>", unsafe_allow_html=True)
    
    if user_data['time_left'] > 0:
        time.sleep(1)
        user_data['time_left'] -= 1
        st.session_state.user_sessions[username] = user_data
        st.rerun()
    else:
        st.error("Time's up! Game Over.")
        time.sleep(2)
        del st.session_state.user_sessions[username]
        st.rerun()

    if user_data['current_question'] < len(QUESTIONS):
        question = QUESTIONS[user_data['current_question']]
        if question['question'] not in user_data['asked_questions']:
            user_data['asked_questions'].add(question['question'])

        st.markdown(f"<div class='question'>{user_data['current_question'] + 1}. {question['question']}</div>", unsafe_allow_html=True)

        for option in question['options']:
            button_key = f"{username}_q{user_data['current_question']}_option_{option}"
            if st.button(option, key=button_key):
                user_data['selected_option'] = option
                user_data['show_answer'] = True
                if option == question['answer']:
                    user_data['score'] += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! The correct answer was **{question['answer']}**.")
                st.session_state.user_sessions[username] = user_data
                time.sleep(1)
                user_data['current_question'] += 1
                user_data['selected_option'] = None
                user_data['show_answer'] = False
                st.session_state.user_sessions[username] = user_data
                st.rerun()

    else:
        st.balloons()
        st.markdown(f"### 🎉 Game Over! Your final score is {'⭐' * user_data['score']} {'🍏' * (len(QUESTIONS) - user_data['score'])}")
        st.markdown("#### 🔄 Click Restart to play again!")
        if st.button("Restart"):
            del st.session_state.user_sessions[username]
            st.rerun()
        st.stop()

if __name__ == "__main__":
    main()
