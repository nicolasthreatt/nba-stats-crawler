import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    parser.add_argument('--name', dest='name', type=str, nargs=2, metavar='', required=False, default=[str(), str()],
                         help='Player Name')
    
    parser.add_argument('--all', dest='all', required=False, action='store_true',
                         help='Every Player in Database')
    
    parser.add_argument('--rosters', dest='rosters', required=False, action='store_true',
                        help='Collect Each Team\'s Rosters')

    # MOVE TO ENUM CLASS
    # class StorageType(IntEnum):
    #     INSERT = 1
    #     UPDATE = 2

    # parser.add_argument('--storage', dest='storage', type=StorageType, required=False, default=StorageType.INSERT,
    #                      help='Insert New Data into Existing Table in Database')
    parser.add_argument('--insert', dest='insert', required=False, action='store_true',
                         help='Insert New Data into Existing Table in Database')

    parser.add_argument('--update', dest='update', required=False, action='store_true',
                        help='Update Existing Table in Database with new Data')

    return parser.parse_args()
