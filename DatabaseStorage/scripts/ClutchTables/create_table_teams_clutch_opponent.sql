-- Create a new table called '[Opponent]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Opponent]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Opponent]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Opponent]
(
    [OpponentID]      INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]            NVARCHAR(50)    NOT NULL,    -- Team Name
    [OppFgM]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Field Goals Made
    [OppFgA]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Field Goals Attempted
    [OppFgPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Field Goals Percentage
    [OppFg3M]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Three Points Made
    [OppFg3A]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Three Points Attempted
    [OppFg3Pct]       DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Three Point Percentage
    [OppFtM]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Free Throws Made
    [OppFtA]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Free Throws Attempted
    [OppFtPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Free Throw Percentage
    [OppOReb]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Offensive Rebounds
    [OppDReb]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Defensive Rebounds
    [OppTReb]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Total Rebounds
    [OppAst]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Assists Per Game
    [OppTov]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Turnovers Per Game
    [OppStl]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Steals Per Game
    [OppBlk]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Blocks Per Game
    [OppBlkA]         DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Blocked Field Goal Attempts
    [OppPfC]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Personal Fouls Commited
    [OppPfD]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Personal Fouls Drawn
    [OppPts]          DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Points
    [OppPlusMinus]    DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Plus Minus
);
GO