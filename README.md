
# Data-Visualization-Using-Pandas 

Data visualization is an essential step in making data science projects successful — an effective plot tells a thousand words. 

Data visualization is a powerful way to capture trends and share the insights gained from data. There are plenty of data visualization tools on the shelf with a lot of outstanding features, but in this tutorial, we're going to learn plotting with the Pandas package.


## Features

- Line Plot
- Bar Plot
- Histogram
- Box Plot
- Area Plot
- Pie Plot
- Scatter Plot
- Hexbin Plot
- KDE Plot

## Programing Language
- Python
## Line Plot

The default plot is the line plot that plots the index on the x-axis and the other numeric columns in the DataFrame on the y-axis.

```
df.plot(y='MSFT', figsize=(9,6))
```

![Line Plot](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name.png)


We can plot multiple lines from the data by providing a list of column names and assigning it to the y-axis.

```
df.plot.line(y=['FB', 'AAPL', 'MSFT'], figsize=(10,6))
```

![Line Plot Multiple Plots](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name-1.png)

We can use the other parameters provided by the plot() method to add more details to a plot, like this:

```
df.plot(y='FB', figsize=(10,6), title='Facebook Stock', ylabel='USD')
```

![Line Plot Details](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name-2.png)

As we see in the figure, the title argument adds a title to the plot, and the ylabel sets a label for the y-axis of the plot. The plot's legend display by default, however, we may set the legend argument to false to hide the legend