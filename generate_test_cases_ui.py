import streamlit as st

def generate_test_cases(feature):
    test_cases = []

    if "login" in feature.lower():
        test_cases.append("Valid login with correct username & password")
        test_cases.append("Invalid login with wrong password")
        test_cases.append("Empty username and password")
        test_cases.append("Password case sensitivity check")

    elif "signup" in feature.lower():
        test_cases.append("Valid signup with all fields")
        test_cases.append("Email already exists")
        test_cases.append("Weak password check")
        test_cases.append("Empty fields")

    else:
        test_cases.append(f"Valid input for {feature}")
        test_cases.append(f"Invalid input for {feature}")
        test_cases.append(f"Empty input for {feature}")

    return test_cases


st.title("AI Test Case Generator 🚀")

feature = st.text_input("Enter Feature (e.g. login, signup)")

if st.button("Generate Test Cases"):
    cases = generate_test_cases(feature)

    st.subheader("Generated Test Cases:")
    for i, case in enumerate(cases, 1):
        st.write(f"{i}. {case}")