import pandas as pd

kickoff_clash_df = pd.read_csv('kickoff-clash/main/kickoff-clash-2022.csv')
summer_showdown_df = pd.read_csv('summer-showdown/main/summer-showdown-2022.csv')
midseason_madness_df = pd.read_csv('midseason-madness/main/midseason-madness-2022.csv')
countdown_cup_df = pd.read_csv('countdown-cup/main/countdown-cup-2022.csv')
grand_finals_df = pd.read_csv('grand-finals/main/grand-finals-2022.csv')

kickoff_clash_qualifiers_heroes_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.hero_name != "All Heroes") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Qualifiers")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

kickoff_clash_tournament_heroes_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.hero_name != "All Heroes") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Tournament")] \
                                                        .loc[:, ["hero_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

kickoff_clash_qualifiers_players_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Qualifiers")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

kickoff_clash_tournament_players_total_played_time = kickoff_clash_df.loc[(kickoff_clash_df.stat_name == "Time Played") \
                                                        & (kickoff_clash_df.tournament_title == "Kickoff Clash: Tournament")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

midseason_madness_qualifiers_heroes_total_played_time = midseason_madness_df.loc[(midseason_madness_df.stat_name == "Time Played") \
                                                        & (midseason_madness_df.hero_name != "All Heroes") \
                                                        & (midseason_madness_df.tournament_title == "Midseason Madness: Qualifiers")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

midseason_madness_tournament_heroes_total_played_time = midseason_madness_df.loc[(midseason_madness_df.stat_name == "Time Played") \
                                                        & (midseason_madness_df.hero_name != "All Heroes") \
                                                        & (midseason_madness_df.tournament_title == "Midseason Madness: Tournament")] \
                                                        .loc[:, ["hero_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

midseason_madness_qualifiers_players_total_played_time = midseason_madness_df.loc[(midseason_madness_df.stat_name == "Time Played") \
                                                        & (midseason_madness_df.tournament_title == "Midseason Madness: Qualifiers")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

midseason_madness_tournament_players_total_played_time = midseason_madness_df.loc[(midseason_madness_df.stat_name == "Time Played") \
                                                        & (midseason_madness_df.tournament_title == "Midseason Madness: Tournament")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

summer_showdown_qualifiers_heroes_total_played_time = summer_showdown_df.loc[(summer_showdown_df.stat_name == "Time Played") \
                                                        & (summer_showdown_df.hero_name != "All Heroes") \
                                                        & (summer_showdown_df.tournament_title == "Summer Showdown: Qualifiers")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

summer_showdown_tournament_heroes_total_played_time = summer_showdown_df.loc[(summer_showdown_df.stat_name == "Time Played") \
                                                        & (summer_showdown_df.hero_name != "All Heroes") \
                                                        & (summer_showdown_df.tournament_title == "Summer Showdown: Tournament")] \
                                                        .loc[:, ["hero_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 

summer_showdown_qualifiers_players_total_played_time = summer_showdown_df.loc[(summer_showdown_df.stat_name == "Time Played") \
                                                        & (summer_showdown_df.tournament_title == "Summer Showdown: Qualifiers")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

summer_showdown_tournament_players_total_played_time = summer_showdown_df.loc[(summer_showdown_df.stat_name == "Time Played") \
                                                        & (summer_showdown_df.tournament_title == "Summer Showdown: Tournament")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)

countdown_cup_qualifiers_heroes_total_played_time = countdown_cup_df.loc[(countdown_cup_df.stat_name == "Time Played") \
                                                        & (countdown_cup_df.hero_name != "All Heroes")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 


countdown_cup_qualifiers_players_total_played_time = countdown_cup_df.loc[(countdown_cup_df.stat_name == "Time Played")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)


grand_finals_heroes_total_played_time = grand_finals_df.loc[(grand_finals_df.stat_name == "Time Played") \
                                                        & (grand_finals_df.hero_name != "All Heroes")] \
                                                        .loc[:, ["hero_name", "team_name", "stat_name", "amount"]] \
                                                        .groupby(["hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True) 


grand_finals_players_total_played_time = grand_finals_df.loc[(grand_finals_df.stat_name == "Time Played")] \
                                                        .loc[:, ["player_name", "team_name", "hero_name", "stat_name", "amount"]] \
                                                        .groupby(["player_name", "team_name", "hero_name", "stat_name"]) \
                                                        .sum(numeric_only=True)


kickoff_clash_qualifiers_heroes_total_played_time.to_csv("kickoff-clash/total-played-time/kickoff-clash-qualifiers-heroes-total-played-time.csv")
kickoff_clash_qualifiers_players_total_played_time.to_csv("kickoff-clash/total-played-time/kickoff-clash-qualifiers-players-total-played-time.csv")
kickoff_clash_tournament_heroes_total_played_time.to_csv("kickoff-clash/total-played-time/kickoff-clash-tournament-heroes-total-played-time.csv")
kickoff_clash_tournament_players_total_played_time.to_csv("kickoff-clash/total-played-time/kickoff-clash-tournament-players-total-played-time.csv")

midseason_madness_qualifiers_heroes_total_played_time.to_csv("midseason-madness/total-played-time/midseason-madness-qualifiers-heroes-total-played-time.csv")
midseason_madness_qualifiers_players_total_played_time.to_csv("midseason-madness/total-played-time/midseason-madness-qualifiers-players-total-played-time.csv")
midseason_madness_tournament_heroes_total_played_time.to_csv("midseason-madness/total-played-time/midseason-madness-tournament-heroes-total-played-time.csv")
midseason_madness_tournament_players_total_played_time.to_csv("midseason-madness/total-played-time/midseason-madness-tournament-players-total-played-time.csv")

summer_showdown_qualifiers_heroes_total_played_time.to_csv("summer-showdown/total-played-time/summer-showdown-qualifiers-heroes-total-played-time.csv")
summer_showdown_qualifiers_players_total_played_time.to_csv("summer-showdown/total-played-time/summer-showdown-qualifiers-players-total-played-time.csv")
summer_showdown_tournament_heroes_total_played_time.to_csv("summer-showdown/total-played-time/summer-showdown-tournament-heroes-total-played-time.csv")
summer_showdown_tournament_players_total_played_time.to_csv("summer-showdown/total-played-time/summer-showdown-tournament-players-total-played-time.csv")

countdown_cup_qualifiers_heroes_total_played_time.to_csv("countdown-cup/total-played-time/countdown-cup-qualifiers-heroes-total-played-time.csv")
countdown_cup_qualifiers_players_total_played_time.to_csv("countdown-cup/total-played-time/countdown-cup-qualifiers-players-total-played-time.csv")

grand_finals_heroes_total_played_time.to_csv("grand-finals/total-played-time/grand-finals-heroes-total-played-time.csv")
grand_finals_players_total_played_time.to_csv("grand-finals/total-played-time/grand-finals-players-total-played-time.csv")