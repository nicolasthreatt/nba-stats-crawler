-- Create a new table called '[Misc]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Misc]', 'U') IS NOT NULL
DROP TABLE [General].[Misc]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Misc]
(
    [MiscID]             INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [PtsOffTov]          DECIMAL(6,1)    NOT NULL,    -- General Points Off Turnover
    [Pts2ndChance]       DECIMAL(6,1)    NOT NULL,    -- General 2nd Chance Points
    [PtsFastBreak]       DECIMAL(6,1)    NOT NULL,    -- General Fastbreak Points
    [PtsInPaint]         DECIMAL(6,1)    NOT NULL,    -- General Points in the Paint
    [OppPtsOffTov]       DECIMAL(6,1)    NOT NULL,    -- General Opponent Points Off Turnovers
    [OppPts2ndChance]    DECIMAL(6,1)    NOT NULL,    -- General Opponent 2nd Chance Points
    [OppPtsFastBreak]    DECIMAL(6,1)    NOT NULL,    -- General Opponent Fastbreak Points
    [OppPtsInPaint]      DECIMAL(6,1)    NOT NULL,    -- General Opponent Points In the Paint
);
GO