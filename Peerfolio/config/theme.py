import streamlit as st

def apply_dark_theme():
    """Apply custom dark theme styling to the Streamlit app"""
    
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main background and text colors */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a1a 0%, #2a2a2a 100%);
        border-right: 1px solid #333;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* UBS Red accent color */
    .css-1lcbmhc .css-1outpf7 {
        background-color: #E60012;
    }
    
    /* Metrics styling */
    [data-testid="metric-container"] {
        background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
        border: 1px solid #333;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    [data-testid="metric-container"] > div {
        color: #ffffff;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #E60012;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #E60012, #ff1a2e);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(230, 0, 18, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #cc0010, #E60012);
        box-shadow: 0 6px 20px rgba(230, 0, 18, 0.4);
        transform: translateY(-2px);
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 6px;
    }
    
    /* File uploader */
    .css-1cpxqw2 {
        background-color: #2a2a2a;
        border: 2px dashed #E60012;
        border-radius: 10px;
    }
    
    /* Dataframe styling */
    .dataframe {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #333;
        border-radius: 8px;
    }
    
    .streamlit-expanderContent {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-top: none;
    }
    
    /* Radio button styling */
    .stRadio > div {
        background-color: #2a2a2a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        color: #E60012;
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background-color: rgba(40, 167, 69, 0.1);
        border: 1px solid #28a745;
        color: #28a745;
    }
    
    .stError {
        background-color: rgba(220, 53, 69, 0.1);
        border: 1px solid #dc3545;
        color: #dc3545;
    }
    
    .stWarning {
        background-color: rgba(255, 193, 7, 0.1);
        border: 1px solid #ffc107;
        color: #ffc107;
    }
    
    /* Chart containers */
    .js-plotly-plot {
        background-color: transparent !important;
    }
    
    /* Form styling */
    .stForm {
        background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
        border: 1px solid #333;
        border-radius: 10px;
        padding: 2rem;
    }
    
    /* Navigation styling */
    .css-1544g2n {
        color: #ffffff;
    }
    
    /* Loading spinner */
    .stSpinner {
        color: #E60012;
    }
    
    /* Custom animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Professional card styling */
    .professional-card {
        background: linear-gradient(145deg, #2a2a2a, #1a1a1a);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .professional-card:hover {
        border-color: #E60012;
        box-shadow: 0 12px 30px rgba(230, 0, 18, 0.2);
        transform: translateY(-3px);
    }
    
    /* Header gradient text */
    .gradient-text {
        background: linear-gradient(45deg, #E60012, #ff4757);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)
