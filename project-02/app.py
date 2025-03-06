import streamlit as st
import random
import string
import re


st.set_page_config(page_title="🔐Password Strength Meter", page_icon="🔑", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #0D0D0D;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .password-box {
            background: linear-gradient(45deg, #ffcc00, #ff6699);
            color: #000000;
            border-radius: 12px;
            padding: 14px;
            font-family: monospace;
            font-size: 1.3rem;
            word-break: break-word;
            text-align: center;
            font-weight: bold;
        }
        .strength-bar {
            height: 10px;
            border-radius: 5px;
            margin-top: 8px;
            transition: width 0.4s ease-in-out;
        }
        .custom-button {
            background: linear-gradient(90deg, #ff6699, #ffcc00);
            color: #0D0D0D;
            padding: 10px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .custom-button:hover {
            transform: scale(1.1);
            box-shadow: 0px 0px 15px #ffcc00;
        }
    </style>
""", unsafe_allow_html=True)

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("❌ At least 12 characters needed.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase & lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("❌ Add a special character.")

    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_colors = ["#ff4e50", "#ffa700", "#ffff00", "#aaff00", "#00ff00"]

    return score, feedback, strength_labels[min(score, 4)], strength_colors[min(score, 4)]

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

st.title("🔐Password Strength Meter")

password = st.text_input("🔐 Enter your password:", type="password")
if st.button("Check Strength", key="check", help="Click to check password strength"):
    if password:
        score, feedback, strength_text, strength_color = check_strength(password)
        st.markdown(f"<p style='font-weight: bold;'>Strength: {strength_text}</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='strength-bar' style='width: {score * 25}%; background-color: {strength_color};'></div>", unsafe_allow_html=True)
        if feedback:
            st.subheader("🔍 Suggestions:")
            for item in feedback:
                st.markdown(f"- {item}")
        else:
            st.success("✅ Your password is strong!")
    else:
        st.warning("⚠ Please enter a password.")


st.header("🔑 Generate a Secure Password")
length = st.slider("🔢 Password Length:", 8, 32, 16)
if st.button("Generate Password", key="generate", help="Click to generate a strong password"):
    new_password = generate_password(length)
    st.markdown(f"<div class='password-box'>{new_password}</div>", unsafe_allow_html=True)
