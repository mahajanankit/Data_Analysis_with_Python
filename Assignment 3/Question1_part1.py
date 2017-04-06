import pandas

#Change this variable for relative path
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"


#Reading the csv into a dataframe
fields = ["DATE","BOROUGH"]
df = pandas.read_csv(rpath+"/vehicle_collisions.csv", sep=",", usecols=fields)


#Filtering data for 2016 data
df = df[df["DATE"].str.endswith("16")]


# Creating the result dataframe
result = pandas.DataFrame(index=range(1,13), columns=["Month", "Manhattan", "NYC","Percentage"])
result["Month"] = pandas.Series(data = ["","January", "February", "March", "April", "May", "June", "July","August", "September", "October","November", "December"])
result = result.fillna(0.1)


#Calculating values for each month
for i in range(1,13):
    temp=df[df.DATE.str.startswith(str(i)+'/')]
    result.NYC[i] = len(temp)
    result.Manhattan[i] = len(temp[temp.BOROUGH == "MANHATTAN"])
    result.Percentage[i] = result.Manhattan[i]/result.NYC[i]

#Displaying a few rows
result.head()

#Exporting to a csv
result.to_csv("./Output/Question1_part1.csv")

