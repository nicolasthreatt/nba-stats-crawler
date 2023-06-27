-- Create a new table called '[FourFactors]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[FourFactors]', 'U') IS NOT NULL
DROP TABLE [General].[FourFactors]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[FourFactors]
(
    [FourFactorsID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]             NVARCHAR(50)    NOT NULL,    -- Team Name
    [EfgPct]           DECIMAL(6,1)    NOT NULL,    -- General Effective Field Goal Percentage
    [FTARate]          DECIMAL(6,1)    NOT NULL,    -- General Free Throw Attempt Rate
    [TovPct]           DECIMAL(6,1)    NOT NULL,    -- General Turnover Percentage
    [ORebPct]          DECIMAL(6,1)    NOT NULL,    -- General Offensive Rebound Percentage
    [OppEfgPct]        DECIMAL(6,1)    NOT NULL,    -- General Opponent's Effective Field Goal Percentage
    [OppFTARate]       DECIMAL(6,1)    NOT NULL,    -- General Opponent's Free Throw Attempted Rate
    [OppTovPct]        DECIMAL(6,1)    NOT NULL,    -- General Opponent's Turnover Percentage
    [OppOrebPct]       DECIMAL(6,1)    NOT NULL,    -- General Opponent's Offensive Rebound Percentage
);
GO