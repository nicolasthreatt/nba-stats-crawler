-- Create a new table called '[Misc]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Misc]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Misc]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Misc]
(
    [MiscID]             INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [PtsOffTov]          DECIMAL(4,1)    NOT NULL,    -- Clutch Points Off Turnover
    [Pts2ndChance]       DECIMAL(4,1)    NOT NULL,    -- Clutch 2nd Chance Points
    [PtsFastBreak]       DECIMAL(4,1)    NOT NULL,    -- Clutch Fastbreak Points
    [PtsInPaint]         DECIMAL(4,1)    NOT NULL,    -- Clutch Points in the Paint
    [OppPtsOffTov]       DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent Points Off Turnovers
    [OppPts2ndChance]    DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent 2nd Chance Points
    [OppPtsFastBreak]    DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent Fastbreak Points
    [OppPtsInPaint]      DECIMAL(4,1)    NOT NULL,    -- Clutch Opponent Points In the Paint
);
GO