import pandas

rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

fields = ["Job Family","Employee Identifier","Year Type","Salaries","Overtime","Total Benefits","Total Compensation"]
df = pandas.read_csv(rpath+"/employee_compensation.csv", sep=",", usecols=fields)

df = df[df["Year Type"] == "Calendar"]
df = df.groupby(["Employee Identifier","Job Family"], as_index=False).mean()

df = df[df["Overtime"] > (0.05*df["Salaries"])]
df.__delitem__("Salaries")
df.__delitem__("Overtime")

df = df.groupby("Job Family", as_index=False).sum()
df.__delitem__("Employee Identifier")
df["Percentage"] = pandas.Series(index=df.index, data=df["Total Benefits"]/df["Total Compensation"])

df = df.sort_values(by='Percentage', ascending=0)

df.to_csv("./Output/Question2_Part2.csv", index=False)

df.head()