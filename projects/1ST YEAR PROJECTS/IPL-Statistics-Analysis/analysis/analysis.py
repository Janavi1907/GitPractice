# IPL Statistics Analysis
# Project setup
import pandas as pd
df = pd.read_csv(r"c:\Users\Janavi S\OneDrive\Desktop\gitpractice\projects\1ST YEAR PROJECTS\IPL-Statistics-Analysis\data\Match_Info.csv")

#Team Statistics

winning_count=df["winner"].value_counts()
print(winning_count)
# PROGRAM 1
most_wins=df["winner"].value_counts().index[0]
print(most_wins)
#PROGRAM 2
least_wins=df["winner"].value_counts().index[-1]
print(least_wins)
#PROGRAM 3
toss_match_win_same=df["toss_winner"]==df["winner"]
print(toss_match_win_same.value_counts())
#PROGRAM 4
toss_match_win_same_count=toss_match_win_same.value_counts()[True]
percentage=(toss_match_win_same_count/df.shape[0])*100
print("Toss and Match win Same percentage",percentage.round(2),"%")
# PROGRAM 5
toss_decision=df["toss_decision"].value_counts().index[0]
print("Most common toss decision:",toss_decision)

#Player Statistics

# PROGRAM 1
print(df["player_of_match"])
# PROGRAM 2
print(df["player_of_match"].value_counts())
# PROGRAM 3
most_pom=df["player_of_match"].value_counts().index[0]
print("Most awarded Player of the Match:",most_pom)
# PROGRAM 4
top_players=df["player_of_match"].value_counts().head(10)
print(top_players)
# PROGRAM 5
print(df["player_of_match"].isnull().sum())
#PROGRAM 6
percentage_top_players=(top_players.iloc[0]/df.shape[0])*100
print(percentage_top_players)
#CHALLENGE 1
print("Second-most awarded Player of the Match:",df["player_of_match"].value_counts().index[1])
#CHALLENGE 2
print("Third-most awarded Player of the Match:",df["player_of_match"].value_counts().index[2])
#CHALLENGE 3
unquie_players=df["player_of_match"].nunique()
print(unquie_players)
#CHALLENGE 4
print(df["player_of_match"].isnull().sum())

