import pandas as pd


kickoff_clash_df = pd.read_csv('kickoff_clash/main/kickoff_clash_2022.csv')
summer_showdown_df = pd.read_csv('summer_showdown/main/summer_showdown_2022.csv')
midseason_madness_df = pd.read_csv('midseason_madness/main/midseason_madness_2022.csv')
countdown_cup_df = pd.read_csv('countdown_cup/main/countdown_cup_2022.csv')
grand_finals_df = pd.read_csv('grand_finals/main/grand_finals_2022.csv')

kickoff_clash_maps = kickoff_clash_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name']) \
                    .loc[kickoff_clash_df.hero_name != "All Heroes"] \
                    .loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
kickoff_clash_global_maps_count = kickoff_clash_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]) \
                                .loc[:, ["esports_match_id", "map_name", "map_type"]] \
                                .groupby(["map_name", "map_type"]) \
                                .size() \
                                .to_frame("map_count")

kickoff_clash_teams_maps_count = kickoff_clash_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first") \
                                .loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]] \
                                .groupby(["team_name", "map_type"]) \
                                .size() \
                                .to_frame("play_count") \
                                .pivot_table(values="play_count", index="team_name", columns="map_type", aggfunc="first")
kickoff_clash_teams_maps_count["total_map_played"] = kickoff_clash_teams_maps_count.iloc[:].sum(axis=1)


summer_showdown_maps = summer_showdown_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name']) \
                    .loc[summer_showdown_df.hero_name != "All Heroes"] \
                    .loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
summer_showdown_global_maps_count = summer_showdown_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]) \
                                .loc[:, ["esports_match_id", "map_name", "map_type"]] \
                                .groupby(["map_name", "map_type"]) \
                                .size() \
                                .to_frame("map_count")

summer_showdown_teams_maps_count = summer_showdown_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first") \
                                .loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]] \
                                .groupby(["team_name", "map_type"]) \
                                .size() \
                                .to_frame("play_count") \
                                .pivot_table(values="play_count", index="team_name", columns="map_type", aggfunc="first")
summer_showdown_teams_maps_count["total_map_played"] = summer_showdown_teams_maps_count.iloc[:].sum(axis=1)

midseason_madness_maps = midseason_madness_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name']) \
                    .loc[midseason_madness_df.hero_name != "All Heroes"] \
                    .loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
midseason_madness_global_maps_count = midseason_madness_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]) \
                                .loc[:, ["esports_match_id", "map_name", "map_type"]] \
                                .groupby(["map_name", "map_type"]) \
                                .size() \
                                .to_frame("map_count")

midseason_madness_teams_maps_count = midseason_madness_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first") \
                                .loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]] \
                                .groupby(["team_name", "map_type"]) \
                                .size() \
                                .to_frame("play_count") \
                                .pivot_table(values="play_count", index="team_name", columns="map_type", aggfunc="first")
midseason_madness_teams_maps_count["total_map_played"] = midseason_madness_teams_maps_count.iloc[:].sum(axis=1)

countdown_cup_maps = countdown_cup_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name']) \
                    .loc[countdown_cup_df.hero_name != "All Heroes"] \
                    .loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
countdown_cup_global_maps_count = countdown_cup_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]) \
                                .loc[:, ["esports_match_id", "map_name", "map_type"]] \
                                .groupby(["map_name", "map_type"]) \
                                .size() \
                                .to_frame("map_count")

countdown_cup_teams_maps_count = countdown_cup_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first") \
                                .loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]] \
                                .groupby(["team_name", "map_type"]) \
                                .size() \
                                .to_frame("play_count") \
                                .pivot_table(values="play_count", index="team_name", columns="map_type", aggfunc="first")
countdown_cup_teams_maps_count["total_map_played"] = countdown_cup_teams_maps_count.iloc[:].sum(axis=1)

grand_finals_maps = grand_finals_df.drop_duplicates(subset=['esports_match_id', 'map_name', 'map_type', 'player_name', 'team_name', 'hero_name']) \
                    .loc[grand_finals_df.hero_name != "All Heroes"] \
                    .loc[:, ["esports_match_id", "map_name", "map_type", "player_name", "team_name", "hero_name"]]
grand_finals_global_maps_count = grand_finals_maps.drop_duplicates(subset=["esports_match_id", "map_type", "map_name"]) \
                                .loc[:, ["esports_match_id", "map_name", "map_type"]] \
                                .groupby(["map_name", "map_type"]) \
                                .size() \
                                .to_frame("map_count")

grand_finals_teams_maps_count = grand_finals_maps.drop_duplicates(subset=["map_type", "map_name", "team_name"], keep="first") \
                                .loc[:, ["esports_match_id", "map_name", "map_type", "team_name"]] \
                                .groupby(["team_name", "map_type"]) \
                                .size() \
                                .to_frame("play_count") \
                                .pivot_table(values="play_count", index="team_name", columns="map_type", aggfunc="first")
grand_finals_teams_maps_count["total_map_played"] = grand_finals_teams_maps_count.iloc[:].sum(axis=1)

kickoff_clash_maps.to_csv("kickoff_clash/main/kickoff_clash_maps.csv")
kickoff_clash_global_maps_count.to_csv("kickoff_clash/maps_count/kickoff_clash_global_maps_count.csv")
kickoff_clash_teams_maps_count.to_csv("kickoff_clash/maps_count/kickoff_clash_teams_maps_count.csv")

midseason_madness_maps.to_csv("midseason_madness/main/midseason_madness_maps.csv")
midseason_madness_global_maps_count.to_csv("midseason_madness/maps_count/midseason_madness_global_maps_count.csv")
midseason_madness_teams_maps_count.to_csv("midseason_madness/maps_count/midseason_madness_teams_maps_count.csv")

summer_showdown_maps.to_csv("summer_showdown/main/summer_showdown_maps.csv")
summer_showdown_global_maps_count.to_csv("summer_showdown/maps_count/summer_showdown_global_maps_count.csv")
summer_showdown_teams_maps_count.to_csv("summer_showdown/maps_count/summer_showdown_teams_maps_count.csv")

countdown_cup_maps.to_csv("countdown_cup/main/countdown_cup_maps.csv")
countdown_cup_global_maps_count.to_csv("countdown_cup/maps_count/countdown_cup_global_maps_count.csv")
countdown_cup_teams_maps_count.to_csv("countdown_cup/maps_count/countdown_cup_teams_maps_count.csv")

grand_finals_maps.to_csv("grand_finals/main/grand_finals_maps.csv")
grand_finals_global_maps_count.to_csv("grand_finals/maps_count/grand_finals_global_maps_count.csv")
grand_finals_teams_maps_count.to_csv("grand_finals/maps_count/grand_finals_teams_maps_count.csv")