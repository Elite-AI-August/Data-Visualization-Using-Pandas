
# Data-Visualization-Using-Pandas 

Data visualization is an essential step in making data science projects successful — an effective plot tells a thousand words. 

Data visualization is a powerful way to capture trends and share the insights gained from data. There are plenty of data visualization tools on the shelf with a lot of outstanding features, but in this tutorial, we're going to learn plotting with the Pandas package.

We're going to work on the weekly closing price of the Facebook, Microsoft, and Apple stocks over the last previous months


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
## Bar Plot

A bar chart is a basic visualization for comparing values between data groups and representing categorical data with rectangular bars. This plot may include the count of a specific category or any defined value, and the lengths of the bars correspond to the values they represent.


We'll create a bar chart based on the average monthly stock price to compare the average stock price of each company to others in a particular month. To do so, first, we need to resample data by month-end and then use the mean() method to calculate the average stock price in each month. We also select the last three months of data, like this:

```
df_3Months = df.resample(rule='M').mean()[-3:]
print(df_3Months)
```

Now, we're ready to create a bar chart based on the aggregated data by assigning the bar string value to the kind argument:

```
df_3Months.plot(kind='bar', figsize=(10,6), ylabel='Price')
```

![Bar Plot](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name-3.png)

We can create horizontal bar charts by assigning the barh string value to the kind argument.

```
df_3Months.plot(kind='barh', figsize=(9,6))
```

![Bar Plot](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name-20.png)

To create a stacked bar chart we need to assign True to the stacked argument, like this:

```
df_3Months.plot(kind='bar', stacked=True, figsize=(9,6))
```

![Bar Plot](https://github.com/SulemanMughal/Data-Visualization-Using-Pandas/blob/main/name-4.png)
