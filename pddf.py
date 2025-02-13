import numpy as np
import pandas as pd
import matplotlib


# filttering in DataFrame
movies = pd.read_csv('/home/development/Downloads/practice/movies1.csv')
# print(movies)
matches = pd.read_csv('/home/development/Downloads/practice/ipl-matches.csv')
# print(matches)


# find all the final winners
final_matches = matches['MatchNumber']== 'Final'
final_winners = matches[final_matches]
ipl_winner = final_winners[['Season', 'WinningTeam']]
# print(ipl_winner)

final_winners = matches.loc[matches['MatchNumber'] == 'Final', ['Season', 'WinningTeam']]
# print(final_winners)

# how many super over have occured
super_over =matches[matches['SuperOver']== 'Y'].shape[0]
# print(super_over)

# how many matches has csk won in kolkata
csk_matches = matches[(matches['City'] == 'Kolkata') & (matches['WinningTeam'] == 'Chennai Super Kings')].shape[0]
# print(csk_matches)

# toss winner is match winner in percentage
winner_per = (matches[matches['TossWinner']== matches['WinningTeam']].shape[0]/matches.shape[0])* 100
# print(winner_per)
# second way to solve this 
per = (matches['TossWinner']== matches['WinningTeam']).sum()/len(matches)*100
# print(per)
# third way to solve this 
percentage = (matches['TossWinner'] == matches['WinningTeam']).mean()* 100
# print(percentage)

# movies with rating higher than 8 and votes>10000
rating = movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0]
# print(rating)

# Action movies with rating higher than 7.5
action = movies['genres'].apply(lambda x: 'Action' in x)
# print(action)
rating = movies['imdb_rating'] > 7.5
# print(rating)
action_rat = movies[action & rating]
# print(action_rat)

# write a function that can return the track record of 2 teams against each other

def track_record(matches, team1, team2):
    teams = ((matches['Team1'] == team1) & (matches['Team2'] == team2)) |((matches['Team2'] == team1) & (matches['Team1'] == team2))
    match = matches[teams]
    team1_win = int((match['WinningTeam']== team1).sum())
    team2_win = int((match['WinningTeam']== team2).sum())

    return { 'matches':match, team1: team1_win, team2: team2_win}

# print(track_record(matches, 'Rajasthan Royals', 'Gujarat Titans'))
# print(track_record(matches, 'Chennai Super Kings', 'Royal Challengers Bangalore'))

# Consider the following Python dictionary data and Python list labels:

