#(5/5 points) Initial comments with your name, class and project at the top of your .py file.

# INF601 - Advanced Programming in Python
# Derrick Aragon
# Mini Project #2

#(5/5 points) Proper import of packages used.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets


#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.

# Dataset containing all countries ranked based on their global happiness index
data = pd.read_csv('happiness.csv', index_col='Countries')



# Gets the last 5 or most unhappy countries back

unhappy = data.tail(5)
print("5 Most Unhappy Countries:")
print(unhappy)

#Gets the first 5 most happy countries back

happy = data.head(5)
print("5 Happiest Countries:")
print(happy)

# Creates the charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

# Plots the graph for the most unhappy countries in comparison to the global index
plt.figure(figsize=(10, 5))
unhappy.plot(title="5 Most Unhappy Countries", kind='bar')
plt.ylabel("Happiness Score")
plt.tight_layout()

# Saves chart
plt.savefig("charts/unhappy_countries.png")
plt.show()



# Plots the graph for the most happy countires in comparison to the global index
plt.figure(figsize=(10, 5))
happy.plot(title="5 Happiest Countries", kind='bar')
plt.ylabel("Happiness Score")
plt.tight_layout()

# Saves Chart
plt.savefig("charts/happy_countries.png")
plt.show()

# Concatenation for comparison of happy and unhappy

compare = pd.concat([happy, unhappy])

# Plotting the comparison graph
plt.figure(figsize=(12, 6))
compare.plot(kind='bar', title="Comparison of 5 Happiest and 5 Unhappiest Countries")
plt.ylabel("Happiness Score")
plt.tight_layout()

# Saves chart
plt.savefig("charts/combined_countries.png")
plt.show()

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.


#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!

#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.

#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.