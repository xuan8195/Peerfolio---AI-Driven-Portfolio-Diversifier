import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Peerfolio - AI Wealth Management",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply dark theme CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #ffffff;
    }
    
    .main-header {
        text-align: center;
        padding: 20px 0;
        color: #E60012;
        font-size: 3rem;
        margin-bottom: 10px;
    }
    
    .sub-header {
        text-align: center;
        color: #888;
        font-weight: 300;
        margin-top: 0;
    }
    
    .metric-container {
        background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
        border: 1px solid #333;
        padding: 1rem;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏦 Peerfolio</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="sub-header">AI-Powered Wealth Management for High-Net-Worth Individuals</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 1.1rem;">Powered by UBS Digital Innovation</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.markdown("### 👤 User Profile")
    
    age = st.sidebar.slider("Age", 25, 65, 35)
    location = st.sidebar.selectbox(
        "Location", 
        ["Singapore", "Hong Kong", "Switzerland", "New York", "London", "Dubai"]
    )
    net_worth = st.sidebar.selectbox(
        "Net Worth (USD)",
        ["$1M - $2.5M", "$2.5M - $5M", "$5M - $10M", "$10M - $25M", "$25M+"]
    )
    investment_style = st.sidebar.selectbox(
        "Investment Preference",
        ["Conservative", "Moderate", "Aggressive", "Crypto-focused", "ESG-focused", "Tech-focused"]
    )
    
    user_profile = {
        'age': age,
        'location': location,
        'net_worth': net_worth,
        'investment_style': investment_style
    }
    
    st.sidebar.markdown("---")
    
    # Navigation
    page = st.sidebar.radio(
        "Select Page",
        ["Portfolio Analysis", "Peer Insights", "AI Recommendations", "Market Intelligence"]
    )
    
    # Main content
    if page == "Portfolio Analysis":
        portfolio_analysis_page(user_profile)
    elif page == "Peer Insights":
        peer_insights_page(user_profile)
    elif page == "AI Recommendations":
        ai_recommendations_page(user_profile)
    elif page == "Market Intelligence":
        market_intelligence_page(user_profile)

def portfolio_analysis_page(user_profile):
    st.markdown("### 📈 Portfolio Upload & Analysis")
    
    upload_method = st.radio(
        "Choose upload method:",
        ["Upload CSV", "Use Sample Data", "Manual Input"]
    )
    
    if upload_method == "Upload CSV":
        uploaded_file = st.file_uploader(
            "Upload your portfolio CSV file",
            type=['csv'],
            help="CSV should contain columns: Symbol, Shares, Purchase_Price, Current_Price"
        )
        
        if uploaded_file:
            try:
                portfolio_df = pd.read_csv(uploaded_file)
                st.success("Portfolio uploaded successfully!")
                display_portfolio_analysis(portfolio_df, user_profile)
            except Exception as e:
                st.error(f"Error reading CSV: {str(e)}")
    
    elif upload_method == "Use Sample Data":
        if st.button("Generate Sample Portfolio"):
            portfolio_df = generate_sample_portfolio(user_profile)
            st.success("Sample portfolio generated!")
            display_portfolio_analysis(portfolio_df, user_profile)
    
    else:  # Manual Input
        st.markdown("#### Manual Portfolio Entry")
        with st.form("portfolio_form"):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                symbol = st.text_input("Symbol (e.g., AAPL)")
            with col2:
                shares = st.number_input("Shares", min_value=0.0, step=0.1)
            with col3:
                purchase_price = st.number_input("Purchase Price", min_value=0.0, step=0.01)
            with col4:
                current_price = st.number_input("Current Price", min_value=0.0, step=0.01)
            
            if st.form_submit_button("Add to Portfolio"):
                if symbol and shares > 0:
                    if 'manual_portfolio' not in st.session_state:
                        st.session_state.manual_portfolio = []
                    
                    st.session_state.manual_portfolio.append({
                        'Symbol': symbol.upper(),
                        'Shares': shares,
                        'Purchase_Price': purchase_price,
                        'Current_Price': current_price
                    })
                    
                    st.success(f"Added {symbol} to portfolio!")
                    st.rerun()
        
        if 'manual_portfolio' in st.session_state and st.session_state.manual_portfolio:
            portfolio_df = pd.DataFrame(st.session_state.manual_portfolio)
            st.dataframe(portfolio_df, use_container_width=True)
            
            if st.button("Analyze Portfolio"):
                display_portfolio_analysis(portfolio_df, user_profile)

def generate_sample_portfolio(user_profile):
    """Generate sample portfolio based on user profile"""
    if user_profile['investment_style'] == 'Tech-focused':
        stocks = [
            {'Symbol': 'AAPL', 'Shares': 100, 'Purchase_Price': 150.00, 'Current_Price': 175.43},
            {'Symbol': 'MSFT', 'Shares': 50, 'Purchase_Price': 320.00, 'Current_Price': 384.52},
            {'Symbol': 'GOOGL', 'Shares': 30, 'Purchase_Price': 125.00, 'Current_Price': 138.76},
            {'Symbol': 'NVDA', 'Shares': 25, 'Purchase_Price': 380.00, 'Current_Price': 459.75},
            {'Symbol': 'TSLA', 'Shares': 20, 'Purchase_Price': 220.00, 'Current_Price': 248.87},
        ]
    else:
        stocks = [
            {'Symbol': 'AAPL', 'Shares': 100, 'Purchase_Price': 150.00, 'Current_Price': 175.43},
            {'Symbol': 'MSFT', 'Shares': 50, 'Purchase_Price': 320.00, 'Current_Price': 384.52},
            {'Symbol': 'JNJ', 'Shares': 80, 'Purchase_Price': 155.00, 'Current_Price': 159.87},
            {'Symbol': 'UNH', 'Shares': 30, 'Purchase_Price': 450.00, 'Current_Price': 524.32},
            {'Symbol': 'V', 'Shares': 60, 'Purchase_Price': 220.00, 'Current_Price': 241.65},
            {'Symbol': 'JPM', 'Shares': 70, 'Purchase_Price': 140.00, 'Current_Price': 154.76},
        ]
    
    return pd.DataFrame(stocks)

def display_portfolio_analysis(portfolio_df, user_profile):
    """Display comprehensive portfolio analysis"""
    
    # Calculate metrics
    portfolio_df['Market_Value'] = portfolio_df['Shares'] * portfolio_df['Current_Price']
    portfolio_df['Cost_Basis'] = portfolio_df['Shares'] * portfolio_df['Purchase_Price']
    portfolio_df['P&L'] = portfolio_df['Market_Value'] - portfolio_df['Cost_Basis']
    portfolio_df['Return_%'] = (portfolio_df['P&L'] / portfolio_df['Cost_Basis']) * 100
    
    total_value = portfolio_df['Market_Value'].sum()
    total_cost = portfolio_df['Cost_Basis'].sum()
    total_return = ((total_value - total_cost) / total_cost) * 100
    
    st.markdown("---")
    st.markdown("### 📊 Portfolio Analysis Results")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Value", f"${total_value:,.0f}", f"{total_return:.1f}%")
    
    with col2:
        diversification_score = calculate_diversification_score(portfolio_df)
        st.metric("Diversification Score", f"{diversification_score:.1f}/10", "Higher is better")
    
    with col3:
        risk_level = assess_risk_level(portfolio_df)
        st.metric("Risk Level", risk_level, "Assessment")
    
    with col4:
        esg_score = calculate_esg_score(portfolio_df)
        st.metric("ESG Score", f"{esg_score:.1f}/10", "Sustainability")
    
    # Portfolio composition
    st.markdown("### 💼 Portfolio Composition")
    st.dataframe(portfolio_df[['Symbol', 'Shares', 'Market_Value', 'Return_%']], use_container_width=True)
    
    # Recommendations
    st.markdown("### 💡 AI Recommendations")
    recommendations = generate_recommendations(portfolio_df, user_profile, total_value)
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"**{i}.** {rec}")

