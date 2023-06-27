-- Create a new table called '[Advanced]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Advanced]', 'U') IS NOT NULL
DROP TABLE [General].[Advanced]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Advanced]
(
    [AdvancedID]     INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]           NVARCHAR(50)    NOT NULL,    -- Team Name
    [OffRating]      DECIMAL(6,1)    NOT NULL,    -- General Offensive Rating
    [DefRating]      DECIMAL(6,1)    NOT NULL,    -- General Defensive Rating
    [NetRating]      DECIMAL(6,1)    NOT NULL,    -- General Net Rating
    [AstPct]         DECIMAL(6,1)    NOT NULL,    -- General Assist Percentage
    [AstTovRatio]    DECIMAL(6,1)    NOT NULL,    -- General Assist Turover Ratio
    [AstRatio]       DECIMAL(6,1)    NOT NULL,    -- General Assist Ratio
    [ORebPct]        DECIMAL(6,1)    NOT NULL,    -- General Offensive Rebound Percentage
    [DRebPct]        DECIMAL(6,1)    NOT NULL,    -- General Defensive Rebound Percentage
    [RebPct]         DECIMAL(6,1)    NOT NULL,    -- General Total Rebound Percentage
    [TovPct]         DECIMAL(6,1)    NOT NULL,    -- General Turnover Percentage
    [EfgPct]         DECIMAL(6,1)    NOT NULL,    -- General Effective Field Goal Percentage
    [TsPct]          DECIMAL(6,1)    NOT NULL,    -- General True Shooting Percentage
    [Pace]           DECIMAL(6,1)    NOT NULL,    -- General Pace
    [PIE]            DECIMAL(6,1)    NOT NULL,    -- General Player Impact Estimate (PIE)
);
GO