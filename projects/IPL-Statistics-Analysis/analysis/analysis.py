# IPL Statistics Analysis
# Project setup
import pandas as pd
df=pd.read_csv("projects/IPL-Statistics-Analysis/data/Match_Info.csv")
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

