import threading
from players import initializers
# from .db.players import insert_player_data


def collect_single_player(name: str, storage = None):
    fname, lname = name

    player = initializers.player(fname, lname)
    # scrape_stats(player)
    
    # db.insert_player_data(player)


def collect_all_players(insert = False, update = False):
    players_names = Player.get_players()
    players      = Player.initialize_players(players_names)

    for player in players:
        scrape_stats(player)
        # db.insert_player_data(player)


def scrape_stats(player):
    threads = [
        threading.Thread(target=BoxOuts.scrape_player,          args=(player,)),
        # threading.Thread(target=box_scores.scrape_player,        args=(player,)),
        # threading.Thread(target=Clutch.scrape_player,           args=(player,)),
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
