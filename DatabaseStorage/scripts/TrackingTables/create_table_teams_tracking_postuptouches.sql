-- Create a new table called '[PostUpTouches]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[PostUpTouches]', 'U') IS NOT NULL
DROP TABLE [Tracking].[PostUpTouches]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[PostUpTouches]
(
    [PostUpTouchesID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]               NVARCHAR(50)    NOT NULL,    -- Team Name
    [Touches]            DECIMAL(6,1)    NOT NULL,    -- Tracking Touches
    [PostUpTouches]      DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Touches
    [FgM]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Field Goals Made
    [FgA]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Field Goals Attempted
    [FgPct]              DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Field Goal Percentage
    [FtM]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Free Throws Made
    [FtA]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Free Throws Attempted
    [FtPct]              DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Free Throw Percentage
    [Pts]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Points
    [PctPts]             DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Points Percentage
    [Passes]             DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Pass
    [PctPasses]          DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Pass Percentage
    [Ast]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Assists
    [PctAst]             DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Assists Percentage
    [Tov]                DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Turnovers
    [PctTov]             DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Turnovers Percentage
    [Pf]                 DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Personal Foul
    [PctPf]              DECIMAL(6,1)    NOT NULL,    -- Tracking Post-Up Personal Foul Percentage
);
GO