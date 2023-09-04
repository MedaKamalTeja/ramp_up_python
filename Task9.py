import plotly.graph_objects as go
import pandas as pd

# Load data from CSV
data_path = 'https://raw.githubusercontent.com/MedaKamalTeja/ramp_up_python/main/heatmap_colorcodes.csv'
df = pd.read_csv(data_path)

# Extract data from DataFrame
areas = df['Area'].tolist()
team_members = df['Existing Team Members'].tolist()
colors = df['Average Team Expertise (1-5)'].tolist()

# Create a basic treemap trace
trace = go.Treemap(
    labels=areas,
    parents=[""] * len(areas),
    values=team_members,
    text=[f"Team Members: {tm}" for tm in team_members],
    hoverinfo="text+label+value+percent parent",
    marker_colors=colors,  # Set marker colors here
)

# Create the layout
layout = go.Layout(
    title='Team Expertise Treemap',
    margin=dict(l=0, r=0, b=0, t=40)
)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Show the plot
fig.show()
