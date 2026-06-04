import numpy as np
scores = np.array([
    [80, 75, 90],  #abel   m p c
    [65, 70, 60],  # sara
    [95, 88, 92],  #jhon
    [72, 78, 85]  #helen
])

print("Saras Physics score",scores[1,1])
print("all Math scores:",scores[:,0])
print("all Chemistry scores:",scores[:,2])
print("John's full scores",scores[2])
print("the first 2 students",scores[:2])
print("Physics and Chemistry scores for all students",scores[:,1:])

print(scores[:2, 2:])

#highest all sugjetc
#avaerage --
#average all student

print (np.max(scores))
print (np.average(scores)) #   all subject 
print (np.average(scores[:,0]))  # each subject
print (np.average(scores[:,1]))
print (np.average(scores[:,2]))

print ("avg of abel:",np.average(scores[0]))
print ("avg of sara:",np.average(scores[1]))
print ("avg of jhon:",np.average(scores[2]))
print ("avg of helen:",np.average(scores[3]))




