import pandas

#Change this variable for relative path
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

#Reading the csv into a dataframe
fields = ["home","winner","innings1_runs","innings2_runs"]
df = pandas.read_csv(rpath+"/cricket_matches.csv", sep=",", usecols=fields)

#Filtering data for where teams which won at home
df= df[df.home == df.winner]

#Picking maximum of runs from both innings
df["runs"]=df.max(axis=1)

df.__delitem__("winner")
df.__delitem__("innings1_runs")
df.__delitem__("innings2_runs")

#Finding mean for every team
df.groupby("home").mean()

#Sorting by runs
df.sort_values(by="runs", ascending=False)

#Displaying few rows
df.head()

#Exporting to a csv
df.to_csv("./Output/Question3_Part1.csv", index=False)