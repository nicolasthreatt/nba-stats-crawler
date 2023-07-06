-- Create a new table called '[Usage]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Usage]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Usage]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Usage]
(
    [UsageID]          INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]           NVARCHAR(50)    NOT NULL,    -- Player Name
    [UsagePct]         DECIMAL(6,1)    NOT NULL,    -- Clutch Usage Percentage
    [PctOfTeamFgM]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Field Goals Made
    [PctOfTeamFgA]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Field Goals Attempted
    [PctOfTeamFg3M]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's 3 Point Field Goals Made
    [PctOfTeamFg3A]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's 3 Point Field Goals Attempted
    [PctOfTeamFtM]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Free Throws Made
    [PctOfTeamFtA]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Free Throws Attempted
    [PctOfTeamOReb]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Offensive Rebounds
    [PctOfTeamDReb]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Defensive Rebounds
    [PctOfTeamTReb]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Total Rebounds
    [PctOfTeamAst]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Assists
    [PctOfTeamTov]     DECIMAL(6,1)    NOT NULL,    -- Clutch Percent of Team's Turnovers
    [PctOfTeamStl]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Steals
    [PctOfTeamBlk]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Blocks
    [PctOfTeamBlkA]    DECIMAL(6,1)    NOT NULL,    -- Clutch Percent of Team's Block Attempted
    [PctOfTeamPF_C]    DECIMAL(6,1)    NOT NULL,    -- Clutch Percent of Team's Personal Fouls Committed
    [PctOfTeamPF_D]    DECIMAL(6,1)    NOT NULL,    -- Clutch Percent of Team's Personal Fouls Drawn
    [PctOfTeamPts]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Team's Pts
);
GO