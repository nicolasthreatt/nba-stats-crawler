-- Create a new table called '[PaintTouches]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[PaintTouches]', 'U') IS NOT NULL
DROP TABLE [Tracking].[PaintTouches]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[PaintTouches]
(
    [PaintTouchesID]    INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]            NVARCHAR(50)    NOT NULL,    -- Player Name
    [Touches]           DECIMAL(6,1)    NOT NULL,    -- Tracking Touches
    [PaintTouches]      DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Touches
    [FgM]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Field Goals Made
    [FgA]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Field Goals Attempted
    [FgPct]             DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Field Goal Percentage
    [FtM]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Free Throws Made
    [FtA]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Free Throws Attempted
    [FtPct]             DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Free Throw Percentage
    [Pts]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Points
    [PctPts]            DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Points Percentage
    [Passes]            DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Pass
    [PctPasses]         DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Pass Percentage
    [Ast]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Assists
    [PctAst]            DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Assists Percentage
    [Tov]               DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Turnovers
    [PctTov]            DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Turnovers Percentage
    [Pf]                DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Personal Foul
    [PctPf]             DECIMAL(6,1)    NOT NULL,    -- Tracking Paint Personal Foul Percentage
);
GO