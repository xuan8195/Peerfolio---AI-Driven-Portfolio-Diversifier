# Peerfolio Configuration Settings

# Application Settings
APP_NAME = "Peerfolio"
APP_VERSION = "1.0.0"
COMPANY = "UBS Digital Innovation"

# UI Configuration
DEFAULT_THEME = "dark"
PRIMARY_COLOR = "#E60012"  # UBS Red
SECONDARY_COLOR = "#ffffff"
BACKGROUND_COLOR = "#0a0a0a"

# Portfolio Analysis Settings
MIN_PORTFOLIO_SIZE = 1000  # Minimum portfolio value
MAX_PORTFOLIO_SIZE = 1000000000  # Maximum portfolio value
DEFAULT_RISK_FREE_RATE = 0.045  # 4.5% risk-free rate

# Peer Matching Settings
MIN_SIMILARITY_SCORE = 0.3  # Minimum similarity to include peers
MAX_PEER_RESULTS = 50  # Maximum number of peers to return
AGE_WEIGHT = 0.3  # Weight for age similarity
LOCATION_WEIGHT = 0.2  # Weight for location similarity
NET_WORTH_WEIGHT = 0.25  # Weight for net worth similarity
STYLE_WEIGHT = 0.25  # Weight for investment style similarity

# AI Advisor Settings
MAX_RECOMMENDATIONS = 10  # Maximum recommendations per category
DEFAULT_MODEL = "gpt-4"  # OpenAI model to use
MAX_TOKENS = 2000  # Maximum tokens for AI responses

# Data Sources
YAHOO_FINANCE_ENABLED = True
ALPHA_VANTAGE_ENABLED = False
POLYGON_ENABLED = False

# Security Settings
SESSION_TIMEOUT = 3600  # 1 hour in seconds
MAX_UPLOAD_SIZE = 10  # Maximum file upload size in MB
ALLOWED_FILE_TYPES = ["csv", "xlsx", "json"]

# Feature Flags
ENABLE_LIVE_DATA = True
ENABLE_AI_CHAT = True
ENABLE_PEER_INSIGHTS = True
ENABLE_MARKET_INTELLIGENCE = True

# Development Settings
DEBUG_MODE = True
LOG_LEVEL = "INFO"
CACHE_ENABLED = True
CACHE_TTL = 300  # 5 minutes cache time-to-live
