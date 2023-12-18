-- Create a new table called '[Defense]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Defense]', 'U') IS NOT NULL
DROP TABLE [General].[Defense]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Defense]
(
    [DefenseID]          INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]             NVARCHAR(50)    NOT NULL,    -- Player Name
    [DRating]            DECIMAL(6,1)    NOT NULL,    -- General Defensive Rating
    [DReb]               DECIMAL(6,1)    NOT NULL,    -- General Defensive Rebounds
    [DRebPct]            DECIMAL(6,1)    NOT NULL,    -- General Defensive Rebound Percentage
    [Stl]                DECIMAL(6,1)    NOT NULL,    -- General Steals
    [Blk]                DECIMAL(6,1)    NOT NULL,    -- General Blocks
    [OppPtsOffTov]       DECIMAL(6,1)    NOT NULL,    -- General Opponent Points Off Turnovers 
    [OppPts2ndChance]    DECIMAL(6,1)    NOT NULL,    -- General Opponent 2nd Chance Points 
    [OppPtsFastBreak]    DECIMAL(6,1)    NOT NULL,    -- General Opponent Fast Break Points 
    [OppPtsInPaint]      DECIMAL(6,1)    NOT NULL,    -- General Opponent Points in the Paint
    [PctDReb]            DECIMAL(6,1)    NOT NULL,    -- General Percent of Team's Defensive Rebounds 
    [PctStl]             DECIMAL(6,1)    NOT NULL,    -- General Percent of Team's Steals
    [PctBlk]             DECIMAL(6,1)    NOT NULL,    -- General Percent of Team's Blocks 
    [DefWS]              DECIMAL(6,3)    NOT NULL,    -- General Defensive Win Shares
);
GO