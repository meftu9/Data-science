import numpy as np
import pandas as pd 

# arr = np.array([[1,2,3,4],   
# 	[5,6,7,8],
# 	[9,10,11,12]],)
student = { "Name":["hayu","titi","emu","hana"], 
            "Age":[20,30,40,50],
            "Score":[80,90,85,91]}

df = pd.DataFrame(student)
print(df)

print()

print(df["Score"].mean())


print(df.describe())

print()

print(df.head(1))
print()
print(df.tail(2))
print()
print(df.iloc[0,1])
print()
print(df.shape)
print()
print(df.size)
print()
print(df.dtypes)
print()
print(df[["Age","Score"]])

print()  
df.rename(columns={"Score": "CGPA"}, inplace=True)  

print() 
print(df[df["CGPA"] > 3.5])
print()

df.drop("CGPA",axis = 1 ,inplace =True)
print(df)

df.drop(0,axis = 0,inplace =True )
print(df)

