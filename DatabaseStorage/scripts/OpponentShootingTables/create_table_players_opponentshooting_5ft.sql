-- Create a new table called '[5ft]' in schema '[OpponentShooting]'
-- Drop the table if it already exists
IF OBJECT_ID('[OpponentShooting].[5ft]', 'U') IS NOT NULL
DROP TABLE [OpponentShooting].[5ft]
GO
-- Create the table in the specified schema
CREATE TABLE [OpponentShooting].[5ft]
(
    [5ftID]             INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]            NVARCHAR(50)    NOT NULL,    -- Player Name
    [FgM_LT_5ft]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made Less Than 5FT
    [FgA_LT_5ft]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted Less Than 5FT
    [FgPct_LT_5ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage Less Than 5FT
    [FgM_5To9ft]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 5ft to 9ft
    [FgA_5To9ft]        DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 5ft to 9ft
    [FgPct_5To9ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 5ft to 9ft
    [FgM_10To14ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 10ft to 14ft
    [FgA_10To14ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 10ft to 14ft
    [FgPct_10To14ft]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 10ft to 14ft
    [FgM_15To19ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 15ft to 19ft
    [FgA_15To19ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 15ft to 19ft
    [FgPct_15To19ft]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 15ft to 19ft
    [FgM_20To24ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 20ft to 24ft
    [FgA_20To24ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 20ft to 24ft
    [FgPct_20To24ft]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 20ft to 24ft
    [FgM_25To29ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Made 25ft to 29ft
    [FgA_25To29ft]      DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Attempted 25ft to 29ft
    [FgPct_25To29ft]    DECIMAL(6,1)    NOT NULL,    -- Opponent Shooting Field Goals Percentage 25ft to 29ft
);
GO