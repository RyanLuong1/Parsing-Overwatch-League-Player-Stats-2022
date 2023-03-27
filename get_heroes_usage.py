import pandas as pd


kickoff_clash_df = pd.read_csv('kickoff-clash/main/kickoff-clash-2022.csv')
summer_showdown_df = pd.read_csv('summer-showdown/main/summer-showdown-2022.csv')
midseason_madness_df = pd.read_csv('midseason-madness/main/midseason-madness-2022.csv')
countdown_cup_df = pd.read_csv('countdown-cup/main/countdown-cup-2022.csv')
grand_finals_df = pd.read_csv('grand-finals/main/grand-finals-2022.csv')

support_heroes = ["Ana", "Baptiste", "Brigitte", "Kiriko", "Lucio", "Mercy", "Moira", "Zenyatta"]
dps_heroes = ["Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]
tank_heroes = ["D.va", "Doomfist", "Junker Queen", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya"]

kickoff_clash_heroes = kickoff_clash_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[kickoff_clash_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
kickoff_clash_global_heroes_usage = kickoff_clash_heroes.groupby(["hero_name"]).size().to_frame("total_times_played")
kickoff_clash_support_players_heroes_usage = kickoff_clash_heroes[kickoff_clash_heroes.hero_name.isin(support_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
kickoff_clash_support_players_heroes_usage["total_times_played"] = kickoff_clash_support_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
kickoff_clash_dps_players_heroes_usage = kickoff_clash_heroes[kickoff_clash_heroes.hero_name.isin(dps_heroes)] \
                                        .groupby(["player_name", "team_name", "hero_name"]) \
                                        .size().to_frame("times_played")
kickoff_clash_dps_players_heroes_usage["total_times_played"] = kickoff_clash_dps_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
kickoff_clash_tank_players_heroes_usage = kickoff_clash_heroes[kickoff_clash_heroes.hero_name.isin(tank_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
kickoff_clash_tank_players_heroes_usage["total_times_played"] = kickoff_clash_tank_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()


summer_showdown_heroes = summer_showdown_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[summer_showdown_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
summer_showdown_global_heroes_usage = summer_showdown_heroes.groupby(["hero_name"]).size().to_frame("total_times_played")
summer_showdown_support_players_heroes_usage = summer_showdown_heroes[summer_showdown_heroes.hero_name.isin(support_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
summer_showdown_support_players_heroes_usage["total_times_played"] = summer_showdown_support_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
summer_showdown_dps_players_heroes_usage = summer_showdown_heroes[summer_showdown_heroes.hero_name.isin(dps_heroes)] \
                                        .groupby(["player_name", "team_name", "hero_name"]) \
                                        .size().to_frame("times_played")
summer_showdown_dps_players_heroes_usage["total_times_played"] = summer_showdown_dps_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
summer_showdown_tank_players_heroes_usage = summer_showdown_heroes[summer_showdown_heroes.hero_name.isin(tank_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
summer_showdown_tank_players_heroes_usage["total_times_played"] = summer_showdown_tank_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()

midseason_madness_heroes = midseason_madness_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[midseason_madness_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
midseason_madness_global_heroes_usage = midseason_madness_heroes.groupby(["hero_name"]).size().to_frame("total_times_played")
midseason_madness_support_players_heroes_usage = midseason_madness_heroes[midseason_madness_heroes.hero_name.isin(support_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
midseason_madness_support_players_heroes_usage["total_times_played"] = midseason_madness_support_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
midseason_madness_dps_players_heroes_usage = midseason_madness_heroes[midseason_madness_heroes.hero_name.isin(dps_heroes)] \
                                        .groupby(["player_name", "team_name", "hero_name"]) \
                                        .size().to_frame("times_played")
midseason_madness_dps_players_heroes_usage["total_times_played"] = midseason_madness_dps_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
midseason_madness_tank_players_heroes_usage = midseason_madness_heroes[midseason_madness_heroes.hero_name.isin(tank_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
midseason_madness_tank_players_heroes_usage["total_times_played"] = midseason_madness_tank_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()

countdown_cup_heroes = countdown_cup_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[countdown_cup_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
countdown_cup_global_heroes_usage = countdown_cup_heroes.groupby(["hero_name"]).size().to_frame("total_times_played")
countdown_cup_support_players_heroes_usage = countdown_cup_heroes[countdown_cup_heroes.hero_name.isin(support_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
countdown_cup_support_players_heroes_usage["total_times_played"] = countdown_cup_support_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
countdown_cup_dps_players_heroes_usage = countdown_cup_heroes[countdown_cup_heroes.hero_name.isin(dps_heroes)] \
                                        .groupby(["player_name", "team_name", "hero_name"]) \
                                        .size().to_frame("times_played")
countdown_cup_dps_players_heroes_usage["total_times_played"] = countdown_cup_dps_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
countdown_cup_tank_players_heroes_usage = countdown_cup_heroes[countdown_cup_heroes.hero_name.isin(tank_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
countdown_cup_tank_players_heroes_usage["total_times_played"] = countdown_cup_tank_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()

grand_finals_heroes = grand_finals_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[grand_finals_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
grand_finals_global_heroes_usage = grand_finals_heroes.groupby(["hero_name"]).size().to_frame("total_times_played")
grand_finals_support_players_heroes_usage = grand_finals_heroes[grand_finals_heroes.hero_name.isin(support_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
grand_finals_support_players_heroes_usage["total_times_played"] = grand_finals_support_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
grand_finals_dps_players_heroes_usage = grand_finals_heroes[grand_finals_heroes.hero_name.isin(dps_heroes)] \
                                        .groupby(["player_name", "team_name", "hero_name"]) \
                                        .size().to_frame("times_played")
grand_finals_dps_players_heroes_usage["total_times_played"] = grand_finals_dps_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()
grand_finals_tank_players_heroes_usage = grand_finals_heroes[grand_finals_heroes.hero_name.isin(tank_heroes)] \
                                            .groupby(["player_name", "team_name", "hero_name"]) \
                                            .size().to_frame("times_played")
grand_finals_tank_players_heroes_usage["total_times_played"] = grand_finals_tank_players_heroes_usage.groupby(["player_name", "team_name"])["times_played"].sum()

kickoff_clash_heroes.to_csv("kickoff-clash/main/kickoff-clash-heroes.csv")
kickoff_clash_global_heroes_usage.to_csv("kickoff-clash/heroes-usage/kickoff-clash-global-heroes-usage.csv")
kickoff_clash_support_players_heroes_usage.to_csv("kickoff-clash/heroes-usage/kickoff-clash-support-players-heroes-usage.csv")
kickoff_clash_dps_players_heroes_usage.to_csv("kickoff-clash/heroes-usage/kickoff-clash-dps-players-heroes-usage.csv")
kickoff_clash_tank_players_heroes_usage.to_csv("kickoff-clash/heroes-usage/kickoff-clash-tank-players-heroes-usage.csv")

midseason_madness_heroes.to_csv("midseason-madness/main/midseason-madness-heroes.csv")
midseason_madness_global_heroes_usage.to_csv("midseason-madness/heroes-usage/midseason-madness-global-heroes-usage.csv")
midseason_madness_support_players_heroes_usage.to_csv("midseason-madness/heroes-usage/midseason-madness-support-players-heroes-usage.csv")
midseason_madness_dps_players_heroes_usage.to_csv("midseason-madness/heroes-usage/midseason-madness-dps-players-heroes-usage.csv")
midseason_madness_tank_players_heroes_usage.to_csv("midseason-madness/heroes-usage/midseason-madness-tank-players-heroes-usage.csv")

summer_showdown_heroes.to_csv("summer-showdown/main/summer-showdown-heroes.csv")
summer_showdown_global_heroes_usage.to_csv("summer-showdown/heroes-usage/summer-showdown-global-heroes-usage.csv")
summer_showdown_support_players_heroes_usage.to_csv("summer-showdown/heroes-usage/summer-showdown-support-players-heroes-usage.csv")
summer_showdown_dps_players_heroes_usage.to_csv("summer-showdown/heroes-usage/summer-showdown-dps-players-heroes-usage.csv")
summer_showdown_tank_players_heroes_usage.to_csv("summer-showdown/heroes-usage/summer-showdown-tank-players-heroes-usage.csv")

countdown_cup_heroes.to_csv("countdown-cup/main/countdown-cup-heroes.csv")
countdown_cup_global_heroes_usage.to_csv("countdown-cup/heroes-usage/countdown-cup-global-heroes-usage.csv")
countdown_cup_support_players_heroes_usage.to_csv("countdown-cup/heroes-usage/countdown-cup-support-players-heroes-usage.csv")
countdown_cup_dps_players_heroes_usage.to_csv("countdown-cup/heroes-usage/countdown-cup-dps-players-heroes-usage.csv")
countdown_cup_tank_players_heroes_usage.to_csv("countdown-cup/heroes-usage/countdown-cup-tank-players-heroes-usage.csv")

grand_finals_heroes.to_csv("grand-finals/main/grand-finals-heroes.csv")
grand_finals_global_heroes_usage.to_csv("grand-finals/heroes-usage/grand-finals-global-heroes-usage.csv")
grand_finals_support_players_heroes_usage.to_csv("grand-finals/heroes-usage/grand-finals-support-players-heroes-usage.csv")
grand_finals_dps_players_heroes_usage.to_csv("grand-finals/heroes-usage/grand-finals-dps-players-heroes-usage.csv")
grand_finals_tank_players_heroes_usage.to_csv("grand-finals/heroes-usage/grand-finals-tank-players-heroes-usage.csv")