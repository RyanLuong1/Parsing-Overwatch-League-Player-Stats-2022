import pandas as pd


qualifier_and_tournament = ["Kickoff Clash: Qualifiers", "Kickoff Clash: Tournament"]
owl_df = pd.read_csv('phs-2022.csv').loc[:, ["tournament_title", "player_name", "team_name", "stat_name", "hero_name", "amount"]]
kickoff_clash_df = owl_df[owl_df.tournament_title.isin(qualifier_and_tournament)]
kickoff_clash_df.to_csv("kickoff_clash_2022.csv", header=False, index=False)
