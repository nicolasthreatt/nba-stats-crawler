-- Create a new table called '[Dashboard]' in schema '[OpponentShooting]'
-- Drop the table if it already exists
IF OBJECT_ID('[OpponentShooting].[Dashboard]', 'U') IS NOT NULL
DROP TABLE [OpponentShooting].[Dashboard]
GO
-- Create the table in the specified schema
CREATE TABLE [OpponentShooting].[Dashboard]
(
    [DashboardID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]           NVARCHAR(50)    NOT NULL,    -- Team Name
    [Type]           NVARCHAR(50)    NOT NULL,    -- Opponent Shooting Type
    [FgFreq]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Frequency
    [FgM]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made
    [FgA]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attemped
    [FgPct]          DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage
    [eFgPct]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Effective Field Goal Percentage
    [Fg2Freq]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Two Point Field Goal Frequency
    [Fg2M]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Two Field Goals Made
    [Fg2A]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Two Point Field Goals
    [Fg2Pct]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Two Field Goal Percentage
    [Fg3Freq]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Three Point Field Goal Frequency
    [Fg3M]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Three Field Goals Made
    [Fg3A]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Three Field Goals Attemped
    [Fg3Pct]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Three Field Goal Percentage
);
GO