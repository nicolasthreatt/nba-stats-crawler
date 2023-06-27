-- Create a new table called '[Zone]' in schema '[OpponentShooting]'
-- Drop the table if it already exists
IF OBJECT_ID('[OpponentShooting].[Zone]', 'U') IS NOT NULL
DROP TABLE [OpponentShooting].[Zone]
GO
-- Create the table in the specified schema
CREATE TABLE [OpponentShooting].[Zone]
(
    [ZoneID]                  INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]                  NVARCHAR(50)    NOT NULL,    -- Player Name
    [FgM_RestrictedArea]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Restricted Area
    [FgA_RestrictedArea]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Restricted Area
    [FgPct_RestrictedArea]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Restricted Area
    [FgM_Paint]               DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made In Paint (Non Restricted Area)
    [FgA_Paint]               DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted In Paint (Non Restricted Area)
    [FgPct_Paint]             DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage In Paint (Non Restricted Area)
    [FgM_Midrange]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Midrange
    [FgA_Midrange]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Midrange
    [FgPct_Midrange]          DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Midrange
    [FgM_LeftCorner3]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Left Corner 3
    [FgA_LeftCorner3]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Left Corner 3
    [FgPct_LeftCorner3]       DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Left Corner 3
    [FgM_RightCorner3]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Right Corner 3
    [FgA_RightCorner3]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Right Corner 3
    [FgPct_RightCorner3]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Right Corner 3
    [FgM_Corner3]             DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Corner 3
    [FgA_Corner3]             DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Corner 3
    [FgPct_Corner3]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Corner 3
    [FgM_AboveBreak3]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Above The Break 3
    [FgA_AboveBreak3]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Above The Break 3
    [FgPct_AboveBreak3]       DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goal Percentage Above The Break 3
);
GO