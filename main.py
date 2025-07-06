def riddle_quiz():
    riddles = {
        "What has keys but can't open locks?": "A piano",
        "What has to be broken before you can use it?": "An egg",
        "I’m tall when I’m young, and I’m short when I’m old. What am I?": "A candle",
        "What begins with T, ends with T, and has T in it?": "A teapot",
    }

    score = 0

    print("Welcome to the Riddle Quiz!")
    print("Try to answer the following riddles:\n")

    for riddle, answer in riddles.items():
        user_answer = input(riddle + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}\n")

    print(f"You scored {score} out of {len(riddles)}.")

if __name__ == "__main__":
    riddle_quiz()