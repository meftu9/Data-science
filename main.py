import numpy as np
print("NumPy imported successfully!")

arr = np.array([1, 2, 3, 4])
print( arr * 2)


grades = np.array([
[85, 90, 88],
[70, 65, 60],
[95, 92, 98]
])

print(grades)

attendance = np.zeros((5,7))
print (attendance)

attendanc1 = np.ones((5,7))
print(attendanc1)

employee_ids = np.arange(1000, 1010)
print(employee_ids)

time = np.linspace(0,24,6) # create an equally spaced 6 number in between 0-24
print(time)

time2 = np.linspace(9,60,8)
print(time2)


sales = np.array([
[200, 300, 250],
[400, 500, 450],
])
print(sales.shape)
print(sales.ndim) 
print(sales.size)

age = np.linspace(1,25,5)
print(age)
print(age.ndim)
print(age.shape)


sales = np.array([
[200, 300, 250],
[400, 500, 450],
[150, 200, 180]
])


print(sales[:1,2:])

sales2 = np.array([
    [120, 150, 180],
    [200, 220, 210],
    [170, 160, 190]
])

print(sales2[1,1])
print(sales2[0:])
print(sales2[:,0:])
print(sales2[0])
print(sales2[1:])
print(sales2[:,1:])


print(sales2[:2,2])
print(sales2[:2,0])


