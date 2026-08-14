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

#PROGARM 1
MI_wins=df[df["winner"]=="Mumbai Indians"]
print(MI_wins)
#PROGARM 2
MI_wins_count=MI_wins.shape[0]
print("MI won :",MI_wins_count)
#PROGRAM 3
banglore_matches=df[df["city"]=="Bangalore"]
print(banglore_matches)
#PROGRAM 4
MI_wins_mumbai=df[(df["winner"]=="Mumbai Indians")&(df["city"]=="Mumbai")]
print(MI_wins_mumbai)
#PROGRAM 5
toss_decision_bat=df[df["toss_decision"]=="bat"]
print(toss_decision_bat)
#PROGRAM 6
toss_decision_bat_count=toss_decision_bat.shape[0]
print("Toss decision bat count:",toss_decision_bat_count)
#PROGRAM 7
MI_win_with_tosswin=df[(df["winner"]=="Mumbai Indians")&(df["toss_winner"]=="Mumbai Indians")]
print(MI_win_with_tosswin)
#PROGRAM 8
RCB_win=df[(df["winner"]=="Royal Challengers Bangalore")|(df["winner"]=="Royal Challengers Bengaluru")]
RCB_win_count=RCB_win.shape[0]
print("RCB won:",RCB_win_count)
#PROGRAM 9
RCB_played=df[
(df["team1"]=="Royal Challengers Bangalore")
|(df["team1"]=="Royal Challengers Bengaluru")
|(df["team2"]=="Royal Challengers Bangalore")
|(df["team2"]=="Royal Challengers Bengaluru")]
RCB_losses=RCB_played.shape[0]-RCB_win_count
print("RCB losses:",RCB_losses)
#PROGRAM 10
RCB_toss=df[(df["toss_winner"]=="Royal Challengers Bangalore")|(df["toss_winner"]=="Royal Challengers Bengaluru")]
RCB_toss_count=RCB_toss.shape[0]
print("RCB won the toss:",RCB_toss_count)
#PROGRAM 11
RCB_win_with_tosswin=df[((df["winner"]=="Royal Challengers Bangalore")|(df["winner"]=="Royal Challengers Bengaluru"))&((df["toss_winner"]=="Royal Challengers Bangalore")|(df["toss_winner"]=="Royal Challengers Bengaluru"))]
RCB_win_with_tosswin_count=RCB_win_with_tosswin.shape[0]
print("RCB won with toss win:",RCB_win_with_tosswin_count)
#PROGRAM 12
RCB_win_percentage=((RCB_win_count/RCB_played.shape[0])*100)
print("RCB win percentage:",RCB_win_percentage.__round__(2),"%")
#PROGRAM 13(COMPARE CSK & MI)
CSK_win=df[(df["winner"]=="Chennai Super Kings")]
CSK_win_count=CSK_win.shape[0]
print("CSK won:",CSK_win_count)
print("MI won:",MI_wins_count)
#PROGRAM 14(COMPARE CSK & MI)
MI_toss_win=df[df["toss_winner"]=="Mumbai Indians"]
MI_toss_win_count=MI_toss_win.shape[0]
CSK_toss_win=df[df["toss_winner"]=="Chennai Super Kings"]
CSK_toss_win_count=CSK_toss_win.shape[0]
print("MI won the toss:",MI_toss_win_count)
print("CSK won the toss:",CSK_toss_win_count)
#PROGRAM 15(COMPARE CSK & MI)
CSK_win_with_tosswin=df[(df["winner"]=="Chennai Super Kings")&(df["toss_winner"]=="Chennai Super Kings")]
CSK_win_with_tosswin_count=CSK_win_with_tosswin.shape[0]
CSK_percentage=(CSK_win_with_tosswin_count/CSK_toss_win_count)*100
MI_win_with_tosswin_count=MI_win_with_tosswin.shape[0]
MI_percentage=(MI_win_with_tosswin_count/MI_toss_win_count)*100
print("CSK win percentage:",CSK_percentage.__round__(2),"%")
print("MI win percentage:",MI_percentage.__round__(2),"%")
#CHALLENGE 1
print(df[df["winner"]=="Mumbai Indians"])
#CHALLENGE 2
print(df[df["winner"]=="Chennai Super Kings"])
#CHALLENGE 3
print(df[df["city"]=="Bangalore"])
##CHALLENGE 4
print(df[df["toss_decision"]=="field"])
#CHALLENGE 5
print("MI won with toss win :",MI_win_with_tosswin)
##CHALLENGE 6
print(df[(df["team1"]=="Mumbai Indians")|(df["team2"]=="Mumbai Indians")])

