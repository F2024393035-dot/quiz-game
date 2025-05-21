import streamlit as st
import pandas as pd

# Load the quiz questions CSV
df = pd.read_csv("quiz_questions.csv")

st.set_page_config(page_title="ML Quiz Game", layout="centered")
st.title("🧠 ML-Based Quiz Game")
st.markdown("Test your knowledge in Data Science and Machine Learning!")

# Initialize score
score = 0

# Loop through each question
for i in range(len(df)):
    st.markdown(f"### Q{i+1}: {df.iloc[i]['question']}")
    
    # Display answer options
    options = [df.iloc[i][f"option{j}"] for j in range(1, 5)]
    answer = st.radio("Choose your answer:", options, key=f"q{i}")

    # Check the correct answer
    correct_index = int(df.iloc[i]['correct']) - 1  # Convert to 0-based index
    if answer == options[correct_index]:
        st.success("✅ Correct!")
        score += 1
    else:
        st.error(f"❌ Wrong! Correct answer: {options[correct_index]}")

    st.markdown("---")

# Final score
st.markdown(f"## 🎯 Your Final Score: `{score} / {len(df)}`")
