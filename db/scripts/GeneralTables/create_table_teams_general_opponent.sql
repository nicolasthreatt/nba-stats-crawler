-- Create a new table called '[Opponent]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Opponent]', 'U') IS NOT NULL
DROP TABLE [General].[Opponent]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Opponent]
(
    [OpponentID]      INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]            NVARCHAR(50)    NOT NULL,    -- Team Name
    [OppFgM]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Field Goals Made
    [OppFgA]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Field Goals Attempted
    [OppFgPct]        DECIMAL(6,1)    NOT NULL,    -- General Opponent's Field Goals Percentage
    [OppFg3M]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Three Points Made
    [OppFg3A]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Three Points Attempted
    [OppFg3Pct]       DECIMAL(6,1)    NOT NULL,    -- General Opponent's Three Point Percentage
    [OppFtM]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Free Throws Made
    [OppFtA]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Free Throws Attempted
    [OppFtPct]        DECIMAL(6,1)    NOT NULL,    -- General Opponent's Free Throw Percentage
    [OppOReb]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Offensive Rebounds
    [OppDReb]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Defensive Rebounds
    [OppTReb]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Total Rebounds
    [OppAst]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Assists Per Game
    [OppTov]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Turnovers Per Game
    [OppStl]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Steals Per Game
    [OppBlk]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Blocks Per Game
    [OppBlkA]         DECIMAL(6,1)    NOT NULL,    -- General Opponent's Blocked Field Goal Attempts
    [OppPfC]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Personal Fouls Commited
    [OppPfD]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Personal Fouls Drawn
    [OppPts]          DECIMAL(6,1)    NOT NULL,    -- General Opponent's Points
    [OppPlusMinus]    DECIMAL(6,1)    NOT NULL,    -- General Opponent's Plus Minus
);
GO