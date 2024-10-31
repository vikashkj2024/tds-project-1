import pandas as pd

filePath = 'users.csv'


fileC=pd.read_csv(filePath)

nameList = fileC['name'].tolist()
surnameList = []


for names in nameList:
    #names = names.split('')
    print(names)
    #surnameList.append(names[1])

#print(surnameList)




