-- Create a new table called '[Scoring]' in schema '[Clutch]'
-- Drop the table if it already exists
IF OBJECT_ID('[Clutch].[Scoring]', 'U') IS NOT NULL
DROP TABLE [Clutch].[Scoring]
GO
-- Create the table in the specified schema
CREATE TABLE [Clutch].[Scoring]
(
    [ScoringID]          INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [PctFgA2Pt]          DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Field Goals Attempted (2 Pointers)
    [PctFgA3Pt]          DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Field Goals Attempted (3 Pointers)
    [PctPts2Pt]          DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (2 Pointers)
    [PctPtsMid]          DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (Mid-Range)
    [PctPts3pt]          DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (3 Pointers)
    [PctPtsFb]           DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (Fast Break Points)
    [PctPtsFT]           DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (Free Throw Points)
    [PctPtsOffTov]       DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (Off Turnovers)
    [PctPtsInPaint]      DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Points (Points in Paint)
    [PctPts2PtsAst]      DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of 2 Point Field Goals Made Assisted
    [PctPts2PtsUnAst]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of 2 Point Field Goals Made Unassisted
    [PctPts3PtsAst]      DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of 3 Point Field Goals Made Assisted
    [PctPts3PtsUnAst]    DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of 3 Point Field Goals Made Unassisted
    [PctPtsFgMAst]       DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Total Field Goals Made Assisted
    [PctPtsFgMUnAst]     DECIMAL(4,1)    NOT NULL,    -- Clutch Percent of Total Field Goals Made Unassisted
);
GO