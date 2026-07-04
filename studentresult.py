3. Student Result System

Question:
A school wants to determine whether a student has passed or failed based on five subject marks. The passing mark for each subject is 35.

Answer:

marks = []

for i in range(5):
    mark = int(input(f"Enter Subject {i+1} Marks: "))
    marks.append(mark)

if min(marks) >= 35:
    print("PASS")
    print("Total:", sum(marks))
    print("Average:", sum(marks)/5)
else:
    print("FAIL")
 
