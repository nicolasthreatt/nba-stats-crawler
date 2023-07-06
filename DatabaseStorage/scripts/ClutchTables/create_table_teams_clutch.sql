-- Create a new table called '[Clutch]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Clutch]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Clutch]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Clutch]
(
    [ClutchID]   INT IDENTITY     PRIMARY KEY, -- Primary Key
    [Team]       NVARCHAR(50)     NOT NULL,    -- Team Name
    [Games]      INT NOT          NULL,        -- Clutch Games Played
    [Wins]       INT NOT          NULL,        -- Clutch Wins
    [Losses]     INT NOT          NULL,        -- Clutch Losses
    [Mins]       DECIMAL(10,1)    NOT NULL,    -- Clutch Minutes
    [WinPct]     DECIMAL(4,1)     NOT NULL,    -- Clutch Winning Percentage
);
GO