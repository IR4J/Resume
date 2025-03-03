import yfinance as yf
#this is just common names not sure how to get stock names to symbol. 
# you need to install yfinance or it will not work
name2stock = {
    'TESLA': 'TSLA',
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'AMAZON': 'AMZN',
    'FACEBOOK': 'FB',
    'GOOGLE': 'GOOGL',
    'NETFLIX': 'NFLX',
    'NVIDIA': 'NVDA',
    'AMD': 'AMD',
    'INTEL': 'INTC',
    'IBM': 'IBM',
    'ORACLE': 'ORCL',
    'CISCO': 'CSCO',
    'QUALCOMM': 'QCOM',
    'PAYPAL': 'PYPL',
    'SQUARE': 'SQ',
    'TWITTER': 'TWTR',
    'UBER': 'UBER',
    'LYFT': 'LYFT',
    'PINTEREST': 'PINS',
    'SNAP': 'SNAP',
    'SPOTIFY': 'SPOT',
    'ZOOM': 'ZM',
    'SLACK': 'WORK',
    'TWITCH': 'AMZN',
    'RIVIAN': 'RIVN',
    'ROBINHOOD': 'HOOD',
    'ALIBABA': 'BABA',
    'TENCENT': 'TCEHY',
    'JD.COM': 'JD',
    'BAIDU': 'BIDU',
    'NETEASE': 'NTES',
}

def get_stock_data():
    stocks = []
    while True:
        choice = input("Do you want to calculate multiple stocks or just one? (one or more): ").strip().lower()
        if choice == "more":
            stocknumber = int(input("How many stocks do you own? "))
            break
        elif choice == "one":
            stocknumber = 1
            break
        else:
            print("You mistyped something. Try again.")
    
    for i in range(stocknumber):
        while True:
            user_input = input("Enter stock symbol: ").strip().upper()

            symbol = name2stock.get(user_input, user_input)
            stock = yf.Ticker(symbol)
            try:
                history = stock.history(period='1d')
                if history.empty:
                    raise ValueError
                break
            except:
                print(f"The stock {user_input} is not correct. Try another one.")
        
        shares = float(input(f"Enter number of shares for {symbol}: "))
        if shares != int(shares):           # need to fix this.
            print("Number of shares must be an integer. Try again.")

        avg_price = float(input(f"Enter average purchase price for {symbol}: "))
        stocks.append((symbol, shares, avg_price))
    
    return stocks

def calculate_portfolio(stocks):
    total_invested = 0
    total_value = 0
    print("\nCurrent Portfolio Value:")
    print("--------------------------------------------------------------")
    print(f"{'Symbol':<10} {'Shares':<10} {'Average Cost':<15} {'Current Cost':<15} {'Gain or Loss':<15}")
    print("--------------------------------------------------------------")
    
    for symbol, shares, avg_price in stocks:
        stock = yf.Ticker(symbol)
        try:
            history = stock.history(period='1d')
            current_price = history['Close'].iloc[-1]
        except:
            print(f"Could not retrieve data for {symbol}.")
            continue
        
        total_cost = shares * avg_price
        current_value = shares * current_price
        gain_loss = current_value - total_cost
        total_invested += total_cost
        total_value += current_value
        print(f"{symbol:<10} {shares:<10} {avg_price:<15.2f}  {current_price:<15.2f} {gain_loss:<15.2f}")
    
    print("--------------------------------------------------------------")
    print(f"Total Invested: ${total_invested:.2f}")
    print(f"Total Value: ${total_value:.2f}")
    print(f"Net Gain/Loss: ${total_value - total_invested:.2f}")

def main():
    stocks = get_stock_data()
    calculate_portfolio(stocks)

main()
