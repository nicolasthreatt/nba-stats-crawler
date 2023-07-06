-- Create a new table called '[Playtypes]' in schema '[Playtypes]'
-- Drop the table if it already exists
IF OBJECT_ID('[Playtypes].[Playtypes]', 'U') IS NOT NULL
DROP TABLE [Playtypes].[Playtypes]
GO
-- Create the table in the specified schema
CREATE TABLE [Playtypes].[Playtypes]
(
    [PlaytypeID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]        NVARCHAR(50)    NOT NULL,    -- Player Name
    [Playtype]      NVARCHAR(50)    NOT NULL,    -- Playtype
    [Poss]          DECIMAL(6,1)    NOT NULL,    -- Possessions
    [Freq]          DECIMAL(6,1)    NOT NULL,    -- Frequency
    [PPP]           DECIMAL(6,2)    NOT NULL,    -- Points Per Possession
    [Pts]           DECIMAL(6,1)    NOT NULL,    -- Points
    [FgM]           DECIMAL(6,1)    NOT NULL,    -- Fields Goals Made
    [FgA]           DECIMAL(6,1)    NOT NULL,    -- Field Goals Attempted
    [FgPct]         DECIMAL(6,1)    NOT NULL,    -- Field Goal Percentage
    [eFgPct]        DECIMAL(6,1)    NOT NULL,    -- Effective Field Goal Percentage
    [FtFreq]        DECIMAL(6,1)    NOT NULL,    -- Free Throw Frequency
    [TovFreq]       DECIMAL(6,1)    NOT NULL,    -- Turnover Frequency
    [SfFreq]        DECIMAL(6,1)    NOT NULL,    -- Shooting Foul Frequency
    [And1Freq]      DECIMAL(6,1)    NOT NULL,    -- And1 Frequency
    [ScoreFreq]     DECIMAL(6,1)    NOT NULL,    -- Scoring Frequency
    [Percentile]    DECIMAL(6,1)    NOT NULL,    -- Percentile
);
GO