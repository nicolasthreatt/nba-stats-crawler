-- Create a new table called '[Bio]' in schema '[Players]'
-- Drop the table if it already exists
IF OBJECT_ID('[Players].[Bio]', 'U') IS NOT NULL
DROP TABLE [Players].[Bio]
GO
-- Create the table in the specified schema
CREATE TABLE [Players].[Bio]
(
    [PlayerID]       INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]         NVARCHAR(50)    NOT NULL,    -- Player Name
    [Team]           NVARCHAR(50)    NOT NULL,    -- Current Team
    [Age]            INT             NOT NULL,    -- Age
    [Height]         NVARCHAR(5)     NOT NULL,    -- Height
    [Weight]         INT             NOT NULL,    -- Weight
    [College]        NVARCHAR(50)    NOT NULL,    -- College
    [Country]        NVARCHAR(50)    NOT NULL,    -- Country
    [DraftYear]      NVARCHAR(9)     NOT NULL,    -- Draft Year
    [DraftRound]     NVARCHAR(9)     NOT NULL,    -- Draft Round
    [DraftNumber]    NVARCHAR(9)     NOT NULL,    -- Draft Number
    [GamesPlayed]    INT             NOT NULL,    -- Games Played
    [Pts]            DECIMAL(10,1)   NOT NULL,    -- Points
    [Rebs]           DECIMAL(10,1)   NOT NULL,    -- Rebounds
    [Asts]           DECIMAL(10,1)   NOT NULL,    -- Assists
    [NetRating]      DECIMAL(6,1)    NOT NULL,    -- Net Rating
    [ORebPct]        DECIMAL(6,1)    NOT NULL,    -- Offensive Rebound Percentage
    [DRebPct]        DECIMAL(6,1)    NOT NULL,    -- Defensive Rebound Percentage
    [UsagePct]       DECIMAL(6,1)    NOT NULL,    -- Usage Percentage
    [TsPct]          DECIMAL(6,1)    NOT NULL,    -- True Shooting Percentage
    [AstPct]         DECIMAL(6,1)    NOT NULL,    -- Assist Percentage
);
GO