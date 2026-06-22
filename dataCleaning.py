# meftuha kedir

import pandas as pd
import numpy as np

students = pd.DataFrame({"student_id":[201,202,203,204,205,206,207,208,209,210],
	"name":["abel","sara",None,"jhon","marta",None,"david","helen","tom",None],
	"department":["CS","IT","CS",None,"SW","IT","SE",None,"CS","IT"],
	"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
	"scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]})


print(students.isnull().sum())
print((students.isnull(). sum() / len(students))* 100)
students["name"] = students["name"].fillna("unknown")
print(students)
students["department"] = students["department"].fillna(students["department"].mode()[0])
print(students)
students["gpa"] = students["gpa"].fillna(students["gpa"].median())
print(students)

students["scholarship"] = students["scholarship"].fillna(0)
print(students)
 
dep_total_stud = students["department"].value_counts()
print(dep_total_stud)

count_recipients = (students["scholarship"] > 0).sum()
print("Scholar-recipients:", count_recipients)

highest_gpa = students["gpa"].max()
print("highestgpa:",highest_gpa)

lowest_gpa = students["gpa"].min()
print("lowest-gpa:",lowest_gpa)

ave_gpa = students["gpa"].mean()
print("average-gpa:",ave_gpa)

totalScholar = students["scholarship"].sum()
print(totalScholar)