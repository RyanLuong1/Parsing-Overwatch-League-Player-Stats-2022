import pandas as pd


kickoff_clash_df = pd.read_csv('kickoff_clash/main/kickoff_clash_2022.csv')
summer_showdown_df = pd.read_csv('summer_showdown/main/summer_showdown_2022.csv')
midseason_madness_df = pd.read_csv('midseason_madness/main/midseason_madness_2022.csv')
countdown_cup_df = pd.read_csv('countdown_cup/main/countdown_cup_2022.csv')
grand_finals_df = pd.read_csv('grand_finals/main/grand_finals_2022.csv')

support_heroes = ["Ana", "Baptiste", "Brigitte", "Kiriko", "Lucio", "Mercy", "Moira", "Zenyatta"]
dps_heroes = ["Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]
tank_heroes = ["D.va", "Doomfist", "Junker Queen", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya"]

kickoff_clash_heroes = kickoff_clash_df.drop_duplicates(subset=['esports_match_id', "map_name", "map_type", "player_name", "team_name", "hero_name"]) \
                       .loc[kickoff_clash_df.hero_name != "All Heroes"] \
                       .loc[:, ["map_name", "player_name", "team_name", "hero_name"]]
kickoff_clash_global_heroes_usage = kickoff_clash_heroes.groupby(["hero_name"]).size()
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
summer_showdown_global_heroes_usage = summer_showdown_heroes.groupby(["hero_name"]).size()
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
midseason_madness_global_heroes_usage = midseason_madness_heroes.groupby(["hero_name"]).size()
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
countdown_cup_global_heroes_usage = countdown_cup_heroes.groupby(["hero_name"]).size()
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
grand_finals_global_heroes_usage = grand_finals_heroes.groupby(["hero_name"]).size()
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

kickoff_clash_heroes.to_csv("kickoff_clash/main/kickoff_clash_heroes.csv")
kickoff_clash_global_heroes_usage.to_csv("kickoff_clash/heroes_usage/kickoff_clash_global_heroes_usage.csv")
kickoff_clash_support_players_heroes_usage.to_csv("kickoff_clash/heroes_usage/kickoff_clash_support_players_heroes_usage.csv")
kickoff_clash_dps_players_heroes_usage.to_csv("kickoff_clash/heroes_usage/kickoff_clash_dps_players_heroes_usage.csv")
kickoff_clash_tank_players_heroes_usage.to_csv("kickoff_clash/heroes_usage/kickoff_clash_tank_players_heroes_usage.csv")

midseason_madness_heroes.to_csv("midseason_madness/main/midseason_madness_heroes.csv")
midseason_madness_global_heroes_usage.to_csv("midseason_madness/heroes_usage/midseason_madness_global_heroes_usage.csv")
midseason_madness_support_players_heroes_usage.to_csv("midseason_madness/heroes_usage/midseason_madness_support_players_heroes_usage.csv")
midseason_madness_dps_players_heroes_usage.to_csv("midseason_madness/heroes_usage/midseason_madness_dps_players_heroes_usage.csv")
midseason_madness_tank_players_heroes_usage.to_csv("midseason_madness/heroes_usage/midseason_madness_tank_players_heroes_usage.csv")

summer_showdown_heroes.to_csv("summer_showdown/main/summer_showdown_heroes.csv")
summer_showdown_global_heroes_usage.to_csv("summer_showdown/heroes_usage/summer_showdown_global_heroes_usage.csv")
summer_showdown_support_players_heroes_usage.to_csv("summer_showdown/heroes_usage/summer_showdown_support_players_heroes_usage.csv")
summer_showdown_dps_players_heroes_usage.to_csv("summer_showdown/heroes_usage/summer_showdown_dps_players_heroes_usage.csv")
summer_showdown_tank_players_heroes_usage.to_csv("summer_showdown/heroes_usage/summer_showdown_tank_players_heroes_usage.csv")

countdown_cup_heroes.to_csv("countdown_cup/main/countdown_cup_heroes.csv")
countdown_cup_global_heroes_usage.to_csv("countdown_cup/heroes_usage/countdown_cup_global_heroes_usage.csv")
countdown_cup_support_players_heroes_usage.to_csv("countdown_cup/heroes_usage/countdown_cup_support_players_heroes_usage.csv")
countdown_cup_dps_players_heroes_usage.to_csv("countdown_cup/heroes_usage/countdown_cup_dps_players_heroes_usage.csv")
countdown_cup_tank_players_heroes_usage.to_csv("countdown_cup/heroes_usage/countdown_cup_tank_players_heroes_usage.csv")

grand_finals_heroes.to_csv("grand_finals/main/grand_finals_heroes.csv")
grand_finals_global_heroes_usage.to_csv("grand_finals/heroes_usage/grand_finals_global_heroes_usage.csv")
grand_finals_support_players_heroes_usage.to_csv("grand_finals/heroes_usage/grand_finals_support_players_heroes_usage.csv")
grand_finals_dps_players_heroes_usage.to_csv("grand_finals/heroes_usage/grand_finals_dps_players_heroes_usage.csv")
grand_finals_tank_players_heroes_usage.to_csv("grand_finals/heroes_usage/grand_finals_tank_players_heroes_usage.csv")