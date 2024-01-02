import itertools
from teams.tables.team import Team
from utils.mappings import mascots

CITIES = [city_mascot[0].title() for city_mascot in mascots]
MASCOTS = [city_mascot[1].title() if city_mascot[1] != "SIXERS" else "76ers" for city_mascot in mascots]

def parse(table: str, teams: dict):

    # rank = 1
    city = None
    mascot = None

    # Parse statistic table
    for row, info in enumerate(table.split('\n')):
        # print(info)
        # print()

        # Throwaway junk lines (column names)
        if row > 0:

            # Grab Team City
            if info.strip() in CITIES:
                city = info.strip()
                continue

            # Grab Team Mascot
            if not info.isnumeric() and any(mascot in info.strip() for mascot in MASCOTS):
                mascot = info.strip()
                continue

            # Grab Team Full Name
            if city and mascot and city + ' ' + mascot not in teams:
                team = city + ' ' + mascot
                teams[team] = Team()

            # Grab Team's Respective Stats
            data = info.split(' ')
            if(len(data) == 12):
    
                # Create iterator
                itr = itertools.count()

                overall_w = data[next(itr)]
                teams[team].overall['W'] = int(overall_w)

                overall_l = data[next(itr)]
                teams[team].overall['L'] = int(overall_l)

                win_pct = data[next(itr)]
                teams[team].win_pct = float(win_pct)

                games_back = data[next(itr)]
                if games_back == '--':
                    teams[team].games_back = float()
                else:
                    teams[team].games_back = float(games_back)

                conf = data[next(itr)].split('-')

                conf_w = conf[0]
                teams[team].conference['W'] = int(conf_w)

                conf_l = conf[1]
                teams[team].conference['L'] = int(conf_l)

                div = data[next(itr)].split('-')

                div_w = div[0]
                teams[team].division['W'] = int(div_w)

                div_l = div[0]
                teams[team].division['L'] = int(div_l)

                home = data[next(itr)].split('-')

                home_w = home[0]
                teams[team].division['W'] = int(home_w)

                home_l = home[1]    
                teams[team].division['L'] = int(home_l)

                road = data[next(itr)].split('-')

                road_w = road[0]
                teams[team].road['W'] = int(road_w)

                road_l = road[1]
                teams[team].road['L'] = int(road_l)

                ot = data[next(itr)].split('-')

                ot_w = ot[0]
                teams[team].ot['W'] = int(ot_w)

                ot_l = ot[1]
                teams[team].ot['L'] = int(ot_l)

                last10 = data[next(itr)].split('-')

                last10_w = last10[0]
                teams[team].last10['W'] = int(last10_w)

                last10_l = last10[1]
                teams[team].last10['L'] = int(last10_l)

                streak_result = data[next(itr)]
                streak_num = data[next(itr)]
                streak = streak_result + streak_num
                teams[team].streak = str(streak)
