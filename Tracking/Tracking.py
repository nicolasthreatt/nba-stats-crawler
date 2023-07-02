'''
TRACKING
'''

import itertools

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import browserutils
from utils.headers import getStatColumnType
from utils.Types import TableType

tracking_tables = {
    'Drives':               'drives/',
    'Defensive Impact':     'defensive-impact/',
    'Catch-Shoot':          'catch-shoot/',
    'Passing':              'passing/',
    'Touches':              'touches/',
    'Pull-Up':              'pullup/',
    'Rebounding':           'rebounding/',
    'Offensive Rebounding': 'offensive-rebounding/',
    'Defensive Rebounding': 'defensive-rebounding/',
    'Shooting Efficiency':  'shooting-efficiency/',
    'Speed-Distance':       'speed-distance/',
    'Elbow Touch':          'elbow-touch/',
    'Post Ups':             'tracking-post-ups/',
    'Paint Touches':        'paint-touch/',
}

class Tracking(dict):
    def __init__(self, table_type):
        initTrackingTypes(self, table_type)

    def __getattr__(self, key):
        return self[key]


class Drives:
    def __init__(self):
        self.drives           = float() # Drives
        self.drive_fg_m       = float() # Field Goals Made
        self.drive_fg_a       = float() # Field Goals Attempted
        self.drive_fg_pct     = float() # Field Goal Percentage
        self.drive_ft_m       = float() # Free Throws Made
        self.drive_ft_a       = float() # Free Throws Attempted
        self.drive_ft_pct     = float() # Free Throw Percentage
        self.drive_pts        = float() # Points
        self.drive_pct_pts    = float() # Points Percentage
        self.drive_passes     = float() # Pass
        self.drive_pct_passes = float() # Pass Percentage
        self.drive_ast        = float() # Assists
        self.drive_pct_ast    = float() # Percent of Team's Assists
        self.drive_tov        = float() # Turnovers
        self.drive_pct_tov    = float() # Percent of Team's Turnovers
        self.drive_pf         = float() # Personal Fouls
        self.drive_pct_pf     = float() # Percent of Team's Personal Fouls


class DefensiveImpact:
    def __init__(self):
        self.stl             = float() # Steals
        self.blk             = float() # Blocks
        self.dreb            = float() # Defensive Rebounds
        self.defended_fg_m   = float() # Field Goals Defended at Rim Made
        self.defended_fg_a   = float() # Field Goals Defended at Rim Attempted
        self.defended_fg_pct = float() # Field Goals Defended at Rim Percent


class CatchShoot:
    def __init__(self):
        self.catch_shoot_pts     = float() # Points
        self.catch_shoot_fg_m    = float() # Field Goals Made
        self.catch_shoot_fg_a    = float() # Field Goals Attempted
        self.catch_shoot_fg_pct  = float() # Field Goals Percentage
        self.catch_shoot_fg3_m   = float() # 3 Point Field Goals Made
        self.catch_shoot_fg3_a   = float() # 3 Point Field Goals Attempted
        self.catch_shoot_fg3_pct = float() # 3 Point Field Goals Percentage
        self.catch_shoot_efg_pct = float() # Effective Field Goal Percentage


class Passing:
    def __init__(self):
        self.passes_made              = float() # Passes Made
        self.passes_received          = float() # Passes Received
        self.ast                      = float() # Assists
        self.secondary_ast            = float() # Secondary Assist
        self.potential_ast            = float() # Potential Assist
        self.ast_pts_created          = float() # Assist Points Created
        self.ast_adjusted             = float() # Assist Adjusted
        self.ast_to_pass_pct          = float() # Assist-to-Pass Percentage
        self.ast_to_pass_pct_adjusted = float() # Assist-to-Pass Percentage Adjusted


