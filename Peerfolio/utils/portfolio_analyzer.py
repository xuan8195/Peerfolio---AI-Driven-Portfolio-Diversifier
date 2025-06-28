import pandas as pd
import numpy as np
from typing import Dict, List
import yfinance as yf

class PortfolioAnalyzer:
    """Advanced portfolio analysis with AI-powered insights"""
    
    def __init__(self):
        self.sector_mapping = {
            'AAPL': 'Technology',
            'MSFT': 'Technology', 
            'GOOGL': 'Technology',
            'AMZN': 'Consumer Discretionary',
            'TSLA': 'Consumer Discretionary',
            'NVDA': 'Technology',
            'META': 'Technology',
            'BRK-B': 'Financial Services',
            'UNH': 'Healthcare',
            'JNJ': 'Healthcare',
            'V': 'Financial Services',
            'WMT': 'Consumer Staples',
            'JPM': 'Financial Services',
            'PG': 'Consumer Staples',
            'MA': 'Financial Services',
            'HD': 'Consumer Discretionary',
            'CVX': 'Energy',
            'ABBV': 'Healthcare',
            'KO': 'Consumer Staples',
            'BAC': 'Financial Services',
            'PFE': 'Healthcare',
            'AVGO': 'Technology',
            'PEP': 'Consumer Staples',
            'TMO': 'Healthcare',
            'COST': 'Consumer Staples',
            'DIS': 'Communication Services',
            'ABT': 'Healthcare',
            'VZ': 'Communication Services',
            'ADBE': 'Technology',
            'WFC': 'Financial Services'
        }
        
        self.esg_scores = {
            'AAPL': 8.5, 'MSFT': 9.2, 'GOOGL': 7.8, 'AMZN': 6.9,
            'TSLA': 8.8, 'NVDA': 7.5, 'META': 6.2, 'BRK-B': 7.0,
            'UNH': 7.3, 'JNJ': 8.1, 'V': 7.8, 'WMT': 6.5,
            'JPM': 7.2, 'PG': 8.9, 'MA': 7.6, 'HD': 7.4,
            'CVX': 4.2, 'ABBV': 7.8, 'KO': 6.8, 'BAC': 6.9
        }

    def analyze(self, portfolio_df: pd.DataFrame, user_profile: Dict) -> Dict:
        """Comprehensive portfolio analysis"""
        
        # Calculate basic metrics
        portfolio_df['Market_Value'] = portfolio_df['Shares'] * portfolio_df['Current_Price']
        portfolio_df['Cost_Basis'] = portfolio_df['Shares'] * portfolio_df['Purchase_Price']
        portfolio_df['P&L'] = portfolio_df['Market_Value'] - portfolio_df['Cost_Basis']
        portfolio_df['Return_%'] = (portfolio_df['P&L'] / portfolio_df['Cost_Basis']) * 100
        
        total_value = portfolio_df['Market_Value'].sum()
        total_cost = portfolio_df['Cost_Basis'].sum()
        total_return = ((total_value - total_cost) / total_cost) * 100
        
        # Sector allocation
        portfolio_df['Sector'] = portfolio_df['Symbol'].map(
            lambda x: self.sector_mapping.get(x, 'Other')
        )
        sector_allocation = portfolio_df.groupby('Sector')['Market_Value'].sum().to_dict()
        
        # Diversification analysis
        diversification_score = self.calculate_diversification_score(sector_allocation, total_value)
        
        # Risk assessment
        risk_metrics = self.assess_risk(portfolio_df, user_profile)
        
        # ESG scoring
        esg_score = self.calculate_esg_score(portfolio_df)
        
        # Generate recommendations
        recommendations = self.generate_recommendations(
            portfolio_df, sector_allocation, diversification_score, risk_metrics, user_profile
        )
        
        # Holdings analysis for charts
        holdings_data = self.analyze_holdings(portfolio_df)
        
        return {
            'total_value': total_value,
            'total_return': total_return,
            'diversification_score': diversification_score,
            'risk_level': risk_metrics['level'],
            'risk_score': risk_metrics['score'],
            'esg_score': esg_score,
            'sector_allocation': sector_allocation,
            'recommendations': recommendations,
            'holdings_risk': holdings_data['risk'],
            'holdings_return': holdings_data['return'],
            'holdings_symbols': holdings_data['symbols']
        }

    def calculate_diversification_score(self, sector_allocation: Dict, total_value: float) -> float:
        """Calculate portfolio diversification score (0-10)"""
        if not sector_allocation or total_value == 0:
            return 0.0
        
        # Calculate concentration (Herfindahl index)
        weights = [value / total_value for value in sector_allocation.values()]
        herfindahl = sum(w**2 for w in weights)
        
        # Convert to diversification score (lower concentration = higher score)
        max_herfindahl = 1.0  # Completely concentrated
        min_herfindahl = 1.0 / len(weights) if len(weights) > 0 else 1.0  # Perfectly diversified
        
        if max_herfindahl == min_herfindahl:
            return 10.0
        
        normalized = (max_herfindahl - herfindahl) / (max_herfindahl - min_herfindahl)
        return min(10.0, max(0.0, normalized * 10))

    def assess_risk(self, portfolio_df: pd.DataFrame, user_profile: Dict) -> Dict:
        """Assess portfolio risk level"""
        # Simple risk assessment based on sector concentration and volatility proxies
        tech_weight = 0
        total_value = portfolio_df['Market_Value'].sum()
        
        if total_value > 0:
            tech_symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'META', 'ADBE']
            tech_value = portfolio_df[portfolio_df['Symbol'].isin(tech_symbols)]['Market_Value'].sum()
            tech_weight = tech_value / total_value
        
        # Risk scoring logic
        risk_score = tech_weight * 100  # Higher tech concentration = higher risk
        
        if risk_score < 30:
            risk_level = "Low"
        elif risk_score < 60:
            risk_level = "Moderate"
        else:
            risk_level = "High"
        
        return {
            'level': risk_level,
            'score': f"{risk_score:.1f}/100",
            'tech_concentration': tech_weight
        }

    def calculate_esg_score(self, portfolio_df: pd.DataFrame) -> float:
        """Calculate weighted ESG score for portfolio"""
        total_value = portfolio_df['Market_Value'].sum()
        if total_value == 0:
            return 5.0
        
        weighted_score = 0
        for _, row in portfolio_df.iterrows():
            symbol = row['Symbol']
            weight = row['Market_Value'] / total_value
            esg_score = self.esg_scores.get(symbol, 5.0)  # Default neutral score
            weighted_score += weight * esg_score
        
        return weighted_score

    def analyze_holdings(self, portfolio_df: pd.DataFrame) -> Dict:
        """Analyze individual holdings for risk/return visualization"""
        # Mock risk/return data for visualization
        risk_data = []
        return_data = []
        symbols = []
        
        for _, row in portfolio_df.iterrows():
            symbol = row['Symbol']
            return_pct = row['Return_%']
            
            # Mock risk calculation (in reality, would use historical volatility)
            risk = abs(np.random.normal(15, 5))  # Mock volatility
            
            risk_data.append(risk)
            return_data.append(return_pct)
            symbols.append(symbol)
        
        return {
            'risk': risk_data,
            'return': return_data,
            'symbols': symbols
        }

    def generate_recommendations(self, portfolio_df: pd.DataFrame, sector_allocation: Dict, 
                               diversification_score: float, risk_metrics: Dict, 
                               user_profile: Dict) -> List[str]:
        """Generate actionable portfolio recommendations"""
        recommendations = []
        
        # Diversification recommendations
        if diversification_score < 5:
            recommendations.append(
                "🎯 **Improve Diversification**: Your portfolio is heavily concentrated. "
                "Consider adding holdings from underrepresented sectors."
            )
        
        # Sector-specific recommendations
        total_value = portfolio_df['Market_Value'].sum()
        if total_value > 0:
            for sector, value in sector_allocation.items():
                weight = value / total_value
                if weight > 0.4:  # Over 40% concentration
                    recommendations.append(
                        f"⚖️ **Reduce {sector} Exposure**: {weight:.1%} allocation is high. "
                        f"Consider rebalancing to reduce concentration risk."
                    )
        
        # Risk-based recommendations
        if risk_metrics['level'] == 'High' and user_profile.get('investment_style') == 'Conservative':
            recommendations.append(
                "🛡️ **Risk Mismatch**: Your portfolio has high risk but you prefer conservative investments. "
                "Consider adding bonds or defensive stocks."
            )
        
        # ESG recommendations
        esg_score = self.calculate_esg_score(portfolio_df)
        if esg_score < 6 and user_profile.get('investment_style') == 'ESG-focused':
            recommendations.append(
                "🌱 **ESG Enhancement**: Consider adding more sustainable investments "
                "to align with your ESG preferences."
            )
        
        # Age-based recommendations
        age = user_profile.get('age', 35)
        if age < 40:
            recommendations.append(
                "🚀 **Growth Focus**: At your age, consider increasing exposure to growth stocks "
                "and emerging technologies for long-term wealth building."
            )
        elif age > 50:
            recommendations.append(
                "🏛️ **Stability Focus**: Consider increasing allocation to dividend-paying stocks "
                "and bonds for income generation and capital preservation."
            )
        
        if not recommendations:
            recommendations.append(
                "✅ **Well-Balanced Portfolio**: Your portfolio shows good diversification "
                "and aligns well with your investment profile."
            )
        
        return recommendations
