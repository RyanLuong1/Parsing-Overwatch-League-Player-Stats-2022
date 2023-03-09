import pandas as pd


kickoff_clash_df = pd.read_csv('kickoff_clash_2022.csv')
summer_showdown_df = pd.read_csv('summer_showdown_2022.csv')
midseason_madness_df = pd.read_csv('midseason_madness_2022.csv')
countdown_cup_df = pd.read_csv('countdown_cup_2022.csv')
grand_finals_df = pd.read_csv('grand_finals_2022.csv')

kickoff_clash_maps = kickoff_clash_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name'])[kickoff_clash_df.hero_name != "All Heroes"].loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
kickoff_clash_global_maps_count = kickoff_clash_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]).loc[:, ["esports_match_id", "map_name", "map_type"]].map_name.value_counts()
# kickoff_clash_teams_maps_count = kickoff_clash_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first").loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]].groupby(["map_type", "team_name"]).size()
summer_showdown_maps = summer_showdown_df.map_name.unique()
midseason_madness = midseason_madness_df.map_name.unique()
countdown_cup = countdown_cup_df.map_name.unique()
grand_finals = grand_finals_df.map_name.unique()
