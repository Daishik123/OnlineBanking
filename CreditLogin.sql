/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Id]
      ,[CreditCardNo]
      ,[UserName]
      ,[Password]
      ,[Amount]
      ,[CVV]
  FROM [Project].[dbo].[Credit_login]