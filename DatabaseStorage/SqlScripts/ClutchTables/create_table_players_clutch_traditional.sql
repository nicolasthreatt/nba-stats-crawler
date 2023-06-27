-- Create a new table called '[Traditional]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Traditional]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Traditional]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Traditional]
(
    [TraditionalID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]           NVARCHAR(50)    NOT NULL,    -- Player Name
    [Pts]              DECIMAL(4,1)    NOT NULL,    -- Clutch Pts
    [FgM]              DECIMAL(4,1)    NOT NULL,    -- Clutch Field Goals Made
    [FgA]              DECIMAL(4,1)    NOT NULL,    -- Clutch Field Goals Attempted
    [FgPct]            DECIMAL(4,1)    NOT NULL,    -- Clutch Field Goal Percentage
    [Fg3M]             DECIMAL(4,1)    NOT NULL,    -- Clutch 3 Point Field Goals Made
    [Fg3A]             DECIMAL(4,1)    NOT NULL,    -- Clutch 3 Point Field Goals Attempted
    [Fg3Pct]           DECIMAL(4,1)    NOT NULL,    -- Clutch 3 Point Field Goals Percentage
    [FtM]              DECIMAL(4,1)    NOT NULL,    -- Clutch Free Throws Made
    [FtA]              DECIMAL(4,1)    NOT NULL,    -- Clutch Free Throws Attempted
    [FtPct]            DECIMAL(4,1)    NOT NULL,    -- Clutch Free Throw Percentage
    [OReb]             DECIMAL(4,1)    NOT NULL,    -- Clutch Offensive Rebounds
    [DReb]             DECIMAL(4,1)    NOT NULL,    -- Clutch Defensive Rebounds
    [TReb]             DECIMAL(4,1)    NOT NULL,    -- Clutch Total Rebounds
    [Ast]              DECIMAL(4,1)    NOT NULL,    -- Clutch Assists
    [Tov]              DECIMAL(6,1)    NOT NULL,    -- Clutch Turnovers
    [Stl]              DECIMAL(4,1)    NOT NULL,    -- Clutch Steals
    [Blk]              DECIMAL(4,1)    NOT NULL,    -- Clutch Blocks
    [PF_C]             DECIMAL(6,1)    NOT NULL,    -- Clutch Personal Fouls Committed
    [FantasyPts]       DECIMAL(6,1)    NOT NULL,    -- Clutch Fantasy Points
    [PlusMinus]        DECIMAL(6,1)    NOT NULL,    -- Clutch Plus Minus
);
GO