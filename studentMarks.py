import pandas as pd
import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    DaysPresent=[]
    StudentMarks=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            DaysPresent.append(float(row["Days Present"]))
            StudentMarks.append(float(row["Student Marks"]))
    return{"x":StudentMarks,"y":DaysPresent}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Student Marks and Days Present is",correlation[0,1]) 

def setup():
    data_path="DaysPresent.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

setup()

df=pd.read_csv("DaysPresent.csv")
fig=px.scatter(df,x="Student Marks",y="Days Present")
fig.show()