def calculate_diversification_score(portfolio_df):
    """Calculate portfolio diversification score"""
    num_holdings = len(portfolio_df)
    if num_holdings >= 10:
        return 8.5 + random.uniform(-1, 1.5)
    elif num_holdings >= 5:
        return 6.0 + random.uniform(-1, 2)
    else:
        return 3.0 + random.uniform(-1, 2)

def assess_risk_level(portfolio_df):
    """Assess portfolio risk level"""
    tech_symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'TSLA', 'META']
    tech_count = len([s for s in portfolio_df['Symbol'] if s in tech_symbols])
    total_count = len(portfolio_df)
    
    if tech_count / total_count > 0.6:
        return "High"
    elif tech_count / total_count > 0.3:
        return "Moderate"
    else:
        return "Low"

def calculate_esg_score(portfolio_df):
    """Calculate ESG score"""
    esg_friendly = ['MSFT', 'AAPL', 'JNJ', 'UNH', 'V']
    esg_count = len([s for s in portfolio_df['Symbol'] if s in esg_friendly])
    total_count = len(portfolio_df)
    
    base_score = 5.0
    esg_bonus = (esg_count / total_count) * 3.0
    return min(10.0, base_score + esg_bonus + random.uniform(-0.5, 0.5))

def generate_recommendations(portfolio_df, user_profile, total_value):
    """Generate personalized recommendations"""
    recommendations = []
    
    num_holdings = len(portfolio_df)
    if num_holdings < 5:
        recommendations.append(
            "🎯 **Increase Diversification**: Add 3-5 more holdings to reduce single-stock risk"
        )
    
    tech_symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'TSLA', 'META']
    tech_count = len([s for s in portfolio_df['Symbol'] if s in tech_symbols])
    
    if tech_count / num_holdings > 0.5:
        recommendations.append(
            "⚖️ **Reduce Tech Concentration**: Consider adding holdings from other sectors like healthcare, finance, or consumer goods"
        )
    
    age = user_profile['age']
    if age < 35:
        recommendations.append(
            "🚀 **Growth Focus**: Your young age allows for higher growth allocation - consider emerging technology stocks"
        )
    elif age > 50:
        recommendations.append(
            "🛡️ **Add Defensive Assets**: Consider dividend-paying stocks and bonds for stability"
        )
    
    if user_profile['investment_style'] == 'ESG-focused':
        recommendations.append(
            "🌱 **ESG Enhancement**: Look into clean energy ETFs and sustainable companies to align with your values"
        )
    
    if '$10M' in user_profile['net_worth'] or '$25M' in user_profile['net_worth']:
        recommendations.append(
            "💎 **Alternative Investments**: Consider private equity, real estate, or hedge funds for ultra-high-net-worth diversification"
        )
    
    if not recommendations:
        recommendations.append(
            "✅ **Well-Balanced Portfolio**: Your portfolio shows good diversification and risk management"
        )
    
    return recommendations

