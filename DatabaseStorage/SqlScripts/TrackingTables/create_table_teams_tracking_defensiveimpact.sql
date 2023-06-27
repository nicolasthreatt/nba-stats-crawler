-- Create a new table called '[DefensiveImpact]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[DefensiveImpact]', 'U') IS NOT NULL
DROP TABLE [Tracking].[DefensiveImpact]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[DefensiveImpact]
(
    [DefensiveImpactID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]                 NVARCHAR(50)    NOT NULL,    -- Team Name
    [Stl]                  DECIMAL(6,1)    NOT NULL,    -- Steals
    [Blk]                  DECIMAL(6,1)    NOT NULL,    -- Blocks
    [DReb]                 DECIMAL(6,1)    NOT NULL,    -- Defensive Rebounds
    [DefendedFgM]          DECIMAL(6,1)    NOT NULL,    -- Field Goals Defended at Rim Made
    [DefendedFgA]          DECIMAL(6,1)    NOT NULL,    -- Field Goals Defended at Rim Attempted
    [DefendedFgPct]        DECIMAL(6,1)    NOT NULL,    -- Field Goals Defended at Rim Percent
);
GO