-- Create a new table called '[ClassStats]' in schema '[Draft]'
-- Drop the table if it already exists
IF OBJECT_ID('[Draft].[ClassStats]', 'U') IS NOT NULL
DROP TABLE [Draft].[ClassStats]
GO
-- Create the table in the specified schema
CREATE TABLE [Draft].[ClassStats]
(
    [DrafteeID]   INT IDENTITY    PRIMARY KEY,
    [Player]      NVARCHAR(50)    NOT NULL,
    [Season]      INT             NOT NULL,
    [Round]       INT             NOT NULL,
    [Pick]        INT             NOT NULL,
    [College]     NVARCHAR(50)    NOT NULL,
    [Team]        NVARCHAR(50)    NOT NULL,
    [Years]       INT             NOT NULL,
    [TotalGames]  INT             NOT NULL,
    [TotalMins]   INT             NOT NULL,
    [TotalPts]    INT             NOT NULL,
    [TotalReb]    INT             NOT NULL,
    [TotalAst]    INT             NOT NULL,
    [FgPct]       DECIMAL(4,1)    NOT NULL,
    [Fg3Pct]      DECIMAL(4,1)    NOT NULL,
    [FtPct]       DECIMAL(4,1)    NOT NULL,
    [PerGameMins] DECIMAL(3,1)    NOT NULL,
    [PerGamePts]  DECIMAL(3,1)    NOT NULL,
    [PerGameReb]  DECIMAL(3,1)    NOT NULL,
    [PerGameAst]  DECIMAL(3,1)    NOT NULL,
    [WinShares]   DECIMAL(2,1)    NOT NULL,
    [WinShares48] DECIMAL(3,3)    NOT NULL,
    [PlusMinus]   DECIMAL(3,1)    NOT NULL,
    [VORP]        DECIMAL(2,1)    NOT NULL
);
GO