'''
INTERFACE TEAMS (RENAME LATER)

TODO:
    - Work on threading to improve efficiency and performance
    - Add single or multiple teams options
    - Add season
    - Add option to insert/update data into individual tables
'''
import argparse
import threading
from db import teams
from Team import Team
from BoxScores import Boxscores
from BoxOuts import BoxOuts
from clutch import Clutch
from DefenseDashboard import DefenseDashboard
from General import General
from Hustle import Hustle
from OpponentShooting import OpponentShooting
from Playtype import Playtypes
from Rosters import rosters
from Shooting import Shooting
from ShotDashboard import ShotDashboard
from Tracking import Tracking


def collectStats():

    teams = Team.initTeamsWithInfo()

    # Get Team's Roster
    rosters.collectTraditionalRosters(teams)

    threads = [
        threading.Thread(target=BoxOuts.collectTeamStats, args=(teams,)),
        threading.Thread(target=Boxscores.collectTeamStats, args=(teams,)),
        threading.Thread(target=Clutch.collectTeamStats, args=(teams,)),
        threading.Thread(target=DefenseDashboard.collectTeamStats, args=(teams,)),
        threading.Thread(target=General.collectTeamStats, args=(teams,)),
        threading.Thread(target=Hustle.collectTeamStats, args=(teams,)),
        threading.Thread(target=OpponentShooting.collectTeamStats, args=(teams,)),
        threading.Thread(target=Playtypes.collectTeamStats, args=(teams,)),
        threading.Thread(target=Shooting.collectTeamStats, args=(teams,)),
        threading.Thread(target=ShotDashboard.collectTeamStats, args=(teams,)),
        threading.Thread(target=Tracking.collectTeamStats, args=(teams,)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    dbStorage(teams)


def dbStorage(teams):
    args = getArgs()

    if args.insert: or args.update:
        cnxn = db.connect()
        print('Database connected...')

        if args.insert:
            db.insert_team_info_data(cnxn, teams)
            db.insert_rosters(cnxn, teams)
            db.insert_box_outs(cnxn, teams)
            db.insert_boxscores(cnxn, teams)
            db.insert_clutch(cnxn, teams)
            db.insert_defensive_dashboard(cnxn, teams)
            db.insert_general(cnxn, teams)
            db.insert_hustle(cnxn, teams)
            db.insert_play_types(cnxn, teams)
            db.insert_shot_dashboard(cnxn, teams)
            db.insert_opp_shooting(cnxn, teams)
            db.insert_shooting(cnxn, teams)
            db.insert_tracking(cnxn, teams)
        else: # args.update:
            #TODO: Update existing data in database
            pass


def getArgs():

    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    parser.add_argument('--rosters', dest='rosters', required=False, action='store_true',
                        help='Collect Each Team\'s Rosters')

    parser.add_argument('--insert', dest='insert', required=False, action='store_true',
                        help='Insert New Data into Existing Table in Database')

    parser.add_argument('--update', dest='update', required=False, action='store_true',
                        help='Update Existing Table in Database with new Data')

    return parser.parse_args()


if __name__ == '__main__':
    collectStats()
