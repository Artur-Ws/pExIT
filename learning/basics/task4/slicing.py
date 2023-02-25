"""
Imagine you are working on app for chart generation. This app will support many datasets on one chart,
so you need to create a function that will return list with colors for each dataset. Example: you want to show chart
with average prices for 1m^2 of house in last 10 years in Gdansk, Warsaw and Wroclaw all in one chart, and in example
Gdansk prices will be blue line, Warsaw yellow line and Wroclaw red line.

Implement function that will get 2 parameters: number of datasets, and color list, then return copy of that list which
contains only as many colors as needed for chart.
"""

colors = ['red', 'blue', 'yellow', 'orange', 'purple', 'gray', 'green']


def get_colors(categories, color_list):
    # place your code here
    pass


print(get_colors(4, colors))