def peer_insights_page(user_profile):
    """Display peer insights and comparisons"""
    st.markdown("### 👥 Peer Portfolio Insights")
    st.markdown("Discover how similar HNWIs are investing their wealth")
    
    # Generate mock peer data
    peers_found = random.randint(25, 75)
    avg_return = random.uniform(7.5, 12.3)
    popular_sector = random.choice(["Technology", "Healthcare", "Financial Services"])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Similar Peers Found", peers_found)
    
    with col2:
        st.metric("Average Return", f"{avg_return:.1f}%")
    
    with col3:
        st.metric("Most Popular Sector", popular_sector)
    
    # Peer strategies
    st.markdown("#### 📈 Popular Investment Strategies")
    
    strategies = [
        "Growth-Focused Tech Portfolio",
        "Diversified Blue-Chip Holdings", 
        "ESG-Sustainable Investments",
        "International Market Focus",
        "Real Estate Heavy Allocation"
    ]
    
    strategy_data = []
    for strategy in strategies:
        users = random.randint(15, 45)
        performance = random.uniform(6.5, 14.2)
        strategy_data.append({
            'Strategy': strategy,
            'Users': users,
            'Avg Return': f"{performance:.1f}%"
        })
    
    st.dataframe(pd.DataFrame(strategy_data), use_container_width=True)
    
    # Top performing peers
    st.markdown("#### 🏆 Top Performing Peer Insights")
    
    insights = [
        f"🌱 **ESG Integration**: 67% of top performers include ESG criteria in their investments",
        f"🏠 **Real Estate Allocation**: Average 12% allocation to REITs and direct property",
        f"🌏 **International Exposure**: 28% average allocation to non-US markets",
        f"💎 **Alternative Investments**: 15% in private equity, hedge funds, or crypto",
        f"⚖️ **Rebalancing**: Quarterly rebalancing is the most common practice"
    ]
    
    for insight in insights:
        st.markdown(insight)

