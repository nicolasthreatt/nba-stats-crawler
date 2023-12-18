-- Create a new table called '[Scoring]' in schema '[General]'
-- Drop the table if it already exists
IF OBJECT_ID('[General].[Scoring]', 'U') IS NOT NULL
DROP TABLE [General].[Scoring]
GO
-- Create the table in the specified schema
CREATE TABLE [General].[Scoring]
(
    [ScoringID]          INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [PctFgA2Pt]          DECIMAL(6,1)    NOT NULL,    -- General Percent of Field Goals Attempted (2 Pointers)
    [PctFgA3Pt]          DECIMAL(6,1)    NOT NULL,    -- General Percent of Field Goals Attempted (3 Pointers)
    [PctPts2Pt]          DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (2 Pointers)
    [PctPtsMid]          DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (Mid-Range)
    [PctPts3pt]          DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (3 Pointers)
    [PctPtsFb]           DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (Fast Break Points)
    [PctPtsFT]           DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (Free Throw Points)
    [PctPtsOffTov]       DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (Off Turnovers)
    [PctPtsInPaint]      DECIMAL(6,1)    NOT NULL,    -- General Percent of Points (Points in Paint)
    [PctPts2PtsAst]      DECIMAL(6,1)    NOT NULL,    -- General Percent of 2 Point Field Goals Made Assisted
    [PctPts2PtsUnAst]    DECIMAL(6,1)    NOT NULL,    -- General Percent of 2 Point Field Goals Made Unassisted
    [PctPts3PtsAst]      DECIMAL(6,1)    NOT NULL,    -- General Percent of 3 Point Field Goals Made Assisted
    [PctPts3PtsUnAst]    DECIMAL(6,1)    NOT NULL,    -- General Percent of 3 Point Field Goals Made Unassisted
    [PctPtsFgMAst]       DECIMAL(6,1)    NOT NULL,    -- General Percent of Total Field Goals Made Assisted
    [PctPtsFgMUnAst]     DECIMAL(6,1)    NOT NULL,    -- General Percent of Total Field Goals Made Unassisted
);
GO