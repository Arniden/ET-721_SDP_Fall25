'''
Arnaud Tadonkeng
Oct 22, 2025
Lab 11: APIs
'''
import pandas as pd

# ----------
# 1. Example Dataframe (small APIs)
# ----------
dict_ = {
    "a":[11,21,31], 
    "b":[12,22,32]
    }

# Create a dataframe for dict_
df = pd.DataFrame(dict_)

# Display the first few rows of the dataframe
print(df.head())

# Mean method calculates and returns the mean value of the data
print(df.mean())

# ----------
# 2. Get NBA Teams (internal APIs?)
# ----------
from static import get_teams

# The method get_teams() returns a list of dictionaries
nba_teams = get_teams()
print(f"\nFirst 2 teams: {nba_teams[:2]}")

# Convert list of dictionaries into dataframe
df_teams = pd.DataFrame(nba_teams)
print(f"\n{df_teams.head()}")

# Find the id of the Warriors
df_warrior = df_teams[df_teams["nickname"]=="Warriors"]
print(f"\n{df_warrior}")

# Find the id of the Warriors using the information in the first column
warrior_id = df_warrior[["id"]].values[0][0]
print(f"\nWarriors ID = {warrior_id}")

# ----------
# 3. External APIs
# ----------
import requests
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl" 

file_name = "Golden_State.pkl"

print("\nDownloading external data")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete")
else:
    print("Download failed")

# b. Load dataframe from pickle file
games = pd.read_pickle(file_name)
print(f"\nGames data from pickle file")
print(games.head())

# c. Filter GSW vs TOR
GSW_vs_TOR = games[games["MATCHUP"].str.contains("TOR")]

gsw_home_vs_tor = GSW_vs_TOR[GSW_vs_TOR["MATCHUP"].str.contains(" vs. ")]

gsw_away_vs_tor = GSW_vs_TOR[GSW_vs_TOR["MATCHUP"].str.contains(" @ ")]

# d. Calculate averages
home_avg_plus = gsw_home_vs_tor["PLUS_MINUS"].mean()
away_avg_plus = gsw_away_vs_tor["PLUS_MINUS"].mean()
home_avg_pts = gsw_home_vs_tor["PTS"].mean()
away_avg_pts = gsw_away_vs_tor["PTS"].mean()

print(f"\nWarriors home average: {home_avg_plus}")
print(f"Warriors away average: {away_avg_plus}")

# e. Visualization 
import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label = "Home", color = "skyblue")
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label = "Away", color = "orange")
plt.xticks(x, metrics)
plt.title("Golden State Warriors vs. Raptors - Home vs Away Comparison")
plt.ylabel("Average value")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

input("Press Enter to close...")