def ai_recommendations_page(user_profile):
    """AI-powered recommendations page"""
    st.markdown("### 🤖 AI-Powered Investment Recommendations")
    
    st.markdown("#### 💎 Personalized Investment Suggestions")
    
    # Generate recommendations based on user profile
    age = user_profile['age']
    style = user_profile['investment_style']
    net_worth = user_profile['net_worth']
    
    recommendations = []
    
    if age < 35:
        recommendations.extend([
            {
                'category': 'Growth Opportunities',
                'title': 'Emerging Technology Stocks',
                'description': 'Focus on AI, robotics, and clean energy companies',
                'rationale': 'Young age allows for higher risk tolerance and long-term growth focus'
            },
            {
                'category': 'Risk Management',
                'title': 'Dollar-Cost Averaging',
                'description': 'Invest systematically over time to reduce timing risk',
                'rationale': 'Systematic investing reduces emotional decision-making'
            }
        ])
    
    if style == 'ESG-focused':
        recommendations.append({
            'category': 'Sustainable Investing',
            'title': 'Clean Energy Portfolio',
            'description': 'Allocate 20-30% to renewable energy and sustainable companies',
            'rationale': 'ESG investments show strong long-term performance and align with values'
        })
    
    if style == 'Tech-focused':
        recommendations.append({
            'category': 'Technology Allocation',
            'title': 'AI and Semiconductor Exposure',
            'description': 'Increase exposure to artificial intelligence and chip manufacturers',
            'rationale': 'Technology continues to drive economic growth and innovation'
        })
    
    if '$10M' in net_worth or '$25M' in net_worth:
        recommendations.extend([
            {
                'category': 'Alternative Investments',
                'title': 'Private Equity Allocation',
                'description': 'Consider 10-15% allocation to private equity or hedge funds',
                'rationale': 'High-net-worth individuals benefit from alternative asset diversification'
            },
            {
                'category': 'Tax Optimization',
                'title': 'Tax-Advantaged Structures',
                'description': 'Explore family offices, trusts, or offshore structures',
                'rationale': 'Sophisticated tax planning can significantly enhance after-tax returns'
            }
        ])
    
    # Display recommendations
    for rec in recommendations:
        with st.expander(f"📊 {rec['category']}"):
            st.markdown(f"**{rec['title']}**")
            st.markdown(f"*{rec['description']}*")
            st.markdown(f"**Rationale:** {rec['rationale']}")
    
    # AI Chat Interface
    st.markdown("#### 💬 Ask Our AI Wealth Advisor")
    
    user_question = st.text_input(
        "Ask a question about your portfolio or investment strategy:",
        placeholder="e.g., Should I increase my crypto allocation? What about ESG investments?"
    )
    
    if user_question and st.button("Ask AI Advisor"):
        # Simple keyword-based responses
        response = generate_ai_response(user_question, user_profile)
        st.markdown("#### 🎯 AI Advisor Response")
        st.markdown(response)

