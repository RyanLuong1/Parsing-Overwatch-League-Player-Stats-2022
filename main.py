import pandas as pd

owl_df = pd.read_csv('phs-2022.csv').loc[:, ["tournament_title", "player_name", "team_name", "stat_name", "hero_name", "amount"]]
owl_df = owl_df[owl_df.hero_name == "All Heroes"]
print(owl_df.iloc[:15])
