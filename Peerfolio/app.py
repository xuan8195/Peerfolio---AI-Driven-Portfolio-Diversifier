import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from datetime import datetime, timedelta
import requests
from typing import Dict, List, Tuple
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import custom modules
from utils.portfolio_analyzer import PortfolioAnalyzer
from utils.peer_matcher import PeerMatcher
from utils.ai_advisor import AIAdvisor
from utils.data_generator import generate_sample_data
from config.theme import apply_dark_theme

# Page configuration
st.set_page_config(
    page_title="Peerfolio - AI Wealth Management",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply dark theme
apply_dark_theme()

class PeerfolioApp:
    def __init__(self):
        self.portfolio_analyzer = PortfolioAnalyzer()
        self.peer_matcher = PeerMatcher()
        self.ai_advisor = AIAdvisor()
        
        # Initialize session state
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = {}
        if 'portfolio_data' not in st.session_state:
            st.session_state.portfolio_data = None
        if 'analysis_results' not in st.session_state:
            st.session_state.analysis_results = None

    def render_header(self):
        """Render the main header with UBS branding"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
                <div style='text-align: center; padding: 20px 0;'>
                    <h1 style='color: #E60012; font-size: 3rem; margin-bottom: 10px;'>
                        🏦 Peerfolio
                    </h1>
                    <h3 style='color: #888; font-weight: 300; margin-top: 0;'>
                        AI-Powered Wealth Management for High-Net-Worth Individuals
                    </h3>
                    <p style='color: #666; font-size: 1.1rem;'>
                        Powered by UBS Digital Innovation
                    </p>
                </div>
            """, unsafe_allow_html=True)

    def render_sidebar(self):
        """Render the sidebar with user profile and navigation"""
        st.sidebar.markdown("### 👤 User Profile")
        
        # User profile inputs
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
        
        # Update session state
        st.session_state.user_profile = {
            'age': age,
            'location': location,
            'net_worth': net_worth,
            'investment_style': investment_style
        }
        
        st.sidebar.markdown("---")
        
        # Navigation
        st.sidebar.markdown("### 📊 Navigation")
        page = st.sidebar.radio(
            "Select Page",
            ["Portfolio Analysis", "Peer Insights", "AI Recommendations", "Market Intelligence"]
        )
        
        return page

    def render_portfolio_upload(self):
        """Render portfolio upload section"""
        st.markdown("### 📈 Portfolio Upload & Analysis")
        
        upload_method = st.radio(
            "Choose upload method:",
            ["Upload CSV", "Manual Input", "Use Sample Data"]
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
                    st.session_state.portfolio_data = portfolio_df
                    st.success("Portfolio uploaded successfully!")
                    st.dataframe(portfolio_df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error reading CSV: {str(e)}")
        
        elif upload_method == "Manual Input":
            self.render_manual_portfolio_input()
        
        else:  # Use Sample Data
            if st.button("Generate Sample Portfolio"):
                sample_portfolio = generate_sample_data(st.session_state.user_profile)
                st.session_state.portfolio_data = sample_portfolio
                st.success("Sample portfolio generated!")
                st.dataframe(sample_portfolio, use_container_width=True)

    def render_manual_portfolio_input(self):
        """Render manual portfolio input interface"""
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
                    new_entry = {
                        'Symbol': symbol.upper(),
                        'Shares': shares,
                        'Purchase_Price': purchase_price,
                        'Current_Price': current_price if current_price > 0 else self.get_current_price(symbol)
                    }
                    
                    if st.session_state.portfolio_data is None:
                        st.session_state.portfolio_data = pd.DataFrame([new_entry])
                    else:
                        st.session_state.portfolio_data = pd.concat([
                            st.session_state.portfolio_data,
                            pd.DataFrame([new_entry])
                        ], ignore_index=True)
                    
                    st.success(f"Added {symbol} to portfolio!")
                    st.rerun()

    def get_current_price(self, symbol: str) -> float:
        """Fetch current price for a symbol"""
        try:
            ticker = yf.Ticker(symbol)
            return ticker.history(period="1d")['Close'].iloc[-1]
        except:
            return 0.0

    def render_portfolio_analysis_page(self):
        """Render the main portfolio analysis page"""
        self.render_portfolio_upload()
        
        if st.session_state.portfolio_data is not None:
            st.markdown("---")
            
            # Analyze portfolio
            if st.button("🔍 Analyze Portfolio", type="primary"):
                with st.spinner("Analyzing your portfolio..."):
                    analysis = self.portfolio_analyzer.analyze(
                        st.session_state.portfolio_data,
                        st.session_state.user_profile
                    )
                    st.session_state.analysis_results = analysis
            
            if st.session_state.analysis_results:
                self.render_analysis_results()

    def render_analysis_results(self):
        """Render portfolio analysis results"""
        results = st.session_state.analysis_results
        
        st.markdown("### 📊 Portfolio Analysis Results")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Value",
                f"${results['total_value']:,.0f}",
                f"{results['total_return']:.1f}%"
            )
        
        with col2:
            st.metric(
                "Diversification Score",
                f"{results['diversification_score']:.1f}/10",
                "Higher is better"
            )
        
        with col3:
            st.metric(
                "Risk Level",
                results['risk_level'],
                results['risk_score']
            )
        
        with col4:
            st.metric(
                "ESG Score",
                f"{results['esg_score']:.1f}/10",
                "Sustainability rating"
            )
        
        # Portfolio composition chart
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.pie(
                values=results['sector_allocation'].values(),
                names=results['sector_allocation'].keys(),
                title="Portfolio Allocation by Sector",
                color_discrete_sequence=px.colors.qualitative.Dark24
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Risk-return scatter plot
            fig = go.Figure()
            fig.add_scatter(
                x=results['holdings_risk'],
                y=results['holdings_return'],
                mode='markers+text',
                text=results['holdings_symbols'],
                textposition="top center",
                marker=dict(size=10, color='#E60012')
            )
            fig.update_layout(
                title="Risk vs Return by Holding",
                xaxis_title="Risk (Volatility)",
                yaxis_title="Return (%)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        st.markdown("### 💡 Key Recommendations")
        for i, rec in enumerate(results['recommendations'], 1):
            st.markdown(f"**{i}.** {rec}")

    def render_peer_insights_page(self):
        """Render peer insights page"""
        st.markdown("### 👥 Peer Portfolio Insights")
        st.markdown("Discover how similar HNWIs are investing their wealth")
        
        # Find similar peers
        peers = self.peer_matcher.find_similar_peers(st.session_state.user_profile)
        
        # Peer statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Similar Peers Found", len(peers))
        
        with col2:
            avg_return = np.mean([p['performance'] for p in peers])
            st.metric("Average Return", f"{avg_return:.1f}%")
        
        with col3:
            popular_sector = max(set([p['top_sector'] for p in peers]), 
                               key=[p['top_sector'] for p in peers].count)
            st.metric("Most Popular Sector", popular_sector)
        
        # Peer portfolio analysis
        st.markdown("#### 📈 Popular Investment Strategies")
        
        # Strategy distribution
        strategies = {}
        for peer in peers:
            strategy = peer['strategy']
            strategies[strategy] = strategies.get(strategy, 0) + 1
        
        fig = px.bar(
            x=list(strategies.keys()),
            y=list(strategies.values()),
            title="Investment Strategies Among Peers",
            color_discrete_sequence=['#E60012']
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Top performing peers
        st.markdown("#### 🏆 Top Performing Peer Portfolios")
        
        top_peers = sorted(peers, key=lambda x: x['performance'], reverse=True)[:5]
        
        for i, peer in enumerate(top_peers, 1):
            with st.expander(f"#{i} - {peer['age']}yo {peer['location']} ({peer['performance']:.1f}% return)"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Strategy:** {peer['strategy']}")
                    st.markdown(f"**Top Sector:** {peer['top_sector']}")
                    st.markdown(f"**Risk Level:** {peer['risk_level']}")
                
                with col2:
                    # Mock allocation data
                    allocation = peer['allocation']
                    fig = px.pie(
                        values=list(allocation.values()),
                        names=list(allocation.keys()),
                        title=f"Portfolio Allocation",
                        color_discrete_sequence=px.colors.qualitative.Pastel
                    )
                    fig.update_layout(height=300, showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)

    def render_ai_recommendations_page(self):
        """Render AI recommendations page"""
        st.markdown("### 🤖 AI-Powered Investment Recommendations")
        
        if st.session_state.portfolio_data is not None:
            # Get AI recommendations
            if st.button("Get AI Recommendations", type="primary"):
                with st.spinner("AI is analyzing your portfolio and generating recommendations..."):
                    recommendations = self.ai_advisor.get_recommendations(
                        st.session_state.portfolio_data,
                        st.session_state.user_profile,
                        st.session_state.analysis_results
                    )
                    
                    # Display recommendations
                    st.markdown("#### 💎 Personalized Investment Suggestions")
                    
                    for category, recs in recommendations.items():
                        with st.expander(f"📊 {category.replace('_', ' ').title()}"):
                            for rec in recs:
                                st.markdown(f"• **{rec['title']}**")
                                st.markdown(f"  *{rec['description']}*")
                                st.markdown(f"  **Rationale:** {rec['rationale']}")
                                if rec.get('risk_level'):
                                    st.markdown(f"  **Risk Level:** {rec['risk_level']}")
                                st.markdown("---")
            
            # AI Chat Interface
            st.markdown("#### 💬 Ask Our AI Wealth Advisor")
            
            user_question = st.text_input(
                "Ask a question about your portfolio or investment strategy:",
                placeholder="e.g., Should I increase my crypto allocation? What about ESG investments?"
            )
            
            if user_question and st.button("Ask AI Advisor"):
                with st.spinner("AI is thinking..."):
                    response = self.ai_advisor.chat_response(
                        user_question,
                        st.session_state.user_profile,
                        st.session_state.portfolio_data
                    )
                    
                    st.markdown("#### 🎯 AI Advisor Response")
                    st.markdown(response)
        else:
            st.warning("Please upload your portfolio first to get AI recommendations.")

    def render_market_intelligence_page(self):
        """Render market intelligence page"""
        st.markdown("### 📊 Market Intelligence Dashboard")
        
        # Market overview
        col1, col2 = st.columns(2)
        
        with col1:
            # Major indices
            st.markdown("#### 📈 Major Market Indices")
            indices = {
                '^GSPC': 'S&P 500',
                '^DJI': 'Dow Jones',
                '^IXIC': 'NASDAQ',
                '^FTSE': 'FTSE 100'
            }
            
            for symbol, name in indices.items():
                try:
                    ticker = yf.Ticker(symbol)
                    hist = ticker.history(period="5d")
                    current = hist['Close'].iloc[-1]
                    prev = hist['Close'].iloc[-2]
                    change = ((current - prev) / prev) * 100
                    
                    st.metric(
                        name,
                        f"{current:.2f}",
                        f"{change:+.2f}%"
                    )
                except:
                    st.metric(name, "N/A", "N/A")
        
        with col2:
            # Crypto prices
            st.markdown("#### ₿ Cryptocurrency Market")
            crypto_symbols = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD']
            
            for symbol in crypto_symbols:
                try:
                    ticker = yf.Ticker(symbol)
                    hist = ticker.history(period="5d")
                    current = hist['Close'].iloc[-1]
                    prev = hist['Close'].iloc[-2]
                    change = ((current - prev) / prev) * 100
                    
                    name = symbol.replace('-USD', '')
                    st.metric(
                        name,
                        f"${current:,.2f}",
                        f"{change:+.2f}%"
                    )
                except:
                    st.metric(symbol.replace('-USD', ''), "N/A", "N/A")
        
        # Market sentiment and trends
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

    def run(self):
        """Main application runner"""
        self.render_header()
        
        # Sidebar navigation
        selected_page = self.render_sidebar()
        
        # Main content area
        if selected_page == "Portfolio Analysis":
            self.render_portfolio_analysis_page()
        elif selected_page == "Peer Insights":
            self.render_peer_insights_page()
        elif selected_page == "AI Recommendations":
            self.render_ai_recommendations_page()
        elif selected_page == "Market Intelligence":
            self.render_market_intelligence_page()
        
        # Footer
        st.markdown("---")
        st.markdown(
            "<div style='text-align: center; color: #666; padding: 20px;'>"
            "🏦 Peerfolio - Powered by UBS Digital Innovation | "
            "© 2025 UBS Group AG. All rights reserved."
            "</div>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    app = PeerfolioApp()
    app.run()
