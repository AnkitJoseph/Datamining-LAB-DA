import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Fuel.csv')

# Create a scatterplot for fuel price relationship between 4 states
plt.figure(figsize=(10,6))
plt.scatter(data['Delhi'], data['Kolkata'], label='Delhi vs Kolkata')
plt.scatter(data['Delhi'], data['Mumbai'], label='Delhi vs Mumbai')
plt.scatter(data['Delhi'], data['Chennai'], label='Delhi vs Chennai')
plt.scatter(data['Kolkata'], data['Mumbai'], label='Kolkata vs Mumbai')
plt.scatter(data['Kolkata'], data['Chennai'], label='Kolkata vs Chennai')
plt.scatter(data['Mumbai'], data['Chennai'], label='Mumbai vs Chennai')
plt.title('Fuel Price Relationship between 4 States (1997-2022)')
plt.xlabel('Price (INR/Litre)')
plt.ylabel('Price (INR/Litre)')
plt.legend()
plt.grid(True)
plt.show()