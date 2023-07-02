import threading
from Player import Player
# from .DatabaseStorag.playerDB import insert_player_data


def collect_single_player(name, insert, update):
    fname, lname = name

    player = Player.initialize_player(fname, lname)
    scrape_stats(player)

    # db.insert_player_data(player)


def collect_all_players(insert, update):
    players_names = Player.get_players()
    players      = Player.initialize_players(players_names)

    for player in players:
        scrape_stats(player)
        # db.insert_player_data(player)


def scrape_stats(player):

    threads = [
        threading.Thread(target=BoxOuts.scrape_player,          args=(player,)),
        threading.Thread(target=box_scores.scrape_player,        args=(player,)),
        threading.Thread(target=Clutch.scrape_player,           args=(player,)),
        threading.Thread(target=DefenseDashboard.scrape_player, args=(player,)),
        threading.Thread(target=General.scrape_player,          args=(player,)),
        threading.Thread(target=Hustle.scrape_player,           args=(player,)),
        threading.Thread(target=OpponentShooting.scrape_player, args=(player,)),
        threading.Thread(target=Playtypes.scrape_player,        args=(player,)),
        threading.Thread(target=Shooting.scrape_player,         args=(player,)),
        threading.Thread(target=ShotDashboard.scrape_player,    args=(player,)),
        threading.Thread(target=Tracking.scrape_player,         args=(player,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