def generate_ai_response(question, user_profile):
    """Generate AI-style responses to user questions"""
    question_lower = question.lower()
    age = user_profile['age']
    
    if 'crypto' in question_lower or 'bitcoin' in question_lower:
        if age < 40:
            return """
            🚀 **Cryptocurrency Recommendation**
            
            Given your age and risk profile, a 5-10% allocation to cryptocurrency could be appropriate:
            
            • Start with established cryptocurrencies like Bitcoin and Ethereum
            • Use dollar-cost averaging for entry
            • Never exceed 10% of total portfolio
            • Consider crypto as high-risk, high-reward allocation
            
            Remember: Only invest what you can afford to lose completely.
            """
        else:
            return """
            🛡️ **Conservative Crypto Approach**
            
            For your age group, a cautious approach is recommended:
            
            • Limit to 2-5% allocation if any
            • Focus on Bitcoin as "digital gold"
            • Consider crypto ETFs for easier management
            • Prioritize traditional assets for wealth preservation
            """
    
    elif 'esg' in question_lower or 'sustainable' in question_lower:
        return """
        🌱 **ESG Investment Strategy**
        
        ESG investing has evolved significantly:
        
        • ESG funds often show comparable or better returns
        • Start with 20-30% ESG allocation
        • Focus on companies with strong environmental practices
        • Consider clean energy and sustainable technology
        
        ESG integration aligns values with wealth building goals.
        """
    
    elif 'risk' in question_lower:
        return f"""
        ⚖️ **Risk Management for Age {age}**
        
        Risk guidelines for your profile:
        
        • Equity allocation: {100 - age}% (traditional rule of thumb)
        • Diversify across 15+ holdings minimum
        • Regular quarterly rebalancing
        • Maintain 6-month emergency fund
        
        Take only the risk necessary to meet your goals.
        """
    
    else:
        return """
        🎯 **General Investment Guidance**
        
        Key principles for wealth building:
        
        • Start early, invest consistently
        • Diversify across asset classes and geographies
        • Keep costs low with index funds
        • Stay disciplined during market volatility
        • Focus on long-term goals
        
        Time in the market beats timing the market!
        """

def market_intelligence_page(user_profile):
    """Market intelligence and data page"""
    st.markdown("### 📊 Market Intelligence Dashboard")
    
    # Market overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Major Market Indices")
        
        indices = [
            ('S&P 500', 4567.89, 0.75),
            ('NASDAQ', 14234.56, 1.23),
            ('Dow Jones', 35678.90, -0.45),
            ('FTSE 100', 7456.78, 0.34)
        ]
        
        for name, value, change in indices:
            st.metric(name, f"{value:.2f}", f"{change:+.2f}%")
    
    with col2:
        st.markdown("#### ₿ Cryptocurrency Market")
        
        crypto = [
            ('Bitcoin', 42567.89, 2.34),
            ('Ethereum', 2567.45, 3.45),
            ('BNB', 234.56, -1.23),
            ('Cardano', 0.456, 4.56)
        ]
        
        for name, value, change in crypto:
            st.metric(name, f"${value:,.2f}", f"{change:+.2f}%")
    
    # Market insights
    st.markdown("#### 🔮 AI Market Insights")
    
    insights = [
        "Technology sector showing strong momentum with AI companies leading gains",
        "Emerging markets presenting opportunities amid global economic shifts", 
        "ESG investments gaining traction among institutional investors",
        "Cryptocurrency market showing signs of maturation and stability",
        "Real estate markets adjusting to changing interest rate environment"
    ]
    
    for insight in insights:
        st.markdown(f"• {insight}")
    
    # Sector performance
    st.markdown("#### 📊 Sector Performance (YTD)")
    
    sectors = [
        ('Technology', 15.2, 'Bullish'),
        ('Healthcare', 8.7, 'Neutral'),
        ('Financial Services', 12.1, 'Bullish'),
        ('Energy', -5.3, 'Bearish'),
        ('Real Estate', 3.4, 'Neutral'),
        ('Consumer Discretionary', 9.8, 'Neutral')
    ]
    
    sector_df = pd.DataFrame(sectors, columns=['Sector', 'YTD Return %', 'Outlook'])
    st.dataframe(sector_df, use_container_width=True)

if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; padding: 20px;'>"
    "🏦 Peerfolio - Powered by UBS Digital Innovation | "
    "© 2025 UBS Group AG. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
