-- Create a new table called '[General]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[General]', 'U') IS NOT NULL
DROP TABLE [General].[General]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[General]
(
    [GeneralID]    INT IDENTITY     PRIMARY KEY, -- Primary Key
    [Team]         NVARCHAR(50)     NOT NULL,    -- Team Name
    [Games]        INT              NOT NULL,    -- General Games Played
    [Wins]         INT              NOT NULL,    -- General Wins
    [Losses]       INT              NOT NULL,    -- General Losses
    [Mins]         DECIMAL(10,1)    NOT NULL,    -- General Minutes
    [WinPct]       DECIMAL(4,1)     NOT NULL,    -- General Winning Percentage
);
GO