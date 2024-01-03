'''
TODO (DELETE ONCE MAIN AND INTERFACES ARE FINISHED)
'''

import argparse
import threading

from db import players as db

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
    playersNames = Player.get_all_players()
    players      = Player.initialize_players(playersNames)

    for player in players:
        scrape_stats(player)
        dbCmd(player, insert, update)


def dbCmd(player, insert, update):
    if insert:
        dbStorage(player, insert=insert)
    elif update:
        dbStorage(player, update=update)

# TODO: MOVE TO db.py
def dbStorage(player, insert=None, update=None):

    if not insert and not update:
        return

    cnxn = db.connect()
    print('Database connected...')

    if insert:
        print('Inserting Stats...')
        db.insert_bio(cnxn, player)
        db.insert_box_outs(cnxn, player)
        db.insert_boxscores(cnxn, player)
        db.insert_clutch(cnxn, player)
        db.insert_defensive_dashboard(cnxn, player)
        db.insert_general(cnxn, player)
        db.insert_hustle(cnxn, player)
        db.insert_opp_shooting(cnxn, player)
        db.insert_play_types(cnxn, player)
        db.insert_shooting(cnxn, player)
        db.insert_shot_dashboard(cnxn, player)
        db.insert_tracking(cnxn, player)
    elif update:
        print('Updating Stats...')


def scrape_stats(player):

    threads = [
        threading.Thread(target=BoxOuts.scrape_player,          args=(player,)),
        # threading.Thread(target=Boxscores.scrape_player,        args=(player,)),
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
