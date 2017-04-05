from __future__ import division
import pandas
import os
import csv


rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"
df = pandas.read_csv(rpath+"/vehicle_collisions.csv", sep=",")

data = df[df["DATE"].str.endswith("16")]

result = pandas.DataFrame(index=range(1,13), columns=["Month", "Manhattan", "NYC","Percentage"])

result["Month"] = pandas.Series(data = ["","January", "February", "March", "April", "May", "June", "July","August", "September", "October","November", "December"])
result = result.fillna(0)

for index,row in data.iterrows():
    i = row[1].split("/")[0]
    if row[3] == "MANHATTAN":
        result.Manhattan[int(i)] += 1
    result.NYC[int(i)] += 1

result.Percentage = result.Percentage.replace(to_replace=0, value= 0.1)
for i in result.index:
    result.Percentage[i] = result.Manhattan[i]/result.NYC[i]

result.head()

result.to_csv("./Output/Question1_part1.csv")

