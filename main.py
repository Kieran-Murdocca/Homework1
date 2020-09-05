# Author: Kieran Murdocca kkm5754@psu.edu
lg1 = float(input("Enter your course 1 letter grade: "))
c1 = float(input("Enter your course 1 credit: "))
if lg1 == "A" or lg1 == "a": 
  print("Grade point for course 1 is:" , (4))
elif lg1 == "A-" or lg1 == "a-": 
  print("Grade point for course 1 is:" , (3.67))
elif lg1 == "B+" or lg1 == "b+": 
  print("Grade point for course 1 is:" , (3.33))
elif lg1 == "B" or lg1 == "b": 
  print("Grade point for course 1 is:" , (3.0))
elif lg1 == "B-" or lg1 == "b-": 
  print("Grade point for course 1 is:" , (2.67))
elif lg1 == "C+" or lg1 == "c+": 
  print("Grade point for course 1 is:" , (2.33))
elif lg1 == "C" or lg1 == "c": 
  print("Grade point for course 1 is:" , (2))
elif lg1 == "D" or lg1 == "d": 
  print("Grade point for course 1 is:" , (1))
else:
  print("Grade point for course 1 is:" , (0))
lg2 = float(input("Enter your course 2 letter grade: "))
c2 = float(input("Enter your course 2 credit: "))
if lg2 == "A" or lg2 == "a": 
  print("Grade point for course 2 is:" , (4))
elif lg2 == "A-" or lg2 == "a-": 
  print("Grade point for course 2 is:" , (3.67))
elif lg2 == "B+" or lg2 == "b+": 
  print("Grade point for course 2 is:" , (3.33))
elif lg2 == "B" or lg2 == "b": 
  print("Grade point for course 2 is:" , (3.0))
elif lg2 == "B-" or lg2 == "b-": 
  print("Grade point for course 2 is:" , (2.67))
elif lg2 == "C+" or lg2 == "c+": 
  print("Grade point for course 2 is:" , (2.33))
elif lg2 == "C" or lg2 == "c": 
  print("Grade point for course 2 is:" , (2))
elif lg2 == "D" or lg2 == "d": 
  print("Grade point for course 2 is:" , (1))
else:
  print("Grade point for course 2 is:" , (0))
lg3 = float(input("Enter your course 3 letter grade: "))
c3 = float(input("Enter your course 3 credit: "))
if lg3 == "A" or lg3 == "a": 
  print("Grade point for course 3 is:" , (4))
elif lg3 == "A-" or lg3 == "a-": 
  print("Grade point for course 3 is:" , (3.67))
elif lg3 == "B+" or lg3 == "b+": 
  print("Grade point for course 3 is:" , (3.33))
elif lg3 == "B" or lg3 == "b": 
  print("Grade point for course 3 is:" , (3.0))
elif lg3 == "B-" or lg3 == "b-": 
  print("Grade point for course 3 is:" , (2.67))
elif lg3 == "C+" or lg3 == "c+": 
  print("Grade point for course 3 is:" , (2.33))
elif lg3 == "C" or lg3 == "c": 
  print("Grade point for course 3 is:" , (2))
elif lg3 == "D" or lg3 == "d": 
  print("Grade point for course 3 is:" , (1))
else:
  print("Grade point for course 3 is:" , (0))
print("Your GPA is: ", (lg1 * c1 + lg2 * c2 + lg3 * c3) / (c1 + c2 + c3) )