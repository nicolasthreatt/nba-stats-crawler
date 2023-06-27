-- Create a new table called '[Drives]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[Drives]', 'U') IS NOT NULL
DROP TABLE [Tracking].[Drives]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[Drives]
(
    [DrivesID]     INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]         NVARCHAR(50)    NOT NULL,    -- Team Name
    [Drives]       DECIMAL(6,1)    NOT NULL,    -- Drives
    [FgM]          DECIMAL(6,1)    NOT NULL,    -- Drives Field Goals Made
    [FgA]          DECIMAL(6,1)    NOT NULL,    -- Drives Field Goals Attempted
    [FgPct]        DECIMAL(6,1)    NOT NULL,    -- Drives Field Goal Percentage
    [FtM]          DECIMAL(6,1)    NOT NULL,    -- Drives Free Throws Made
    [FtA]          DECIMAL(6,1)    NOT NULL,    -- Drives Free Throws Attempted
    [FtPct]        DECIMAL(6,1)    NOT NULL,    -- Drives Free Throw Percentage
    [Pts]          DECIMAL(6,1)    NOT NULL,    -- Drives Points
    [PctPts]       DECIMAL(6,1)    NOT NULL,    -- Drives Points Percentage
    [Passes]       DECIMAL(6,1)    NOT NULL,    -- Drives Pass
    [PctPasses]    DECIMAL(6,1)    NOT NULL,    -- Drives Pass Percentage
    [Ast]          DECIMAL(6,1)    NOT NULL,    -- Drives Assists
    [PctAst]       DECIMAL(6,1)    NOT NULL,    -- Drives Percent of Team's Assists
    [Tov]          DECIMAL(6,1)    NOT NULL,    -- Drives Turnovers
    [PctTov]       DECIMAL(6,1)    NOT NULL,    -- Drives Percent of Team's Turnovers
    [Pf]           DECIMAL(6,1)    NOT NULL,    -- Drives Personal Fouls
    [PctPf]        DECIMAL(6,1)    NOT NULL,    -- Drives Percent of Team's Personal Fouls
);
GO