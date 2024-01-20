from players.tables.player import Player


# Initialize Player with Biographical Information
# TODO: MOVE TO Player
def create_new_player(table: dict):
    player = Player()

    name         = table['PLAYER']
    player.name = str(name)

    team         = table['TEAM']
    player.team = str(team)

    age          = table['AGE']
    player.age = int(age)

    height       = table['HEIGHT']
    player.height = str(height)

    weight       = table['WEIGHT']
    player.weight = int(weight)

    college      = table['COLLEGE']
    player.college = str(college)

    country      = table['COUNTRY']
    player.country = str(country)

    draft_year   = table['DRAFT YEAR']
    player.draft_year = str(draft_year)

    draft_rd     = table['DRAFT ROUND']
    player.draft_rd = str(draft_rd)

    draft_num    = table['DRAFT NUMBER']
    player.draft_num = str(draft_num)

    return player
