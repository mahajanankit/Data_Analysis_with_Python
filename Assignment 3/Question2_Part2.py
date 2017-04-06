import pandas

#Change this variable for relative path
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

#Reading the csv into a dataframe
fields = ["Job Family","Employee Identifier","Year Type","Salaries","Overtime","Total Benefits","Total Compensation"]
df = pandas.read_csv(rpath+"/employee_compensation.csv", sep=",", usecols=fields)

#Filtering data for Calender Year
df = df[df["Year Type"] == "Calendar"]

#Finding mean for every employee
df = df.groupby(["Employee Identifier","Job Family"], as_index=False).mean()

#Filtering data where overtime is more than 5% of Salaries
df = df[df["Overtime"] > (0.05*df["Salaries"])]

df.__delitem__("Salaries")
df.__delitem__("Overtime")

#Calculating total values for each job family
df = df.groupby("Job Family", as_index=False).sum()

df.__delitem__("Employee Identifier")

#Creating a new column with percentage
df["Percentage"] = pandas.Series(index=df.index, data=df["Total Benefits"]/df["Total Compensation"])

#Sorting data by percentage
df = df.sort_values(by='Percentage', ascending=0)

#Exporting to a csv
df.to_csv("./Output/Question2_Part2.csv", index=False)

#Displaying few rows
df.head()