class Touches:
    def __init__(self):
        self.pts                   = float() # Points
        self.touches               = float() # Touches
        self.front_cout_touches    = float() # Front Court Touches
        self.time_of_poss          = float() # Time of Possession
        self.avg_sec_per_touch     = float() # Average Seconds Per Touch
        self.avg_dribble_per_touch = float() # Average Dribble Per Touch
        self.pts_per_touch         = float() # Points Per Touch
        self.elbow_touches         = float() # Elbow Touches
        self.post_touches          = float() # Post Touches
        self.paint_touches         = float() # Paint Touches
        self.pts_per_elbow_touch   = float() # Points Per Elbow Touch
        self.pts_per_post_touch    = float() # Points Per Post Touch
        self.pts_per_paint_touch   = float() # Points Per Paint Touch


class PullUpShooting:
    def __init__(self):
        self.pull_up_shooting_pts     = float() # Points
        self.pull_up_shooting_fg_m    = float() # Field Goals Made
        self.pull_up_shooting_fg_a    = float() # Field Goals Attempted
        self.pull_up_shooting_fg_pct  = float() # Field Goals Percentage
        self.pull_up_shooting_fg3_m   = float() # 3 Point Field Goals Made
        self.pull_up_shooting_fg3_a   = float() # 3 Point Field Goals Attempted
        self.pull_up_shooting_fg3_pct = float() # 3 Point Field Goals Percentage
        self.pull_up_shooting_efg_pct = float() # Effective Field Goal Percentage


class Rebounding:
    def __init__(self, table_type):
        self.rebs                 = float() # Rebounds
        self.contested_rebs       = float() # Contested Rebounds
        self.contested_rebs_pct   = float() # Contested Rebound Percentage
        self.reb_chances          = float() # Rebound Chance
        self.reb_chances_pct      = float() # Rebound Chance Percentage
        self.deferred_reb_chances = float() # Deferred Rebound Chances
        self.adj_reb_chance_pct   = float() # Adjusted Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_reb_dist     = float() # Average Rebound Distance


class OffensiveRebounding:
    def __init__(self, table_type):
        self.orebs                 = float() # Offensive Rebounds
        self.contested_orebs       = float() # Contested Offensive Rebounds
        self.contested_orebs_pct   = float() # Contested Offensive Rebound Percentage
        self.oreb_chances          = float() # Offensive Rebound Chance
        self.oreb_chances_pct      = float() # Offensive Rebound Chance Percentage
        self.deferred_oreb_chances = float() # Deferred Offensive Rebound Chances
        self.adj_oreb_chance_pct   = float() # Adjusted Offensive Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_oreb_dist     = float() # Average Offensive Rebound Distance


class DefensiveRebounding:
    def __init__(self, table_type):
        self.drebs                 = float() # Defensive Rebounds
        self.contested_drebs       = float() # Contested Defensive Rebounds
        self.contested_drebs_pct   = float() # Contested Defensive Rebound Percentage
        self.dreb_chances          = float() # Defensive Rebound Chance
        self.dreb_chances_pct      = float() # Defensive Rebound Chance Percentage
        self.deferred_dreb_chances = float() # Deferred Defensive Rebound Chances
        self.adj_dreb_chance_pct   = float() # Adjusted Defensive Rebound Chance Percentage

        if table_type == TableType.PLAYER.name:
            self.avg_dreb_dist     = float() # Average Defensive Rebound Distance


class ShootingEfficiency:
    def __init__(self):
        self.pts                     = float() # Points
        self.drive_pts               = float() # Drive Points
        self.drive_fg_pct            = float() # Drive Field Goal Percentage
        self.catch_shoot_pts         = float() # Catch and Shoot Points
        self.catch_shoot_fg_pct      = float() # Catch and Shoot Field Goals Percentage
        self.pull_up_shooting_pts    = float() # Pull-Up Points
        self.pull_up_shooting_fg_pct = float() # Pull Up Field Goals Percentage
        self.paint_touch_pts         = float() # Paint Touch Points
        self.paint_touch_fg_pct      = float() # Paint Toich Field Goal Percentage
        self.post_touch_pts          = float() # Post Touch Points
        self.post_touch_fg_pct       = float() # Post Touch Field Goal Percentage
        self.elbow_touch_pts         = float() # Elbow Touch Points
        self.elbow_touch_fg_pct      = float() # Elbow Touch Field Goal Percentage
        self.efg_pct                 = float() # Effective Field Goal Percentage


