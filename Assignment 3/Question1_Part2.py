import pandas
import numpy

rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"


fields = ["BOROUGH","VEHICLE 1 TYPE","VEHICLE 2 TYPE","VEHICLE 3 TYPE","VEHICLE 4 TYPE","VEHICLE 5 TYPE" ]
df = pandas.read_csv(rpath+"/vehicle_collisions.csv", sep=",", usecols=fields)

result = pandas.DataFrame(index=df.BOROUGH.unique() ,columns=['One_vehicle', 'Two_vehicle', 'Three_vehicles', 'More_vehicles']).fillna(0)
result = result.reindex(index=result.index.dropna())

df = df[df.BOROUGH.isnull()==False]
df["Vehicles_Involved"] = (5 - df.isnull().sum(axis=1))

for r in result.index:
    temp = df[df.BOROUGH == r]
    result.One_vehicle[r] = temp[temp.Vehicles_Involved==1].Vehicles_Involved.count()
    result.Two_vehicle[r] = temp[temp.Vehicles_Involved==2].Vehicles_Involved.count()
    result.Three_vehicles[r] = temp[temp.Vehicles_Involved==3].Vehicles_Involved.count()
    result.More_vehicles[r] = temp[temp.Vehicles_Involved > 3].Vehicles_Involved.count()

result.to_csv("./Output/Question1_Part2.csv")

result.head()




