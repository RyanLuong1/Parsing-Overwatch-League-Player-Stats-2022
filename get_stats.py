import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff-clash/main/kickoff-clash-2022.csv')
summer_showdown_df = pd.read_csv('summer-showdown/main/summer-showdown-2022.csv')
midseason_madness_df = pd.read_csv('midseason-madness/main/midseason-madness-2022.csv')
countdown_cup_df = pd.read_csv('countdown-cup/main/countdown-cup-2022.csv')
grand_finals_df = pd.read_csv('grand-finals/main/grand-finals-2022.csv')

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

kickoff_clash_support_players_stats.to_csv("kickoff-clash/stats/kickoff-clash-support-players-stats.csv")
kickoff_clash_dps_players_stats.to_csv("kickoff-clash/stats/kickoff-clash-dps-players-stats.csv")
kickoff_clash_tank_players_stats.to_csv("kickoff-clash/stats/kickoff-clash-tank-players-stats.csv")

summer_showdown_support_players_stats.to_csv("summer-showdown/stats/summer-showdown-support-players-stats.csv")
summer_showdown_dps_players_stats.to_csv("summer-showdown/stats/summer-showdown-dps-players-stats.csv")
summer_showdown_tank_players_stats.to_csv("summer-showdown/stats/summer-showdown-tank-players-stats.csv")

midseason_madness_support_players_stats.to_csv("midseason-madness/stats/midseason-madness-support-players-stats.csv")
midseason_madness_dps_players_stats.to_csv("midseason-madness/stats/midseason-madness-dps-players-stats.csv")
midseason_madness_tank_players_stats.to_csv("midseason-madness/stats/midseason-madness-tank-players-stats.csv")

countdown_cup_support_players_stats.to_csv("countdown-cup/stats/countdown-cup-support-players-stats.csv")
countdown_cup_dps_players_stats.to_csv("countdown-cup/stats/countdown-cup-dps-players-stats.csv")
countdown_cup_tank_players_stats.to_csv("countdown-cup/stats/countdown-cup-tank-players-stats.csv")

grand_finals_support_players_stats.to_csv("grand-finals/stats/grand-finals-support-players-stats.csv")
grand_finals_dps_players_stats.to_csv("grand-finals/stats/grand-finals-dps-players-stats.csv")
grand_finals_tank_players_stats.to_csv("grand-finals/stats/grand-finals-tank-players-stats.csv")