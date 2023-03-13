import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff_clash/main/kickoff_clash_2022.csv')
summer_showdown_df = pd.read_csv('summer_showdown/main/summer_showdown_2022.csv')
midseason_madness_df = pd.read_csv('midseason_madness/main/midseason_madness_2022.csv')
countdown_cup_df = pd.read_csv('countdown_cup/main/countdown_cup_2022.csv')
grand_finals_df = pd.read_csv('grand_finals/main/grand_finals_2022.csv')

support_heroes = ["Ana", "Baptiste", "Brigitte", "Kiriko", "Lucio", "Mercy", "Moira", "Zenyatta", "All Heroes"]
dps_heroes = ["Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "All Heroes"]
tank_heroes = ["D.va", "Doomfist", "Junker Queen", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya", "All Heroes"]

kickoff_clash_support_players_stats = kickoff_clash_df.loc[kickoff_clash_df.hero_name.isin(support_heroes)]
kickoff_clash_dps_players_stats = kickoff_clash_df.loc[kickoff_clash_df.hero_name.isin(dps_heroes)]
kickoff_clash_tank_players_stats = kickoff_clash_df.loc[kickoff_clash_df.hero_name.isin(tank_heroes)]

summer_showdown_support_players_stats = summer_showdown_df.loc[summer_showdown_df.hero_name.isin(support_heroes)]
summer_showdown_dps_players_stats = summer_showdown_df.loc[summer_showdown_df.hero_name.isin(dps_heroes)]
summer_showdown_tank_players_stats = summer_showdown_df.loc[summer_showdown_df.hero_name.isin(tank_heroes)]

midseason_madness_support_players_stats = midseason_madness_df.loc[midseason_madness_df.hero_name.isin(support_heroes)]
midseason_madness_dps_players_stats = midseason_madness_df.loc[midseason_madness_df.hero_name.isin(dps_heroes)]
midseason_madness_tank_players_stats = midseason_madness_df.loc[midseason_madness_df.hero_name.isin(tank_heroes)]

countdown_cup_support_players_stats = countdown_cup_df.loc[countdown_cup_df.hero_name.isin(support_heroes)]
countdown_cup_dps_players_stats = countdown_cup_df.loc[countdown_cup_df.hero_name.isin(dps_heroes)]
countdown_cup_tank_players_stats = countdown_cup_df.loc[countdown_cup_df.hero_name.isin(tank_heroes)]

grand_finals_support_players_stats = grand_finals_df.loc[grand_finals_df.hero_name.isin(support_heroes)]
grand_finals_dps_players_stats = grand_finals_df.loc[grand_finals_df.hero_name.isin(dps_heroes)]
grand_finals_tank_players_stats = grand_finals_df.loc[grand_finals_df.hero_name.isin(tank_heroes)]

kickoff_clash_support_players_stats.to_csv("kickoff_clash/stats/kickoff_clash_support_players_stats.csv")
kickoff_clash_dps_players_stats.to_csv("kickoff_clash/stats/kickoff_clash_dps_players_stats.csv")
kickoff_clash_tank_players_stats.to_csv("kickoff_clash/stats/kickoff_clash_tank_players_stats.csv")

summer_showdown_support_players_stats.to_csv("summer_showdown/stats/summer_showdown_support_players_stats.csv")
summer_showdown_dps_players_stats.to_csv("summer_showdown/stats/summer_showdown_dps_players_stats.csv")
summer_showdown_tank_players_stats.to_csv("summer_showdown/stats/summer_showdown_tank_players_stats.csv")

midseason_madness_support_players_stats.to_csv("midseason_madness/stats/midseason_madness_support_players_stats.csv")
midseason_madness_dps_players_stats.to_csv("midseason_madness/stats/midseason_madness_dps_players_stats.csv")
midseason_madness_tank_players_stats.to_csv("midseason_madness/stats/midseason_madness_tank_players_stats.csv")

countdown_cup_support_players_stats.to_csv("countdown_cup/stats/countdown_cup_support_players_stats.csv")
countdown_cup_dps_players_stats.to_csv("countdown_cup/stats/countdown_cup_dps_players_stats.csv")
countdown_cup_tank_players_stats.to_csv("countdown_cup/stats/countdown_cup_tank_players_stats.csv")

grand_finals_support_players_stats.to_csv("grand_finals/stats/grand_finals_support_players_stats.csv")
grand_finals_dps_players_stats.to_csv("grand_finals/stats/grand_finals_dps_players_stats.csv")
grand_finals_tank_players_stats.to_csv("grand_finals/stats/grand_finals_tank_players_stats.csv")