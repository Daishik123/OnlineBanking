/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Id]
      ,[DebitCardNo]
      ,[Amount]
      ,[UserName]
      ,[Password]
      ,[CVV]
  FROM [Project].[dbo].[Debit_login]