# 🏦 Peerfolio - AI-Driven Wealth Management Platform

A sophisticated AI-powered wealth management platform designed specifically for high-net-worth individuals (HNWIs). Built with Streamlit and featuring a professional dark theme.

## 🌟 Features Overview

### 1. **Portfolio Analysis Engine**
- **Smart Portfolio Reading**: Upload CSV files or input holdings manually
- **AI-Powered Risk Assessment**: Automatic concentration risk detection
- **Diversification Scoring**: Advanced algorithms measure portfolio balance
- **ESG Integration**: Environmental, Social, and Governance scoring
- **Performance Visualization**: Interactive charts and real-time metrics

### 2. **Peer Intelligence Network**
- **Smart Matching**: Find similar HNWIs by age, location, and net worth
- **Strategy Benchmarking**: Compare performance against similar investors
- **Trend Discovery**: Identify popular investment strategies among peers
- **Geographic Insights**: Regional investment preferences and performance

### 3. **AI Investment Advisor**
- **Personalized Recommendations**: Tailored advice based on your profile
- **Conversational Interface**: Ask questions about portfolio strategy
- **Risk Management**: Proactive identification of portfolio risks
- **Market Intelligence**: Real-time insights and trend analysis

### 4. **Professional Interface**
- **UBS-Branded Design**: Professional dark theme with UBS red accents
- **Responsive Layout**: Works seamlessly on desktop and tablet
- **Interactive Dashboards**: Real-time data visualization
- **Intuitive Navigation**: Easy-to-use interface for complex analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or later
- pip package manager

### Installation Options

#### Option 1: Automatic Setup (Windows)
```bash
# Double-click start.bat or run in Command Prompt
start.bat
```

#### Option 2: Automatic Setup (Mac/Linux)
```bash
# Make executable and run
chmod +x start.sh
./start.sh
```

#### Option 3: Manual Setup
```bash
# 1. Install dependencies
pip install streamlit pandas numpy plotly matplotlib seaborn scikit-learn python-dotenv yfinance requests altair

# 2. Run the application
streamlit run app_simple.py

# OR run the full-featured version
streamlit run app.py
```

### First Time Setup
1. **Open Browser**: Navigate to `http://localhost:8501`
2. **Set Profile**: Configure your age, location, net worth, and investment style
3. **Upload Portfolio**: Use sample data or upload your own CSV file
4. **Explore Features**: Navigate through the different sections

## 📁 Project Structure

```
Peerfolio/
├── app.py                  # Main application (full-featured)
├── app_simple.py          # Simplified version (fewer dependencies)
├── requirements.txt       # Python dependencies
├── start.bat             # Windows startup script
├── start.sh              # Mac/Linux startup script
├── README.md             # This file
├── DOCUMENTATION.md      # Comprehensive documentation
├── demo.py               # Interactive demo scenarios
├── .env.example          # Environment variables template
├── config/
│   ├── __init__.py
│   ├── theme.py          # Dark theme styling
│   └── settings.py       # Application configuration
├── utils/
│   ├── __init__.py
│   ├── portfolio_analyzer.py    # Portfolio analysis engine
│   ├── peer_matcher.py          # Peer matching algorithm
│   ├── ai_advisor.py            # AI recommendation system
│   └── data_generator.py        # Sample data generation
└── data/
    └── sample_portfolio.csv     # Example portfolio data
```

## 💼 Sample Portfolio Format

Your CSV file should have these columns:

```csv
Symbol,Shares,Purchase_Price,Current_Price
AAPL,500,150.25,175.43
MSFT,300,320.50,384.52
GOOGL,200,125.75,138.76
AMZN,150,135.20,146.89
```

## Technology Stack

- **Frontend**: Streamlit with custom dark theme
- **AI/ML**: OpenAI GPT-4, scikit-learn, pandas
- **Visualization**: Plotly, Matplotlib
- **Data**: yfinance for market data
