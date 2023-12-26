from tables.roster import RosterPlayer, RosterTeam


# Collect Player Info in Roster    
def parser(team: RosterTeam, players):
    num_players = 0

    for player in players:
        for key, value in player.items():

            # Add player
            team.roster.append(RosterPlayer())

            if key == "PLAYER":
                team.roster[num_players].name = str(value.strip())

            elif key == "#":
                team.roster[num_players].number = int(value) if value else int(-1)

            elif key == "POS":
                team.roster[num_players].position = str(value)

            elif key == "HEIGHT":
                team.roster[num_players].height = str(value)

            elif key == "WEIGHT":
                team.roster[num_players].weight = int(value.strip(' lbs'))

            elif key == "BIRTHDATE":
                team.roster[num_players].birthdate = str(value)

            elif key == "AGE":
                team.roster[num_players].age = int(value)

            elif key == "EXP":
                team.roster[num_players].experience = value

            elif key == "SCHOOL":
                team.roster[num_players].school = str(value)

            else:
                sys.exit("Error. Invalid key")

        num_players += 1
