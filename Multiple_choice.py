#menu system for the game

def menu():
    print("Welcome to Multiple Choice Game")
    print("1. Start Game")
    print("3. Make a new question")
    print("4. Delete a question")
    print("q. Exit Game")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Starting Game..")
        play_game()
    elif choice == "q":
        print("Exiting Game...")
        exit()
    elif choice == "3":
        print("Making a new question...")
        make_question()
    elif choice == "4":
        print("Deleting a question...")
        delete_question()
    else:
        print("Invalid Choice")
        menu()


def play_game():
    print("Playing Game...")
    fdev = open("questions.txt", "r")
    questions = fdev.readlines()
    fdev.close()
    score = 0
    total = len(questions)
    for question in questions:
        question = question.strip()
        question = question.split(" ~ ")
        print("Question: ", question[0])
        print("Choices: ", question[1], question[2], question[3], question[4])
        answer = input("Enter the correct answer: ")
        if answer == question[5]:
            print("Correct")
            score += 1
        elif answer == "q":
            score = score / total * 100
            print("Your score is: ", score)
            menu()
        else:
            print("Incorrect")
            print("Correct answer is: ", question[5])
    score = score / total * 100
    print("Your score is: ", score)
    menu()


def make_question():
    print("Making a question...")
    question = input("Enter your question: ")
    print("Enter your 4 choices")
    choice1 = input("Choice 1: ")
    choice2 = input("Choice 2: ")
    choice3 = input("Choice 3: ")
    choice4 = input("Choice 4: ")
    answer = input("Enter the correct answer: ")
    print("Question: ", question)
    print("Choices: ", choice1, choice2, choice3, choice4)
    print("Answer: ", answer)
    print("Saving question...")
    fdev = open("questions.txt", "a")
    fdev.write(question + " ~ " + choice1 + " ~ " + choice2 + " ~ " + choice3 + " ~ " + choice4 + " ~ " + answer + " \n")
    fdev.close()
    print("Question saved")
    menu()


def delete_question():
    print("Deleting a question...")
    fdev = open("questions.txt", "r")
    questions = fdev.readlines()
    
    fdev.close()
    print("Questions: ")
    index_val = 0
    for question in questions:
        question = question.strip()
        question = question.split(" ~ ")
        index_val += 1
        print(str(index_val) + '.', question[0])
    try: 
        question_number = int(input("Enter the question number to delete, or q to return to menu: "))
        if question_number > len(questions):
            print("Not a valid question number returning to menu")
            menu()
    except ValueError:
        print("Invalid input returning to menu")
        menu()
    questions.pop(question_number - 1)
    fdev = open("questions.txt", "w")
    fdev.writelines(questions)
    fdev.close()
    print("Question deleted")
    menu()


if __name__ == '__main__':
    menu()
