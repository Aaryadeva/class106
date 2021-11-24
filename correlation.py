import csv
import numpy as np
import plotly_express as px

def get_data_source(data_path):

    temp=[]
    sales=[]

    with open(data_path) as f:

        df = csv.DictReader(f)

        for row in df:
            temp.append(float(row['Temperature']))
            sales.append(float(row['Ice-cream Sales( â‚¹ )']))

        return{"x":temp , "y":sales}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print(correlation)

def plot_figure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Temperature",y="Ice-cream Sales( â‚¹ )")
        fig.show()

def setup():
    data_path = 'Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()