class SpeedDistance:
    def __init__(self):
        self.dist_feet      = float() # Distance Feet
        self.dist_miles     = float() # Distance Miles
        self.dist_miles_off = float() # Distance Miles Offense
        self.dist_miles_def = float() # Distance Miles Defense
        self.avg_speed      = float() # Average Speed
        self.avg_speed_off  = float() # Average Speed Offense
        self.avg_speed_def  = float() # Average Speed Defense


class ElbowTouches:
    def __init__(self):
        self.touches                = float() # Touches
        self.elbow_touches          = float() # Elbow Touches
        self.elbow_touch_fg_m       = float() # Elbow Field Goals Made
        self.elbow_touch_fg_a       = float() # Elbow Field Goals Attempted
        self.elbow_touch_fg_pct     = float() # Elbow Field Goal Percentage
        self.elbow_touch_ft_m       = float() # Elbow Free Throws Made
        self.elbow_touch_ft_a       = float() # Elbow Free Throws Attempted
        self.elbow_touch_ft_pct     = float() # Elbow Free Throw Percentage
        self.elbow_touch_pts        = float() # Elbow Points
        self.elbow_touch_pct_pts    = float() # Elbow Points Percentage
        self.elbow_touch_passes     = float() # Elbow Pass
        self.elbow_touch_pct_passes = float() # Elbow Pass Percentage
        self.elbow_touch_ast        = float() # Elbow Assists
        self.elbow_touch_pct_ast    = float() # Elbow Assists Percentage
        self.elbow_touch_tov        = float() # Elbow Turnovers
        self.elbow_touch_pct_tov    = float() # Elbow Turnovers Percentage
        self.elbow_touch_pf         = float() # Elbow Personal Foul
        self.elbow_touch_pct_pf     = float() # Elbow Personal Foul Percentage


class PostUpTouches:
    def __init__(self):
        self.touches                  = float() # Touches
        self.post_up_touches          = float() # Post Up Touches
        self.post_up_touch_fg_m       = float() # Field Goals Made
        self.post_up_touch_fg_a       = float() # Field Goals Attempted
        self.post_up_touch_fg_pct     = float() # Field Goal Percentage
        self.post_up_touch_ft_m       = float() # Free Throws Made
        self.post_up_touch_ft_a       = float() # Free Throws Attempted
        self.post_up_touch_ft_pct     = float() # Free Throw Percentage
        self.post_up_touch_pts        = float() # Points
        self.post_up_touch_pct_pts    = float() # Points Percentage
        self.post_up_touch_passes     = float() # Pass
        self.post_up_touch_pct_passes = float() # Pass Percentage
        self.post_up_touch_ast        = float() # Assists
        self.post_up_touch_pct_ast    = float() # Assists Percentage
        self.post_up_touch_tov        = float() # Turnovers
        self.post_up_touch_pct_tov    = float() # Turnovers Percentage
        self.post_up_touch_pf         = float() # Personal Fouls
        self.post_up_touch_pct_pf     = float() # Personal Fouls Percentage


class PaintTouches:
    def __init__(self):
        self.touches                = float() # Touches
        self.paint_touches          = float() # Paint Touches
        self.paint_touch_fg_m       = float() # Paint Field Goals Made
        self.paint_touch_fg_a       = float() # Paint Field Goals Attempted
        self.paint_touch_fg_pct     = float() # Paint Field Goal Percentage
        self.paint_touch_ft_m       = float() # Paint Free Throws Made
        self.paint_touch_ft_a       = float() # Paint Free Throws Attempted
        self.paint_touch_ft_pct     = float() # Paint Free Throw Percentage
        self.paint_touch_pts        = float() # Paint Points
        self.paint_touch_pct_pts    = float() # Paint Points Percentage
        self.paint_touch_passes     = float() # Paint Pass
        self.paint_touch_pct_passes = float() # Paint Pass Percentage
        self.paint_touch_ast        = float() # Paint Assists
        self.paint_touch_pct_ast    = float() # Paint Assists Percentage
        self.paint_touch_tov        = float() # Paint Turnovers
        self.paint_touch_pct_tov    = float() # Paint Turnovers Percentage
        self.paint_touch_pf         = float() # Paint Personal Fouls
        self.paint_touch_pct_pf     = float() # Paint Personal Fouls Percentage


