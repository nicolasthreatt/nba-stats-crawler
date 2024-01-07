import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    parser.add_argument('--player', dest='player', type=str, nargs=2, metavar='', required=False,
                        help='Single Specified Player')
    
    parser.add_argument('--players', dest='players', required=False, action='store_true',
                        help='All Players listed in nba.com/players')
    
    parser.add_argument('--teams', dest='teams', required=False, action='store_true',
                        help='All 30 Teams')
    
    parser.add_argument('--rosters', dest='rosters', required=False, action='store_true',
                        help='Collect Each Team\'s Rosters')

    parser.add_argument('--storage', dest='storage', type=str, required=False, default=str(),
                        choices=['insert', 'update', ''],
                        help='Stores New Data into Table in Azure Database')

    return parser.parse_args()
