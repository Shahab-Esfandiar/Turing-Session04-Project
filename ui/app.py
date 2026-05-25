import streamlit as st
import sys
import os

# Append the project root to sys.path to allow imports from the core module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.pipeline import Pipeline
from utils.logger import logger

# Initialize Session State variables for language and history
if "lang" not in st.session_state:
    st.session_state.lang = "fa"
if "history" not in st.session_state:
    st.session_state.history = []

def set_language(lang_code: str):
    """Updates the active language in the session state."""
    st.session_state.lang = lang_code

def get_texts() -> dict:
    """Returns localized strings based on the selected language."""
    if st.session_state.lang == "fa":
        return {
            "title": "🪄 اعتبارسنجی جادویی اخبار",
            "tab_main": "✨ بررسی خبر",
            "tab_history": "📜 تاریخچه بررسی‌ها",
            "input_label": "متن خبر یا ادعای خود را اینجا بنویسید...",
            "btn_label": "اعتبارسنجی کن 🚀",
            "loading": "هوش مصنوعی در حال جستجوی وب و کشف حقیقت است...",
            "status": "وضعیت خبر",
            "confidence": "درصد اطمینان",
            "explanation": "تحلیل و استدلال",
            "sources": "منابع موثق",
            "no_history": "هنوز خبری بررسی نشده است.",
            "placeholder_result": "نتیجه اعتبارسنجی در این باکس نمایش داده می‌شود..."
        }
    else:
        return {
            "title": "🪄 Magical News Fact-Checker",
            "tab_main": "✨ Fact Check",
            "tab_history": "📜 History",
            "input_label": "Type the news or claim here...",
            "btn_label": "Validate Now 🚀",
            "loading": "AI is surfing the web to discover the truth...",
            "status": "Claim Status",
            "confidence": "Confidence Score",
            "explanation": "AI Reasoning",
            "sources": "Verified Sources",
            "no_history": "No validations performed yet.",
            "placeholder_result": "Validation result will appear in this box..."
        }

