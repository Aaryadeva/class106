import csv
import plotly_express as px

with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x="Temperature",y="Ice-cream Sales( â‚¹ )")
    fig.show()