data = {'bird': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills', 'Cranes'], 
        'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4, 3.5], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2, 2], 
        'priority': ['yes', 'yes', 'no', np.nan, 'no', 'no', 'no', 'yes', 'no', 'no','yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

# Q-1:
# i. Create a DataFrame birds from the above dictionary data which has the index labels.
birds = pd.DataFrame(data)
birds.index = labels
# print(birds)

# ii. Display basic information about the dataFrame.
# print(birds.head())

# iii. Show Alternate rows of the dataframe.

#Q-2:
# i. Show only rows [1st, 3rd, 7th] from columns ['bird', 'age']
show = birds.loc[['b','d','h'], ['bird', 'age']]
# print(show)

# ii. Select rows where the number of visits is less than 4.
vist = birds['visits'] < 4
# print(birds[vist])

#`Q-3:` 
# i. Select all rows with nan values in age and visits column.
col = ['age', 'visits']
rows = birds[col].isna().any(axis=1)
# print(birds[rows])

# ii. Fill nan with respective series mode value.
nan = birds['age'].mean()
fill_value = birds.fillna(nan)
# print(fill_value)


# Q-4
# i. Find the total number of visits of the bird Cranes
cranes_visits = birds[birds['bird']== 'Cranes']['visits'].sum()
# print(cranes_visits)

# ii. Find the number of each type of birds in dataframe.
birds_count = birds['bird'].value_counts()
# print(birds_count)

# iii. Print no of duplicate rows
no_duplicate = birds.duplicated().sum()
# print(no_duplicate)

# iv. Drop Duplicates rows and make this changes permanent. Show dataframe after changes.
birds.drop_duplicates(inplace=True)
# print(birds)


###`Q-5:` In IPL matches dataset some teams name has changed. 
# You will have to consider them as same.

# 'Delhi Capitals' formerly as 'Delhi Daredevils' 
# 'Punjab Kings' formerly as 'Kings XI Punjab'
# 'Rising Pune Supergiant' formerly as 'Rising Pune Supergiants'

# You need to make changes accordingly. Consider current name for each teams.

# Be careful Gujrat Titans and Gujrat Lions are different teams. 
team_changed = {
    'Delhi Capitals': 'Delhi Daredevils',
    'Punjab Kings': 'Kings XI Punjab',
    'Rising Pune Supergiant': 'Rising Pune Supergiants'
}
matches.replace(team_changed, inplace=True)
# print(matches[['Team1', 'Team2']])

###`Q-6` Write a code which can display the bar chart of top 5 teams who have played maximum number of matches in the IPL.
#  Hint: Be careful the data is divided in 2 different cols(Team 1 and Team 2)
top5 = (matches['Team1'].value_counts()+ matches['Team2'].value_counts()).sort_values(ascending=False).head().plot(kind='bar')
# print(top5)

###`Q-7:` Player who got Most no. of player of the match award playing against Mumbai Indians.
# > Just for this question assume player of the match award is given to players from winning team. Although this is true in most of the cases.
lost_match = matches[matches['WinningTeam'] != 'Mumbai Indians']
player_match = lost_match['Player_of_Match'].value_counts().idxmax()
# print(player_match)

# VALUE_COUNTS()
# find which player has won most potm -> in finals and qualifiers

potm = matches[~matches['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts().idxmax()
# print(potm)

# Toss decision plot
toss = matches['TossDecision'].value_counts().plot(kind='pie')
# print(toss)

# how many matches each team has played
match_played = (matches['Team1'].value_counts() + matches['Team2'].value_counts()).sort_values(ascending=False)
# print(match_played)

# SORT_VALUES()
# sort movies on title_x 
sorted = movies.sort_values('title_x')
# print(sorted)

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# sorting students on basis of name 
stu = students.sort_values('name', na_position='first')
# print(stu)

# sorting movies on basis of year_of_release,title_x
sort_movies = movies.sort_values(['year_of_release','title_x'])
# print(sort_movies)

# RANK()
batsman_runs = pd.read_csv('/home/development/Downloads/practice/batsman_runs_ipl.csv')
# print(batsman_runs.head())
batsman_runs['batting_rank'] = batsman_runs['batsman_run'].rank(ascending=False)
# print(batsman_runs.sort_values('batting_rank'))

# SORT_INDEX():
ind = batsman_runs.sort_index(ascending=False)
# print(ind)

# SET_INDEX()
batsman_runs.set_index('batter', inplace=True)
# print(batsman_runs)

# RESET_INDEX()
batsman_runs.reset_index(inplace=True)
# print(batsman_runs)

# how to replace existing index without loosing
batsman = batsman_runs.reset_index().set_index('batting_rank')
# print(batsman)

# RENAME()
column_name = movies.rename(columns={'title_x': 'title', 'poster_path': 'link'})
# print(column_name[['title', 'link']])

movie = column_name.set_index('title')
# print(movie)
index_name = movie.rename(index={'Uri: The Surgical Strike': 'Uri', 'Battalion 609': 'Battalion'})
# print(index_name.head())

# UNIQUE() and NUNIQUE()
# unique_value = len(matches['Season'].unique())
unique_value = matches['Season'].nunique()
# print(unique_value)

# ISNULL()
null_value = students.isnull().sum()
s_count = students['name'].isnull().sum()
# print(s_count)
# print(null_value)

# NOTNULL()
not_value = students.notnull()
# print(not_value)

# HASNANS
has_nan_value = students['name'].hasnans
# print(has_nan_value)

# dropna()
df = students.dropna()
df2 = students.dropna(axis=1)
df3 = students.dropna(how='all')
df4 = students.dropna(thresh=2)
df5 = students.dropna(subset=['name'])
# print(df5)

# fillna()
students[['cgpa', 'package']] = students[['cgpa', 'package']].fillna(5.50)
# print(students)

# students[['college', 'branch']] = students[['college', 'branch']].fillna(method='ffill')
# print(students)

# drop_duplicates()
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

df_unique = marks.drop_duplicates()
df_dup = students['package'].drop_duplicates()
# print(df_dup)
# print(df_unique)

# drop()
df_new = marks.drop(1)
df_new1 = marks.drop([4,2])
df_new2 = marks.drop(columns=['iq'])
df_new3 = marks.drop(['iq', 'package'], axis=1)
# print(df_new3)

# apply()
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})
df['A'] = df['A'].apply(lambda x: x *2)
df['sum'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
def square(x):
    return x** 2
exp = df.apply(square)
# print(df)
# print(exp)

# Questions:
fifa_worldcup = pd.read_csv('/home/development/Downloads/practice/Fifa Worldcup 2022 - Sheet1.csv')
# print(fifa_worldcup.head())

# Q-1: Use the football dataset. Find out the total percentages that each team made on target. 
# Display the result as a python dictionary where the keys are the team list and the values are the percentage values. 
# Round off the percentage values up to 2 decimal places.

unique_count = fifa_worldcup['Team'].unique()
result={}
for team in unique_count:
    team_df = fifa_worldcup[fifa_worldcup['Team'] == team]
    total_attempts = team_df['Total Attempts'].sum()
    on_targets = team_df['On Target'].sum()
    per = round(float(on_targets / total_attempts * 100), 2)
    result[team] = per  

# print(result)


# Q-2: Find out how many times the teams are played in this Fifa Worldcup-2022. On top of this, find out the ranks of the teams.

match_played = pd.concat([fifa_worldcup['Team'], fifa_worldcup['Against']]).value_counts()
teams_ranks = match_played.rank(ascending=False, method='first')
# print(teams_ranks) 

# Q-3: Find out these below topics:
# The information about the Fifa worldcup dataset.
wc_data = fifa_worldcup.head()
# print(wc_data)
# The description about the Fifa worldcup dataset
desc = fifa_worldcup.describe()
# print(desc)
# Check is there any missing values, if there is any missing values, fill that value with the average value for that particular column.
missing_value = fifa_worldcup.isna().sum()
# print(missing_value)
# Drop all the duplicate rows permanently.
dup = fifa_worldcup.drop_duplicates(inplace=True)
# print(dup)
# Drop the columns: "Sl No", "Match No.", "Red Cards" and "Pts" permanently.
fifa_worldcup.drop(columns=['Sl. No', 'Match No.', 'Red Cards', 'Pts'], inplace=True)
# print(fifa_worldcup.head())


# Q-4: Do these below operations:
# Find out the rank based on the "Team" column and save the result by adding a new column named "Rank".
fifa_worldcup['Rank'] = fifa_worldcup['Team'].rank(method='min', ascending=True)
# print(fifa_worldcup[['Rank', 'Team']])
# Change the datatype of this column to integer by using np.int16
# print(fifa_worldcup['Rank'].astype(np.int16))
# Set the index of the DataFrame by using this "Rank" column permanently.
fifa_worldcup.set_index('Rank', inplace=True)
# print(fifa_worldcup)
# After that, sort the dataframe based on the "Rank" index.
new_df = fifa_worldcup.sort_values('Rank', ascending=True)
# print(new_df)

#  Questions on Titanic dataset.
test = pd.read_csv('/home/development/Downloads/practice/test-test.csv')
train = pd.read_csv('/home/development/Downloads/practice/train-train.csv')

# Q-5: Do the below tasks:
# With dataset 1, drop those records which only have missing values of the "Age" column permanently.
test.dropna(subset=['Age'], inplace=True)
# print(test.isna().sum())

# With the dataset 2, fill the missing values with 20 to the only "Age" column permanently.
train.fillna({'Age':20}, inplace=True)
# print(train.isna().sum())

# functions
# concat()
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

result = pd.concat([df1['A'], df1['B']])
# print(result)

df2 = pd.DataFrame({'C': [9, 10]})

result = pd.concat([df1, df2], axis=1)
# print(result)

df3 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

result = pd.concat([df1, df3], keys=['First', 'Second'], axis=1)
# print(result)

result = pd.concat([df1, df3], keys=['First', 'Second'])
# print(result)

# isin()
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Age': [18, 19, 17, 18, 20]
}
df = pd.DataFrame(data)
grades = ['A', 'B']
filtered_df = df[df['Grade'].isin(grades)]

# print(filtered_df)

filter_value = {
    'Grade': ['A', 'B'],
    'Age': [18]
}
filtered_df = df[df['Grade'].isin(filter_value['Grade']) & df['Age'].isin(filter_value['Age'])]
print(filtered_df)