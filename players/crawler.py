from box_outs.scraper import player as box_outs_scraper
from box_scores.scraper import player as box_scores_sraper
from clutch.scraper import player as clutch_scraper
import threading
from players import initializers, fetcher

# from .db.players import insert_player_data

# from BoxScores import Boxscores
# from BoxOuts import BoxOuts
# from clutch import Clutch
# from defense_dashboard.scraper import player as DefenseDashboard
# from General import General
# from Hustle import Hustle
# from OpponentShooting import OpponentShooting
# from Player import Player
# from Playtype import Playtypes
# from Shooting import Shooting
# from ShotDashboard import ShotDashboard
# from Tracking import Tracking


def collect_single_player(name: str, storage: bool=False):
    fname, lname = name

    player = initializers.player(fname, lname)
    scrape_stats(player)
    
    # db.insert_player_data(player)


def collect_all_players(insert = False, update = False):
    players_names = fetcher.get_all_players()
    players      = initializers.players(players_names)

    for player in players:
        scrape_stats(player)
        # db.insert_player_data(player)


def scrape_stats(player):
    threads = [
        # threading.Thread(target=box_outs_scraper,          args=(player,)),
        # threading.Thread(target=box_scores_sraper,         args=(player,)), # TODO: FIX ERROR - File "/Users/nicolasthreatt/nba-stats-crawler/box_scores/parser.py", line 65, in parse (ValueError: invalid literal for int() with base 10: '05/15/2021')
        threading.Thread(target=clutch_scraper,           args=(player,)),
        # threading.Thread(target=DefenseDashboard.scrape_player, args=(player,)),
        # threading.Thread(target=General.scrape_player,          args=(player,)),
        # threading.Thread(target=Hustle.scrape_player,           args=(player,)),
        # threading.Thread(target=OpponentShooting.scrape_player, args=(player,)),
        # threading.Thread(target=Playtypes.scrape_player,        args=(player,)),
        # threading.Thread(target=Shooting.scrape_player,         args=(player,)),
        # threading.Thread(target=ShotDashboard.scrape_player,    args=(player,)),
        # threading.Thread(target=Tracking.scrape_player,         args=(player,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
