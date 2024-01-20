from players.crawler import collect_single_player, collect_all_players
from teams.crawler import collect_all_teams
from utils.cli import parse_arguments

def main():
    args = parse_arguments()

    if args.player: # Collect single player
        collect_single_player(args.player, args.storage)
    elif args.players: # Collect all players from nba.com/players
        collect_all_players(args.storage)
    elif args.teams:  # Collect all 30 teams
        print('Scraping stats....')
        collect_all_teams(args.storage)
    else:
        exit('No player(s) or team specified')

    print('Completed.')


if __name__ == '__main__':
    main()