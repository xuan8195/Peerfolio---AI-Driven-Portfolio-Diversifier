import pandas as pd
import numpy as np
from typing import Dict, List
import json
import os

class AIAdvisor:
    """AI-powered investment advisor using GPT-style responses"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        # Predefined knowledge base for demonstrations
        self.knowledge_base = self._build_knowledge_base()
    
    def _build_knowledge_base(self) -> Dict:
        """Build comprehensive investment knowledge base"""
        return {
            'sector_insights': {
                'Technology': {
                    'outlook': 'Strong long-term growth driven by AI, cloud computing, and digital transformation',
                    'risks': 'High volatility, regulatory concerns, valuation risks',
                    'opportunities': 'AI revolution, cybersecurity growth, semiconductor demand'
                },
                'Healthcare': {
                    'outlook': 'Defensive sector with aging population demographics support',
                    'risks': 'Regulatory changes, drug development failures, pricing pressure',
                    'opportunities': 'Biotech breakthroughs, personalized medicine, medical devices'
                },
                'Financial Services': {
                    'outlook': 'Benefits from rising interest rates and economic growth',
                    'risks': 'Credit losses, regulatory changes, fintech disruption',
                    'opportunities': 'Digital banking, wealth management growth, emerging markets'
                },
                'Real Estate': {
                    'outlook': 'Mixed outlook with interest rate sensitivity',
                    'risks': 'Interest rate increases, oversupply in some markets',
                    'opportunities': 'Data centers, logistics, residential shortage in key markets'
                },
                'Energy': {
                    'outlook': 'Transition period with both traditional and renewable opportunities',
                    'risks': 'Commodity price volatility, regulatory shifts to renewables',
                    'opportunities': 'Renewable energy infrastructure, energy storage, oil dividend yields'
                }
            },
            'investment_strategies': {
                'Conservative': {
                    'allocation': {'Bonds': 60, 'Blue-chip Stocks': 30, 'Cash': 10},
                    'risk_level': 'Low',
                    'expected_return': '4-6%',
                    'description': 'Capital preservation with modest growth'
                },
                'Moderate': {
                    'allocation': {'Stocks': 60, 'Bonds': 30, 'Alternatives': 10},
                    'risk_level': 'Medium',
                    'expected_return': '6-8%',
                    'description': 'Balanced approach between growth and income'
                },
                'Aggressive': {
                    'allocation': {'Growth Stocks': 70, 'International': 20, 'Alternatives': 10},
                    'risk_level': 'High',
                    'expected_return': '8-12%',
                    'description': 'Maximum growth potential with higher volatility'
                }
            }
        }
    
    def get_recommendations(self, portfolio_df: pd.DataFrame, 
                          user_profile: Dict, analysis_results: Dict) -> Dict:
        """Generate comprehensive AI-powered recommendations"""
        
        recommendations = {
            'diversification': self._get_diversification_recommendations(portfolio_df, user_profile),
            'sector_allocation': self._get_sector_recommendations(portfolio_df, analysis_results),
            'risk_management': self._get_risk_recommendations(analysis_results, user_profile),
            'esg_opportunities': self._get_esg_recommendations(portfolio_df, user_profile),
            'market_timing': self._get_market_timing_recommendations(user_profile)
        }
        
        return recommendations
    
    def _get_diversification_recommendations(self, portfolio_df: pd.DataFrame, 
                                           user_profile: Dict) -> List[Dict]:
        """Generate diversification-focused recommendations"""
        recommendations = []
        
        # Analyze current holdings
        total_value = portfolio_df['Market_Value'].sum() if 'Market_Value' in portfolio_df.columns else 0
        
        if total_value == 0:
            return [{
                'title': 'Start Building Your Portfolio',
                'description': 'Begin with a diversified foundation of 5-10 quality stocks across different sectors',
                'rationale': 'Diversification reduces risk while maintaining growth potential',
                'risk_level': 'Low'
            }]
        
        # Check for concentration issues
        if len(portfolio_df) < 5:
            recommendations.append({
                'title': 'Increase Position Count',
                'description': 'Add 3-5 more positions to improve diversification',
                'rationale': 'Single-stock risk decreases significantly with more holdings',
                'risk_level': 'Low'
            })
        
        # Geographic diversification
        recommendations.append({
            'title': 'International Exposure',
            'description': 'Consider adding 15-20% international equity exposure',
            'rationale': 'Global diversification reduces correlation with domestic markets',
            'risk_level': 'Medium'
        })
        
        # Alternative investments for HNWIs
        net_worth = user_profile.get('net_worth', '$2.5M - $5M')
        if '$5M' in net_worth or '$10M' in net_worth or '$25M' in net_worth:
            recommendations.append({
                'title': 'Alternative Investments',
                'description': 'Explore private equity, hedge funds, or real estate investments',
                'rationale': 'High-net-worth individuals benefit from alternative asset diversification',
                'risk_level': 'Medium-High'
            })
        
        return recommendations
    
    def _get_sector_recommendations(self, portfolio_df: pd.DataFrame, 
                                  analysis_results: Dict) -> List[Dict]:
        """Generate sector-specific recommendations"""
        recommendations = []
        
        if not analysis_results or 'sector_allocation' not in analysis_results:
            return recommendations
        
        sector_allocation = analysis_results['sector_allocation']
        total_value = sum(sector_allocation.values())
        
        if total_value == 0:
            return recommendations
        
        # Identify underweight sectors
        target_allocations = {
            'Technology': 0.25,
            'Healthcare': 0.20,
            'Financial Services': 0.15,
            'Consumer': 0.15,
            'Real Estate': 0.10,
            'Energy': 0.05,
            'Other': 0.10
        }
        
        for sector, target_weight in target_allocations.items():
            current_weight = sector_allocation.get(sector, 0) / total_value
            
            if current_weight < target_weight * 0.5:  # Significantly underweight
                sector_info = self.knowledge_base['sector_insights'].get(sector, {})
                recommendations.append({
                    'title': f'Increase {sector} Exposure',
                    'description': f'Current allocation: {current_weight:.1%}, Target: {target_weight:.1%}',
                    'rationale': sector_info.get('outlook', 'Sector diversification benefits'),
                    'risk_level': 'Medium'
                })
        
        # Overweight warnings
        for sector, value in sector_allocation.items():
            weight = value / total_value
            if weight > 0.4:  # Over 40% concentration
                recommendations.append({
                    'title': f'Reduce {sector} Concentration',
                    'description': f'Current allocation of {weight:.1%} is too high',
                    'rationale': 'High concentration increases portfolio risk',
                    'risk_level': 'High'
                })
        
        return recommendations
    
    def _get_risk_recommendations(self, analysis_results: Dict, 
                                user_profile: Dict) -> List[Dict]:
        """Generate risk management recommendations"""
        recommendations = []
        
        risk_level = analysis_results.get('risk_level', 'Medium') if analysis_results else 'Medium'
        user_style = user_profile.get('investment_style', 'Moderate')
        age = user_profile.get('age', 35)
        
        # Age-based risk recommendations
        if age < 35:
            recommendations.append({
                'title': 'Leverage Your Time Horizon',
                'description': 'Consider 80-90% equity allocation for long-term growth',
                'rationale': 'Young investors can weather market volatility for higher returns',
                'risk_level': 'Medium-High'
            })
        elif age > 55:
            recommendations.append({
                'title': 'Increase Defensive Positions',
                'description': 'Consider 30-40% bonds and dividend stocks for income',
                'rationale': 'Approaching retirement requires more capital preservation',
                'risk_level': 'Low-Medium'
            })
        
        # Risk mismatch warnings
        if risk_level == 'High' and user_style == 'Conservative':
            recommendations.append({
                'title': 'Risk Profile Mismatch',
                'description': 'Your portfolio risk exceeds your stated conservative preference',
                'rationale': 'Alignment between risk tolerance and portfolio reduces stress and improves outcomes',
                'risk_level': 'High'
            })
        
        # Volatility management
        recommendations.append({
            'title': 'Implement Dollar-Cost Averaging',
            'description': 'Make regular monthly investments to smooth market volatility',
            'rationale': 'Systematic investing reduces timing risk and emotional decisions',
            'risk_level': 'Low'
        })
        
        return recommendations
    
    def _get_esg_recommendations(self, portfolio_df: pd.DataFrame, 
                               user_profile: Dict) -> List[Dict]:
        """Generate ESG-focused recommendations"""
        recommendations = []
        
        if user_profile.get('investment_style') == 'ESG-focused':
            recommendations.extend([
                {
                    'title': 'Clean Energy ETFs',
                    'description': 'Add exposure to renewable energy and clean technology',
                    'rationale': 'ESG investing aligns with sustainability goals while capturing growth trends',
                    'risk_level': 'Medium'
                },
                {
                    'title': 'ESG-Screened Index Funds',
                    'description': 'Replace traditional index funds with ESG-screened alternatives',
                    'rationale': 'Maintain diversification while excluding controversial industries',
                    'risk_level': 'Low'
                }
            ])
        else:
            recommendations.append({
                'title': 'Consider ESG Integration',
                'description': 'ESG factors increasingly impact long-term returns',
                'rationale': 'Companies with strong ESG practices often show better risk management',
                'risk_level': 'Low'
            })
        
        return recommendations
    
    def _get_market_timing_recommendations(self, user_profile: Dict) -> List[Dict]:
        """Generate market timing and tactical recommendations"""
        recommendations = [
            {
                'title': 'Rebalance Quarterly',
                'description': 'Review and rebalance portfolio allocations every 3 months',
                'rationale': 'Regular rebalancing maintains target allocations and captures market inefficiencies',
                'risk_level': 'Low'
            },
            {
                'title': 'Tax-Loss Harvesting',
                'description': 'Realize losses to offset gains for tax efficiency',
                'rationale': 'Tax-loss harvesting can add 0.5-1% annually to after-tax returns',
                'risk_level': 'Low'
            }
        ]
        
        # HNW-specific recommendations
        net_worth = user_profile.get('net_worth', '$2.5M - $5M')
        if '$10M' in net_worth or '$25M' in net_worth:
            recommendations.extend([
                {
                    'title': 'Tax-Advantaged Structures',
                    'description': 'Explore family offices, trusts, or offshore structures',
                    'rationale': 'High-net-worth individuals benefit from sophisticated tax planning',
                    'risk_level': 'Low'
                },
                {
                    'title': 'Direct Indexing',
                    'description': 'Consider direct stock ownership for tax customization',
                    'rationale': 'Direct indexing allows tax-loss harvesting at the individual stock level',
                    'risk_level': 'Medium'
                }
            ])
        
        return recommendations
    
    def chat_response(self, user_question: str, user_profile: Dict, 
                     portfolio_data: pd.DataFrame = None) -> str:
        """Generate conversational AI responses to user questions"""
        
        # Simple keyword-based response system (in production, would use OpenAI API)
        question_lower = user_question.lower()
        
        if 'crypto' in question_lower or 'bitcoin' in question_lower:
            return self._crypto_response(user_profile)
        elif 'esg' in question_lower or 'sustainable' in question_lower:
            return self._esg_response(user_profile)
        elif 'risk' in question_lower:
            return self._risk_response(user_profile)
        elif 'diversif' in question_lower:
            return self._diversification_response(user_profile)
        elif 'tax' in question_lower:
            return self._tax_response(user_profile)
        elif 'real estate' in question_lower or 'property' in question_lower:
            return self._real_estate_response(user_profile)
        else:
            return self._general_response(user_profile)
    
    def _crypto_response(self, user_profile: Dict) -> str:
        age = user_profile.get('age', 35)
        investment_style = user_profile.get('investment_style', 'Moderate')
        
        if age < 40 and investment_style in ['Aggressive', 'Crypto-focused']:
            return """
            🚀 **Cryptocurrency Allocation Recommendation**
            
            Given your age and risk tolerance, a 5-15% allocation to cryptocurrency could be appropriate:
            
            **Suggested Approach:**
            • Start with 5-10% in Bitcoin and Ethereum (established cryptos)
            • Consider DCA (Dollar Cost Averaging) for entry
            • Never exceed 15% total portfolio allocation
            • Focus on your core traditional portfolio first
            
            **Key Considerations:**
            • High volatility requires strong risk tolerance
            • Regulatory risks remain significant
            • Consider crypto as "venture capital" allocation
            • Ensure you have 6-month emergency fund first
            
            Remember: Only invest what you can afford to lose completely.
            """
        else:
            return """
            🛡️ **Conservative Crypto Approach**
            
            Given your profile, a cautious approach to crypto is recommended:
            
            **Suggested Strategy:**
            • Limit to 2-5% if any allocation
            • Focus on Bitcoin as "digital gold" 
            • Avoid altcoins and DeFi protocols
            • Consider crypto through established ETFs
            
            **Better Alternatives:**
            • Gold or precious metals for inflation hedge
            • TIPS (Treasury Inflation-Protected Securities)
            • Real estate investment trusts (REITs)
            
            Your wealth preservation should prioritize proven asset classes.
            """
    
    def _esg_response(self, user_profile: Dict) -> str:
        return """
        🌱 **ESG Investment Strategy**
        
        ESG investing has evolved significantly and can enhance long-term returns:
        
        **Implementation Options:**
        • ESG-screened index funds (lower fees, broad diversification)
        • Impact investing (directly measurable outcomes)
        • Green bonds (fixed income with environmental benefits)
        • Clean energy ETFs (growth potential with purpose)
        
        **Performance Considerations:**
        • ESG funds often show lower volatility
        • Many studies show comparable or better returns
        • Growing institutional demand supports valuations
        • Regulatory tailwinds in many jurisdictions
        
        **Recommended Allocation:**
        • Start with 20-30% ESG allocation
        • Gradually increase based on performance
        • Maintain diversification across traditional assets
        
        ESG integration can align your values with wealth building goals.
        """
    
    def _risk_response(self, user_profile: Dict) -> str:
        age = user_profile.get('age', 35)
        return f"""
        ⚖️ **Risk Management for Your Portfolio**
        
        At age {age}, here's your optimal risk framework:
        
        **Risk Allocation Guidelines:**
        • Equity percentage: {100 - age}% (rule of thumb)
        • International exposure: 20-30% of equity allocation
        • Alternative investments: 5-15% for diversification
        
        **Risk Mitigation Strategies:**
        • Diversify across 20+ holdings minimum
        • Regular rebalancing (quarterly)
        • Dollar-cost averaging for new investments
        • Maintain 6-month emergency fund
        
        **Volatility Management:**
        • Focus on total return, not daily fluctuations
        • Use limit orders to control entry/exit points
        • Consider covered calls for income enhancement
        
        **Key Principle:** Take only the risk necessary to meet your goals.
        """
    
    def _diversification_response(self, user_profile: Dict) -> str:
        return """
        📊 **Portfolio Diversification Strategy**
        
        True diversification goes beyond just owning multiple stocks:
        
        **Asset Class Diversification:**
        • Domestic stocks (40-60%)
        • International stocks (15-25%)
        • Bonds (20-40% based on age)
        • Real estate (5-15%)
        • Commodities (0-10%)
        
        **Sector Diversification:**
        • No single sector >30% of equity allocation
        • Include defensive sectors (utilities, consumer staples)
        • Balance growth vs. value styles
        
        **Geographic Diversification:**
        • Developed markets (15-20%)
        • Emerging markets (5-10%)
        • Consider currency hedging
        
        **Time Diversification:**
        • Dollar-cost averaging
        • Staggered bond maturities
        • Rebalancing calendar
        
        **Remember:** Diversification is the only free lunch in investing!
        """
    
    def _tax_response(self, user_profile: Dict) -> str:
        net_worth = user_profile.get('net_worth', '$2.5M - $5M')
        
        if '$10M' in net_worth or '$25M' in net_worth:
            return """
            💼 **Advanced Tax Strategies for HNWIs**
            
            Your wealth level opens sophisticated tax optimization opportunities:
            
            **Immediate Strategies:**
            • Max out all retirement accounts (401k, IRA, backdoor Roth)
            • Tax-loss harvesting throughout the year
            • Municipal bonds for high-income tax situations
            • Direct indexing for granular tax control
            
            **Advanced Structures:**
            • Charitable Remainder Trusts (CRT)
            • Grantor Retained Annuity Trusts (GRAT)
            • Family Limited Partnerships
            • Offshore structures (with proper compliance)
            
            **Estate Planning:**
            • Annual gift tax exclusions ($17,000 per recipient)
            • Generation-skipping transfer planning
            • Life insurance trusts
            
            **Recommendation:** Consult with tax professionals specializing in HNW clients.
            """
        else:
            return """
            📋 **Tax-Efficient Investing Basics**
            
            Optimize your after-tax returns with these strategies:
            
            **Account Prioritization:**
            1. 401(k) up to company match
            2. Max HSA contributions (triple tax advantage)
            3. Max traditional/Roth IRA
            4. Taxable account for remaining funds
            
            **Tax-Efficient Investments:**
            • Index funds (low turnover)
            • Municipal bonds (if in high tax bracket)
            • Tax-managed funds
            • Hold growth stocks long-term
            
            **Timing Strategies:**
            • Harvest losses annually
            • Realize long-term gains in low-income years
            • Consider Roth conversions in market downturns
            
            **Rule of Thumb:** Save 20-30% more by optimizing taxes!
            """
    
    def _real_estate_response(self, user_profile: Dict) -> str:
        return """
        🏠 **Real Estate Investment Strategy**
        
        Real estate can provide diversification and inflation protection:
        
        **Investment Approaches:**
        • REITs (liquid, diversified, professional management)
        • Direct property ownership (control, tax benefits)
        • Real estate crowdfunding (lower minimums)
        • Real estate limited partnerships
        
        **REIT Diversification:**
        • Residential REITs (apartments, single-family)
        • Commercial REITs (office, retail, industrial)
        • Specialty REITs (data centers, cell towers, healthcare)
        • International REITs
        
        **Direct Ownership Considerations:**
        • Requires significant capital and time
        • Illiquid but potentially higher returns
        • Tax advantages (depreciation, 1031 exchanges)
        • Consider professional property management
        
        **Recommended Allocation:** 10-20% of total portfolio
        
        **Market Outlook:** Favor industrial, data centers, and residential over retail.
        """
    
    def _general_response(self, user_profile: Dict) -> str:
        age = user_profile.get('age', 35)
        location = user_profile.get('location', 'Singapore')
        
        return f"""
        🎯 **Personalized Wealth Management Guidance**
        
        Based on your profile (Age: {age}, Location: {location}):
        
        **Priority Actions:**
        1. **Emergency Fund:** 6-12 months expenses in high-yield savings
        2. **Retirement Savings:** Maximize tax-advantaged accounts
        3. **Core Portfolio:** Build diversified foundation with low-cost index funds
        4. **Risk Management:** Adequate insurance coverage
        
        **Investment Principles:**
        • Start early, invest consistently
        • Keep costs low (expense ratios <0.5%)
        • Stay disciplined during market volatility
        • Rebalance regularly
        • Focus on long-term goals
        
        **Next Steps:**
        • Define specific financial goals with timelines
        • Assess risk tolerance honestly
        • Create investment policy statement
        • Automate investing process
        
        **Remember:** Time in the market beats timing the market!
        
        Would you like me to elaborate on any specific aspect of your wealth management strategy?
        """
