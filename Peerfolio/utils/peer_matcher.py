import pandas as pd
import numpy as np
from typing import Dict, List
import random

class PeerMatcher:
    """AI-powered peer matching system for HNWIs"""
    
    def __init__(self):
        # Sample peer database (in production, this would be from a secure database)
        self.peer_database = self._generate_peer_database()
    
    def _generate_peer_database(self) -> List[Dict]:
        """Generate sample peer data for demonstration"""
        locations = ["Singapore", "Hong Kong", "Switzerland", "New York", "London", "Dubai"]
        strategies = [
            "Growth-Focused Tech", "Diversified Blue-Chip", "ESG-Sustainable", 
            "Crypto-Enhanced", "Dividend Income", "Emerging Markets",
            "Real Estate Heavy", "Index Fund Core", "Active Trading"
        ]
        sectors = ["Technology", "Healthcare", "Financial Services", "Real Estate", "Energy", "Consumer"]
        
        peers = []
        for i in range(500):  # Generate 500 sample peers
            age = random.randint(25, 65)
            location = random.choice(locations)
            
            # Generate net worth based on realistic distributions
            net_worth_ranges = [
                "$1M - $2.5M", "$2.5M - $5M", "$5M - $10M", 
                "$10M - $25M", "$25M+"
            ]
            net_worth = random.choice(net_worth_ranges)
            
            strategy = random.choice(strategies)
            performance = np.random.normal(8.5, 12.0)  # Average 8.5% with volatility
            
            # Generate realistic portfolio allocation
            allocation = self._generate_allocation(strategy)
            
            peer = {
                'id': f"peer_{i:03d}",
                'age': age,
                'location': location,
                'net_worth': net_worth,
                'strategy': strategy,
                'performance': performance,
                'top_sector': max(allocation, key=allocation.get),
                'risk_level': random.choice(["Low", "Moderate", "High"]),
                'allocation': allocation,
                'years_experience': random.randint(1, 20),
                'investment_style': random.choice([
                    "Conservative", "Moderate", "Aggressive", 
                    "Crypto-focused", "ESG-focused", "Tech-focused"
                ])
            }
            peers.append(peer)
        
        return peers
    
    def _generate_allocation(self, strategy: str) -> Dict[str, float]:
        """Generate portfolio allocation based on strategy"""
        if "Tech" in strategy:
            return {
                "Technology": 45,
                "Healthcare": 20,
                "Financial Services": 15,
                "Consumer": 10,
                "Real Estate": 5,
                "Other": 5
            }
        elif "ESG" in strategy:
            return {
                "Technology": 25,
                "Healthcare": 20,
                "Renewable Energy": 25,
                "Financial Services": 15,
                "Consumer": 10,
                "Other": 5
            }
        elif "Crypto" in strategy:
            return {
                "Cryptocurrency": 30,
                "Technology": 25,
                "Financial Services": 20,
                "Healthcare": 15,
                "Other": 10
            }
        elif "Real Estate" in strategy:
            return {
                "Real Estate": 40,
                "Financial Services": 25,
                "Technology": 15,
                "Healthcare": 10,
                "Consumer": 5,
                "Other": 5
            }
        elif "Dividend" in strategy:
            return {
                "Financial Services": 30,
                "Utilities": 25,
                "Consumer Staples": 20,
                "Healthcare": 15,
                "Technology": 5,
                "Other": 5
            }
        else:  # Diversified
            return {
                "Technology": 25,
                "Healthcare": 20,
                "Financial Services": 20,
                "Consumer": 15,
                "Real Estate": 10,
                "Other": 10
            }
    
    def find_similar_peers(self, user_profile: Dict, max_results: int = 50) -> List[Dict]:
        """Find peers similar to the user based on profile"""
        user_age = user_profile.get('age', 35)
        user_location = user_profile.get('location', 'Singapore')
        user_net_worth = user_profile.get('net_worth', '$2.5M - $5M')
        user_style = user_profile.get('investment_style', 'Moderate')
        
        # Calculate similarity scores for each peer
        scored_peers = []
        for peer in self.peer_database:
            similarity_score = self._calculate_similarity(
                user_profile, peer, user_age, user_location, user_net_worth, user_style
            )
            
            if similarity_score > 0.3:  # Minimum similarity threshold
                peer_with_score = peer.copy()
                peer_with_score['similarity_score'] = similarity_score
                scored_peers.append(peer_with_score)
        
        # Sort by similarity and return top results
        scored_peers.sort(key=lambda x: x['similarity_score'], reverse=True)
        return scored_peers[:max_results]
    
    def _calculate_similarity(self, user_profile: Dict, peer: Dict, 
                            user_age: int, user_location: str, 
                            user_net_worth: str, user_style: str) -> float:
        """Calculate similarity score between user and peer"""
        score = 0.0
        
        # Age similarity (30% weight)
        age_diff = abs(user_age - peer['age'])
        if age_diff <= 5:
            score += 0.3
        elif age_diff <= 10:
            score += 0.2
        elif age_diff <= 15:
            score += 0.1
        
        # Location similarity (20% weight)
        if user_location == peer['location']:
            score += 0.2
        elif self._is_similar_region(user_location, peer['location']):
            score += 0.1
        
        # Net worth similarity (25% weight)
        if user_net_worth == peer['net_worth']:
            score += 0.25
        elif self._is_adjacent_net_worth(user_net_worth, peer['net_worth']):
            score += 0.15
        
        # Investment style similarity (25% weight)
        if user_style == peer['investment_style']:
            score += 0.25
        elif self._is_compatible_style(user_style, peer['investment_style']):
            score += 0.15
        
        return min(score, 1.0)
    
    def _is_similar_region(self, location1: str, location2: str) -> bool:
        """Check if two locations are in similar regions"""
        asia_pacific = ["Singapore", "Hong Kong"]
        europe = ["Switzerland", "London"]
        americas = ["New York"]
        middle_east = ["Dubai"]
        
        regions = [asia_pacific, europe, americas, middle_east]
        
        for region in regions:
            if location1 in region and location2 in region:
                return True
        return False
    
    def _is_adjacent_net_worth(self, net_worth1: str, net_worth2: str) -> bool:
        """Check if net worth ranges are adjacent"""
        ranges = [
            "$1M - $2.5M", "$2.5M - $5M", "$5M - $10M", 
            "$10M - $25M", "$25M+"
        ]
        
        try:
            idx1 = ranges.index(net_worth1)
            idx2 = ranges.index(net_worth2)
            return abs(idx1 - idx2) == 1
        except ValueError:
            return False
    
    def _is_compatible_style(self, style1: str, style2: str) -> bool:
        """Check if investment styles are compatible"""
        compatible_groups = [
            ["Conservative", "Moderate"],
            ["Moderate", "Aggressive"],
            ["Tech-focused", "Aggressive"],
            ["ESG-focused", "Moderate"],
            ["Crypto-focused", "Aggressive"]
        ]
        
        for group in compatible_groups:
            if style1 in group and style2 in group:
                return True
        return False
    
    def get_peer_insights(self, similar_peers: List[Dict]) -> Dict:
        """Generate insights from similar peer data"""
        if not similar_peers:
            return {}
        
        # Calculate aggregate statistics
        avg_performance = np.mean([peer['performance'] for peer in similar_peers])
        top_strategies = {}
        top_sectors = {}
        
        for peer in similar_peers:
            strategy = peer['strategy']
            top_strategies[strategy] = top_strategies.get(strategy, 0) + 1
            
            sector = peer['top_sector']
            top_sectors[sector] = top_sectors.get(sector, 0) + 1
        
        # Sort by popularity
        popular_strategies = sorted(top_strategies.items(), key=lambda x: x[1], reverse=True)
        popular_sectors = sorted(top_sectors.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'total_peers': len(similar_peers),
            'avg_performance': avg_performance,
            'top_strategy': popular_strategies[0][0] if popular_strategies else "Diversified",
            'top_sector': popular_sectors[0][0] if popular_sectors else "Technology",
            'strategy_distribution': dict(popular_strategies[:5]),
            'sector_distribution': dict(popular_sectors[:5])
        }
