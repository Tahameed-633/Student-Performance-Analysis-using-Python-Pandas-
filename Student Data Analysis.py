import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
student_data={
    "Name":["Muntasir","Asif","Afra","Nadia","Sadik","Sabbir","Shamim","Rayhan","Rehnuma","Rezwana","Shovon","Imran","Navid","Farhan","Nusaiba","Ahmed"],
    "Department":["CSE","CSE","EEE","EEE","CE","CE","CSE","BBA","BBA","Law","Law","EEE","CE","EEE","BBA","CSE"],
    "Credits":[10.5,35,100,25,9,12.5,98,45,50,115,80,75,65,20,25,130],
    "CGPA":[1.76,2.50,3.06,2.99,1.50,3.50,3.76,4.00,4.00,3.25,3.00,2.65,3.65,3.95,2.00,4.00]
}
df=pd.DataFrame(student_data)
print("Student's Dataset:")
print(df)
print("Information Of The Dataset:")
print(df.info())
print("Statistical Summary Of The Dataset:")
print(df.describe())
print("Departmentwise Maximum CGPA::")
print(df.groupby("Department")["CGPA"].max())
print("Departmentwise average CGPA:")
print(df.groupby("Department")["CGPA"].mean())
print("Departmentwise Minimum CGPA:")
print(df.groupby("Department")["CGPA"].min())
print("Departmentwise Maximum Credits:")
print(df.groupby("Department")["Credits"].max())
print("Departmentwise average credits:")
print(df.groupby("Department")["Credits"].mean())
print("Departmentwise Minimum Credits:")
print(df.groupby("Department")["Credits"].min())
print("Total students:",len(df))
print("Departmentwise Total Students:")
print(df["Department"].value_counts())
print("Departmentwise Standard Deviation:")
print(df.groupby("Department")["CGPA"].std())
print("Maximum To Minimum CGPA:")
print(df.sort_values("CGPA",ascending=False))
cgpa_std=df.groupby("Department")["CGPA"].std()
for dept,std in cgpa_std.items():
    if std<0.5:
        print(f"{dept} Low CGPA Variation.")
    elif std<1:
        print(f"{dept} Moderate CGPA Variation.")
    else:
        print(f"{dept} High CGPA Variation.")
   
print("Student from CSE Department Who Has CGPA Greater Than Or Equal To 3.50:")
print(df[(df["Department"]=="CSE") &(df["CGPA"]>=3.50)])
print("Student Of CSE Department Who Has CGPA Above Average CGPA Of The Department:")
avg=df[df["Department"]=="CSE"]["CGPA"].mean()
print(df[(df["Department"]=="CSE") & (df["CGPA"]>avg)])
df["CGPA"]>max(df.groupby("Department")["CGPA"].mean())
print("Students Who Has CGPA Above The Highest Average CGPA Among All The Departments:")
print(df[df["CGPA"]>max(df.groupby("Department")["CGPA"].mean())])
print("All The Students With CGPA Above 3.50:")
print(df[df["CGPA"]>3.50])
print("All The Students With CGPA below 3.50:")
print(df[df["CGPA"]<3.50])
print("Count The Number of Students From The EEE Department Who Has CGPA Above 3.25:")
print(df[(df["Department"]=="EEE") &(df["CGPA"]>3.25)].shape[0])
def grade(cgpa):
    if cgpa==4:
        return "A+"
    if 3.75<=cgpa<4.00:
        return "A"
    elif 3.50<=cgpa<3.75:
        return "A-"
    elif 3.25<=cgpa<3.50:
        return "B+"
    elif 3.00<=cgpa<3.25:
        return "B"
    elif 2.75<=cgpa<3.00:
        return "B-"
    elif 2.50<= cgpa<2.75:
        return "C+"
    elif 2.25 <=cgpa<2.50:
        return "C"
    elif 2.00<=cgpa<2.25:
        return "D"
    else:
        return "F"
   
df["Grade"]=df["CGPA"].apply(grade)
df.to_csv("student_dataset.csv",index=False)
df=pd.read_csv("student_dataset.csv")
print(df)
print(pd.crosstab(df["Department"],df["Grade"]))
print(df[["Credits","CGPA"]].corr())
df.to_csv("student_dataset.csv",index=False)
df=pd.read_csv("student_dataset.csv")
df=pd.read_csv("student_dataset.csv")
dept=df["Department"].value_counts()
dept.plot(kind="bar")
plt.title("Departmentwise Student Count")
plt.xlabel("Department")
plt.ylabel("Number Of Students")

plt.show()
df=pd.read_csv("student_dataset.csv")
plt.figure(figsize=(6,4))
plt.hist(df["CGPA"],bins=5,edgecolor="black")
plt.title("CGPA Distribution")
plt.xlabel("CGPA")
plt.ylabel("Students")
plt.savefig("histogram.png")
plt.show()
plt.figure(figsize=(4,6))
plt.boxplot(df["CGPA"])
plt.title("CGPA Box Plot")
plt.ylabel("CGPA")
plt.savefig("cgpa box plot.png")
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df["Credits"],df["CGPA"],marker="o")

plt.title("Credit Vs CGPA")
plt.xlabel("Credits")
plt.ylabel("CGPA")
plt.grid(True)
plt.savefig("Scatter Plot.png")
mean=df.groupby("Department")["CGPA"].mean()
std=df.groupby("Department")["CGPA"].std()
plt.figure(figsize=(6,4))
plt.bar(mean.index,mean.values,std.values,yerr=std.values,capsize=5)
plt.title("Departmentwise Mean CGPA With Standard Deviation")
plt.xlabel("Department")
plt.ylabel("Mean CGPA")
plt.savefig("error bar graph.png")
plt.show()
plt.close()
