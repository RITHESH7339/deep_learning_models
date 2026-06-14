import streamlit as st
import requests

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Telugu Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CUSTOM CSS - DARK THEME WITH CYAN ACCENTS
# =====================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0a0e27,
        #1a1f3a,
        #0d3d56
    );
}

/* Hide Streamlit Elements */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Buttons */

.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:14px;

    background:linear-gradient(
        90deg,
        #00d9ff,
        #0099cc
    );

    color:#0a0e27;

    font-size:16px;

    font-weight:700;

    transition:0.3s;
}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:
    0px 8px 20px rgba(0, 217, 255, 0.5);
}

/* Text Area */

textarea{
    border-radius:15px !important;
    background: #1a2847 !important;
    color: #e0e6ed !important;
    border: 2px solid #00d9ff !important;
}

/* Stats */

.stats{
    color:#00d9ff;
    font-size:13px;
    margin-top:8px;
}

/* Title */

.title{
    text-align:center;
    color:#00d9ff;
    font-size:48px;
    font-weight:800;
    text-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
}

.subtitle{
    text-align:center;
    color:#0099cc;
    font-size:18px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TRANSLATION FUNCTION
# =====================================================

def translate_to_telugu(text):

    try:

        url = "https://translate.googleapis.com/translate_a/single"

        params = {
            "client": "gtx",
            "sl": "en",
            "tl": "te",
            "dt": "t",
            "q": text
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code == 200:

            response_json = response.json()

            translated_text = "".join(
                chunk[0]
                for chunk in response_json[0]
                if chunk[0]
            )

            return translated_text

        return "Translation service unavailable."

    except Exception as e:

        return f"Connection Error: {str(e)}"

# =====================================================
# HEADER
# =====================================================

st.markdown(
    "<div class='title'>🌍 AI Telugu Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>English ➜ Telugu Neural Translation Engine</div>",
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# MAIN LAYOUT
# =====================================================

col1, col2 = st.columns(2, gap="large")

# =====================================================
# LEFT SIDE
# =====================================================

with col1:

    st.markdown("### 🇺🇸 English Input")

    text = st.text_area(
        "",
        height=260,
        placeholder="Type your English text here..."
    )

    chars = len(text)
    words = len(text.split())

    st.markdown(
        f"""
        <div class='stats'>
        Characters: {chars} | Words: {words}
        </div>
        """,
        unsafe_allow_html=True
    )

    translate_btn = st.button(
        "🚀 Translate Now"
    )

# =====================================================
# RIGHT SIDE
# =====================================================

with col2:

    st.markdown("### 🇮🇳 Telugu Output")

    output_container = st.container(
        border=True
    )

    if translate_btn:

        if not text.strip():

            with output_container:

                st.warning(
                    "Please enter some English text."
                )

        else:

            with st.spinner(
                "Translating..."
            ):

                translated_output = (
                    translate_to_telugu(text)
                )

            with output_container:

                st.success(
                    translated_output
                )

                st.code(
                    translated_output,
                    language=None
                )

                st.download_button(
                    label="📥 Download Translation",
                    data=translated_output,
                    file_name="translation.txt",
                    mime="text/plain"
                )

    else:

        with output_container:

            st.info(
                "Enter English text and click Translate Now."
            )

# =====================================================
# FOOTER
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
"""
<div style='
text-align:center;
color:#0099cc;
font-size:12px;
'>
⚡ Powered by Neural Translation Engine
</div>
""",
unsafe_allow_html=True
)
