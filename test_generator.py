def generate_test_cases(input_text):
    test_cases = []

    if "login" in input_text.lower():
        test_cases.append("Test 1: Valid username and password")
        test_cases.append("Test 2: Invalid password")
        test_cases.append("Test 3: Empty fields")
    elif "signup" in input_text.lower():
        test_cases.append("Test 1: Valid registration details")
        test_cases.append("Test 2: Email already exists")
        test_cases.append("Test 3: Weak password")
    else:
        test_cases.append(f"Test 1: Valid input for {input_text}")
        test_cases.append(f"Test 2: Invalid input for {input_text}")
        test_cases.append(f"Test 3: Empty input for {input_text}")

    return test_cases


user_input = input("Enter feature: ")

cases = generate_test_cases(user_input)

for case in cases:
    print(case)