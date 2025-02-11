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
print(unique_value)