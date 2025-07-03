import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="Peerfolio - AI Wealth Management",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply modern classic theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 30px 0 20px 0;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: #ffffff;
        font-size: 3.5rem;
        font-weight: 700;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 25px 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        text-align: center;
        color: #64748b;
        font-weight: 400;
        font-size: 1.4rem;
        margin: -1rem 0 2rem 0;
        letter-spacing: 0.01em;
    }
    
    .metric-container {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid #e2e8f0;
        padding: 1.5rem;
        border-radius: 16px;
        margin: 15px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .metric-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15);
    }
    
    .analysis-card {
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #e2e8f0;
        padding: 25px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .analysis-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    }
    
    .performance-metric {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .performance-metric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .performance-metric:hover::before {
        opacity: 1;
    }
    
    .performance-metric:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
    }
    
    .growth-metric {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .growth-metric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .growth-metric:hover::before {
        opacity: 1;
    }
    
    .growth-metric:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(16, 185, 129, 0.4);
    }
    
    .risk-metric {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(239, 68, 68, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .risk-metric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .risk-metric:hover::before {
        opacity: 1;
    }
    
    .risk-metric:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(239, 68, 68, 0.4);
    }
    
    .esg-metric {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .esg-metric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .esg-metric:hover::before {
        opacity: 1;
    }
    
    .esg-metric:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(245, 158, 11, 0.4);
    }
    
    .portfolio-header {
        background: linear-gradient(135deg, #1e293b 0%, #475569 100%);
        color: white;
        padding: 35px 25px;
        border-radius: 25px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(30, 41, 59, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .portfolio-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.05) 0%, transparent 50%);
    }
    
    .recommendation-card {
        background: grey;
        border-left: 5px solid darkgrey;
        border-radius: 15px;
        padding: 20px 25px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .recommendation-card:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        border-left-color: darkgrey;
    }
    
    .chart-container {
        background: #2f2f2f;
        color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: none;
    }
    
    /* Enhance sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
    }
    
    /* Modern button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    }
    
    /* Enhanced metric cards typography */
    .performance-metric h3, .growth-metric h3, .risk-metric h3, .esg-metric h3 {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 8px;
        opacity: 0.9;
    }
    
    .performance-metric h2, .growth-metric h2, .risk-metric h2, .esg-metric h2 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 10px 0;
        letter-spacing: -0.02em;
    }
    
    .performance-metric p, .growth-metric p, .risk-metric p, .esg-metric p {
        font-size: 0.9rem;
        font-weight: 500;
        margin-top: 8px;
        opacity: 0.9;
    }
    
    /* Enhanced section headers */
    h3 {
        color: #1e293b;
        font-weight: 600;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Refined dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header with elegant styling
    st.markdown('''
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); margin: -1rem -1rem 2rem -1rem; border-radius: 0 0 30px 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h1 style="color: white; font-size: 3.5rem; font-weight: 700; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">💎 Peerfolio</h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.4rem; margin: 0.5rem 0 0 0; font-weight: 400;">AI-Powered Wealth Management Platform</p>
        <p style="color: rgba(255,255,255,0.7); font-size: 1rem; margin: 0.5rem 0 0 0;">Designed for High-Net-Worth Individuals</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Sidebar with enhanced styling
    st.sidebar.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 15px; margin-bottom: 1rem; text-align: center;">
        <h3 style="color: white; margin: 0; font-weight: 600;">👤 User Profile</h3>
    </div>
    ''', unsafe_allow_html=True)
    
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
    
    st.sidebar.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 15px; margin: 1rem 0; text-align: center;">
        <h3 style="color: white; margin: 0; font-weight: 600;">🧭 Navigation</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    # Navigation
    page = st.sidebar.radio(
        "",
        ["Portfolio Analysis", "Peer Insights", "AI Recommendations", "Market Intelligence"],
        label_visibility="collapsed"
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
    st.markdown('''
    <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 2rem; border-radius: 20px; margin: 1rem 0; text-align: center; box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);">
        <h2 style="color: white; margin: 0; font-weight: 600; font-size: 2rem;">📈 Portfolio Analysis</h2>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 1.1rem;">Upload and analyze your investment portfolio</p>
    </div>
    ''', unsafe_allow_html=True)
    
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
    """Display comprehensive portfolio analysis with enhanced UI and graphs"""
    
    # Calculate metrics
    portfolio_df['Market_Value'] = portfolio_df['Shares'] * portfolio_df['Current_Price']
    portfolio_df['Cost_Basis'] = portfolio_df['Shares'] * portfolio_df['Purchase_Price']
    portfolio_df['P&L'] = portfolio_df['Market_Value'] - portfolio_df['Cost_Basis']
    portfolio_df['Return_%'] = (portfolio_df['P&L'] / portfolio_df['Cost_Basis']) * 100
    portfolio_df['Weight_%'] = (portfolio_df['Market_Value'] / portfolio_df['Market_Value'].sum()) * 100
    
    total_value = portfolio_df['Market_Value'].sum()
    total_cost = portfolio_df['Cost_Basis'].sum()
    total_return = ((total_value - total_cost) / total_cost) * 100
    total_pl = total_value - total_cost
    
    # Portfolio Header
    st.markdown(f'''
    <div class="portfolio-header">
        <h2>📊 Portfolio Analysis Results</h2>
        <p style="font-size: 1.2em; opacity: 0.9;">Generated on {datetime.now().strftime("%B %d, %Y")}</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Enhanced Key Metrics with styled cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="performance-metric">
            <h3>💰 Total Value</h3>
            <h2>${total_value:,.0f}</h2>
            <p style="color: {'#34d399' if total_return > 0 else '#f87171'};">
                {'+' if total_return > 0 else ''}{total_return:.1f}% • ${total_pl:+,.0f}
            </p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        diversification_score = calculate_diversification_score(portfolio_df)
        st.markdown(f'''
        <div class="growth-metric">
            <h3>📈 Diversification</h3>
            <h2>{diversification_score:.1f}/10</h2>
            <p>Higher is better</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        risk_level = assess_risk_level(portfolio_df)
        risk_color = "#f87171" if risk_level == "High" else "#fbbf24" if risk_level == "Moderate" else "#34d399"
        st.markdown(f'''
        <div class="risk-metric">
            <h3>⚖️ Risk Level</h3>
            <h2 style="color: {risk_color};">{risk_level}</h2>
            <p>Assessment</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        esg_score = calculate_esg_score(portfolio_df)
        st.markdown(f'''
        <div class="esg-metric">
            <h3>🌱 ESG Score</h3>
            <h2>{esg_score:.1f}/10</h2>
            <p>Sustainability</p>
        </div>
        ''', unsafe_allow_html=True)
    
    # Portfolio composition charts
    st.markdown("---")
    
    # Row 1: Portfolio Composition and Performance
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("💼 Portfolio Composition")
        
        # Pie chart for portfolio allocation
        fig_pie = px.pie(
            portfolio_df, 
            values='Market_Value', 
            names='Symbol',
            title="Portfolio Allocation by Market Value",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            showlegend=True,
            height=400,
            title_x=0.5
        )
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=12,
            marker=dict(line=dict(color='#ffffff', width=2))
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📊 Individual Stock Performance")
        
        # Bar chart for individual stock returns
        fig_bar = px.bar(
            portfolio_df, 
            x='Symbol', 
            y='Return_%',
            title="Individual Stock Returns (%)",
            color='Return_%',
            color_continuous_scale=['#ef4444', '#fbbf24', '#10b981'],
            text='Return_%'
        )
        fig_bar.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            xaxis_title="Stock Symbol",
            yaxis_title="Return (%)",
            height=400,
            title_x=0.5,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            )
        )
        fig_bar.update_traces(
            texttemplate='%{text:.1f}%', 
            textposition='outside',
            textfont_color='#1e293b'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 2: Portfolio Weight Distribution and P&L Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("⚖️ Portfolio Weight Distribution")
        
        # Horizontal bar chart for weights
        fig_weight = px.bar(
            portfolio_df.sort_values('Weight_%', ascending=True), 
            x='Weight_%', 
            y='Symbol',
            title="Portfolio Weight Distribution (%)",
            orientation='h',
            color='Weight_%',
            color_continuous_scale='Blues',
            text='Weight_%'
        )
        fig_weight.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            xaxis_title="Weight (%)",
            yaxis_title="Stock Symbol",
            height=400,
            title_x=0.5,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            )
        )
        fig_weight.update_traces(
            texttemplate='%{text:.1f}%', 
            textposition='outside',
            textfont_color='#1e293b'
        )
        st.plotly_chart(fig_weight, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("💹 Profit & Loss Analysis")
        
        # Waterfall chart for P&L
        fig_pl = go.Figure(go.Waterfall(
            name="P&L",
            orientation="v",
            measure=["relative"] * len(portfolio_df),
            x=portfolio_df['Symbol'],
            y=portfolio_df['P&L'],
            text=portfolio_df['P&L'].apply(lambda x: f"${x:+,.0f}"),
            textposition="outside",
            textfont=dict(color='#1e293b'),
            connector={"line": {"color": "#64748b"}},
            increasing={"marker": {"color": "#10b981"}},
            decreasing={"marker": {"color": "#ef4444"}},
        ))
        fig_pl.update_layout(
            title="Profit & Loss by Stock",
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            xaxis_title="Stock Symbol",
            yaxis_title="P&L ($)",
            height=400,
            title_x=0.5,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            )
        )
        st.plotly_chart(fig_pl, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 3: Risk-Return Analysis and Market Value Comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("� Risk-Return Analysis")
        
        # Scatter plot for risk vs return (using volatility proxy)
        portfolio_df['Volatility_Proxy'] = portfolio_df['Return_%'].abs() + np.random.uniform(5, 15, len(portfolio_df))
        
        fig_scatter = px.scatter(
            portfolio_df, 
            x='Volatility_Proxy', 
            y='Return_%',
            size='Market_Value',
            color='Symbol',
            title="Risk vs Return Analysis",
            labels={'Volatility_Proxy': 'Risk (Volatility Proxy)', 'Return_%': 'Return (%)'},
            hover_data=['Market_Value'],
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_scatter.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            height=400,
            title_x=0.5,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            )
        )
        fig_scatter.update_traces(
            marker=dict(
                line=dict(color='#ffffff', width=1),
                opacity=0.8
            )
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("💰 Market Value vs Cost Basis")
        
        # Comparison chart
        comparison_df = portfolio_df.melt(
            id_vars=['Symbol'], 
            value_vars=['Market_Value', 'Cost_Basis'],
            var_name='Type', 
            value_name='Value'
        )
        
        fig_comparison = px.bar(
            comparison_df, 
            x='Symbol', 
            y='Value',
            color='Type',
            title="Market Value vs Cost Basis",
            barmode='group',
            color_discrete_map={'Market_Value': '#10b981', 'Cost_Basis': '#3b82f6'}
        )
        fig_comparison.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            xaxis_title="Stock Symbol",
            yaxis_title="Value ($)",
            height=400,
            title_x=0.5,
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            legend=dict(
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='rgba(0,0,0,0.1)',
                borderwidth=1
            )
        )
        st.plotly_chart(fig_comparison, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 4: Sector Analysis and Portfolio Performance History
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("🏢 Sector Analysis")
        
        # Sector allocation chart
        sector_data = create_sector_analysis_chart(portfolio_df)
        
        fig_sector = px.pie(
            sector_data,
            values='Market_Value',
            names='Sector',
            title="Portfolio Allocation by Sector",
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        fig_sector.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            height=400,
            title_x=0.5
        )
        fig_sector.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=12,
            marker=dict(line=dict(color='#ffffff', width=2))
        )
        st.plotly_chart(fig_sector, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📅 Portfolio Performance History")
        
        # Historical performance chart
        perf_data = create_portfolio_performance_history(portfolio_df)
        
        fig_history = px.line(
            perf_data.reset_index(),
            x='index',
            y='Portfolio',
            title="Portfolio Performance Over Time",
            labels={'index': 'Date', 'Portfolio': 'Portfolio Value ($)'},
            color_discrete_sequence=['#3b82f6']
        )
        fig_history.update_layout(
            plot_bgcolor='rgba(255,255,255,0)',
            paper_bgcolor='rgba(255,255,255,0)',
            font_color='#1e293b',
            title_font_size=18,
            title_font_weight=600,
            height=400,
            title_x=0.5,
            xaxis_title="Date",
            yaxis_title="Portfolio Value ($)",
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                color='#64748b'
            )
        )
        fig_history.update_traces(
            line=dict(width=3, color='#3b82f6'),
            fill='tonexty',
            fillcolor='rgba(59, 130, 246, 0.1)'
        )
        st.plotly_chart(fig_history, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Portfolio Table
    st.markdown("---")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📋 Detailed Portfolio Holdings")
    
    # Format the dataframe for better display
    display_df = portfolio_df.copy()
    display_df['Market_Value'] = display_df['Market_Value'].apply(lambda x: f"${x:,.2f}")
    display_df['Cost_Basis'] = display_df['Cost_Basis'].apply(lambda x: f"${x:,.2f}")
    display_df['P&L'] = display_df['P&L'].apply(lambda x: f"${x:+,.2f}")
    display_df['Return_%'] = display_df['Return_%'].apply(lambda x: f"{x:+.2f}%")
    display_df['Weight_%'] = display_df['Weight_%'].apply(lambda x: f"{x:.2f}%")
    display_df['Current_Price'] = display_df['Current_Price'].apply(lambda x: f"${x:.2f}")
    display_df['Purchase_Price'] = display_df['Purchase_Price'].apply(lambda x: f"${x:.2f}")
    
    # Rename columns for better display
    display_df = display_df.rename(columns={
        'Symbol': 'Stock',
        'Shares': 'Shares',
        'Purchase_Price': 'Purchase Price',
        'Current_Price': 'Current Price',
        'Market_Value': 'Market Value',
        'Cost_Basis': 'Cost Basis',
        'P&L': 'P&L',
        'Return_%': 'Return %',
        'Weight_%': 'Weight %'
    })
    
    st.dataframe(
        display_df[['Stock', 'Shares', 'Purchase Price', 'Current Price', 'Market Value', 'Cost Basis', 'P&L', 'Return %', 'Weight %']], 
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Recommendations
    st.markdown("---")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("🤖 AI-Powered Investment Recommendations")
    
    recommendations = generate_recommendations(portfolio_df, user_profile, total_value)
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f'''
        <div class="recommendation-card">
            <strong>{i}.</strong> {rec}
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Portfolio Performance History
    st.markdown("---")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Portfolio Performance History")
    
    # Create and display the portfolio performance history chart
    perf_history_df = create_portfolio_performance_history(portfolio_df)
    
    fig_history = px.line(
        perf_history_df,
        x=perf_history_df.index,
        y=perf_history_df.columns,
        title="Portfolio Performance Over Time",
        labels={'value': 'Portfolio Value ($)', 'variable': 'Asset'},
        template="plotly_dark"
    )
    fig_history.update_layout(
        xaxis_title="Date",
        yaxis_title="Value ($)",
        legend_title="Assets",
        height=400
    )
    st.plotly_chart(fig_history, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
            "🎯 **Increase Diversification**: Add 3-5 more holdings across different sectors to reduce single-stock risk and improve portfolio stability."
        )
    
    # Check sector concentration
    tech_symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'TSLA', 'META', 'AMZN']
    tech_count = len([s for s in portfolio_df['Symbol'] if s in tech_symbols])
    
    if tech_count / num_holdings > 0.5:
        recommendations.append(
            "⚖️ **Reduce Tech Concentration**: Consider adding holdings from defensive sectors like healthcare (JNJ, PFE), consumer staples (PG, KO), or utilities (NEE, SO) to balance your portfolio."
        )
    
    # Age-based recommendations
    age = user_profile['age']
    if age < 35:
        recommendations.append(
            "🚀 **Growth Focus**: At your age, consider increasing allocation to growth stocks and emerging markets for long-term wealth building."
        )
    elif age > 50:
        recommendations.append(
            "🛡️ **Capital Preservation**: Consider increasing allocation to dividend-paying stocks and bonds to preserve capital as you approach retirement."
        )
    
    # Check for high-risk positions
    high_risk_positions = portfolio_df[portfolio_df['Weight_%'] > 25]
    if not high_risk_positions.empty:
        recommendations.append(
            f"⚠️ **Position Sizing**: {high_risk_positions.iloc[0]['Symbol']} represents {high_risk_positions.iloc[0]['Weight_%']:.1f}% of your portfolio. Consider reducing to under 20% to manage risk."
        )
    
    # ESG recommendations
    if user_profile['investment_style'] == 'ESG-focused':
        recommendations.append(
            "🌱 **ESG Enhancement**: Consider adding ESG-focused ETFs like VTSAX or individual stocks with strong sustainability ratings to align with your values."
        )
    
    # Performance-based recommendations
    poor_performers = portfolio_df[portfolio_df['Return_%'] < -10]
    if not poor_performers.empty:
        recommendations.append(
            f"📉 **Review Underperformers**: {', '.join(poor_performers['Symbol'].tolist())} are down significantly. Consider if these align with your long-term thesis or if rebalancing is needed."
        )
    
    # Net worth based recommendations
    if '$25M+' in user_profile['net_worth']:
        recommendations.append(
            "💎 **Alternative Investments**: With your high net worth, consider adding alternative investments like REITs, commodities, or private equity for further diversification."
        )
    
    # Location-based recommendations
    if user_profile['location'] == 'Singapore':
        recommendations.append(
            "🌏 **Regional Exposure**: Consider adding Singapore REITs or Asian market ETFs to capitalize on regional growth opportunities."
        )
    
    if not recommendations:
        recommendations.append(
            "✅ **Well-Balanced Portfolio**: Your portfolio shows good diversification and risk management. Continue monitoring and rebalancing quarterly."
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
    """Generate simple text responses to user questions"""
    question_lower = question.lower()
    age = user_profile['age']
    
    if 'crypto' in question_lower or 'bitcoin' in question_lower:
        if age < 40:
            return (
                "Cryptocurrency Recommendation:\n"
                "Given your age and risk profile, a 5-10% allocation to cryptocurrency could be appropriate.\n"
                "- Start with established cryptocurrencies like Bitcoin and Ethereum\n"
                "- Use dollar-cost averaging for entry\n"
                "- Never exceed 10% of total portfolio\n"
                "- Consider crypto as high-risk, high-reward allocation\n"
                "Remember: Only invest what you can afford to lose completely."
            )
        else:
            return (
                "Conservative Crypto Approach:\n"
                "For your age group, a cautious approach is recommended.\n"
                "- Limit to 2-5% allocation if any\n"
                "- Focus on Bitcoin as digital gold\n"
                "- Consider crypto ETFs for easier management\n"
                "- Prioritize traditional assets for wealth preservation"
            )
    elif 'esg' in question_lower or 'sustainable' in question_lower:
        return (
            "ESG Investment Strategy:\n"
            "ESG investing has evolved significantly.\n"
            "- ESG funds often show comparable or better returns\n"
            "- Start with 20-30% ESG allocation\n"
            "- Focus on companies with strong environmental practices\n"
            "- Consider clean energy and sustainable technology"
        )
    elif 'risk' in question_lower:
        return (
            f"Risk Management for Age {age}:\n"
            f"- Equity allocation: {100 - age}% (traditional rule of thumb)\n"
            "- Diversify across 15+ holdings minimum\n"
            "- Regular quarterly rebalancing\n"
            "- Maintain 6-month emergency fund\n"
            "Take only the risk necessary to meet your goals."
        )
    else:
        return (
            "General Investment Guidance:\n"
            "Key principles for wealth building:\n"
            "- Start early, invest consistently\n"
            "- Diversify across asset classes and geographies\n"
            "- Keep costs low with index funds\n"
            "- Stay disciplined during market volatility\n"
            "- Focus on long-term goals\n"
            "Time in the market beats timing the market!"
        )

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

def create_portfolio_performance_history(portfolio_df):
    """Create a mock portfolio performance history chart"""
    
    # Generate mock historical data
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    
    # Create mock performance data for each stock
    performance_data = {}
    for symbol in portfolio_df['Symbol']:
        # Start with base value and add random walk
        base_value = 10000
        returns = np.random.normal(0.0008, 0.02, len(dates))  # Daily returns
        values = [base_value]
        
        for daily_return in returns:
            values.append(values[-1] * (1 + daily_return))
        
        performance_data[symbol] = values[1:]  # Remove initial value
    
    # Create DataFrame
    perf_df = pd.DataFrame(performance_data, index=dates)
    
    # Add portfolio total (weighted average)
    weights = portfolio_df.set_index('Symbol')['Weight_%'] / 100
    perf_df['Portfolio'] = 0
    for symbol in portfolio_df['Symbol']:
        if symbol in weights.index:
            perf_df['Portfolio'] += perf_df[symbol] * weights[symbol]
    
    return perf_df

def create_sector_analysis_chart(portfolio_df):
    """Create sector analysis based on stock symbols"""
    
    # Simple sector mapping
    sector_map = {
        'AAPL': 'Technology', 'MSFT': 'Technology', 'GOOGL': 'Technology',
        'NVDA': 'Technology', 'TSLA': 'Automotive', 'META': 'Technology',
        'AMZN': 'E-commerce', 'JNJ': 'Healthcare', 'PFE': 'Healthcare',
        'PG': 'Consumer Goods', 'KO': 'Consumer Goods', 'NEE': 'Utilities',
        'SO': 'Utilities', 'V': 'Financial', 'MA': 'Financial',
        'JPM': 'Financial', 'BAC': 'Financial', 'BRK.B': 'Financial'
    }
    
    # Add sector information
    portfolio_df['Sector'] = portfolio_df['Symbol'].map(sector_map).fillna('Other')
    
    # Calculate sector allocation
    sector_allocation = portfolio_df.groupby('Sector')['Market_Value'].sum().reset_index()
    sector_allocation['Percentage'] = (sector_allocation['Market_Value'] / sector_allocation['Market_Value'].sum()) * 100
    
    return sector_allocation

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
