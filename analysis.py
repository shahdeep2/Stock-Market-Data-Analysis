import pandas as pd
import matplotlib.pyplot as plt

# Load the stock market data from CSV file
data = pd.read_csv('C:/stock-market-analysis/National_Stock_Exchange_of_India_Ltd.csv')


# Display the first few rows of the dataset
print(data.head())

# Get basic information about the dataset
print(data.info())

# Calculate Daily Return using the 'LTP' column
data['Daily Return'] = data['LTP'].replace(',', '', regex=True).astype(float).pct_change()
data['LTP'] = pd.to_numeric(data['LTP'], errors='coerce') 

# Print the updated DataFrame
print(data.head())

print(data[['Symbol', 'LTP', 'Daily Return']].head())

# Plotting the Daily Return
plt.figure(figsize=(10, 6))
plt.plot(data['Daily Return'], label='Daily Return', color='blue')
plt.title('Daily Returns of Stocks')
plt.xlabel('Days')
plt.ylabel('Daily Return')
plt.legend()
plt.show()


# Calculate the moving average (50-day and 200-day) using the 'LTP' column
data['50 MA'] = data['LTP'].rolling(window=50).mean()
data['200 MA'] = data['LTP'].rolling(window=200).mean()

data['Trading Date'] = pd.to_datetime(data['Trading Date'])

# If the 'Date' column is not in datetime format, convert it
data['Date'] = pd.to_datetime(data['Date'])


data['Trading Date'] = pd.to_datetime(data['Trading Date'])

# Plot the moving averages along with the Last Traded Price
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['LTP'], label='LTP', color='blue')
plt.plot(data['Date'], data['50 MA'], label='50-Day MA', color='orange')
plt.plot(data['Date'], data['200 MA'], label='200-Day MA', color='red')
plt.title('Nifty 50 Closing Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.xticks(rotation=45)
plt.show()