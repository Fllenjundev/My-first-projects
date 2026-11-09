classroom = {}
print("How many students will you be recording today? ")
students = int(input())
for i in range(students):

  while True:
    print("Insert your name")
    name = input()
    if name.isdigit() or len(name) > 12:
        print("Try again...")
    else:
        break

  while True:
    try:
        print("Insert grade")
        grade = int(input())
        if 0 <= grade <= 100:
            break
        else:
            print("Try again baka...")
    except ValueError:
        print("Try again...")

  classroom[name] = grade
print(classroom)

total_score = 0
current_score = 0
highest_mark = -1
top_student = ""

for name, grade in classroom.items():
   total_score += grade
   current_score = grade
   if current_score > highest_mark:
      highest_mark = current_score
      top_student = name

average = total_score // students
print(f"The classes average is {average}")
print(f"The top student is {top_student} with a mark of {highest_mark}")
   

    