# Get Tracking Stats
def initTrackingTypes(StatClass, table_type):
    for table in tracking_tables:

        if table == 'Drives':
            StatClass[table] = Drives()

        elif table == 'Defensive Impact':
            StatClass[table] = DefensiveImpact()

        elif table == 'Catch-Shoot':
            StatClass[table] = CatchShoot()

        elif table == 'Passing':
            StatClass[table] = Passing()

        elif table == 'Touches':
            StatClass[table] = Touches()

        elif table == 'Pull-Up':
            StatClass[table] = PullUpShooting()

        elif table == 'Rebounding':
            StatClass[table] = Rebounding(table_type)

        elif table == 'Offensive Rebounding':
            StatClass[table] = OffensiveRebounding(table_type)

        elif table == 'Defensive Rebounding':
            StatClass[table] = DefensiveRebounding(table_type)

        elif table == 'Shooting Efficiency':
            StatClass[table] = ShootingEfficiency()

        elif table == 'Speed-Distance':
            StatClass[table] = SpeedDistance()

        elif table == 'Elbow Touch':
            StatClass[table] = ElbowTouches()

        elif table == 'Post Ups':
            StatClass[table] = PostUpTouches()

        elif table == 'Paint Touches':
            StatClass[table] = PaintTouches()


# Store Stats to Player
def scrape_player(player, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each player's tracking stats from:
        - https://www.nba.com/stats/players/drives/
        - https://www.nba.com/stats/players/defensive-impact/
        - https://www.nba.com/stats/players/catch-shoot/
        - https://www.nba.com/stats/players/passing/
        - https://www.nba.com/stats/players/touches/
        - https://www.nba.com/stats/players/pullup/
        - https://www.nba.com/stats/players/rebounding/
        - https://www.nba.com/stats/players/offensive-rebounding/
        - https://www.nba.com/stats/players/defensive-rebounding/
        - https://www.nba.com/stats/players/shooting-efficiency/
        - https://www.nba.com/stats/players/speed-distance/
        - https://www.nba.com/stats/players/elbow-touch/
        - https://www.nba.com/stats/players/tracking-post-ups/
        - https://www.nba.com/stats/players/paint-touch/
    '''

    # Add stat class to player
    player.addTable('tracking', Tracking(TableType.PLAYER.name))

    # URL Configurations
    name       = player.name.split(' ')[0] + '%20' + player.name.split(' ')[1]
    table_type = 'players/'
    stat       = 'PLAYER_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Get stats from correct url path
    for stat_key, stat_url in tracking_tables.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '#!?CF=PLAYER_NAME*E*' + name + '&sort=' + stat + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            getTrackingStats(table, stat_key, player=player)

    # Close browser
    browser.quit()


# Store Stats to Teams
def scrape_teams(teams, season_year = '2020-21', season_type = 'Regular%20Season'):
    '''
    Produces each team's tracking stats from:
        - https://nba.com/stats/teams/drives/
        - https://nba.com/stats/teams/defensive-impact/
        - https://nba.com/stats/teams/catch-shoot/
        - https://nba.com/stats/teams/passing/
        - https://nba.com/stats/teams/touches/
        - https://nba.com/stats/teams/pullup/
        - https://nba.com/stats/teams/rebounding/
        - https://nba.com/stats/teams/offensive-rebounding/
        - https://nba.com/stats/teams/defensive-rebounding/
        - https://nba.com/stats/teams/shooting-efficiency/
        - https://nba.com/stats/teams/speed-distance/
        - https://nba.com/stats/teams/elbow-touch/
        - https://nba.com/stats/teams/tracking-post-ups/
        - https://nba.com/stats/teams/paint-touch/
    '''

    # Add stat class to teams
    for team in teams:
        teams[team].addTable('tracking', Tracking(TableType.TEAM.name))

    # URL Configurations
    table_type = 'teams/'
    stat       = 'TEAM_NAME'

    # Start browser
    browser = webdriver.Chrome(ChromeDriverManager().install())

    for stat_key, stat_url in tracking_tables.items():

        # Browse to correct stat category
        url = 'https://nba.com/stats/' + table_type + stat_url + '?sort=' + stat + '&dir=-1' + '&Season=' + season_year + '&SeasonType=' + season_type
        browser.get(url)

        # Scrape stats if table exist
        table = browserutils.loadStatTable(browser)
        if table is not None:
            getTrackingStats(table, stat_key, teams=teams)

    # Close browser
    browser.quit()


# Collect Tracking Stats
def getTrackingStats(table, stat_key, player=None, teams=None):

    table_type = TableType.PLAYER.name if player is not None else TableType.TEAM.name
    (table_header_row, table_column_offset) = getStatColumnType('Tracking ' + stat_key, table_type)

    # Parse statistic table
    index = 1
    for row, info in enumerate(table.split('\n')):

        # Throwaway junk lines (column names)
        if row > table_header_row:

            # Get Correct Player/Team
            if (index % 2) == 1:

                if player is not None:
                    name = info.title()
                    player.name = name
                    StatClass = player

                elif teams is not None:
                    team = info.upper()
                    StatClass = teams[team]

            # Extract stats
            elif (index % 2) == 0:

                # Create iterator
                itr = itertools.count(table_column_offset)

                # Parse and store stats
                data = info.split(' ')
                data = [stat.replace("-", "0") for stat in data]

                if stat_key == 'Drives':
                    drives           = data[next(itr)]
                    StatClass.tracking[stat_key].drives = float(drives)

                    drive_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_m = float(drive_fg_m)

                    drive_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_a = float(drive_fg_a)

                    drive_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_pct = float(drive_fg_pct)

                    drive_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_m = float(drive_ft_m)

                    drive_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_a = float(drive_ft_a)

                    drive_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ft_pct = float(drive_ft_pct)

                    drive_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pts = float(drive_pts)

                    drive_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_pts = float(drive_pct_pts)

                    drive_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_passes = float(drive_passes)

                    drive_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_passes = float(drive_pct_passes)

                    drive_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_ast = float(drive_ast)

                    drive_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_ast = float(drive_pct_ast)

                    drive_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].drive_tov = float(drive_tov)

                    drive_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_tov = float(drive_pct_tov)

                    drive_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pf = float(drive_pf)

                    drive_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pct_pf = float(drive_pct_pf)

                elif stat_key == 'Defensive Impact':
                    stl             = data[next(itr)]
                    StatClass.tracking[stat_key].stl = float(stl)

                    blk             = data[next(itr)]
                    StatClass.tracking[stat_key].blk = float(blk)

                    dreb            = data[next(itr)]
                    StatClass.tracking[stat_key].dreb = float(dreb)

                    defended_fg_m   = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_m = float(defended_fg_m)

                    defended_fg_a   = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_a = float(defended_fg_a)

                    defended_fg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].defended_fg_pct = float(defended_fg_pct)

                elif stat_key == 'Catch-Shoot':
                    catch_shoot_pts   = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_pts = float(catch_shoot_pts)

                    catch_shoot_fg_m  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_m = float(catch_shoot_fg_m)

                    catch_shoot_fg_a  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_a = float(catch_shoot_fg_a)

                    catch_shoot_fg_pct  = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_pct = float(catch_shoot_fg_pct)

                    catch_shoot_fg3_m = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_m = float(catch_shoot_fg3_m)

                    catch_shoot_fg3_a = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_a = float(catch_shoot_fg3_a)

                    catch_shoot_fg3_pct = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg3_pct = float(catch_shoot_fg3_pct)

                    catch_shoot_efg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_efg_pct = float(catch_shoot_efg_pct)

                elif stat_key == 'Passing':
                    passes_made              = data[next(itr)]
                    StatClass.tracking[stat_key].passes_made = float(passes_made)

                    passes_received          = data[next(itr)]
                    StatClass.tracking[stat_key].passes_received = float(passes_received)

                    ast                      = data[next(itr)]
                    StatClass.tracking[stat_key].ast = float(ast)

                    secondary_ast            = data[next(itr)]
                    StatClass.tracking[stat_key].secondary_ast = float(secondary_ast)

                    potential_ast            = data[next(itr)]
                    StatClass.tracking[stat_key].potential_ast = float(potential_ast)

                    ast_pts_created          = data[next(itr)]
                    StatClass.tracking[stat_key].ast_pts_created = float(ast_pts_created)

                    ast_adjusted             = data[next(itr)]
                    StatClass.tracking[stat_key].ast_adjusted = float(ast_adjusted)

                    ast_to_pass_pct          = data[next(itr)]
                    StatClass.tracking[stat_key].ast_to_pass_pct = float(ast_to_pass_pct)

                    ast_to_pass_pct_adjusted = data[next(itr)]
                    StatClass.tracking[stat_key].ast_to_pass_pct_adjusted = float(ast_to_pass_pct_adjusted)

                elif stat_key == 'Touches':
                    pts                   = data[next(itr)]
                    StatClass.tracking[stat_key].pts = float(pts)

                    touches               = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    front_cout_touches    = data[next(itr)]
                    StatClass.tracking[stat_key].front_cout_touches = float(front_cout_touches)

                    time_of_poss          = data[next(itr)]
                    StatClass.tracking[stat_key].time_of_poss = float(time_of_poss)

                    avg_sec_per_touch     = data[next(itr)]
                    StatClass.tracking[stat_key].avg_sec_per_touch = float(avg_sec_per_touch)

                    avg_dribble_per_touch = data[next(itr)]
                    StatClass.tracking[stat_key].avg_dribble_per_touch = float(avg_dribble_per_touch)

                    pts_per_touch         = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_touch = float(pts_per_touch)

                    elbow_touches         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touches = float(elbow_touches)

                    post_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].post_touches = float(post_touches)

                    paint_touches         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touches = float(paint_touches)

                    pts_per_elbow_touch   = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_elbow_touch = float(pts_per_elbow_touch)

                    pts_per_post_touch    = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_post_touch = float(pts_per_post_touch)

                    pts_per_paint_touch   = data[next(itr)]
                    StatClass.tracking[stat_key].pts_per_paint_touch = float(pts_per_paint_touch)

                elif stat_key == 'Pull-Up':
                    pull_up_shooting_pts     = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_pts = float(pull_up_shooting_pts)

                    pull_up_shooting_fg_m    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_m = float(pull_up_shooting_fg_m)

                    pull_up_shooting_fg_a    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_a = float(pull_up_shooting_fg_a)

                    pull_up_shooting_fg_pct  = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_pct = float(pull_up_shooting_fg_pct)

                    pull_up_shooting_fg3_m   = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_m = float(pull_up_shooting_fg3_m)

                    pull_up_shooting_fg3_a   = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_a = float(pull_up_shooting_fg3_a)

                    pull_up_shooting_fg3_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg3_pct = float(pull_up_shooting_fg3_pct)

                    pull_up_shooting_efg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_efg_pct = float(pull_up_shooting_efg_pct)

                elif stat_key == 'Rebounding':
                    rebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].rebs = float(rebs)

                    contested_rebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_rebs = float(contested_rebs)

                    contested_rebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_rebs_pct = float(contested_rebs_pct)

                    reb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].reb_chances = float(reb_chances)

                    reb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].reb_chances_pct = float(reb_chances_pct)

                    deferred_reb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_reb_chances = float(deferred_reb_chances)

                    adj_reb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_reb_chance_pct = float(adj_reb_chance_pct)

                    if player is not None:
                        avg_reb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_reb_dist = float(avg_reb_dist)

                elif stat_key == 'Offensive Rebounding':
                    orebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].orebs = float(orebs)

                    contested_orebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_orebs = float(contested_orebs)

                    contested_orebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_orebs_pct = float(contested_orebs_pct)

                    oreb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].oreb_chances = float(oreb_chances)

                    oreb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].oreb_chances_pct = float(oreb_chances_pct)

                    deferred_oreb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_oreb_chances = float(deferred_oreb_chances)

                    adj_oreb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_oreb_chance_pct = float(adj_oreb_chance_pct)

                    if player:
                        avg_oreb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_oreb_dist = float(avg_oreb_dist)

                elif stat_key == 'Defensive Rebounding':
                    drebs                 = data[next(itr)]
                    StatClass.tracking[stat_key].drebs = float(drebs)

                    contested_drebs       = data[next(itr)]
                    StatClass.tracking[stat_key].contested_drebs = float(contested_drebs)

                    contested_drebs_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].contested_drebs_pct = float(contested_drebs_pct)

                    dreb_chances          = data[next(itr)]
                    StatClass.tracking[stat_key].dreb_chances = float(dreb_chances)

                    dreb_chances_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].dreb_chances_pct = float(dreb_chances_pct)

                    deferred_dreb_chances = data[next(itr)]
                    StatClass.tracking[stat_key].deferred_dreb_chances = float(deferred_dreb_chances)

                    adj_dreb_chance_pct   = data[next(itr)]
                    StatClass.tracking[stat_key].adj_dreb_chance_pct = float(adj_dreb_chance_pct)

                    if player is not None:
                        avg_dreb_dist     = data[next(itr)]
                        StatClass.tracking[stat_key].avg_dreb_dist = float(avg_dreb_dist)

                elif stat_key == 'Shooting Efficiency':
                    pts                     = data[next(itr)]
                    StatClass.tracking[stat_key].pts = float(pts)

                    drive_pts               = data[next(itr)]
                    StatClass.tracking[stat_key].drive_pts = float(drive_pts)

                    drive_fg_pct            = data[next(itr)]
                    StatClass.tracking[stat_key].drive_fg_pct = float(drive_fg_pct)

                    catch_shoot_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_pts = float(catch_shoot_pts)

                    catch_shoot_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].catch_shoot_fg_pct = float(catch_shoot_fg_pct)

                    pull_up_shooting_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_pts = float(pull_up_shooting_pts)

                    pull_up_shooting_fg_pct = data[next(itr)]
                    StatClass.tracking[stat_key].pull_up_shooting_fg_pct = float(pull_up_shooting_fg_pct)

                    paint_touch_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pts = float(paint_touch_pts)

                    paint_touch_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_pct = float(paint_touch_fg_pct)

                    post_touch_pts          = data[next(itr)]
                    StatClass.tracking[stat_key].post_touch_pts = float(post_touch_pts)

                    post_touch_fg_pct       = data[next(itr)]
                    StatClass.tracking[stat_key].post_touch_fg_pct = float(post_touch_fg_pct)

                    elbow_touch_pts         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pts = float(elbow_touch_pts)

                    elbow_touch_fg_pct      = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_pct = float(elbow_touch_fg_pct)

                    efg_pct                 = data[next(itr)]
                    StatClass.tracking[stat_key].efg_pct = float(efg_pct)

                elif stat_key == 'Speed-Distance':
                    dist_feet      = data[next(itr)]
                    StatClass.tracking[stat_key].dist_feet = float(dist_feet)

                    dist_miles     = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles = float(dist_miles)

                    dist_miles_off = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles_off = float(dist_miles_off)

                    dist_miles_def = data[next(itr)]
                    StatClass.tracking[stat_key].dist_miles_def = float(dist_miles_def)

                    avg_speed      = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed = float(avg_speed)

                    avg_speed_off  = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed_off = float(avg_speed_off)

                    avg_speed_def  = data[next(itr)]
                    StatClass.tracking[stat_key].avg_speed_def = float(avg_speed_def)

                elif stat_key == 'Elbow Touch':
                    touches                = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    elbow_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touches = float(elbow_touches)

                    elbow_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_m = float(elbow_touch_fg_m)

                    elbow_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_a = float(elbow_touch_fg_a)

                    elbow_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_fg_pct = float(elbow_touch_fg_pct)

                    elbow_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_m = float(elbow_touch_ft_m)

                    elbow_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_a = float(elbow_touch_ft_a)

                    elbow_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ft_pct = float(elbow_touch_ft_pct)

                    elbow_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pts = float(elbow_touch_pts)

                    elbow_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_pts = float(elbow_touch_pct_pts)

                    elbow_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_passes = float(elbow_touch_passes)

                    elbow_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_passes = float(elbow_touch_pct_passes)

                    elbow_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_ast = float(elbow_touch_ast)

                    elbow_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_ast = float(elbow_touch_pct_ast)

                    elbow_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_tov = float(elbow_touch_tov)

                    elbow_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_tov = float(elbow_touch_pct_tov)

                    elbow_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pf = float(elbow_touch_pf)

                    elbow_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].elbow_touch_pct_pf = float(elbow_touch_pct_pf)

                elif stat_key == 'Post Ups':
                    touches                 = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    post_up_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touches = float(post_up_touches)

                    post_up_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_m = float(post_up_touch_fg_m)

                    post_up_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_a = float(post_up_touch_fg_a)

                    post_up_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_fg_pct = float(post_up_touch_fg_pct)

                    post_up_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_m = float(post_up_touch_ft_m)

                    post_up_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_a = float(post_up_touch_ft_a)

                    post_up_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ft_pct = float(post_up_touch_ft_pct)

                    post_up_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pts = float(post_up_touch_pts)

                    post_up_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_pts = float(post_up_touch_pct_pts)

                    post_up_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_passes = float(post_up_touch_passes)

                    post_up_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_passes = float(post_up_touch_pct_passes)

                    post_up_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_ast = float(post_up_touch_ast)

                    post_up_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_ast = float(post_up_touch_pct_ast)

                    post_up_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_tov = float(post_up_touch_tov)

                    post_up_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_tov = float(post_up_touch_pct_tov)

                    post_up_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pf = float(post_up_touch_pf)

                    post_up_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].post_up_touch_pct_pf = float(post_up_touch_pct_pf)

                elif stat_key == 'Paint Touches':
                    touches                = data[next(itr)]
                    StatClass.tracking[stat_key].touches = float(touches)

                    paint_touches          = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touches = float(paint_touches)

                    paint_touch_fg_m       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_m = float(paint_touch_fg_m)

                    paint_touch_fg_a       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_a = float(paint_touch_fg_a)

                    paint_touch_fg_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_fg_pct = float(paint_touch_fg_pct)

                    paint_touch_ft_m       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_m = float(paint_touch_ft_m)

                    paint_touch_ft_a       = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_a = float(paint_touch_ft_a)

                    paint_touch_ft_pct     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ft_pct = float(paint_touch_ft_pct)

                    paint_touch_pts        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pts = float(paint_touch_pts)

                    paint_touch_pct_pts    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_pts = float(paint_touch_pct_pts)

                    paint_touch_passes     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_passes = float(paint_touch_passes)

                    paint_touch_pct_passes = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_passes = float(paint_touch_pct_passes)

                    paint_touch_ast        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_ast = float(paint_touch_ast)

                    paint_touch_pct_ast    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_ast = float(paint_touch_pct_ast)

                    paint_touch_tov        = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_tov = float(paint_touch_tov)

                    paint_touch_pct_tov    = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_tov = float(paint_touch_pct_tov)

                    paint_touch_pf         = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pf = float(paint_touch_pf)

                    paint_touch_pct_pf     = data[next(itr)]
                    StatClass.tracking[stat_key].paint_touch_pct_pf = float(paint_touch_pct_pf)

            index += 1
