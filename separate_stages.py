import pandas as pd

owl_df = pd.read_csv('phs-2022.csv').loc[:, ["esports_match_id", "tournament_title", "map_type", "map_name", "player_name", "team_name", "stat_name", "hero_name", "amount"]]
kickoff_clash_df = owl_df[owl_df.tournament_title.isin(["Kickoff Clash: Qualifiers", "Kickoff Clash: Tournament"])]
midseason_madness_df = owl_df[owl_df.tournament_title.isin(["Midseason Madness: Qualifiers", "Midseason Madness: Tournament"])]
summer_showdown_df = owl_df[owl_df.tournament_title.isin(["Summer Showdown: Qualifiers", "Summer Showdown: Tournament"])]
countdown_cup_df = owl_df[owl_df.tournament_title.isin(["Countdown Cup: Qualifiers"])]
grand_finals_df =  owl_df[owl_df.tournament_title.isin(["Postseason"])]

kickoff_clash_df.to_csv("kickoff-clash/main/kickoff-clash-2022.csv", index=False)
midseason_madness_df.to_csv("midseason-madness/main/midseason-madness-2022.csv", index=False)
summer_showdown_df.to_csv("summer-showdown/main/summer-showdown-2022.csv", index=False)
countdown_cup_df.to_csv("countdown-cup/main/countdown-cup-2022.csv", index=False)
grand_finals_df.to_csv("grand-finals/main/grand-finals-2022.csv", index=False)

