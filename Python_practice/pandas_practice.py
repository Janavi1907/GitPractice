import pandas as pd
data = {
    "Team":["RCB","CSK","RCB","MI"],
    "Wins":[10,8,7,9]
}
df=pd.DataFrame(data)
print(df)
print(df["Team"])
print(df["Team"].value_counts())