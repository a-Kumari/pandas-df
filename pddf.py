import numpy as np
import pandas as pd

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