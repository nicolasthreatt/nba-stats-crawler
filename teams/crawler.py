import threading
from db.teams import insert_teams_stats
from teams.initializers import initialize
from box_outs.scraper import teams as box_outs_scraper
from box_scores.scraper import teams as box_scores_scraper
from clutch.scraper import teams as clutch_scraper
from defense.scraper import teams as defense_scraper
from general.scraper import teams as general_scraper
from hustle.scraper import teams as hustle_scraper
from opponent_shooting.scraper import teams as opponent_shooting_scraper
from play_types.scraper import teams as play_types_scraper
from shooting.scraper import teams as shooting_scraper
from shot_dashboard.scraper import teams as shot_dashboard_scraper
from tracking.scraper import teams as tracking_scraper


def collect_all_teams(storage: bool=False):
    # Initalize All 30 Teams
    teams = initialize()

    # Scrape Stats
    scrape_stats(teams)

    # Dump Data into Azure Database
    if storage == "insert":
        insert_teams_stats(teams)


def scrape_stats(teams):
    threads = [
        threading.Thread(target=box_outs_scraper,          args=(teams,)),
        threading.Thread(target=box_scores_scraper,        args=(teams,)),
        threading.Thread(target=clutch_scraper,            args=(teams,)),
        threading.Thread(target=defense_scraper,           args=(teams,)),
        threading.Thread(target=general_scraper,           args=(teams,)),
        threading.Thread(target=hustle_scraper,            args=(teams,)),
        threading.Thread(target=opponent_shooting_scraper, args=(teams,)),
        threading.Thread(target=play_types_scraper,        args=(teams,)),
        threading.Thread(target=shooting_scraper,          args=(teams,)),
        threading.Thread(target=shot_dashboard_scraper,    args=(teams,)),
        threading.Thread(target=tracking_scraper,          args=(teams,)),   
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
