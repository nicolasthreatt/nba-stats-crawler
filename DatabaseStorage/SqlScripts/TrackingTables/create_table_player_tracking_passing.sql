-- Create a new table called '[Passing]' in schema '[Tracking]'
-- Drop the table if it already exists
IF OBJECT_ID('[Tracking].[Passing]', 'U') IS NOT NULL
DROP TABLE [Tracking].[Passing]
GO
-- Create the table in the specified schema
CREATE TABLE [Tracking].[Passing]
(
    [PassingID]               INT IDENTITY    PRIMARY KEY, -- Primary Key
    [Player]                  NVARCHAR(50)    NOT NULL,    -- Player Name
    [PassesMaded]             DECIMAL(6,1)    NOT NULL,    -- Passes Made
    [PassesReceived]          DECIMAL(6,1)    NOT NULL,    -- Passes Received
    [Ast]                     DECIMAL(6,1)    NOT NULL,    -- Assists
    [SecondaryAst]            DECIMAL(6,1)    NOT NULL,    -- Secondary Assist
    [PotentialAst]            DECIMAL(6,1)    NOT NULL,    -- Potential Assist
    [AstPtsCreated]           DECIMAL(6,1)    NOT NULL,    -- Assist Points Created
    [AstAdjusted]             DECIMAL(6,1)    NOT NULL,    -- Assist Adjusted
    [AstPassRatio]            DECIMAL(6,1)    NOT NULL,    -- Assist-to-Pass Percentage
    [AstPassRatioAdjusted]    DECIMAL(6,1)    NOT NULL,    -- Assist-to-Pass Percentage Adjusted
);
GO