import argparse
from utils.player_stats import scrape_player
from utils.team_stats import scrape_teams

def main():
    parser = argparse.ArgumentParser(description='Collect various stats from stats.nba.com/')

    # Add command-line arguments here
    args = parser.parse_args()

    print('Scraping stats....\n')

    if args.player: # Collect single player
        collect_single_player(args.player, args.storage)
    elif args.players: # Collect all players (args.players)
        collect_all_players(args.storage)
    elif args.teams:
        scrape_teams(args)
    else:
        exit('No player(s) specified')

    print('Stats scraping complete\n')


if __name__ == '__main__':
    main()