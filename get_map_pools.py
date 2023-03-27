import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff_clash/main/kickoff_clash_2022.csv')
summer_showdown_df = pd.read_csv('summer_showdown/main/summer_showdown_2022.csv')
midseason_madness_df = pd.read_csv('midseason_madness/main/midseason_madness_2022.csv')
countdown_cup_df = pd.read_csv('countdown_cup/main/countdown_cup_2022.csv')
grand_finals_df = pd.read_csv('grand_finals/main/grand_finals_2022.csv')

kickoff_clash_map_pools = kickoff_clash_df.drop_duplicates(subset=["map_name", "map_type"]).loc[:, ["map_name", "map_type"]]
summer_showdown_map_pools = summer_showdown_df.drop_duplicates(subset=["map_name", "map_type"]).loc[:, ["map_name", "map_type"]]
midseason_madness_map_pools = midseason_madness_df.drop_duplicates(subset=["map_name", "map_type"]).loc[:, ["map_name", "map_type"]]
countdown_cup_map_pools = countdown_cup_df.drop_duplicates(subset=["map_name", "map_type"]).loc[:, ["map_name", "map_type"]]
grand_finals_map_pools = grand_finals_df.drop_duplicates(subset=["map_name", "map_type"]).loc[:, ["map_name", "map_type"]]

kickoff_clash_map_pools.to_csv("kickoff_clash/main/kickoff_clash_map_pools.csv")
summer_showdown_map_pools.to_csv("summer_showdown/main/summer_showdown_map_pools.csv")
midseason_madness_map_pools.to_csv("midseason_madness/main/midseason_madness_map_pools.csv")
countdown_cup_map_pools.to_csv("countdown_cup/main/countdown_cup_map_pools.csv")
grand_finals_map_pools.to_csv("grand_finals/main/grand_finals_map_pools.csv")
