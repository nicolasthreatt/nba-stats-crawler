from tables.player import Player


# Initialize Player with Biographical Information
def parse(table: dict, player_obj: Player):
    name         = table['PLAYER']
    player_obj.name = str(name)

    team         = table['TEAM']
    player_obj.team = str(team)

    age          = table['AGE']
    player_obj.age = int(age)

    height       = table['HEIGHT']
    player_obj.height = str(height)

    weight       = table['WEIGHT']
    player_obj.weight = int(weight)

    college      = table['COLLEGE']
    player_obj.college = str(college)

    country      = table['COUNTRY']
    player_obj.country = str(country)

    draft_year   = table['DRAFT YEAR']
    player_obj.draft_year = str(draft_year)

    draft_rd     = table['DRAFT ROUND']
    player_obj.draft_rd = str(draft_rd)

    draft_num    = table['DRAFT NUMBER']
    player_obj.draft_num = str(draft_num)

    games_played = table['GP']
    player_obj.games_played = int(games_played)

    pts          = table['PTS']
    player_obj.pts = float(pts)

    reb          = table['REB']
    player_obj.reb = float(reb)

    ast          = table['AST']
    player_obj.ast = float(ast)

    netrtg       = table['NETRTG']
    player_obj.netrtg = float(netrtg)

    oreb_pct     = table['OREB%'].strip('%')
    player_obj.oreb_pct = float(oreb_pct)

    dreb_pct     = table['DREB%'].strip('%')
    player_obj.dreb_pct = float(dreb_pct)

    usage_pct    = table['USG%'].strip('%')
    player_obj.usage_pct = float(usage_pct)

    ts_pct       = table['TS%'].strip('%')
    player_obj.ts_pct = float(ts_pct)

    ast_pct      = table['AST%'].strip('%')
    player_obj.ast_pct = float(ast_pct)

    return players
