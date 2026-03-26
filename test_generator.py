def generate_test_cases(feature):
    test_cases = []

    if "login" in feature.lower():
        test_cases.append("Test 1: Valid login with correct username & password")
        test_cases.append("Test 2: Invalid login with wrong password")
        test_cases.append("Test 3: Empty username and password")
        test_cases.append("Test 4: Password case sensitivity check")

    elif "signup" in feature.lower():
        test_cases.append("Test 1: Valid signup with all fields")
        test_cases.append("Test 2: Email already exists")
        test_cases.append("Test 3: Weak password check")
        test_cases.append("Test 4: Empty fields")

    else:
        test_cases.append(f"Test 1: Valid input for {feature}")
        test_cases.append(f"Test 2: Invalid input for {feature}")
        test_cases.append(f"Test 3: Empty input for {feature}")

    return test_cases


feature = input("Enter feature: ")
cases = generate_test_cases(feature)

for case in cases:
    print(case)
