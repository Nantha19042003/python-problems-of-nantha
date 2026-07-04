2. Employee Salary Calculator

Question:
A company wants to calculate an employee's gross salary by adding HRA (20%) and DA (10%) to the basic salary.

Answer:

basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10

gross = basic + hra + da

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
