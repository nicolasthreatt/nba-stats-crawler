from players.crawler import collect_single_player, collect_all_players
from utils.cli import parse_arguments

def main():
    # Add command-line arguments here
    args = parse_arguments()

    print('Scraping stats....\n')

    if args.player: # Collect single player
        collect_single_player(args.player, args.storage)
    elif args.players: # Collect all players (args.players)
        collect_all_players(args.storage)
    # elif args.teams:
    #     scrape_teams(args)
    else:
        exit('No player(s) specified')

    print('Stats scraping complete\n')


if __name__ == '__main__':
    main()