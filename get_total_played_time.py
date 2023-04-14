import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff-clash/main/kickoff-clash-2022.csv')
summer_showdown_df = pd.read_csv('summer-showdown/main/summer-showdown-2022.csv')
midseason_madness_df = pd.read_csv('midseason-madness/main/midseason-madness-2022.csv')
countdown_cup_df = pd.read_csv('countdown-cup/main/countdown-cup-2022.csv')
grand_finals_df = pd.read_csv('grand-finals/main/grand-finals-2022.csv')

support_heroes = ["Ana", "Baptiste", "Brigitte", "Kiriko", "Lucio", "Mercy", "Moira", "Zenyatta"]
dps_heroes = ["Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]
tank_heroes = ["D.va", "Doomfist", "Junker Queen", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya"]

kickoff_clash_qualifiers_all_heroes_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.hero_name != "All Heroes") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Qualifiers")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum() 

kickoff_clash_tournament_all_heroes_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.hero_name != "All Heroes") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Tournament")] \
                                                        .loc[:, ["hero_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum() 

kickoff_clash_qualifiers_players_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Qualifiers")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum()



print(kickoff_clash_qualifiers_players_total_played_time)