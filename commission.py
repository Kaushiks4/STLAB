def calcEmmission(lockprice,stockprice,barrelprice,locks,stocks,barrels):
    if locks > 70 or locks < 1:
        print('Locks exceeded')
        return
    elif stocks > 80 or stocks < 1:
        print('Stocks exceeded')
        return
    elif barrels > 90 or barrels < 1:
        print('Barrels exceeded')
        return
    else:
        locksales = lockprice*locks
        stocksales = stockprice*stocks
        barrelsales = barrelprice*barrels
        sales = locksales + stocksales + barrelsales
        print("Total sales: ",sales)
        if sales>1800.0:
            com = 220
            com=com+0.20*(sales-1800.0)
        elif sales>1000.0:
            com=100
            com=com+0.15*(sales-1000.0)
        else:
            com=0.10*sales
        print("Commision is $" + str(com))

if __name__ == "__main__":
    lockprice=45.0
    stockprice=30.0
    barrelprice=25.0
    print("Lock Price: "+ str(lockprice))
    print("Stock Price: " + str(stockprice))
    print("Barrel Price: "+ str(barrelprice))
    locks=int(input("Enter number of locks: "))
    stocks=int(input("Enter number of stocks: "))
    barrels=int(input("Enter number of barrels: "))
    calcEmmission(lockprice,stockprice,barrelprice,locks,stocks,barrels)

