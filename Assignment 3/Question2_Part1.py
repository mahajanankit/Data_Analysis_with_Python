import pandas

#Change this variable for relative path
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

#Reading the csv into a dataframe
fields = ["Organization Group","Department","Total Compensation"]
df = pandas.read_csv(rpath+"/employee_compensation.csv", sep="," ,usecols=fields)

#Finding mean for every department in every organization
df = df.groupby(["Organization Group","Department"]).mean()

#Sorting the dataframe based on total compensation in descending order
df = df.sort_values(by='Total Compensation', ascending=0)

#Exporting to a csv
df.to_csv("./Output/Question2_Part1.csv")

#Displaying few rows
df.head()