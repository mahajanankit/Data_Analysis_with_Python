import pandas
import numpy

#Change this variable for relative path
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

#Reading the csv into a dataframe
fields = ["BOROUGH","VEHICLE 1 TYPE","VEHICLE 2 TYPE","VEHICLE 3 TYPE","VEHICLE 4 TYPE","VEHICLE 5 TYPE" ]
df = pandas.read_csv(rpath+"/vehicle_collisions.csv", sep=",", usecols=fields)

#Creating the result dataframe
result = pandas.DataFrame(index=df.BOROUGH.unique() ,columns=['One_vehicle', 'Two_vehicle', 'Three_vehicles', 'More_vehicles']).fillna(0)
result = result.reindex(index=result.index.dropna())

#Filtering data rows where borough is unknown
df = df[df.BOROUGH.isnull()==False]
df["Vehicles_Involved"] = (5 - df.isnull().sum(axis=1))

#Calculating values for every column
for r in result.index:
    temp = df[df.BOROUGH == r]
    result.One_vehicle[r] = temp[temp.Vehicles_Involved==1].Vehicles_Involved.count()
    result.Two_vehicle[r] = temp[temp.Vehicles_Involved==2].Vehicles_Involved.count()
    result.Three_vehicles[r] = temp[temp.Vehicles_Involved==3].Vehicles_Involved.count()
    result.More_vehicles[r] = temp[temp.Vehicles_Involved > 3].Vehicles_Involved.count()

#Exporting to a csv
result.to_csv("./Output/Question1_Part2.csv")

#Displaying few rows
result.head()




