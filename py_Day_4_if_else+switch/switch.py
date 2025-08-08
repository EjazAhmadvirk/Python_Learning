grade = input("Enter your grade:   ")
switch = {
    'A': "Excellent!",
    'B': "Good job!",
    'C': "You passed.",
    'D': "You need to improve.",
    'F': "Failed. Better luck next time."
}
print(switch.get(grade, "Invalid grade."))