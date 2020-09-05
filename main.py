# Author: Kieran Murdocca kkm5754@psu.edu
lg1 = input("Enter your course 1 letter grade: ")
c1 = input("Enter your course 1 credit: ")
if lg1 == "A": 
  print("Grade point for course 1 is:" , (4))
  P1=4.0
elif lg1 == "A-": 
  print("Grade point for course 1 is:" , (3.67))
  P1=3.67
elif lg1 == "B+": 
  print("Grade point for course 1 is:" , (3.33))
  P1=3.33
elif lg1 == "B": 
  print("Grade point for course 1 is:" , (3.0))
  P1=3.0
elif lg1 == "B-": 
  print("Grade point for course 1 is:" , (2.67))
  P1=2.67
elif lg1 == "C+": 
  print("Grade point for course 1 is:" , (2.33))
  P1=2.33
elif lg1 == "C": 
  print("Grade point for course 1 is:" , (2.0))
  P1=2.0
elif lg1 == "D": 
  print("Grade point for course 1 is:" , (1.0))
  P1=1.0
else:
  print("Grade point for course 1 is:" , (0.0))
  P1=0.0
lg2 = input("Enter your course 2 letter grade: ")
c2 = input("Enter your course 2 credit: ")
if lg2 == "A": 
  print("Grade point for course 2 is:" , (4.0))
  P2=4.0
elif lg2 == "A-": 
  print("Grade point for course 2 is:" , (3.67))
  P2=3.67
elif lg2 == "B+": 
  print("Grade point for course 2 is:" , (3.33))
  P2=3.33
elif lg2 == "B": 
  print("Grade point for course 2 is:" , (3.0))
  P2=3.0
elif lg2 == "B-": 
  print("Grade point for course 2 is:" , (2.67))
  P2=2.67
elif lg2 == "C+": 
  print("Grade point for course 2 is:" , (2.33))
  P2=2.33
elif lg2 == "C": 
  print("Grade point for course 2 is:" , (2.0))
  P2=2.0
elif lg2 == "D": 
  print("Grade point for course 2 is:" , (1.0))
  P2=1.0
else:
  print("Grade point for course 2 is:" , (0.0))
  P2=0.0
lg3 = input("Enter your course 3 letter grade: ")
c3 = input("Enter your course 3 credit: ")
if lg3 == "A": 
  print("Grade point for course 3 is:" , (4.0))
  P3=4.0
elif lg3 == "A-": 
  print("Grade point for course 3 is:" , (3.67))
  P3=3.67
elif lg3 == "B+": 
  print("Grade point for course 3 is:" , (3.33))
  P3=3.33
elif lg3 == "B": 
  print("Grade point for course 3 is:" , (3.0))
  P3=3.0
elif lg3 == "B-": 
  print("Grade point for course 3 is:" , (2.67))
  P3=2.67
elif lg3 == "C+": 
  print("Grade point for course 3 is:" , (2.33))
  P3=2.33
elif lg3 == "C": 
  print("Grade point for course 3 is:" , (2.0))
  P3=2.0
elif lg3 == "D": 
  print("Grade point for course 3 is:" , (1.0))
  P3=1.0
else:
  print("Grade point for course 3 is:" , (0.0))
  P3=0.0
print("Your GPA is: ", (float(P1) * float(c1) + float(P2) * float(c2) + float(P3) * float(c3)) / (float(c1) + float(c2) + float(c3) ))