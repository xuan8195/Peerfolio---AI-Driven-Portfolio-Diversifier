import pandas as pd
import numpy as np
from typing import Dict
import random

def generate_sample_data(user_profile: Dict) -> pd.DataFrame:
    """Generate realistic sample portfolio data based on user profile"""
    
    investment_style = user_profile.get('investment_style', 'Moderate')
    age = user_profile.get('age', 35)
    net_worth = user_profile.get('net_worth', '$2.5M - $5M')
    
    # Define stock universes based on investment style
    if investment_style == 'Tech-focused':
        primary_stocks = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'META', 'TSLA', 'ADBE', 'CRM', 'NFLX', 'AMD']
        secondary_stocks = ['AMZN', 'V', 'MA', 'UNH', 'JNJ']
    elif investment_style == 'Conservative':
        primary_stocks = ['JNJ', 'PG', 'KO', 'WMT', 'UNH', 'V', 'MA', 'HD', 'PFE', 'VZ']
        secondary_stocks = ['AAPL', 'MSFT', 'JPM', 'BAC', 'T']
    elif investment_style == 'ESG-focused':
        primary_stocks = ['MSFT', 'AAPL', 'GOOGL', 'UNH', 'PG', 'V', 'MA', 'HD', 'JNJ', 'PFE']
        secondary_stocks = ['NVDA', 'ADBE', 'CRM', 'TMO', 'ABT']
    elif investment_style == 'Crypto-focused':
        primary_stocks = ['TSLA', 'NVDA', 'COIN', 'MSTR', 'SQ', 'PYPL', 'HOOD', 'RIOT', 'MARA']
        secondary_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
    else:  # Moderate/Aggressive
        primary_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'UNH', 'JNJ', 'V', 'MA', 'NVDA']
        secondary_stocks = ['JPM', 'PG', 'HD', 'PFE', 'WMT', 'BAC', 'DIS', 'ADBE', 'CRM', 'TMO']
    
    # Determine portfolio size based on net worth
    if '$1M' in net_worth:
        num_positions = random.randint(8, 12)
        base_investment = random.randint(50000, 150000)
    elif '$2.5M' in net_worth:
        num_positions = random.randint(10, 15)
        base_investment = random.randint(100000, 300000)
    elif '$5M' in net_worth:
        num_positions = random.randint(12, 18)
        base_investment = random.randint(200000, 500000)
    elif '$10M' in net_worth:
        num_positions = random.randint(15, 25)
        base_investment = random.randint(400000, 800000)
    else:  # $25M+
        num_positions = random.randint(20, 30)
        base_investment = random.randint(500000, 1500000)
    
    # Select stocks for portfolio
    selected_stocks = random.sample(primary_stocks, min(len(primary_stocks), int(num_positions * 0.7)))
    remaining_positions = num_positions - len(selected_stocks)
    if remaining_positions > 0:
        selected_stocks.extend(random.sample(secondary_stocks, min(len(secondary_stocks), remaining_positions)))
    
    # Stock price data (realistic current prices)
    stock_prices = {
        'AAPL': 175.43, 'MSFT': 384.52, 'GOOGL': 138.76, 'AMZN': 146.89, 'TSLA': 248.87,
        'NVDA': 459.75, 'META': 298.54, 'UNH': 524.32, 'JNJ': 159.87, 'V': 241.65,
        'MA': 421.23, 'PG': 156.78, 'HD': 365.43, 'PFE': 28.95, 'WMT': 165.32,
        'JPM': 154.76, 'BAC': 32.87, 'DIS': 96.54, 'ADBE': 512.34, 'CRM': 234.56,
        'TMO': 578.90, 'ABT': 108.76, 'VZ': 38.95, 'T': 19.45, 'KO': 59.32,
        'COIN': 87.65, 'MSTR': 189.43, 'SQ': 76.23, 'PYPL': 58.76, 'HOOD': 12.34,
        'RIOT': 8.76, 'MARA': 15.43, 'AMD': 142.87, 'NFLX': 445.67
    }
    
    portfolio_data = []
    
    for stock in selected_stocks:
        current_price = stock_prices.get(stock, 100.0)
        
        # Generate realistic purchase price (could be higher or lower than current)
        price_change = random.uniform(-0.4, 0.6)  # -40% to +60% from current
        purchase_price = current_price * (1 - price_change)
        
        # Calculate shares based on investment amount
        position_size = base_investment * random.uniform(0.3, 2.0)  # Vary position sizes
        shares = position_size / current_price
        
        # Round shares to reasonable numbers
        if shares > 1000:
            shares = round(shares, -1)  # Round to nearest 10
        elif shares > 100:
            shares = round(shares, 0)   # Round to nearest whole number
        else:
            shares = round(shares, 1)   # One decimal place
        
        portfolio_data.append({
            'Symbol': stock,
            'Shares': shares,
            'Purchase_Price': round(purchase_price, 2),
            'Current_Price': current_price
        })
    
    # Create DataFrame
    df = pd.DataFrame(portfolio_data)
    
    # Add calculated columns
    df['Market_Value'] = df['Shares'] * df['Current_Price']
    df['Cost_Basis'] = df['Shares'] * df['Purchase_Price']
    df['P&L'] = df['Market_Value'] - df['Cost_Basis']
    df['Return_%'] = (df['P&L'] / df['Cost_Basis']) * 100
    
    # Sort by market value (largest positions first)
    df = df.sort_values('Market_Value', ascending=False).reset_index(drop=True)
    
    return df[['Symbol', 'Shares', 'Purchase_Price', 'Current_Price']]

