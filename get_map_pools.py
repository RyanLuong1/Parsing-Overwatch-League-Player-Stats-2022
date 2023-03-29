import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff-clash/main/kickoff-clash-2022.csv')
summer_showdown_df = pd.read_csv('summer-showdown/main/summer-showdown-2022.csv')
midseason_madness_df = pd.read_csv('midseason-madness/main/midseason-madness-2022.csv')
countdown_cup_df = pd.read_csv('countdown-cup/main/countdown-cup-2022.csv')
grand_finals_df = pd.read_csv('grand-finals/main/grand-finals-2022.csv')

kickoff_clash_map_pools = kickoff_clash_df.drop_duplicates(subset=["map_name", "map_type", "tournament_title"]).loc[:, ["map_name", "map_type", "tournament_title"]]
kickoff_clash_qualifiers_map_pools = kickoff_clash_map_pools[kickoff_clash_map_pools["tournament_title"] == "Kickoff Clash: Qualifiers"]
kickoff_clash_tournament_map_pools = kickoff_clash_map_pools[kickoff_clash_map_pools["tournament_title"] == "Kickoff Clash: Tournament"]

summer_showdown_map_pools = summer_showdown_df.drop_duplicates(subset=["map_name", "map_type", "tournament_title"]).loc[:, ["map_name", "map_type", "tournament_title"]]
summer_showdown_qualifiers_map_pools = summer_showdown_map_pools[summer_showdown_map_pools["tournament_title"] == "Summer Showdown: Qualifiers"]
summer_showdown_tournament_map_pools = summer_showdown_map_pools[summer_showdown_map_pools["tournament_title"] == "Summer Showdown: Tournament"]

midseason_madness_map_pools = midseason_madness_df.drop_duplicates(subset=["map_name", "map_type", "tournament_title"]).loc[:, ["map_name", "map_type", "tournament_title"]]
midseason_madness_qualifiers_map_pools = midseason_madness_map_pools[midseason_madness_map_pools["tournament_title"] == "Midseason Madness: Qualifiers"]
midseason_madness_tournament_map_pools = midseason_madness_map_pools[midseason_madness_map_pools["tournament_title"] == "Midseason Madness: Tournament"]

countdown_cup_map_pools = countdown_cup_df.drop_duplicates(subset=["map_name", "map_type", "tournament_title"]).loc[:, ["map_name", "map_type", "tournament_title"]]

grand_finals_map_pools = grand_finals_df.drop_duplicates(subset=["map_name", "map_type", "tournament_title"]).loc[:, ["map_name", "map_type", "tournament_title"]]


kickoff_clash_qualifiers_map_pools.to_csv("kickoff-clash/main/kickoff-clash-qualifiers-map-pools.csv")
kickoff_clash_tournament_map_pools.to_csv("kickoff-clash/main/kickoff-clash-tournament-map-pools.csv")
summer_showdown_qualifiers_map_pools.to_csv("summer-showdown/main/summer-showdown-qualifiers-map-pools.csv")
summer_showdown_tournament_map_pools.to_csv("summer-showdown/main/summer-showdown-tournament-map-pools.csv")
midseason_madness_qualifiers_map_pools.to_csv("midseason-madness/main/midseason-madness-qualifiers-map-pools.csv")
midseason_madness_tournament_map_pools.to_csv("midseason-madness/main/midseason-madness-tournament-map-pools.csv")
countdown_cup_map_pools.to_csv("countdown-cup/main/countdown-cup-map-pools.csv")
grand_finals_map_pools.to_csv("grand-finals/main/grand-finals-map-pools.csv")
