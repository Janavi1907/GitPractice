# IPL Statistics Analysis
# Project setup
import pandas as pd
df = pd.read_csv(r"c:\Users\Janavi S\OneDrive\Desktop\gitpractice\projects\1ST YEAR PROJECTS\IPL-Statistics-Analysis\data\Match_Info.csv")

#Team Statistics
print("Team Statistics")
# Team with most wins
most_wins=df["winner"].value_counts().index[0]
print("Team with most wins:",most_wins)
# Team with least wins
least_wins=df["winner"].value_counts().index[-1]
print("Team with least wins:",least_wins)
# Team comparison
CSK_win=df[(df["winner"]=="Chennai Super Kings")]
MI_wins=df[df["winner"]=="Mumbai Indians"]
CSK_win_count=CSK_win.shape[0]
MI_wins_count=MI_wins.shape[0]
print("CSK won:",CSK_win_count)
print("MI won:",MI_wins_count)
MI_toss_win=df[df["toss_winner"]=="Mumbai Indians"]
MI_toss_win_count=MI_toss_win.shape[0]
CSK_toss_win=df[df["toss_winner"]=="Chennai Super Kings"]
CSK_toss_win_count=CSK_toss_win.shape[0]
print("MI won the toss:",MI_toss_win_count)
print("CSK won the toss:",CSK_toss_win_count)
CSK_win_with_tosswin=df[(df["winner"]=="Chennai Super Kings")&(df["toss_winner"]=="Chennai Super Kings")]
MI_win_with_tosswin=df[(df["winner"]=="Mumbai Indians")&(df["toss_winner"]=="Mumbai Indians")]
CSK_win_with_tosswin_count=CSK_win_with_tosswin.shape[0]
MI_win_with_tosswin_count=MI_win_with_tosswin.shape[0]
CSK_percentage=(CSK_win_with_tosswin_count/CSK_toss_win_count)*100
MI_percentage=(MI_win_with_tosswin_count/MI_toss_win_count)*100
print("CSK toss-to-match win percentage:",CSK_percentage.__round__(2),"%")
print("MI toss-to-match win percentage:",MI_percentage.__round__(2),"%")


#Player Statistics
print("Player Statistics")
# Most-awarded Player of the Match
most_pom=df["player_of_match"].value_counts().index[0]
print("Most awarded Player of the Match:",most_pom)
print("Most awarded player of the Match award count:",df["player_of_match"].value_counts().max())
print("Second-most awarded Player of the Match:",df["player_of_match"].value_counts().index[1])
print("Third-most awarded Player of the Match:",df["player_of_match"].value_counts().index[2])
# Top players
top_players=df["player_of_match"].value_counts().head(10)
df_top10=top_players.to_frame(name="Count").reset_index()
df_top10.index=df_top10.index+1
df_top10=df_top10.rename(columns={"index":"Player Name"})
percentage_top_players=(top_players.iloc[0]/df.shape[0])*100
print("Percentage of top player:",percentage_top_players.__round__(2),"%")
#Unique Player of the Match recipients
unquie_players=df["player_of_match"].nunique()
print("Unique Player of the Match recipients:",unquie_players)


#Toss Analysis
print("Toss Analysis")
#Most common toss decision
toss_decision=df["toss_decision"].value_counts().index[0]
print("Most common toss decision:",toss_decision)
toss_decision_bat=df[df["toss_decision"]=="bat"]
toss_decision_bat_count=toss_decision_bat.shape[0]
print("Toss decision bat count:",toss_decision_bat_count)
#Toss winner vs match winner
toss_match_win_same=df["toss_winner"]==df["winner"]
print("Toss and Match win Same:",toss_match_win_same.value_counts())
toss_match_win_same_count=toss_match_win_same.value_counts()[True]
percentage=(toss_match_win_same_count/df.shape[0])*100
print("Toss and Match win Same percentage",percentage.round(2),"%")
#Team-specific toss analysis
RCB_toss=df[(df["toss_winner"]=="Royal Challengers Bangalore")|(df["toss_winner"]=="Royal Challengers Bengaluru")]
RCB_toss_count=RCB_toss.shape[0]
print("RCB won the toss:",RCB_toss_count)


#Filters & Analysis
print("Filters & Analysis")
#Selected team analysis
RCB_win=df[(df["winner"]=="Royal Challengers Bangalore")|(df["winner"]=="Royal Challengers Bengaluru")]
RCB_win_count=RCB_win.shape[0]
print("RCB won:",RCB_win_count)
RCB_played=df[
(df["team1"]=="Royal Challengers Bangalore")
|(df["team1"]=="Royal Challengers Bengaluru")
|(df["team2"]=="Royal Challengers Bangalore")
|(df["team2"]=="Royal Challengers Bengaluru")]
RCB_losses=RCB_played.shape[0]-RCB_win_count
print("RCB losses:",RCB_losses)
RCB_win_with_tosswin=df[((df["winner"]=="Royal Challengers Bangalore")|(df["winner"]=="Royal Challengers Bengaluru"))&((df["toss_winner"]=="Royal Challengers Bangalore")|(df["toss_winner"]=="Royal Challengers Bengaluru"))]
RCB_win_with_tosswin_count=RCB_win_with_tosswin.shape[0]
print("RCB won with toss win:",RCB_win_with_tosswin_count)
RCB_win_percentage=((RCB_win_count/RCB_played.shape[0])*100)
print("RCB win percentage:",RCB_win_percentage.__round__(2),"%")
#Selected city analysis
banglore_matches=df[df["city"]=="Bangalore"]
banglore_matches_count=banglore_matches.shape[0]
print("Banglore matches Count:",banglore_matches_count)
MI_wins_mumbai=df[(df["winner"]=="Mumbai Indians")&(df["city"]=="Mumbai")]
MI_wins_mumbai_count=MI_wins_mumbai.shape[0]
print("MI wins in Mumbai:",MI_wins_mumbai_count)

#SUMMARY
#A Team with most wins is Mumbai Indians
#A player having Most Player of the Match award is AB de Villiers
#The most common toss decision is field
#The percentage of tosses resulted in the toss winner also winning the match is 50.52%
#Mumbai Indians had a higher toss-to-match-win percentage than Chennai Super Kings in this analysis.
