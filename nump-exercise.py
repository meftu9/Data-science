import numpy as np
print(np.__version__)

sales = np.array([
   [120, 130, 125, 140, 150],  # Coffee
   [200, 210, 190, 220, 230],  # Milk
   [90,  85,  95,  100, 110],  # Bread
   [60,  70,  65,  80,  75]    # Sugar
])

# PART 1: Data Understanding

print("full sales data:",sales[0:,0:])
print("sales of milk:",sales[1])
print("sales of day 3:",sales[:,2])
print("last 2 days sales for all:",sales[:,3:])

# PART 2: Product Performance

coffe = np.sum(sales[0])
milk = np.sum(sales[1])
bread = np.sum(sales[2])
suger = np.sum(sales[3])

products = [coffe ,milk ,bread, suger]

print("total sale of coffe:", coffe)
print("total sale of milk:",milk )
print("total sale of bread:",bread )
print("total sale of suger:",suger )
print ("product sold the most overall :", np.max(products))

print("average daily sale product of coffe;", np.average(sales[0]))
print("average daily sale product of milk;" ,np.average(sales[1]))
print("average daily sale product of bread;", np.average(sales[2]))
print("average daily sale product of suger;" ,np.average(sales[3]))

print("highest single day sale for coffe:" ,np.max(sales[0]))
print("highest single day sale for milk:" ,np.max(sales[1]))
print("highest single day sale for bread:" ,np.max(sales[2]))
print("highest single day sale for suger:" ,np.max(sales[3]))

print("lowest single day sale for coffe:" ,np.min(sales[0]))
print("lowest single day sale for milk:" ,np.min(sales[1]))
print("lowest single day sale for bread:" ,np.min(sales[2]))
print("lowest single day sale for suger:" ,np.min(sales[3]))


#PART 3: Daily Analysis

monday = np.sum(sales[:,0])
tuseday = np.sum(sales[:,1])
wednesday = np.sum(sales[:,2])
thursday = np.sum(sales[:,3])
friday = np.sum(sales[:,4])

total_days = [monday, tuseday, wednesday, thursday,friday]

print("total sale of monday:", monday)
print("total sale of tuseday:",tuseday )
print("total sale of wednesday:",wednesday )
print("total sale of thursday:",thursday )
print("total sale of friday:",friday )

print ("product sold the most overall :", np.max(total_days))


print("average sale of monday:", np.average(sales[:,0]))
print("average sale of tuseday:" ,np.average(sales[:,1]))
print("average sale of wednesday:", np.average(sales[:,2]))
print("average sale of thursday:" ,np.average(sales[:,3]))
print("average sale of friday:" ,np.average(sales[:,4]))


#exerscie 4











