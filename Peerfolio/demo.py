"""
Peerfolio Demo Script
Showcases the AI-driven wealth management platform features
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

def run_demo():
    """Run an interactive demo of Peerfolio features"""
    
    st.markdown("""
    # 🎭 Peerfolio Interactive Demo
    
    Welcome to the interactive demonstration of Peerfolio, the AI-powered wealth management platform for high-net-worth individuals.
    
    ## Demo Scenarios
    
    Choose a scenario to explore:
    """)
    
    scenario = st.selectbox(
        "Select Demo Scenario",
        [
            "New HNWI - Portfolio Analysis",
            "Experienced Investor - Peer Insights", 
            "ESG-Focused Client - Sustainable Investing",
            "Tech Entrepreneur - Growth Strategy",
            "Pre-Retirement - Risk Management"
        ]
    )
    
    if scenario == "New HNWI - Portfolio Analysis":
        demo_new_hnwi()
    elif scenario == "Experienced Investor - Peer Insights":
        demo_peer_insights()
    elif scenario == "ESG-Focused Client - Sustainable Investing":
        demo_esg_focus()
    elif scenario == "Tech Entrepreneur - Growth Strategy":
        demo_tech_entrepreneur()
    elif scenario == "Pre-Retirement - Risk Management":
        demo_pre_retirement()

def demo_new_hnwi():
    """Demo for new HNWI with concentrated portfolio"""
    
    st.markdown("## 🌟 Scenario: New High-Net-Worth Individual")
    st.markdown("""
    **Profile**: Sarah Chen, 32, Tech Executive in Singapore
    - Net Worth: $3.2M (mostly from stock options)
    - Investment Experience: Limited
    - Goals: Diversify wealth, long-term growth
    """)
    
    # Show concentrated portfolio
    portfolio_data = pd.DataFrame({
        'Symbol': ['AAPL', 'GOOGL', 'MSFT', 'Cash'],
        'Value': [1800000, 900000, 400000, 100000],
        'Percentage': [56.25, 28.125, 12.5, 3.125]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.pie(portfolio_data, values='Value', names='Symbol', 
                    title="Current Portfolio - Highly Concentrated")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🚨 Key Issues Identified")
        st.error("**High Concentration Risk**: 97% in 3 tech stocks")
        st.warning("**Sector Risk**: 100% technology exposure")
        st.warning("**Geographic Risk**: US-only exposure")
        st.info("**Opportunity**: Diversification can reduce risk by 40%")
    
    # AI Recommendations
    st.markdown("### 🤖 AI-Generated Recommendations")
    
    recommendations = [
        "🎯 **Immediate Action**: Reduce tech concentration to <40% of portfolio",
        "🌏 **Geographic Diversification**: Add 20% international exposure (Europe, Asia)",
        "🏠 **Asset Class Expansion**: Consider 15% real estate, 10% bonds",
        "💰 **Dollar-Cost Averaging**: Systematically diversify over 6 months",
        "🛡️ **Risk Management**: Implement stop-losses on concentrated positions"
    ]
    
    for rec in recommendations:
        st.markdown(rec)
    
    # Show improved portfolio
    if st.button("Show Optimized Portfolio"):
        with st.spinner("AI is optimizing your portfolio..."):
            time.sleep(2)
            
        optimized_data = pd.DataFrame({
            'Asset Class': ['US Stocks', 'International Stocks', 'Bonds', 'Real Estate', 'Cash'],
            'Current': [97, 0, 0, 0, 3],
            'Recommended': [55, 20, 15, 8, 2]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Current', x=optimized_data['Asset Class'], y=optimized_data['Current']),
            go.Bar(name='Recommended', x=optimized_data['Asset Class'], y=optimized_data['Recommended'])
        ])
        fig.update_layout(title="Portfolio Optimization: Before vs After", barmode='group')
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("✅ Diversification reduces portfolio risk by 38% while maintaining growth potential")

def demo_peer_insights():
    """Demo peer insights for experienced investor"""
    
    st.markdown("## 👥 Scenario: Experienced Investor Seeking Peer Insights")
    st.markdown("""
    **Profile**: Michael Rodriguez, 45, Investment Manager in New York
    - Net Worth: $8.5M
    - Investment Experience: 15+ years
    - Goals: Benchmark against peers, identify new opportunities
    """)
    
    # Peer comparison
    st.markdown("### 📊 Peer Performance Analysis")
    
    peer_data = pd.DataFrame({
        'Age Group': ['40-45', '45-50', '50-55'],
        'Average Return': [9.2, 8.7, 7.8],
        'Your Return': [8.4, 8.4, 8.4],
        'Top Quartile': [12.5, 11.8, 10.9],
        'Peer Count': [234, 189, 156]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Peer Average', x=peer_data['Age Group'], y=peer_data['Average Return']))
    fig.add_trace(go.Bar(name='Your Performance', x=peer_data['Age Group'], y=peer_data['Your Return']))
    fig.add_trace(go.Bar(name='Top Quartile', x=peer_data['Age Group'], y=peer_data['Top Quartile']))
    fig.update_layout(title="Performance vs Similar Peers", barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
    # Peer strategies
    st.markdown("### 🎯 Popular Strategies Among Top Performers")
    
    strategies = pd.DataFrame({
        'Strategy': ['ESG + Growth', 'Tech + Real Estate', 'International Focus', 'Alternative Investments'],
        'Users': [45, 38, 32, 28],
        'Avg Return': [11.8, 10.9, 10.2, 13.4],
        'Risk Level': ['Medium', 'Medium-High', 'Medium', 'High']
    })
    
    st.dataframe(strategies, use_container_width=True)
    
    # Specific insights
    st.markdown("### 💡 Key Insights from Top Performers")
    
    insights = [
        "🌱 **ESG Integration**: 67% of top performers include ESG criteria",
        "🏠 **Real Estate Allocation**: Average 12% in REITs and direct property",
        "🌏 **International Exposure**: 28% average allocation to non-US assets",
        "💎 **Alternative Investments**: 15% in private equity, hedge funds, or crypto",
        "⚖️ **Rebalancing Frequency**: Quarterly rebalancing most common"
    ]
    
    for insight in insights:
        st.markdown(insight)
    
    if st.button("Get Personalized Peer Matching"):
        with st.spinner("Finding your investment peers..."):
            time.sleep(2)
        
        st.success("Found 47 similar investors!")
        st.markdown("**Similar Profile**: Investment managers, 40-50 years old, $5M-$15M net worth")
        st.markdown("**Top Strategy Match**: ESG + Growth (78% match)")

def demo_esg_focus():
    """Demo for ESG-focused investing"""
    
    st.markdown("## 🌱 Scenario: ESG-Focused Sustainable Investing")
    st.markdown("""
    **Profile**: Emma Thompson, 38, Sustainability Consultant in London
    - Net Worth: $4.2M
    - Values: Environmental and social impact
    - Goals: Align investments with values without sacrificing returns
    """)
    
    # ESG Portfolio Analysis
    st.markdown("### 🌍 ESG Portfolio Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("ESG Score", "7.8/10", "+0.8")
    with col2:
        st.metric("Carbon Footprint", "Low", "-23%")
    with col3:
        st.metric("Impact Alignment", "85%", "+12%")
    
    # ESG vs Traditional comparison
    comparison_data = pd.DataFrame({
        'Metric': ['5-Year Return', 'Volatility', 'Sharpe Ratio', 'ESG Score'],
        'Your ESG Portfolio': [9.2, 14.5, 0.63, 7.8],
        'Traditional Benchmark': [9.8, 16.2, 0.60, 3.2]
    })
    
    st.markdown("### 📈 ESG vs Traditional Portfolio Performance")
    st.dataframe(comparison_data, use_container_width=True)
    
    # ESG Opportunities
    st.markdown("### 🎯 ESG Investment Opportunities")
    
    opportunities = [
        "🔋 **Clean Energy**: Solar and wind infrastructure funds",
        "💧 **Water Technology**: Water treatment and conservation companies",
        "🌿 **Sustainable Agriculture**: Plant-based food and vertical farming",
        "♻️ **Circular Economy**: Waste reduction and recycling technology",
        "🏥 **Healthcare Access**: Companies improving global health outcomes"
    ]
    
    for opp in opportunities:
        st.markdown(opp)
    
    # Impact measurement
    if st.button("View Impact Report"):
        st.markdown("### 🌟 Your Investment Impact")
        
        impact_metrics = {
            'CO2 Emissions Avoided': '1,247 tons/year',
            'Clean Energy Generated': '3.2 GWh/year',
            'Jobs Created': '89 sustainable jobs',
            'Water Saved': '2.1M gallons/year'
        }
        
        cols = st.columns(2)
        for i, (metric, value) in enumerate(impact_metrics.items()):
            with cols[i % 2]:
                st.metric(metric, value)

def demo_tech_entrepreneur():
    """Demo for tech entrepreneur growth strategy"""
    
    st.markdown("## 🚀 Scenario: Tech Entrepreneur Growth Strategy")
    st.markdown("""
    **Profile**: David Kim, 29, Startup Founder in San Francisco
    - Net Worth: $12M (from startup exit)
    - Risk Tolerance: High
    - Goals: Aggressive growth, angel investing, building generational wealth
    """)
    
    # Growth portfolio
    st.markdown("### 🎯 Aggressive Growth Portfolio Allocation")
    
    allocation = pd.DataFrame({
        'Asset Class': ['Growth Stocks', 'Venture Capital', 'Crypto', 'International', 'Cash'],
        'Allocation %': [45, 25, 15, 10, 5],
        'Expected Return': [12.5, 18.2, 25.0, 9.8, 2.5]
    })
    
    fig = px.bar(allocation, x='Asset Class', y='Allocation %', 
                title="Aggressive Growth Allocation")
    st.plotly_chart(fig, use_container_width=True)
    
    # Angel investing opportunities
    st.markdown("### 👼 Angel Investing Pipeline")
    
    deals = pd.DataFrame({
        'Company': ['AI Health Startup', 'FinTech Platform', 'Clean Energy', 'EdTech Solution'],
        'Sector': ['Healthcare', 'Financial', 'Energy', 'Education'],
        'Stage': ['Series A', 'Seed', 'Series B', 'Pre-Seed'],
        'Min Investment': ['$50K', '$25K', '$100K', '$10K'],
        'AI Score': [8.7, 9.2, 7.8, 8.1]
    })
    
    st.dataframe(deals, use_container_width=True)
    
    # Risk management for high-growth
    st.markdown("### ⚖️ Risk Management for High-Growth Strategy")
    
    risk_strategies = [
        "📊 **Position Sizing**: Limit single investments to 5% of portfolio",
        "⏰ **Time Diversification**: Spread investments over 2-3 years",
        "🌐 **Geographic Spread**: Include international growth markets",
        "🛡️ **Downside Protection**: 10% in defensive assets",
        "🔄 **Rebalancing**: Monthly review for high-volatility positions"
    ]
    
    for strategy in risk_strategies:
        st.markdown(strategy)

def demo_pre_retirement():
    """Demo for pre-retirement risk management"""
    
    st.markdown("## 🏛️ Scenario: Pre-Retirement Risk Management")
    st.markdown("""
    **Profile**: Robert Wilson, 58, Senior Executive in Zurich
    - Net Worth: $18M
    - Time Horizon: 7 years to retirement
    - Goals: Capital preservation, income generation, wealth transfer
    """)
    
    # Asset allocation transition
    st.markdown("### 📊 Age-Appropriate Asset Allocation")
    
    allocation_data = pd.DataFrame({
        'Age': ['Current (58)', 'Target (65)', 'Retirement (70)'],
        'Stocks': [65, 50, 40],
        'Bonds': [25, 35, 45],
        'Real Estate': [8, 12, 12],
        'Cash': [2, 3, 3]
    })
    
    fig = go.Figure()
    for column in ['Stocks', 'Bonds', 'Real Estate', 'Cash']:
        fig.add_trace(go.Bar(name=column, x=allocation_data['Age'], 
                           y=allocation_data[column]))
    
    fig.update_layout(title="Asset Allocation Glide Path", barmode='stack')
    st.plotly_chart(fig, use_container_width=True)
    
    # Income generation strategy
    st.markdown("### 💰 Income Generation Strategy")
    
    income_sources = pd.DataFrame({
        'Source': ['Dividend Stocks', 'Corporate Bonds', 'REITs', 'Municipal Bonds'],
        'Allocation %': [30, 25, 15, 10],
        'Current Yield': [3.2, 4.8, 5.1, 3.8],
        'Annual Income': ['$172K', '$216K', '$137K', '$68K']
    })
    
    st.dataframe(income_sources, use_container_width=True)
    
    # Estate planning
    st.markdown("### 🏛️ Estate Planning Considerations")
    
    estate_items = [
        "📄 **Trust Structures**: Revocable and irrevocable trusts for tax efficiency",
        "🎁 **Gifting Strategy**: Annual exclusion gifts to family members",
        "💼 **Business Succession**: If applicable, plan for business transfer",
        "🏥 **Insurance Review**: Life insurance for estate liquidity",
        "🌍 **International Considerations**: Cross-border tax implications"
    ]
    
    for item in estate_items:
        st.markdown(item)
    
    # Stress testing
    if st.button("Run Portfolio Stress Test"):
        st.markdown("### 📉 Market Stress Test Results")
        
        scenarios = pd.DataFrame({
            'Scenario': ['Market Crash (-30%)', 'Recession (-15%)', 'Inflation Spike', 'Base Case'],
            'Portfolio Impact': ['-18.2%', '-9.1%', '-5.3%', '+7.8%'],
            'Recovery Time': ['18 months', '8 months', '12 months', 'N/A'],
            'Income Impact': ['-12%', '-6%', '-8%', 'Stable']
        })
        
        st.dataframe(scenarios, use_container_width=True)
        st.success("✅ Portfolio shows resilience with manageable downside risk")

if __name__ == "__main__":
    run_demo()
