# Author: Kieran Murdocca kkm5754@psu.edu
input("Enter your course 1 letter grade: ")
c1 = float(input("Enter your course 1 credit: "))
if lg1 == "A": 
  print("Grade point for course 1 is:" , (4.00))
  P1=float(4.00)
elif lg1 == "A-": 
  print("Grade point for course 1 is:" , (3.67))
  P1=float(3.67)
elif lg1 == "B+": 
  print("Grade point for course 1 is:" , (3.33))
  P1=float(3.33)
elif lg1 == "B": 
  print("Grade point for course 1 is:" , (3.00))
  P1=float(3.00)
elif lg1 == "B-": 
  print("Grade point for course 1 is:" , (2.67))
  P1=float(2.67)
elif lg1 == "C+": 
  print("Grade point for course 1 is:" , (2.33))
  P1=float(2.33)
elif lg1 == "C": 
  print("Grade point for course 1 is:" , (2.00))
  P1=float(2.00)
elif lg1 == "D": 
  print("Grade point for course 1 is:" , (1.00))
  P1=float(1.00)
else:
  print("Grade point for course 1 is:" , (0.00))
  P1=float(0.00)
input("Enter your course 2 letter grade: ")
c2 = float(input("Enter your course 2 credit: "))
if lg2 == "A": 
  print("Grade point for course 2 is:" , (4.00))
  P2=float(4.00)
elif lg2 == "A-": 
  print("Grade point for course 2 is:" , (3.67))
  P2=float(3.67)
elif lg2 == "B+": 
  print("Grade point for course 2 is:" , (3.33))
  P2=float(3.33)
elif lg2 == "B": 
  print("Grade point for course 2 is:" , (3.00))
  P2=float(3.00)
elif lg2 == "B-": 
  print("Grade point for course 2 is:" , (2.67))
  P2=float(2.67)
elif lg2 == "C+": 
  print("Grade point for course 2 is:" , (2.33))
  P2=float(2.33)
elif lg2 == "C": 
  print("Grade point for course 2 is:" , (2.00))
  P2=float(2.00)
elif lg2 == "D": 
  print("Grade point for course 2 is:" , (1.00))
  P2=float(1.00)
else:
  print("Grade point for course 2 is:" , (0.00))
  P2=float(0.00)
input("Enter your course 3 letter grade: ")
c3 = float(input("Enter your course 3 credit: "))
if lg3 == "A": 
  print("Grade point for course 3 is:" , (4.00))
  P3=float(4.00)
elif lg3 == "A-": 
  print("Grade point for course 3 is:" , (3.67))
  P3=float(3.67)
elif lg3 == "B+": 
  print("Grade point for course 3 is:" , (3.33))
  P3=float(3.33)
elif lg3 == "B": 
  print("Grade point for course 3 is:" , (3.00))
  P3=float(3.00)
elif lg3 == "B-": 
  print("Grade point for course 3 is:" , (2.67))
  P3=float(2.67)
elif lg3 == "C+": 
  print("Grade point for course 3 is:" , (2.33))
  P3=float(2.33)
elif lg3 == "C": 
  print("Grade point for course 3 is:" , (2.00))
  P3=float(2.00)
elif lg3 == "D": 
  print("Grade point for course 3 is:" , (1.00))
  P3=float(1.00)
else:
  print("Grade point for course 3 is:" , (0.00))
  P3=float(0.00)
print("Your GPA is: ", (float(P1) * float(c1) + float(P2) * float(c2) + float(P3) * float(c3)) / (float(c1) + float(c2) + float(c3) ))