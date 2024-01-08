import threading
from box_outs.scraper import player as box_outs_scraper
from box_scores.scraper import player as box_scores_scraper
from clutch.scraper import player as clutch_scraper
from defense.scraper import player as defense_scraper
from general.scraper import player as general_scraper
from hustle.scraper import player as hustle_scraper
from opponent_shooting.scraper import player as opponent_shooting_scraper
from players import initializers, fetcher
# from .db.players import insert_player_data


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
        # threading.Thread(target=box_scores_scraper,        args=(player,)), # TODO: FIX ERROR (parser)
        # threading.Thread(target=clutch_scraper,            args=(player,)),
        # threading.Thread(target=defense_scraper,           args=(player,)), # TODO: FIX ERROR (parser)
        # threading.Thread(target=general_scraper,           args=(player,)), # TODO: FIX ERROR (parser)
        # threading.Thread(target=hustle_scraper,            args=(player,)),
        threading.Thread(target=opponent_shooting_scraper, args=(player,)), # TODO:
        # threading.Thread(target=Playtypes.scrape_player,   args=(player,)), # TODO:
        threading.Thread(target=shooting_scraper,          args=(player,)), # TODO:
        # threading.Thread(target=ShotDashboard.scrape_player,    args=(player,)), # TODO:
        # threading.Thread(target=Tracking.scrape_player,         args=(player,)), # TODO:
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
