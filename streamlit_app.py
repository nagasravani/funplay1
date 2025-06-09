import streamlit as st
import time
import random
# Define trivia questions and answers
QUESTIONS = [
  {"question": "D-SNP stands for", "options": ["Dual Super Number Plans", "Dual Special Needs Programs", "Dual Eligible Specific Need Plan", "Dual Eligible Special Needs Plans"], "answer": "Dual Eligible Special Needs Plans"},
    {"question": "SDOH stands for", "options": ["Society Determinants of Humans", "Same Determinants of Health", "Social Determinants of Health", "Social Dual of Health"], "answer": "Social Determinants of Health"},
    {"question": "HEDIS stands for", "options": ["Healthcare Effectiveness Data and Information Set", "Health Enumerate Data and Intelligence Set", "Human Effectiveness Device and Information Set", "Healthcare Efficient Data and Information Source"], "answer": "Healthcare Effectiveness Data and Information Set"},
    {"question": "CAHPS stands for", "options": ["Continued Assessment of Health Providers and Sources", "Consumer Assessment of Healthcare Providers and Systems", "Consumer Arrival of Health Providers and Sources", "Count Assessment of Healthcare People and Systems"], "answer": "Consumer Assessment of Healthcare Providers and Systems"},
    {"question": "HNA stands for", "options": ["Health Numeric Assessment", "Health Needs Assessment", "Health Nature Assessment", "Health Needs Assignment"], "answer": "Health Needs Assessment"},
    {"question": "HIPAA stands for", "options": ["Health Insure Portability and Arrival Act", "Health Intelligence Profitability and Accountability Act", "Health Insurance Portability and Accountability Act", "Health Intelligence Portability and Assessment Act"], "answer": "Health Insurance Portability and Accountability Act"},
    {"question": "PHI stands for", "options": ["Permanent Health Insurance", "Protected Health Information", "Protected Health Insurance", "Protected Human Information"], "answer": "Protected Health Information"},
    {"question": "SDOH stands for", "options": ["Social Determinants of Health", "Social Determinants of Humans", "Semi Determinants of Health", "Social Doers of Health"], "answer": "Social Determinants of Health"},
    {"question": "LHPC stands for", "options": ["Local Health Programs of California", "Local Health Plans of California", "Life Health Plans of California", "Live Health Plans of California"], "answer": "Local Health Plans of California"},
    {"question": "CMS stands for", "options": ["Centers for Medicare & Medicaid Services", "Centers for Medicare & Medicaid Supplies", "Community for Medicare & Medicaid Services", "Centers for Medicare & Medicaid Standards"], "answer": "Centers for Medicare & Medicaid Services"}
]

#random.shuffle(QUESTIONS)

def main():
    st.set_page_config(page_title="Trivia Game", layout="centered")
    st.markdown("""
        <style>
            body { background-color: #1E1E1E; color: #FF8C00; font-family: Arial, sans-serif; }
            .title { text-align: center; color: #FFD700; font-size: 45px; font-weight: bold; padding: 20px; }
            .question { text-align: center; color: #FF8C00; font-size: 26px; font-weight: bold; padding: 15px; background-color: #333; border-radius: 15px; }
            .option-button { background-color: #444; color: white; font-size: 22px; padding: 15px; margin: 8px; border-radius: 20px; width: 100%; text-align: center; transition: 0.3s; border: 2px solid #FFA500; cursor: pointer; }
            .option-button:hover { background-color: #FF8C00; color: white; transform: scale(1.07); }
            .score { text-align: center; color: #FFD700; font-size: 28px; padding: 12px; }
            .timer { text-align: center; color: #FF4444; font-size: 22px; font-weight: bold; }
            .correct { background-color: #4CAF50 !important; color: white !important; }
            .wrong { background-color: #FF5733 !important; color: white !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🔥 Ultimate Trivia Challenge! 🔥</div>", unsafe_allow_html=True)
    
    username = st.text_input("Enter your name to start:", placeholder="Type your name here...")
    if not username:
        st.warning("Please enter your name to begin.")
        st.stop()

    if 'user_sessions' not in st.session_state:
        st.session_state.user_sessions = {}

    if username not in st.session_state.user_sessions:
        st.session_state.user_sessions[username] = {
            'current_question': 0,
            'score': 0,
            'selected_option': None,
            'show_answer': False,
            'time_left': 60,
            'start_time': time.time()
        }

    user_data = st.session_state.user_sessions[username]
    elapsed_time = int(time.time() - user_data['start_time'])
    user_data['time_left'] = max(60 - elapsed_time, 0)
    
    st.markdown(f"<div class='score'>Score: {'⭐' * user_data['score']}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown(f"<div class='timer'>⏳ Time Left: {user_data['time_left']} sec</div>", unsafe_allow_html=True)
    
    if user_data['time_left'] == 0:
        st.error("⏳ Time's up! Game Over!")
        if st.button("🔄 Play Again"):
            del st.session_state.user_sessions[username]
            st.rerun()
    elif user_data['current_question'] < len(QUESTIONS):
        question_data = QUESTIONS[user_data['current_question']]
        st.markdown(f"<div class='question'>{user_data['current_question'] + 1}. {question_data['question']}</div>", unsafe_allow_html=True)

        for option in question_data['options']:
            if st.button(option, key=f"{username}_q{user_data['current_question']}_option_{option}", help="Click to select answer"):
                user_data['selected_option'] = option
                user_data['show_answer'] = True
                if option == question_data['answer']:
                    user_data['score'] += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! The correct answer was **{question_data['answer']}**.")
                st.session_state.user_sessions[username] = user_data
                time.sleep(1)
                user_data['current_question'] += 1
                user_data['selected_option'] = None
                user_data['show_answer'] = False
                st.session_state.user_sessions[username] = user_data
                st.rerun()
    else:
        st.success(f"🎉 Game Over! {username}, you scored {'⭐' * user_data['score']}! 🎉")
        if st.button("🔄 Play Again"):
            del st.session_state.user_sessions[username]
            st.rerun()

if __name__ == "__main__":
    main()
