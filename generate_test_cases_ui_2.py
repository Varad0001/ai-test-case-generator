import streamlit as st
import pandas as pd
from generator import generate_test_cases

st.title("AI Test Case Generator 🚀")
st.write("Generate structured software test cases instantly!")

feature = st.text_input("Enter Feature (e.g. login, signup, payment)")


valid_features = ["login", "signup", "payment"]

if st.button("Generate Test Cases"):

    # 🔴 Empty input
    if not feature:
        st.warning("⚠️ Please enter a feature!")
    
    # 🔴 Unknown feature warning
    elif not any(f in feature.lower() for f in valid_features):
        st.error("❌ Unknown feature! Showing generic test cases.")

        cases = generate_test_cases(feature)

    else:
        cases = generate_test_cases(feature)

    # 👉 Output
    if feature:
        st.subheader("Generated Test Cases:")

        for category, items in cases.items():
            st.markdown(f"### {category} Tests")

            for i, case in enumerate(items, 1):

                case_lower = case.lower()

                if "valid" in case_lower:
                    st.success(f"{i}. {case}")   # 🟢 Green

                elif "invalid" in case_lower or "wrong" in case_lower:
                    st.error(f"{i}. {case}")     # 🔴 Red

                elif "empty" in case_lower:
                    st.warning(f"{i}. {case}")   # 🟡 Yellow

                else:
                    st.info(f"{i}. {case}")      # 🔵 Blue

        # 📥 Download CSV
        all_cases = []
        for category, items in cases.items():
            for case in items:
                all_cases.append({"Type": category, "Test Case": case})

        df = pd.DataFrame(all_cases)

        st.download_button(
            label="📥 Download Test Cases (CSV)",
            data=df.to_csv(index=False),
            file_name="test_cases.csv",
            mime="text/csv"
        )
