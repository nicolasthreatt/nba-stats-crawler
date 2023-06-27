-- Create a new table called '[FourFactors]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[FourFactors]', 'U') IS NOT NULL
DROP TABLE [Clutch].[FourFactors]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[FourFactors]
(
    [FourFactorsID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]             NVARCHAR(50)    NOT NULL,    -- Team Name
    [EfgPct]           DECIMAL(4,1)    NOT NULL,    -- Clutch Effective Field Goal Percentage
    [FTARate]          DECIMAL(4,1)    NOT NULL,    -- Clutch Free Throw Attempt Rate
    [TovPct]           DECIMAL(4,1)    NOT NULL,    -- Clutch Turnover Percentage
    [ORebPct]          DECIMAL(4,1)    NOT NULL,    -- Clutch Offensive Rebound Percentage
    [OppEfgPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Effective Field Goal Percentage
    [OppFTARate]       DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Free Throw Attempted Rate
    [OppTovPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Turnover Percentage
    [OppOrebPct]       DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent's Offensive Rebound Percentage
);
GO