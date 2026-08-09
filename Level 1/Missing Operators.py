import random

print("--- ROUND 1: Find the Missing Number ---")

for q in range(1, 4):
    print("Question", q, "of 3:")
    num1 = random.randint(1, 20)
    hidden_num = random.randint(1, 20)
    op_index = random.randint(0, 2)

    if op_index == 0:
        target = num1 + hidden_num
        op_word = "plus"
    elif op_index == 1:
        target = num1 - hidden_num
        op_word = "minus"
    else:
        target = num1 * hidden_num
        op_word = "times"

    print("Solev for missing number:")
    print(num1, op_word, "BLANK equals", target)
    
    try:
        user_guess = int(input("Your answer: "))
        if user_guess == hidden_num:
            print("Well done! Correct answer.\n")
        else:
            print("Incorrect. The missing number was", hidden_num, "\n")
    except ValueError:
        print("Invalid input! You must enter a whole number. The correct answer was", hidden_num, "\n")


print("---  ROUND 2: Double Missing Numbers --")

for q in range(1, 4):
    print("Question", q, "of 3:")
    start_num = random.randint(1, 15)
    hidden_a = random.randint(1, 10)
    hidden_b = random.randint(1, 10)

    op1_index = random.randint(0, 1)
    op2_index = random.randint(0, 1)

    if op1_index == 0:
        step1 = start_num + hidden_a
        op1_word = "plus"
    else:
        step1 = start_num - hidden_a
        op1_word = "minus"

    if op2_index == 0:
        final_target = step1 + hidden_b
        op2_word = "plus"
    else:
        final_target = step1 - hidden_b
        op2_word = "minus"

    print("Enter the two missing numbers separated by a space:")
    print(start_num, op1_word, "FIRST_BLANK", op2_word, "SECOND_BLANK equals", final_target)
    
    raw_answers = input("Your answers: ").split()
    
    try:
        if len(raw_answers) == 2 and int(raw_answers[0]) == hidden_a and int(raw_answers[1]) == hidden_b:
            print("Outstanding! You solved both missing numbers.\n")
        else:
            print("Not quite. The missing numbers were", hidden_a, "and", hidden_b, "\n")
    except ValueError:
        print("Invalid input! Please enter two whole numbers separated by a space. Missing numbers were", hidden_a, "and", hidden_b, "\n")


print("--- ROUND 3: Target Equation Puzzle ---")

for q in range(1, 4):
    print("Question", q, "of 3:")
    start_val = random.randint(2, 10)
    hidden_multiplier = random.randint(2, 5)
    hidden_adder = random.randint(1, 20)

    round3_target = (start_val * hidden_multiplier) + hidden_adder

    print("Find the multiplier and the bonus added at the end.")
    print("Start with", start_val, "then multiply by FIRST_BLANK then plus SECOND_BLANK to reach", round3_target)
    
    ans_r3 = input("Your answers: ").split()

    try:
        if len(ans_r3) == 2 and int(ans_r3[0]) == hidden_multiplier and int(ans_r3[1]) == hidden_adder:
            print("Mastermind! You beat the question.\n")
        else:
            print("Incorrect. The multiplier was", hidden_multiplier, "and the bonus was", hidden_adder, "\n")
    except ValueError:
        print("Invalid input! Please enter two whole numbers separated by a space. Multiplier was", hidden_multiplier, "and bonus was", hidden_adder, "\n")