import pandas as pd


qualifier = ["Countdown Cup: Qualifiers"]
owl_df = pd.read_csv('phs-2022.csv').loc[:, ["tournament_title", "player_name", "team_name", "stat_name", "hero_name", "amount"]]
owl_df = owl_df[owl_df.tournament_title.isin(qualifier)]
print(owl_df)
