-- Create a new table called '[8ft]' in schema '[OpponentShooting]'
-- Drop the table if it already exists
IF OBJECT_ID('[OpponentShooting].[8ft]', 'U') IS NOT NULL
DROP TABLE [OpponentShooting].[8ft]
GO
-- Create the table in the specified schema
CREATE TABLE [OpponentShooting].[8ft]
(
    [8ftID]                  INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Team]                   NVARCHAR(50)    NOT NULL,    -- Team Name
    [FgM_LT_8ft]             DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Less Than 8FT
    [FgA_LT_8ft]             DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Less Than 8FT
    [FgPct_LT_8ft]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage Less Than 8FT
    [FgM_8To16ft]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 8ft to 16ft
    [FgA_8To16ft]            DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 8ft to 16ft
    [FgPct_8To16ft]          DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 8ft to 16ft
    [FgM_16To24ft]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 16ft to 24ft
    [FgA_16To24ft]           DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 16ft to 24ft
    [FgPct_16To24ft]         DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 16ft to 24ft
    [FgM_24ft_Plus]          DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 24ft Plus
    [FgA_24ft_Plus]          DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 24ft Plus
    [FgPct_24ft_Plus]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 24ft Plus
    [FgM_BackcourtShot]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Backcourt Shot
    [FgA_BackcourtShot]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Backcourt Shot
    [FgPct_BackcourtShot]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage Backcourt Shot
);
GO