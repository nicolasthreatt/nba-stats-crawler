-- Create a new table called '[FuturePicks]' in schema '[Draft]'
-- Drop the table if it already exists
IF OBJECT_ID('[Draft].[FuturePicks]', 'U') IS NOT NULL
DROP TABLE [Draft].[FuturePicks]
GO
-- Create the table in the specified schema
CREATE TABLE [Draft].[FuturePicks]
(
    [DraftID]      INT IDENTITY    PRIMARY KEY,
    [Team]         NVARCHAR(50)    NOT NULL,
    [Season]       NVARCHAR(50)    NOT NULL,
    [Round]        INT             NOT NULL,
    [PickInfo]     NVARCHAR(160)    NOT NULL
);
GO