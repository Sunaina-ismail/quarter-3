import streamlit as st


def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2


st.title("🏋️‍♀️ Simple BMI Calculator ")

height = st.number_input("📏 Enter your height (cm):", min_value=100, max_value=250, value=170, step=1)
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=40, max_value=200, value=70, step=1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"## Your BMI: **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("You are **Underweight**. Consider a nutritious diet.")
    elif 18.5 <= bmi <= 24.9:
        st.success("Your weight is **Normal**. Great job! 😊")
    elif 25 <= bmi <= 29.9:
        st.warning("You are **Overweight**. A healthy lifestyle is recommended.")
    else:
        st.error("You are in the **Obesity** category. Focus on your health.")


st.write("### What Your BMI Means:")
st.write("- **Underweight**: BMI is **less than 18.5** → You may need to gain weight for better health.")
st.write("- **Normal weight**: BMI is **between 18.5 and 24.9** → You have a healthy weight. Keep it up! 😊")
st.write("- **Overweight**: BMI is **between 25 and 29.9** → You may need to manage your weight for better health.")
st.write("- **Obesity**: BMI is **30 or greater** → It's important to focus on a healthy lifestyle.")
