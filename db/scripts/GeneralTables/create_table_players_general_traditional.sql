-- Create a new table called '[Traditional]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Traditional]', 'U') IS NOT NULL
DROP TABLE [General].[Traditional]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Traditional]
(
    [TraditionalID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]           NVARCHAR(50)    NOT NULL,    -- Player Name
    [Pts]              DECIMAL(6,1)    NOT NULL,    -- General Pts
    [FgM]              DECIMAL(6,1)    NOT NULL,    -- General Field Goals Made
    [FgA]              DECIMAL(6,1)    NOT NULL,    -- General Field Goals Attempted
    [FgPct]            DECIMAL(6,1)    NOT NULL,    -- General Field Goal Percentage
    [Fg3M]             DECIMAL(6,1)    NOT NULL,    -- General 3 Point Field Goals Made
    [Fg3A]             DECIMAL(6,1)    NOT NULL,    -- General 3 Point Field Goals Attempted
    [Fg3Pct]           DECIMAL(6,1)    NOT NULL,    -- General 3 Point Field Goals Percentage
    [FtM]              DECIMAL(6,1)    NOT NULL,    -- General Free Throws Made
    [FtA]              DECIMAL(6,1)    NOT NULL,    -- General Free Throws Attempted
    [FtPct]            DECIMAL(6,1)    NOT NULL,    -- General Free Throw Percentage
    [OReb]             DECIMAL(6,1)    NOT NULL,    -- General Offensive Rebounds
    [DReb]             DECIMAL(6,1)    NOT NULL,    -- General Defensive Rebounds
    [TReb]             DECIMAL(6,1)    NOT NULL,    -- General Total Rebounds
    [Ast]              DECIMAL(6,1)    NOT NULL,    -- General Assists
    [Tov]              DECIMAL(6,1)    NOT NULL,    -- General Turnovers
    [Stl]              DECIMAL(6,1)    NOT NULL,    -- General Steals
    [Blk]              DECIMAL(4,1)    NOT NULL,    -- General Blocks
    [PF_C]             DECIMAL(6,1)    NOT NULL,    -- General Personal Fouls Committed
    [FantasyPts]       DECIMAL(6,1)    NOT NULL,    -- General Fantasy Points
    [DD2]              INT             NOT NULL,    -- General Double-Double
    [TD3]              INT             NOT NULL,    -- General Triple-Double
    [PlusMinus]        DECIMAL(6,1)    NOT NULL,    -- General Plus Minus
);
GO