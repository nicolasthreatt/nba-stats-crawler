import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    parser.add_argument('--player', dest='player', type=str, nargs=2, metavar='', required=False,
                        help='Single Specified Player')
    
    parser.add_argument('--all', dest='all', required=False, action='store_true',
                        help='Every Player listed in nba.com/players')
    
    parser.add_argument('--rosters', dest='rosters', required=False, action='store_true',
                        help='Collect Each Team\'s Rosters')

    # MOVE TO ENUM CLASS
    # class StorageType(IntEnum):
    #     INSERT = 1
    #     UPDATE = 2

    parser.add_argument('--storage', dest='storage', type=str, required=False, default=str(),
                        choices=['insert', 'update', ''],
                        help='Stores New Data into Table in Azure Database')

    return parser.parse_args()
