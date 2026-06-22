import pandas as pd

df = pd.DataFrame({"student_id":[101,102,103,102,104,101],
	  "name":["Abel","Sara","Jhon","Sara","Helen","Abel"],
	  "score":[80,90,75,90,88,80]
	})

print(df.duplicated())
print("Duplicate Count:",)