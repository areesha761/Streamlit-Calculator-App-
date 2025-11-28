# app.py
import streamlit as st
import time


st.set_page_config(page_title="Animated Calculator", page_icon="🧮", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .title {
            font-size: 48px;
            font-weight: 800;
            text-align: center;
            color: #4A90E2;
            animation: fadeIn 2s ease-in-out;
        }

        .result-box {
            padding: 20px;
            background: #f0f8ff;
            border-radius: 15px;
            font-size: 24px;
            text-align: center;
            margin-top: 20px;
            animation: pop 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes pop {
            0% { transform: scale(0.5); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Animation
st.markdown('<div class="title">✨ Animated Calculator ✨</div>', unsafe_allow_html=True)

st.write("## Enter Values Below")

# Animated Inputs
num1 = st.number_input("Enter first number", value=0.0, key="n1")
num2 = st.number_input("Enter second number", value=0.0, key="n2")

operation = st.selectbox(
    "Choose an Operation",
    ["➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"],
)

if st.button("Calculate", type="primary"):
    with st.spinner("Calculating..."):
        time.sleep(1)

    if operation == "➕ Add":
        result = num1 + num2
    elif operation == "➖ Subtract":
        result = num1 - num2
    elif operation == "✖ Multiply":
        result = num1 * num2
    elif operation == "➗ Divide":
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2

    st.markdown(f'<div class="result-box">✨ Result: <strong>{result}</strong> ✨</div>', unsafe_allow_html=True)



