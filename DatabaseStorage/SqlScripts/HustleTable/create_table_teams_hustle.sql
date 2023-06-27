-- Create a new table called '[Hustle]' in schema '[Hustle]'
-- Drop the table if it already exists
IF OBJECT_ID('[Hustle].[Hustle]', 'U') IS NOT NULL
DROP TABLE [Hustle].[Hustle]
GO
-- Create the table in the specified schema
CREATE TABLE [Hustle].[Hustle]
(
    [HustleID]             INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]                 NVARCHAR(50)    NOT NULL,    -- Team Name
    [ScreenAst]            DECIMAL(6,1)    NOT NULL,    -- Screen Assists
    [ScreenAstPts]         DECIMAL(6,1)    NOT NULL,    -- Points From Screen Assists
    [Deflections]          DECIMAL(6,1)    NOT NULL,    -- Deflections
    [OLooseBallsRecovered] DECIMAL(6,1)    NOT NULL,    -- Offensive Loose Balls Recovered
    [DLooseBallsRecovered] DECIMAL(6,1)    NOT NULL,    -- Defensive Loose Balls Recovered
    [TLooseBallsRecovered] DECIMAL(6,1)    NOT NULL,    -- Total Loose Balls Recovered
    [PctLooseBallsO]       DECIMAL(6,1)    NOT NULL,    -- Percentage of Loose Balls Recovered Offensively
    [PctLooseBallsD]       DECIMAL(6,1)    NOT NULL,    -- Percentage of Loose Balls Recovered Defensively
    [ChargesDrawn]         DECIMAL(6,1)    NOT NULL,    -- Charges Drawn
    [Contested2ptShots]    DECIMAL(6,1)    NOT NULL,    -- Contested 2Pt Shots
    [Contested3ptShots]    DECIMAL(6,1)    NOT NULL,    -- Contested 3Pt Shots
    [ContestedAllShots]    DECIMAL(6,1)    NOT NULL,    -- Contested All Shots
);
GO