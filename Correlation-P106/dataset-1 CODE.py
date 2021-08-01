import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getDataSource(data_path):
	marks_in_percentage = []
	days_present = []

	with open(data_path) as csv_file:
		cvs_reader = csv.DictReader(csv_file)
		
		for row in cvs_reader:
			marks_in_percentage.append(float(row["Marks In Percentage"]))
			days_present.append(float(row["Days Present"]))

	return {"x": marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
	correlation = np.corrcoef(datasource["x"], datasource["y"])
	print("Correlation between marks and days present: \n->",correlation[0,1])

def plotFigure(data_path):
	df = pd.read_csv(data_path)
	fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
	fig.show()

def setup():
	data_path = "dataset-1.csv"
	datasource = getDataSource(data_path)
	
	findCorrelation(datasource)

	plotFigure(data_path)

setup()