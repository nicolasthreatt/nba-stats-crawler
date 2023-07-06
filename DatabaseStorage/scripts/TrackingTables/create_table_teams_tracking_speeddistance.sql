-- Create a new table called '[SpeedDistance]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[SpeedDistance]', 'U') IS NOT NULL
DROP TABLE [Tracking].[SpeedDistance]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[SpeedDistance]
(
    [SpeedDistanceID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [DistFeet]           DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Distance Feet
    [DistMiles]          DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Distance Miles
    [DistMilesOff]       DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Distance Miles Offense
    [DistMilesDef]       DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Distance Miles Defense
    [AvgSpeed]           DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Average Speed
    [AvgSpeedOff]        DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Average Speed Offense
    [AvgSpeedDef]        DECIMAL(6,1)    NOT NULL,    -- Tracking Speed-Distance Average Speed Defense
);
GO