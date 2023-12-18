-- Create a new table called '[Rebounding]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[Rebounding]', 'U') IS NOT NULL
DROP TABLE [Tracking].[Rebounding]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[Rebounding]
(
    [ReboundingID]           INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]                 NVARCHAR(50)    NOT NULL,    -- Player Name
    [Rebs]                   DECIMAL(6,1)    NOT NULL,    -- Tracking Rebounds
    [ContestedReb]           DECIMAL(6,1)    NOT NULL,    -- Tracking Contested Rebounds
    [ContestedRebPct]        DECIMAL(6,1)    NOT NULL,    -- Tracking Contested Rebound Percentage
    [RebChances]             DECIMAL(6,1)    NOT NULL,    -- Tracking Rebound Chance
    [RebChancesPct]          DECIMAL(6,1)    NOT NULL,    -- Tracking Rebound Chance Percentage
    [DeferredRebChances]     DECIMAL(6,1)    NOT NULL,    -- Tracking Deferred Rebound Chances
    [AdjRebChancePct]        DECIMAL(6,1)    NOT NULL,    -- Tracking Adjusted Rebound Chance Percentage
    [AvgRebDistanceFeet]     DECIMAL(6,1)    NOT NULL,    -- Average Rebound Distance
);
GO