def generate_market_data():
    """Generate sample market data for testing"""
    
    # Major indices with realistic values
    indices = {
        'S&P 500': {'current': 4567.89, 'change': 0.75},
        'NASDAQ': {'current': 14234.56, 'change': 1.23},
        'Dow Jones': {'current': 35678.90, 'change': -0.45},
        'FTSE 100': {'current': 7456.78, 'change': 0.34}
    }
    
    # Cryptocurrency prices
    crypto = {
        'Bitcoin': {'current': 42567.89, 'change': 2.34},
        'Ethereum': {'current': 2567.45, 'change': 3.45},
        'BNB': {'current': 234.56, 'change': -1.23},
        'Cardano': {'current': 0.456, 'change': 4.56}
    }
    
    return {
        'indices': indices,
        'crypto': crypto,
        'last_updated': '2025-06-28 14:30:00'
    }

def generate_peer_performance_data():
    """Generate sample peer performance data"""
    
    locations = ["Singapore", "Hong Kong", "Switzerland", "New York", "London", "Dubai"]
    age_groups = ["25-30", "31-35", "36-40", "41-45", "46-50", "51-55", "56-60", "60+"]
    
    performance_data = []
    
    for location in locations:
        for age_group in age_groups:
            # Generate realistic performance data
            avg_return = random.uniform(4.5, 15.2)
            volatility = random.uniform(8.5, 25.3)
            sharpe_ratio = avg_return / volatility
            
            performance_data.append({
                'location': location,
                'age_group': age_group,
                'avg_return': avg_return,
                'volatility': volatility,
                'sharpe_ratio': sharpe_ratio,
                'sample_size': random.randint(45, 234)
            })
    
    return performance_data

def generate_sector_trends():
    """Generate sector trend data"""
    
    sectors = [
        'Technology', 'Healthcare', 'Financial Services', 'Consumer Discretionary',
        'Consumer Staples', 'Energy', 'Real Estate', 'Utilities', 'Materials',
        'Communication Services', 'Industrials'
    ]
    
    trends = {}
    for sector in sectors:
        trends[sector] = {
            'ytd_return': random.uniform(-15.5, 35.7),
            'momentum_score': random.uniform(1, 10),
            'outlook': random.choice(['Bullish', 'Neutral', 'Bearish']),
            'key_drivers': random.choice([
                'AI Innovation', 'Interest Rates', 'Regulatory Changes',
                'Economic Growth', 'Commodity Prices', 'Consumer Spending'
            ])
        }
    
    return trends
