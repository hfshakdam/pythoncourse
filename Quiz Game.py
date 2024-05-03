def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C or D: ").upper()
        guesses.append(guess)
#literally don't know why it doesn't work
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1 #every iteration of the loop adds 1 to the index

    display_score(correct_guesses, guesses)
def check_answer(answer_guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("wrong")
        return 0
def display_score(correct_guesses, guesses):
    print("---------------")
    print("Results:")
    print("---------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print("")

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print("")

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    response = input("Wanna play again? (yes or no)").upper()

    if response == "YES":
        return True
    else:
        return False

questions = { #key:value pairs
    "Who created Python: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Rick and Morty"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("bye")