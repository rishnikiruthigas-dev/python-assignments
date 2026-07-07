a=int(input("enter a name:"))
c=a-10
print(type(a))
print(type(c))
print(c)



import pandas as pd
data=pd.read_csv("sales_data.csv")
print(data)

strong password weak password
password=input("enter the password:")
letter=False
number=False
for i in password:
   if i.isalpha():
      letter=True
   if i.isdigit():
      number=True
if len(password)>=8 and letter and number:
   print("strong password")
else:
   print("weak password")

check temperature
temperature=int(input("enter temperature:"))
if temperature<=15:
    print("its cold")
elif temperature>=15 and temperature<=37:
    print("its normal")
else:
    print("hot")
    
# even number counter
a=int(input("enter a number:"))
count=0
for a in range(1,0):
    if a%2==0:
        count=count+1
print(count)
      
# multiplication table generator
num=int(input("enter a number:"))
print("multiplication table:")
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# exam score filter
marks=[]
n=int(input("enter a number:"))
for i in range(n):
    marks.append(int(input("enter marks:")))
print("marks above 50:")
for m in marks:
    if m>50:
        print(m)

# electricity bill generator
units=int(input("enter a number of units:"))
 if units<=100:
    print("free")
elif units<=200:
    bill=units*3
else:
    bill=units*5
print("the electricity bill is=",bill)       

# ATM withdrawal system
balance = float(input("Enter balance: "))
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= balance:
    balance -= withdraw
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

# Employee Bonus Calculation
salary = float(input("Enter salary: "))
if salary >= 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05
print("Bonus:", bonus)
print("Final Salary:", salary + bonus)

 #Online Shopping Discount
amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
print("Final Amount:", amount - discount)

#Login Authentication
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

Attendance Eligibility Checker
total = int(input("Total classes: "))
attended = int(input("Attended classes: "))
percentage = (attended / total) * 100
print("Attendance:", percentage)
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

#Restaurant Billing System
amount = float(input("Enter food bill: "))
gst = amount * 0.05
total = amount + gst
print("GST:", gst)
print("Final Bill:", total)

#Temperature Monitoring System
temp = float(input("Enter temperature: "))
if temp < 20:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")

#Weekly Sales Report
sales = []
for i in range(7):
    sales.append(float(input("Enter sales: ")))

print("Total Weekly Sales:", sum(sales))

#Multiplication Table Generator
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#Employee Attendance Tracker
present = 0
for i in range(5):
    status = input("Present (Y/N): ")
    if status.upper() == "Y":
        present += 1
print("Present Employees:", present)

#Monthly Expense Calculator
expenses = []
for i in range(5):
    expenses.append(float(input("Enter expense: ")))
print("Total Expense:", sum(expenses))

#Product Price Analysis
prices = []
for i in range(5):
    prices.append(float(input("Enter price: ")))
print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))

# Exam Score Filter
scores = []
for i in range(5):
    scores.append(int(input("Enter score: ")))
print("Scores above 50:")
for s in scores:
    if s > 50:
        print(s)
        
# Employee Information System
name = input("Enter Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
print("Name:", name)
print("Department:", department)
print("Salary:", salary)

# Student Result Lookup
students = { "Arun": 85, "Priya": 90, "Kumar": 75}
name = input("Enter student name: ")
if name in students:
    print("Mark:", students[name])
else:
    print("Student not found")