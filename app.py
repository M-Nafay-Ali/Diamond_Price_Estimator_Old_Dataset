import streamlit as str
import pandas as pd
import joblib
import time

# 1. Page Configuration
str.set_page_config(
    page_title="GemValue | Premium Diamond Price Predictor",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Custom Stunning Diamond Theme CSS (Shiny effects, premium fonts, custom button)
str.markdown("""
    <style>
    /* Main Background & Font Color */
    .stApp {
        background: linear-gradient(135deg, #0b132b 0%, #1c2541 100%);
        color: #f0f3fa;
    }
    
    /* Luxury Header styling with a diamond sparkle feel */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(45deg, #a4f4f9, #ffffff, #64dfdf, #e0aaff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 6s ease infinite;
        margin-bottom: 5px;
    }
    
    .subtitle {
        text-align: center;
        color: #b0c4de;
        font-size: 1.1rem;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }

    @keyframes shine {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism Container Card for Inputs */
    div.element-container:has(div.input-card), .input-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 25px;
        border: 1px solid rgba(164, 244, 249, 0.15);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }

    /* Premium Shiny Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #4ea8de, #56cfe1, #64dfdf);
        color: #0b132b !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        border: none !important;
        padding: 12px 0px !important;
        border-radius: 30px !important;
        transition: all 0.4s ease-in-out !important;
        box-shadow: 0 0 15px rgba(100, 223, 223, 0.4) !important;
        cursor: pointer;
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 25px rgba(100, 223, 223, 0.8), inset 0 0 10px rgba(255,255,255,0.5) !important;
        background: linear-gradient(45deg, #64dfdf, #7400b8); /* Changes color on hover dynamically */
        color: #ffffff !important;
    }

    /* Footer Branding */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 0.9rem;
        color: #8da9c4;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    .footer span {
        color: #64dfdf;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load the Saved Model safely
@str.cache_resource
def load_model():
    try:
        return joblib.load('best_diamond_pricing_model.pkl')
    except:
        return None

model = load_model()

# 4. App Headers
str.markdown('<div class="main-title">💎 GEMVALUE PREDICTOR</div>', unsafe_allow_html=True)
str.markdown('<div class="subtitle">AI-Powered Premium Diamond Valuation Engine</div>', unsafe_allow_html=True)

if model is None:
    str.error("⚠️ Error: 'best_diamond_pricing_model.pkl' file not found! Please upload it to your repository.")
else:
    # Interactive features: Estimator Info Accordion
    with str.expander("✨ How are Diamond Prices Calculated? (The 4 Cs Info)"):
        str.write("""
        * **Carat:** The physical weight of the diamond. Larger carats increase value exponentially.
        * **Cut:** Quality of the diamond facets (Ideal is best, Fair is lowest).
        * **Color:** Diamond color rating from colorless (D) to light color (J).
        * **Clarity:** Presence of internal flaws (IF/VVS are flawless, SI/I have slight inclusions).
        """)

    str.markdown('### 🛠️ Configure Diamond Specifications')
    
    # 5. Organizing Inputs using interactive sliders and dropdowns
    col1, col2 = str.columns(2)
    
    with col1:
        carat = str.slider("⚖️ Carat Weight", min_value=0.2, max_value=5.5, value=1.0, step=0.01)
        cut = str.selectbox("🎬 Cut Quality", ["Ideal", "Premium", "Very Good", "Good", "Fair"])
        color = str.selectbox("🎨 Color Grade (D is best, J is lowest)", ["D", "E", "F", "G", "H", "I", "J"])
        clarity = str.selectbox("🔍 Clarity Grade", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])

    with col2:
        depth = str.slider("📐 Depth Percentage (%)", min_value=43.0, max_value=79.0, value=61.5, step=0.1)
        table = str.slider("🪟 Table Width (%)", min_value=43.0, max_value=95.0, value=57.0, step=0.1)
        x = str.slider("📏 Length (x) in mm", min_value=0.0, max_value=12.0, value=6.4, step=0.1)
        y = str.slider("📐 Width (y) in mm", min_value=0.0, max_value=59.0, value=6.4, step=0.1)
        z = str.slider("💎 Depth (z) in mm", min_value=0.0, max_value=31.0, value=4.0, step=0.1)

    # Convert user selections into a clean DataFrame matching your pipeline structure
    input_data = pd.DataFrame([{
        'carat': carat, 'cut': cut, 'color': color, 'clarity': clarity,
        'depth': depth, 'table': table, 'x': x, 'y': y, 'z': z
    }])

    str.markdown("---")

    # 6. Prediction Button & Dynamic Animations
    if str.button("✨ VALUATE DIAMOND PRICE"):
        with str.spinner("⚡ Running AI Appraisal Engine..."):
            time.sleep(1.2) # Elegant delay to simulate complex AI calculations
            prediction = model.predict(input_data)[0]
        
        # Display the output inside a beautiful alert/success card
        str.balloons() # Interactive celebratory trigger
        str.markdown(f"""
            <div style="background: rgba(100, 223, 223, 0.1); border-left: 6px solid #64dfdf; padding: 20px; border-radius: 8px; text-align: center; margin-top: 20px;">
                <h3 style="color: #64dfdf; margin: 0; font-size: 1.4rem;">Estimated Valuation</h3>
                <h1 style="color: #ffffff; margin: 10px 0 0 0; font-size: 3rem; font-weight: 800;">${prediction:,.2f} USD</h1>
                <p style="color: #b0c4de; margin: 5px 0 0 0; font-size: 0.9rem;">Market values fluctuate based on physical certificate details.</p>
            </div>
        """, unsafe_allow_html=True)

# 7. Signature Footer with your Name
str.markdown("""
    <div class="footer">
        Crafted with Luxury & Precision by <span>M.Nafay Ali</span><br>
        © 2026 GemValue Engine | All Rights Reserved
    </div>
""", unsafe_allow_html=True)
