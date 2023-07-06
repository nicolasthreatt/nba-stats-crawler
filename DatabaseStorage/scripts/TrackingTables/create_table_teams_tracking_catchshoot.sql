-- Create a new table called '[CatchShoot]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[CatchShoot]', 'U') IS NOT NULL
DROP TABLE [Tracking].[CatchShoot]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[CatchShoot]
(
    [CatchShootID]     INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]             NVARCHAR(50)    NOT NULL,    -- Team Name
    [Pts]              DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot Points
    [FgM]              DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot Field Goals Made
    [FgA]              DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot Field Goals Attempted
    [FgPct]            DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot Field Goals Percentage
    [Fg3M]             DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot 3 Point Field Goals Made
    [Fg3A]             DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot 3 Point Field Goals Attempted
    [Fg3Pct]           DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot 3 Point Field Goals Percentage
    [eFgPct]           DECIMAL(6,1)    NOT NULL,    -- Catch-Shoot Effective Field Goal Percentage
);
GO