def load_custom_ui_styles():
    """
    Injects custom CSS to apply fancy fonts, symmetric layouts, 
    balance font sizes, and securely disable full-page scrolling.
    """
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Baloo+Bhaijaan+2:wght@400;600;800&family=Lalezar&family=Fredoka:wght@400;500;600&display=swap');

    /* 1. Prevent global page scrolling */
    html, body, .stApp {
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0;
        padding: 0;
    }
    
    /* 2. Lock the main Streamlit container height */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        max-width: 95% !important;
        height: 100vh !important;
        overflow: hidden !important;
    }
    
    /* 3. Style the input text area to look modern */
    .stTextArea textarea {
        border-radius: 15px !important;
        border: 2px solid #e0e0e0 !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
        resize: none !important; /* Disable user resizing */
    }
    
    /* 4. Remove default margin from h1 to align with buttons */
    h1 {
        margin-top: 0 !important;
        padding-top: 0 !important;
        line-height: 1.2 !important;
    }
    """

    if st.session_state.lang == "fa":
        css += """
        /* Persian layout configuration - Increased font size to match English weight */
        html, body, [class*="css"], p, div, span, label, button, .stTextArea textarea {
            font-family: 'Baloo Bhaijaan 2', sans-serif !important;
            direction: rtl !important;
            text-align: right !important;
            font-size: 1.26rem !important; 
        }
        h1, h2, h3, h4, .stTabs [data-baseweb="tab"] {
            font-family: 'Lalezar', cursive !important;
            color: #2c3e50;
        }
        """
    else:
        css += """
        /* English layout configuration */
        html, body, [class*="css"], p, div, span, label, button, .stTextArea textarea {
            font-family: 'Fredoka', sans-serif !important;
            direction: ltr !important;
            text-align: left !important;
            font-size: 1.22rem !important;
        }
        h1, h2, h3, h4, .stTabs [data-baseweb="tab"] {
            font-weight: 600 !important;
            color: #2c3e50;
        }
        """
        
    css += "</style>"
    st.markdown(css, unsafe_allow_html=True)

def main():
    # Set app layout to wide mode for a better split view
    st.set_page_config(page_title="Fact Checker AI", layout="wide", page_icon="🪄")
    load_custom_ui_styles()
    texts = get_texts()

    # Header and Language Toggles
    header_col1, header_col2, header_col3 = st.columns([5, 1, 1])
    
    with header_col1:
        # Title with removed margins via inline CSS
        st.markdown(f"<h1 style='margin:0; padding:0;'>{texts['title']}</h1>", unsafe_allow_html=True)
    
    with header_col2:
        # Added an invisible spacer to push the button down slightly for perfect center alignment
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.button("🇮🇷 فارـسی", type="primary" if st.session_state.lang == "fa" else "secondary", 
                  on_click=set_language, args=("fa",), use_container_width=True)
                  
    with header_col3:
        # Added spacer for alignment
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.button("🇬🇧 English", type="primary" if st.session_state.lang == "en" else "secondary", 
                  on_click=set_language, args=("en",), use_container_width=True)

    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)

    # Main Application Tabs
    tab_main, tab_hist = st.tabs([texts["tab_main"], texts["tab_history"]])

    with tab_main:
        # Strict left-right layout (Input Left, Results Right)
        col_input, col_result = st.columns([1, 1.1], gap="large")

        # LEFT COLUMN: User Input
        with col_input:
            user_claim = st.text_area(label="hidden", label_visibility="collapsed", 
                                      height=320, placeholder=texts["input_label"])
            submit_btn = st.button(texts["btn_label"], type="primary", use_container_width=True)

        # RIGHT COLUMN: Validation Results
        with col_result:
            # Container with fixed height
            with st.container(height=380, border=True):
                if submit_btn:
                    if not user_claim.strip():
                        st.warning("ابتدا متن را وارد کنید." if st.session_state.lang == "fa" else "Enter text first.")
                        logger.warning("Empty input submitted.")
                    else:
                        with st.spinner(texts["loading"]):
                            logger.info("Validation started.")
                            pipeline = Pipeline()
                            result = pipeline.run(user_claim, st.session_state.lang)

                            if "error" in result:
                                st.error(f"Error: {result['error']}")
                            else:
                                # Prepend the result to the session history
                                st.session_state.history.insert(0, {"claim": user_claim, "result": result})

                                # Render structured validation output
                                status_val = result.get('status', 'UNKNOWN')
                                if status_val == "TRUE":
                                    st.success(f"{texts['status']}: {status_val} ✅")
                                elif status_val == "FALSE":
                                    st.error(f"{texts['status']}: {status_val} ❌")
                                else:
                                    st.warning(f"{texts['status']}: {status_val} ⚠️")

                                st.metric(label=texts["confidence"], value=f"{result.get('confidence_score', 0)}%")
                                
                                st.markdown(f"**{texts['explanation']}:**")
                                st.info(result.get('explanation', ''))
                                
                                st.markdown(f"**{texts['sources']}:**")
                                sources = result.get('sources', [])
                                if sources:
                                    for src in sources:
                                        st.markdown(f"🔗 [{src}]({src})")
                                else:
                                    st.write("ندارد" if st.session_state.lang == "fa" else "None")
                else:
                    # Idle placeholder view before a claim is submitted
                    st.markdown(f"<div style='text-align: center; color: #aaa; margin-top: 120px;'>{texts['placeholder_result']}</div>", unsafe_allow_html=True)

    with tab_hist:
        with st.container(height=380, border=True):
            if not st.session_state.history:
                st.info(texts["no_history"])
            else:
                for item in st.session_state.history:
                    with st.expander(f"📌 {item['claim'][:50]}..."):
                        res = item['result']
                        st.write(f"**{texts['status']}:** {res.get('status')}")
                        st.write(f"**{texts['explanation']}:** {res.get('explanation')}")

if __name__ == "__main__":
    main()