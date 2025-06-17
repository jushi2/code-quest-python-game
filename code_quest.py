def level_1():
    print("\n🎯 Level 1: Conditional Trap")
    x = int(input("Enter a number: "))
    if x >= 10:
        print("Big")
    else:
        print("Small")


def level_2():
    print("\n🔁 Level 2: Infinite Loop Escape")
    counter = 1
    while True:
        print("Step", counter)
        if counter == 5:
            print("You escaped the loop!")
            break
        else:
            counter += 1


def level_3():
    print("\n🔒 Level 3: The Password Gate")
    correct_password = "openSesame"
    attempts_left = 3
    while attempts_left > 0:
        password = input(f"Enter password ({attempts_left} attempts left): ")
        if password == correct_password:
            print("Access Granted")
            break
        else:
            attempts_left -= 1
            print("Access Denied!")
            if attempts_left == 0:
                print("No attempts remaining. Access locked.")


def level_4():
    print("\n🧠 Level 4: The True/False Quiz")
    quiz = [
        {"question": "Python is a snake.", "answer": "False"},
        {"question": "Python can be used for web development.", "answer": "True"},
        {"question": "2 + 2 = 5", "answer": "False"},
        {"question": "Lists are mutable in Python.", "answer": "True"},
    ]
    score = 0
    for item in quiz:
        user_answer = input(item["question"] + " (True/False): ")
        if user_answer.lower() == item["answer"].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", item["answer"])
    print(f"Quiz completed! Your score is {score} out of {len(quiz)}")


def show_menu():
    print("\n🎮 Welcome to CODE QUEST 🎮")
    print("Select a level to begin:")
    print("1. Level 1 - Conditional Trap")
    print("2. Level 2 - Infinite Loop")
    print("3. Level 3 - Password Gate")
    print("4. Level 4 - Quiz Core")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            level_1()
        elif choice == "2":
            level_2()
        elif choice == "3":
            level_3()
        elif choice == "4":
            level_4()
        elif choice == "5":
            print("Thanks for playing Code Quest. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Ask if user wants to return to menu or quit
        again = input("\nDo you want to return to the main menu? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for playing Code Quest. See you soon!")
            break


if __name__ == "__main__":
    main()
