import pandas as pd
import numpy as np

students = pd.DataFrame({"student_id":[101,102,103,104,105,106,107,108,109,110],
	"name":["abel","sara",None,"jhon","marta",None,"david","helen","tom",None],
	"department":["CS","IT","CS",None,"SW","IT","SE",None,"CS","IT"],
	"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
	"scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]})


print (students.isnull())
print()
print(students.isnull().sum())
print()
print(students.isnull().sum().sum())
print()
print((students.isnull().sum() / len(students))*100)
print()
print (students.columns[students.isnull().any()])
print()
print (students[students.isnull().any(axis=1)])
print()
print(students[students["gpa"].isnull()])
print()
print (students[students["scholarship"].isnull()])
print()
students["name"] = students["name"].fillna("unknown")
print(students)
print()
students["gpa"] = students["gpa"].fillna(students["gpa"].mean())
print(students)
print()
students["gpa"] = students["gpa"].fillna(students["gpa"].median())
print(students)
print()


students["department"] = students["department"].fillna(students["department"].mode()[0])
print(students)
print()
students["scholarship"] = students["scholarship"].fillna(0)
print(students)
print()
students.dropna()
print(students)
print()
students.dropna(axis=1)
print(students)
print()

students["gpa_missing"]= students["gpa"].isnull()
print(students)

print()

students["scholar_missing"]= students["scholarship"].isnull()
print(students)
print()
students.isnull().sum().idxmax()
print(students)

print()
students.isnull().sum().idxmin()
print(students)