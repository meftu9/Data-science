import pandas as pd
import numpy as np
data = {
    "Name": ["sihu","ekru","hayu"],
    "Age":[20,30,35]
}
df = pd.DataFrame(data)
print(df)

department = ["CS","IT","IS","SW"]
df = pd.DataFrame(department)
print(df)


department = ["CS","IT","IS","SW"]
df = pd.DataFrame(department)
print(df)

students = {
    "Name":["sihu","ekru","hayu","intu"],
    "Age":[20,22,23,24],
    "CGPA":[3.4,3.5,3.9,3.7],
    "Department":["CS","IT","IS","SW"]
}

df = pd.DataFrame(students)

print(df.shape)
print(df.columns)
print(df.dtypes)


print(df.head(2))
print(df.tail(2))
print(df["Name"])
print(df[["Name","CGPA"]])
print(df.loc[0])
print(df.iloc[2])
print(df.loc[1,"CGPA"])
print(df.iloc[3,1])


print(df[df["Age"] > 21])

print(df[(df["Age"]> 20) & (df["CGPA"]> 3.5)])
print()

print(df[(df["Department"]== "CS") | (df["Department"] =="IT")])

df["Percentage"] = df["CGPA"]*25
print(df)

print()

df["pass"]= df["CGPA"].apply(lambda x :"pass" if x > 2.0 else "fail")
print(df)
print()

print(df["Age"].mean())
print(df["Age"].var())
print(df["Age"].std())
print(df["Age"].max())
print(df["Age"].min())
print(df["Age"].sum())
print(df["Age"].count())
print(df.sort_values("CGPA"))
print(df.sort_values("CGPA",ascending = False))

data = {
    "Name": ["Abel","Sara","Jhon"],
    "Age": [22,np.nan,20]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())
print(df.fillna(0))
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)
print(df.dropna())

for index, row in df.iterrowa():
    print(row["Name"])

for row in df.itertuples():
    print(row.Name)
def scholarship(gpa):
    if gpa >= 3.7:
        return"full"
    elif gpa >=3.3:
        return "partial"
    return "None"

df["Scholarship"] = df["GPA"].apply(scholarship)
print(df)

def classify(gpa):
    if gpa >= 3.7:
        return "Distinction"
    elif gpa >=3.0:
        return "Vert Good"
    elif gpa >= 2.0:
        return"Good"
    return "probation"

    df["Classification"] = df ["GPA"].apply(classify)
    print(df)


