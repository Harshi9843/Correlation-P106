import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getDataSource(data_path):
	coffee_in_ml = []
	sleep_in_hours = []

	with open(data_path) as csv_file:
		cvs_reader = csv.DictReader(csv_file)
		
		for row in cvs_reader:
			coffee_in_ml.append(float(row["Coffee in ml"]))
			sleep_in_hours.append(float(row["sleep in hours"]))

	return {"x": coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
	correlation = np.corrcoef(datasource["x"], datasource["y"])
	print("Correlation between drinking coffee and sleep in hours is: \n->",correlation[0,1])

def plotFigure(data_path):
	df = pd.read_csv(data_path)
	fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
	fig.show()

def setup():
	data_path = "dataset-2.csv"
	datasource = getDataSource(data_path)
	
	findCorrelation(datasource)

	plotFigure(data_path)

setup()