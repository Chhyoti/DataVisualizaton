import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation  import FuncAnimation
import seaborn as sns

# read csv file
df= pd.read_csv('Project/pldb.csv')
print(df)
print(df.head)

# get top 10  popular languages used 
top_10_languages = df.nlargest(10, 'numberOfUsers')

#Plot the result
plt.figure(figsize=(10, 6))
plt.bar(top_10_languages['title'], top_10_languages['numberOfUsers'])
plt.title('Top 10 programming language used')
plt.xlabel('Title')
plt.ylabel('numberOfUsers')
plt.xticks(rotation=45)
plt.show()

#Barplot  using funcanimation for Number of GitHub Repositories by Programming Language
top_10_languages = df.nlargest(10, 'numberOfRepos')

# Function to update the bar plot for Number of GitHub Repositories by Programming Language
def update(num):
    plt.clf()  # Clear the current figure
    sns.barplot(x='githubLanguage', y=top_10_languages.iloc[:, num + 1], data=top_10_languages,errorbar=None)
    plt.title(f'Number of GitHub Repositories by Programming Language (Month {num + 1})')
    plt.xlabel('Programming Language')
    plt.ylabel('Number of Repositories')
    plt.xticks(rotation=90)

# Create the figure and set up FuncAnimation
fig = plt.figure(figsize=(16, 8))
ani = FuncAnimation(fig, update, frames=len(top_10_languages.columns) , repeat=False, interval=500)
plt.show()

# Correlation analysis 
# Selecting relevant numerical columns for correlation analysis
selected_columns = [
    'rank', 'languageRank', 'factCount', 'numberOfUsers', 'numberOfJobs', 
    'githubBigQuery.repos', 'githubRepo.stars', 'githubRepo.forks', 
    'wikipedia.dailyPageViews', 'wikipedia.backlinksCount'
]

# Filtering the DataFrame for selected columns and handling missing values
correlation_data = df[selected_columns].dropna()

# Compute the correlation matrix using numpy
correlation_matrix = np.corrcoef(correlation_data.values.T)

# Create a heatmap using seaborn
plt.figure(figsize=(14, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", xticklabels=selected_columns, yticklabels=selected_columns, cmap='coolwarm')
plt.title('Correlation Heatmap of Selected Features')
plt.show()



# Scatter plot on stackOverflowSurvey.2021.medianSalary vs numberOfJobs
plt.figure(figsize=(10, 6))
plt.scatter(df['stackOverflowSurvey.2021.medianSalary'], df['numberOfJobs'], alpha=0.5)
plt.title('Median Salary vs Number of Jobs')
plt.xlabel('Median Salary (StackOverflow Survey 2021)')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.show()


