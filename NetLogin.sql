/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Id]
      ,[UserName]
      ,[Password]
      ,[AccountNo]
      ,[Amount]
  FROM [Project].[dbo].[Net_login]