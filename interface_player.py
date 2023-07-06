'''
INTERFACE (RENAME LATER)
'''

import argparse
import threading

from DatabaseStorage import playerDB

from Player import Player

from BoxScores import Boxscores
from BoxOuts import BoxOuts
from clutch import Clutch
from DefenseDashboard import DefenseDashboard
from General import General
from Hustle import Hustle
from OpponentShooting import OpponentShooting
from Playtype import Playtypes
from Shooting import Shooting
from ShotDashboard import ShotDashboard
from Tracking import Tracking

# MOVE TO ENUM CLASS
    # class StorageType(IntEnum):
    #     INSERT = 1
    #     UPDATE = 2
    # parser.add_argument('--storage', dest='storage', type=StorageType, required=False, default=StorageType.INSERT,
    #                      help='Insert New Data into Existing Table in Database')

def collectStats(args):

    print('Scraping stats....\n')

    if args.player: # Collect single player
        collect_single_player(args.player, args.storage)
    else: # Collect all players (args.players)
        collect_all_players(args.storage)

    print('Stats scraping complete\n')


def collect_single_player(name, insert, update):
    fname, lname = name

    player = Player.initialize_player(fname, lname)
    scrape_stats(player)

    dbCmd(player, insert, update)


def collect_all_players(insert, update):
    playersNames = Player.get_players()
    players      = Player.initialize_players(playersNames)

    for player in players:
        scrape_stats(player)
        dbCmd(player, insert, update)


def dbCmd(player, insert, update):
    if insert:
        dbStorage(player, insert=insert)
    elif update:
        dbStorage(player, update=update)

# TODO: MOVE TO playerDB.py
def dbStorage(player, insert=None, update=None):

    if not insert and not update:
        return

    cnxn = playerDB.connect()
    print('Database connected...')

    if insert:
        print('Inserting Stats...')
        playerDB.insert_bio(cnxn, player)
        playerDB.insert_box_outs(cnxn, player)
        playerDB.insert_boxscores(cnxn, player)
        playerDB.insert_clutch(cnxn, player)
        playerDB.insert_defensive_dashboard(cnxn, player)
        playerDB.insert_general(cnxn, player)
        playerDB.insert_hustle(cnxn, player)
        playerDB.insert_opp_shooting(cnxn, player)
        playerDB.insert_play_types(cnxn, player)
        playerDB.insert_shooting(cnxn, player)
        playerDB.insert_shot_dashboard(cnxn, player)
        playerDB.insert_tracking(cnxn, player)
    elif update:
        print('Updating Stats...')


def scrape_stats(player):

    threads = [
        threading.Thread(target=BoxOuts.scrape_player,          args=(player,)),
        threading.Thread(target=Boxscores.scrape_player,        args=(player,)),
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


def getArgs():

    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    parser.add_argument('--name', dest='name', type=str, nargs=2, metavar='', required=False, default=[str(), str()],
                         help='Player Name')
    
    parser.add_argument('--all', dest='all', required=False, action='store_true',
                         help='Every Player in Database')

    parser.add_argument('--insert', dest='insert', required=False, action='store_true',
                         help='Insert New Data into Existing Table in Database')

    parser.add_argument('--update', dest='update', required=False, action='store_true',
                        help='Update Existing Table in Database with new Data')

    return parser.parse_args()


if __name__ == '__main__':
    args = getArgs()

    collectStats(args.name[0], args.name[1], args.all, args.insert, args.update)
