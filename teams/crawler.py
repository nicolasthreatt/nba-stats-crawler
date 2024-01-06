import threading
from box_outs.scraper import teams as box_outs_scraper
from teams.initializers import initialize
# from db.teams import insert_teams_stats


def collect_all_teams(storage: bool=False):
    teams = initialize()
    scrape_stats(teams)
    
    # db.insert_teams_stats(player)


def scrape_stats(teams):
    threads = [
        threading.Thread(target=box_outs_scraper,          args=(teams,)),
        # threading.Thread(target=Boxscores.collectTeamStats, args=(teams,)),
        # threading.Thread(target=Clutch.collectTeamStats, args=(teams,)),
        # threading.Thread(target=DefenseDashboard.collectTeamStats, args=(teams,)),
        # threading.Thread(target=General.collectTeamStats, args=(teams,)),
        # threading.Thread(target=Hustle.collectTeamStats, args=(teams,)),
        # threading.Thread(target=OpponentShooting.collectTeamStats, args=(teams,)),
        # threading.Thread(target=Playtypes.collectTeamStats, args=(teams,)),
        # threading.Thread(target=Shooting.collectTeamStats, args=(teams,)),
        # threading.Thread(target=ShotDashboard.collectTeamStats, args=(teams,)),
        # threading.Thread(target=Tracking.collectTeamStats, args=(teams,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # dbStorage(teams)


# TODO: MOVE TO DIFFERENT FILE
# def dbStorage(teams):
#     args = getArgs()

#     if args.insert: or args.update:
#         cnxn = db.connect()
#         print('Database connected...')

#         if args.insert:
#             db.insert_team_info_data(cnxn, teams)
#             db.insert_rosters(cnxn, teams)
#             db.insert_box_outs(cnxn, teams)
#             db.insert_boxscores(cnxn, teams)
#             db.insert_clutch(cnxn, teams)
#             db.insert_defensive_dashboard(cnxn, teams)
#             db.insert_general(cnxn, teams)
#             db.insert_hustle(cnxn, teams)
#             db.insert_play_types(cnxn, teams)
#             db.insert_shot_dashboard(cnxn, teams)
#             db.insert_opp_shooting(cnxn, teams)
#             db.insert_shooting(cnxn, teams)
#             db.insert_tracking(cnxn, teams)
#         else: # args.update:
#             #TODO: Update existing data in database
#             pass
