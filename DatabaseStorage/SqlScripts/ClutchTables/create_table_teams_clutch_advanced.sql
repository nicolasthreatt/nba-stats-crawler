-- Create a new table called '[Advanced]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Advanced]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Advanced]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Advanced]
(
    [AdvancedID]     INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]           NVARCHAR(50)    NOT NULL,    -- Team Name
    [OffRating]      DECIMAL(4,1)    NOT NULL,    -- Clutch Offensive Rating
    [DefRating]      DECIMAL(4,1)    NOT NULL,    -- Clutch Defensive Rating
    [NetRating]      DECIMAL(4,1)    NOT NULL,    -- Clutch Net Rating
    [AstPct]         DECIMAL(4,1)    NOT NULL,    -- Clutch Assist Percentage
    [AstTovRatio]    DECIMAL(4,1)    NOT NULL,    -- Clutch Assist Turover Ratio
    [AstRatio]       DECIMAL(4,1)    NOT NULL,    -- Clutch Assist Ratio
    [ORebPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Offensive Rebound Percentage
    [DRebPct]        DECIMAL(4,1)    NOT NULL,    -- Clutch Defensive Rebound Percentage
    [RebPct]         DECIMAL(4,1)    NOT NULL,    -- Clutch Total Rebound Percentage
    [TovRatio]       DECIMAL(4,1)    NOT NULL,    -- Clutch Turnover Ratio
    [EfgPct]         DECIMAL(4,1)    NOT NULL,    -- Clutch Effective Field Goal Percentage
    [TsPct]          DECIMAL(6,1)    NOT NULL,    -- General True Shooting Percentage
    [Pace]           DECIMAL(4,1)    NOT NULL,    -- Clutch Pace
    [PIE]            DECIMAL(4,1)    NOT NULL,    -- Clutch Player Impact Estimate (PIE)
);
GO