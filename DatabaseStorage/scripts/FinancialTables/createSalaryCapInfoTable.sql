-- Create a new table called '[SalaryCapOverview2019-20]' in schema '[Teams]'
-- Drop the table if it already exists
IF OBJECT_ID('[Teams].[SalaryCapOverview2019-20]', 'U') IS NOT NULL
DROP TABLE [Teams].[SalaryCapOverview2019-20]
GO
-- Create the table in the specified schema
CREATE TABLE [Teams].[SalaryCapOverview2019-20]
(
    [TeamSalaryCapID] INT IDENTITY  PRIMARY KEY, -- Primary Key column
    [Team]            NVARCHAR(50)  NOT NULL,
    [2019-20]         NVARCHAR(50),
    [2020-21]         NVARCHAR(50),
    [2021-22]         NVARCHAR(50),
    [2022-23]         NVARCHAR(50),
    [2023-24]         NVARCHAR(50),
    [2024-25]         NVARCHAR(50),
);
GO