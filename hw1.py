i = 1
right_answers = 0
answer = ""
while i < 10:
    if i == 1:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 2:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 3:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 4:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 5:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 6:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 7:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 8:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 9:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    elif i == 10:
        answer = "Right" if input("Question 1: ").lower() == "10" else "Wrong"
    i = i + 1
    print(answer)
    if answer == "Right":
        right_answers += 1
print("You gave {} answers".format(right_answers))


