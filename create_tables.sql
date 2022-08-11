USE StockMarketDB

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'tbl_StockData' and xtype = 'U')
    CREATE TABLE tbl_StockData (
        "Date" date not NULL,
        Ticker varchar(12) not NULL,
        PriceOpen decimal(12,2) not NULL,
        PriceHigh decimal(12,2) not NULL,
        PriceLow decimal(12,2) not NULL,
        PriceClose decimal(12,2) not NULL,
        PriceAdjClose decimal(12,2) not NULL,
        Volume int not NULL,
        CONSTRAINT PK_StockData PRIMARY KEY ("Date", Ticker)
    )
GO