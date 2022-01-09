#1 Write a Python program to find average of three numbers entered by the user.
print('                   Question 1')
a = int(input('Enter First Number 1:'))
b = int(input('Enter Second Number 2:'))
c = int(input('Enter Third Number 3:'))
print('Average of three numbers:', (a+b+c)/3)

#2 Write a python program to compute a person's income tax.
print('\n                   Question 2')
Gross_Income = int(input('Enter Your Gross Icome:'))
Dependents = int(input('Enter Number of Dependents:'))
Standard_Deduction = 10000
Dependent_Deduction = 3000
Tax_Rate = 20/100
Taxable_Income = Gross_Income - Standard_Deduction -(Dependent_Deduction*Dependents)
Income_Tax = Taxable_Income*Tax_Rate
print('Your Income Tax will be:', Income_Tax)

#3 Write a python program to store different data type values into a list.
print('\n                   Question 3')
Student_Name = str(input('Student Name:'))
SID = int(input('Enter Student SID:'))
Gender = str(input('Gender:'))
Department_Name = str(input('Department Name:'))
CGPA = float(input('CGPA Value:'))
List = [Student_Name , SID , Gender , Department_Name , CGPA]
print(List)

#4 Write a python program to enter marks of 5 students into a list and display them in sorted manner.
print('\n                    Question 4')
Entry_1 = float(input('Marks of first student:'))
Entry_2 = float(input('Marks of second student:'))
Entry_3 = float(input('Marks of third student:'))
Entry_4 = float(input('Marks of fourth student:'))
Entry_5 = float(input('Marks of fifth student:'))
List_Marks = [Entry_1, Entry_2, Entry_3, Entry_4, Entry_5]
print('List in random manner:', List_Marks)
List_Marks.sort()
print('List in sorted manner:', List_Marks)

#5 List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#(a) Write a Python program to print a specified list after removing 4th element.
print('\n                   Question 5 (a)')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('Original List:', color)
color.pop(3)
print('Modified List:', color)

#(b) Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’. Do that in one line code.
print('\n                    Question 5 (b)')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('Original List:', color)
color[3:5] = ['Purple']
print('Modified List:', color)

