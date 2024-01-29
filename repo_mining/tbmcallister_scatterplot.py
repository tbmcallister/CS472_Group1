import pandas as pd
import matplotlib.pyplot as plt

#use pandas in order to effectively parse and organize the data gathered in the csv

#read the csv file into a df
df = pd.read_csv('data/file_rootbeer.csv')

#convert Timestamp column to datetime format
df['timestamp'] = pd.to_datetime(df['Timestamp'])
#find the minimum timestamp (project start date)
projectStartTime = df['timestamp'].min()
#calculate weeks since the start of the project (like 250 weeks ago)
df['weeksSinceStart'] = ((df['timestamp'] - projectStartTime).dt.days) / 7

#make each filename into a number
df['filenameAsNumber'] = pd.factorize(df['Filename'].astype('category'))[0]

#get the authors and add a color to each
uniqueAuthors = df['Authorname'].unique()
#this will assign a unique color to the list of unique authors
authorColors = {}
for i, author in enumerate(uniqueAuthors):
    authorColors[author] = plt.cm.tab20(i)

#plot the scatter plot with color-coded unique colored authors
#expanded for readability
plt.scatter(df['filenameAsNumber'], 
            df['weeksSinceStart'], 
            c=df['Authorname'].map(authorColors), 
            cmap='tab20', 
            edgecolors='black'
        )

#customize labels and title
plt.xlabel('File')
plt.ylabel('Weeks')
plt.title('Commits by Author on Files in scottyab/rootbeer')

#make a legend to show which color is for what author
legendHandles = []
#iterate over the list of colors and their respective authors
#add each author,color pair to the legend
for author, color in authorColors.items():
    handle = plt.Line2D([0], 
                    [0], 
                    marker='o', 
                    color='w', 
                    label=author, 
                    markerfacecolor=color, 
                    markersize=10
                )
    legendHandles.append(handle)
#create the legend based off the handles
plt.legend(handles=legendHandles, title='Authors')

#create the plot and show it
plt.show()
