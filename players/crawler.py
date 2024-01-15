import threading
from db.players import insert_player_data
from players import initializers, fetcher
from box_outs.scraper import player as box_outs_scraper
from box_scores.scraper import player as box_scores_scraper
from clutch.scraper import player as clutch_scraper
from defense.scraper import player as defense_scraper
from general.scraper import player as general_scraper
from hustle.scraper import player as hustle_scraper
from opponent_shooting.scraper import player as opponent_shooting_scraper
from play_types.scraper import player as play_types_scraper
from shooting.scraper import player as shooting_scraper
from shot_dashboard.scraper import player as shot_dashboard_scraper
from tracking.scraper import player as tracking_scraper


def collect_single_player(name: str, storage: bool=False):
    fname, lname = name

    player = initializers.player(fname, lname)
    scrape_stats(player)
    
    if storage == "insert":
        insert_player_data(player)


def collect_all_players(insert = False, update = False):
    players_names = fetcher.get_all_players()
    players      = initializers.players(players_names)

    for player in players:
        scrape_stats(player)

        if storage == "insert":
            insert_player_data(player)


def scrape_stats(player):
    threads = [
        # threading.Thread(target=box_outs_scraper,          args=(player,)),
        # threading.Thread(target=box_scores_scraper,        args=(player,)), # TODO: FIX ERROR (parser)
        # threading.Thread(target=clutch_scraper,            args=(player,)),
        # threading.Thread(target=defense_scraper,           args=(player,)),
        # threading.Thread(target=general_scraper,           args=(player,)), # TODO: FIX ERROR (parser)
        # threading.Thread(target=hustle_scraper,            args=(player,)),
        # threading.Thread(target=opponent_shooting_scraper, args=(player,)),
        # threading.Thread(target=play_types_scraper,        args=(player,)),  # TODO: FIX ERROR (parser)
        # threading.Thread(target=shooting_scraper,          args=(player,)),
        # threading.Thread(target=shot_dashboard_scraper,    args=(player,)),
        # threading.Thread(target=tracking_scraper,          args=(player,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
