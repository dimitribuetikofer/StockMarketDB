IF NOT EXISTS(SELECT * FROM sys.databases Where name = 'StockMarketDB')
BEGIN
    CREATE DATABASE StockMarketDB
END
GO