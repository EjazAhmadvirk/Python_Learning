mark = []
subjects = [
    "Biology", "Math", "English", "Physics", "Chemistry",
    "Computer Science", "History", "Geography", "Economics", "Political Science"
]

for subject in subjects:
    while True:
        try:
            score = int(input(f"Enter the number of {subject}: "))
            mark.append(score)
            break
        except ValueError:
            print("Please enter a valid integer.")

print(mark)







