# Data visualization for literacy rate by countrys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import numpy as np

# Read csv file
df = pd.read_csv('Project/Literacy Rate.csv')
print(df)

# Get the top 10 most literate countries
top_10_country = df.nlargest(10, 'Literacy Rate')

# Plot the result
plt.figure(figsize=(10, 6))
plt.bar(top_10_country['Country'], top_10_country['Literacy Rate'])
plt.title('Top 10 Literate Countries by Literacy Rate')
plt.xlabel('Country')
plt.ylabel('Literacy Rate')
plt.xticks(rotation=45)
plt.show()

# for nepal
# Filter the data for Nepal
country = 'Nepal'
country_data = df[df['Country'] == country].sort_values(by='Year')

# Extract the years and literacy rates
years = country_data['Year'].values
literacy_rates = country_data['Literacy Rate'].values

# Initialize the figure and bar container
fig, ax = plt.subplots()
bars = ax.bar([country], [0], color='blue')

# Set up the plot's appearance
ax.set_ylim(0, 100)
ax.set_title(f'Literacy Rate in {country} Over the Years')
ax.set_xlabel('Country')
ax.set_ylabel('Literacy Rate')

# Initialize function for the animation
def init():
    for bar in bars:
        bar.set_height(0)
    return bars

# # Animation function
def animate(i):
    year = years[i]
    literacy_rate = literacy_rates[i]
    for bar in bars:
        bar.set_height(literacy_rate)
    ax.set_title(f'Literacy Rate in {country} - {year}')
    return bars

# # Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(years), init_func=init, interval=1000, blit=False)

plt.show()

# Get the top 10 countries by average literacy rate
top_10_countries = df.groupby('Country')['Literacy Rate'].mean().nlargest(10).index
top_10_data = df[df['Country'].isin(top_10_countries)]

# Plot the line plot for the comparison of Literacy Rates by Year for Top 10 Countries'
plt.figure(figsize=(14, 8))
sns.lineplot(data=top_10_data, x='Year', y='Literacy Rate', hue='Country', marker='o')
plt.title('Comparison of Literacy Rates by Year for Top 10 Countries')
plt.xlabel('Year')
plt.ylabel('Literacy Rate')
plt.legend(title='Country')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()



# # Extract literacy rates
# literacy_rates = df['Literacy Rate'].values

# # Create histogram
plt.figure(figsize=(10, 6))
plt.hist(literacy_rates, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribution of Literacy Rates')
plt.xlabel('Literacy Rate')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


#for calculation of literacy rate
# Extract literacy rates
literacy_rates = df['Literacy Rate'].values

# # Calculate statistical measures
mean_literacy = np.mean(literacy_rates)
median_literacy = np.median(literacy_rates)
std_literacy = np.std(literacy_rates)

print(f'Mean Literacy Rate: {mean_literacy}')
print(f'Median Literacy Rate: {median_literacy}')
print(f'Standard Deviation of Literacy Rate: {std_literacy}')



# #3D diagram 



# Load the data
df = pd.read_csv('Project/Literacy Rate.csv')

# Filter the data for Nepal and the specified years
df_nepal = df[(df['Country'] == 'Nepal') & (df['Year'] >= 2015) & (df['Year'] <= 2020)]

# Check if the filtered DataFrame is empty
if df_nepal.empty:
    print("No data found for Nepal from 2010 to 2020.")
else:
    # Sort the data by year
    df_nepal = df_nepal.sort_values(by='Year')

    # Prepare the data for the 3D bar chart
    x = np.arange(len(df_nepal))  # X axis: Indices of the years
    y = np.ones_like(x)  # Y axis: All ones (since we have only one country)
    z = np.zeros_like(x)  # Z axis: All zeros (the base of the bars)
    dx = np.ones_like(x) * 0.5  # Width of the bars
    dy = np.ones_like(x) * 0.5  # Depth of the bars
    dz = df_nepal['Literacy Rate'].values  # Height of the bars (literacy rates)

    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.bar3d(x, y, z, dx, dy, dz)

    # Set the labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Country')
    ax.set_zlabel('Literacy Rate')
    ax.set_title('Fluctuation of Literacy Rate in Nepal (2010-2020)')

    # Customize the ticks
    ax.set_xticks(x)
    ax.set_xticklabels(df_nepal['Year'].astype(str).values)
    ax.set_yticks([1])
    ax.set_yticklabels(['Nepal'])
    ax.set_zticks(np.arange(0, max(dz)+10, 10))

    plt.show()


