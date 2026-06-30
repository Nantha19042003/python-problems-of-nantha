# Scenario-Based Question 4

## Student Grade Calculator

A school wants to automate the process of assigning grades to students based on their marks.

**Rules:**

* **90–100** → Grade **A**
* **75–89** → Grade **B**
* **60–74** → Grade **C**
* **50–59** → Grade **D**
* **Below 50** → Grade **F (Fail)**

**Task:**

1. Accept the student's marks from the user.
2. Determine the grade based on the marks.
3. Display the marks and the grade.

### Python Program

```python
# Student Grade Calculator

marks = int(input("Enter Student Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n------ Student Result ------")
print("Marks :", marks)
print("Grade :", grade)
```

### Sample Output 1

```text
Enter Student Marks: 92

------ Student Result ------
Marks : 92
Grade : A
```

### Sample Output 2

```text
Enter Student Marks: 48

------ Student Result ------
Marks : 48
Grade : F (Fail)
```
