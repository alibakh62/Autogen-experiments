# filename: stock_price_chart.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker list
tickers_list = ['NVDA', 'AAPL', 'TSLA']

# Fetch the data
data = yf.download(tickers_list,'2022-01-01')['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Plot all the close prices
data.plot(figsize=(10, 7))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ", ".join(tickers_list), fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year 2022 - till date', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()