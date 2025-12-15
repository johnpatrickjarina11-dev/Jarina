import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Cat BMI App",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE INITIALIZATION ---
# We use session_state to manage navigation and data persistence
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'gender' not in st.session_state:
    st.session_state.gender = 'male'
if 'height' not in st.session_state:
    st.session_state.height = 145
if 'weight' not in st.session_state:
    st.session_state.weight = 70
if 'age' not in st.session_state:
    st.session_state.age = 25
if 'bmi_score' not in st.session_state:
    st.session_state.bmi_score = 0.0
if 'bmi_category' not in st.session_state:
    st.session_state.bmi_category = ""
if 'bmi_color' not in st.session_state:
    st.session_state.bmi_color = "#000000"

# --- CUSTOM CSS ---
# This replicates the CSS from your HTML file
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* General App Styling */
    .stApp {
        background-color: #FAFAFA;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        border-radius: 30px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.1s;
    }
    
    div.stButton > button:active {
        transform: scale(0.98);
    }

    /* Pink Button Style (Primary) */
    .pink-btn button {
        background-color: #FFB6C1 !important;
        color: white !important;
    }
    
    /* Purple Button Style */
    .purple-btn button {
        background: linear-gradient(135deg, #E0B0FF, #DA70D6) !important;
        color: white !important;
    }

    /* Cards */
    .card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Inputs */
    .stTextInput > div > div > input {
        background-color: #FFE4E1;
        border: none;
        border-radius: 12px;
        color: #333;
    }
    
    /* Slider */
    div[data-baseweb="slider"] > div > div > div > div {
        background-color: #E0B0FF !important;
    }

    /* Navigation Headers */
    .nav-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .gender-box {
        cursor: pointer;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid transparent;
        transition: 0.3s;
    }
    
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def calculate_bmi():
    h_m = st.session_state.height / 100
    bmi = st.session_state.weight / (h_m * h_m)
    st.session_state.bmi_score = round(bmi, 1)
    
    if bmi < 18.5:
        st.session_state.bmi_category = "Underweight"
        st.session_state.bmi_color = "#60A5FA" # Blue
    elif 18.5 <= bmi <= 24.9:
        st.session_state.bmi_category = "Healthy"
        st.session_state.bmi_color = "#4ADE80" # Green
    elif 25 <= bmi <= 29.9:
        st.session_state.bmi_category = "Overweight"
        st.session_state.bmi_color = "#FACC15" # Yellow
    else:
        st.session_state.bmi_category = "Obese"
        st.session_state.bmi_color = "#F87171" # Red
        
    navigate_to('result')

# --- SCREENS ---

def show_welcome():
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <div style='width: 100px; height: 100px; background-color: #60A5FA; border-radius: 25px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 40px; box-shadow: 0 10px 20px rgba(96, 165, 250, 0.3);'>
                ⚖️
            </div>
            <h1 style='color: #333; font-size: 24px; margin-top: 20px;'>BMI CHECKER</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
        if st.button("Get Started"):
            navigate_to('signup')
        st.markdown('</div>', unsafe_allow_html=True)

def show_signup():
    st.markdown("## Welcome on board!")
    st.markdown("<p style='color: #aaa; font-size: 12px;'>Let's work together to achieve your goal</p>", unsafe_allow_html=True)
    
    st.text_input("Full Name", placeholder="Enter your full name", label_visibility="collapsed")
    st.text_input("Email", placeholder="Enter your email", label_visibility="collapsed")
    st.text_input("Password", placeholder="Enter password", type="password", label_visibility="collapsed")
    st.text_input("Confirm Password", placeholder="Confirm password", type="password", label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Sign up"):
        navigate_to('otp')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; font-size: 12px; color: #60A5FA; margin-top: 10px; cursor: pointer;'>
            Already have an account? Sign In
        </div>
    """, unsafe_allow_html=True)

def show_otp():
    if st.button("← Back", key='back_otp'):
        navigate_to('signup')
        
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("### Let's get you back in")
    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=200", width=120)
    st.markdown("</div>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    with cols[0]: st.text_input("1", value="1", label_visibility="collapsed")
    with cols[1]: st.text_input("2", value="2", label_visibility="collapsed")
    with cols[2]: st.text_input("3", value="3", label_visibility="collapsed")
    with cols[3]: st.text_input("4", value="4", label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Verify OTP"):
        navigate_to('profile')
    st.markdown('</div>', unsafe_allow_html=True)

def show_profile():
    if st.button("← Back", key='back_prof'):
        navigate_to('otp')
        
    st.markdown("<h3 style='text-align: center;'>Profile</h3>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <img src='https://images.unsplash.com/photo-1543852786-1cf6624b9987?w=200' style='width: 120px; height: 120px; border-radius: 50%; border: 4px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); object-fit: cover;'>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Username:**")
    st.info("John Patrick Jarina")
    
    st.markdown("**Email:**")
    st.info("johnpatrickjarina@gmail.com")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Save & Continue"):
        navigate_to('dashboard')
    st.markdown('</div>', unsafe_allow_html=True)

def show_dashboard():
    st.markdown("<p style='color: #aaa; font-weight: bold; font-size: 12px; margin-bottom: 0;'>GOOD MORNING</p>", unsafe_allow_html=True)
    st.markdown("### John Patrick Jarina")
    
    # Calculate Card
    st.markdown("""
    <div style='background-color: #FFE4E1; border-radius: 20px; padding: 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
        <div>
            <h3 style='margin: 0; font-size: 18px;'>Calculate your BMI</h3>
            <p style='margin: 5px 0 0 0; font-size: 12px; color: #d68a98;'>Check your health stats</p>
        </div>
        <div style='font-size: 40px;'>📊</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Go to Calculator"):
        navigate_to('calculator')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Cat Image Card
    st.markdown("""
    <div class='card'>
        <img src='https://images.unsplash.com/photo-1513245543132-31f507417b26?w=200' style='width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 10px;'>
        <p style='color: #888; margin: 0;'>Keep Healthy!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bottom Nav simulation
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🏠", key="nav_home")
    with col2:
        if st.button("📊", key="nav_res"):
            navigate_to('result')
    with col3:
        if st.button("⚙️", key="nav_more"):
            navigate_to('more')

def show_calculator():
    if st.button("← Back", key='back_calc'):
        navigate_to('dashboard')
        
    st.markdown("<h3 style='text-align: center;'>BMI CALCULATOR</h3>", unsafe_allow_html=True)
    
    # Gender Selection
    col_male, col_female = st.columns(2)
    
    # Logic to style selected gender
    m_bg = "#FFF0F5" if st.session_state.gender == 'male' else "white"
    m_border = "#FF69B4" if st.session_state.gender == 'male' else "transparent"
    f_bg = "#FFF0F5" if st.session_state.gender == 'female' else "white"
    f_border = "#FF69B4" if st.session_state.gender == 'female' else "transparent"

    with col_male:
        if st.button("♂ Male"):
            st.session_state.gender = 'male'
            st.rerun()
            
    with col_female:
        if st.button("♀ Female"):
            st.session_state.gender = 'female'
            st.rerun()
            
    st.caption(f"Selected: {st.session_state.gender.capitalize()}")

    # Height Slider
    st.markdown("""
    <div class='card' style='margin-top: 20px;'>
        <p style='color: #aaa; font-weight: bold; font-size: 12px;'>HEIGHT (cm)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.height = st.slider("Height", 100, 220, st.session_state.height, label_visibility="collapsed")
    st.markdown(f"<h2 style='text-align: center; color: #8A2BE2;'>{st.session_state.height} <small>cm</small></h2>", unsafe_allow_html=True)

    # Weight and Age
    col_w, col_a = st.columns(2)
    
    with col_w:
        st.markdown("<div class='card' style='padding: 10px;'><p style='color: #aaa; font-size: 10px; font-weight: bold;'>WEIGHT</p></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{st.session_state.weight}</h3>", unsafe_allow_html=True)
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            if st.button("-", key="w_minus"): st.session_state.weight -= 1; st.rerun()
        with sub_c2:
            if st.button("+", key="w_plus"): st.session_state.weight += 1; st.rerun()

    with col_a:
        st.markdown("<div class='card' style='padding: 10px;'><p style='color: #aaa; font-size: 10px; font-weight: bold;'>AGE</p></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{st.session_state.age}</h3>", unsafe_allow_html=True)
        sub_c3, sub_c4 = st.columns(2)
        with sub_c3:
            if st.button("-", key="a_minus"): st.session_state.age -= 1; st.rerun()
        with sub_c4:
            if st.button("+", key="a_plus"): st.session_state.age += 1; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="purple-btn">', unsafe_allow_html=True)
    if st.button("Calculate BMI"):
        calculate_bmi()
    st.markdown('</div>', unsafe_allow_html=True)

def show_result():
    col_top, col_title, col_dum = st.columns([1, 4, 1])
    with col_top:
        if st.button("←", key='back_res'):
            navigate_to('calculator')
    with col_title:
        st.markdown("<h3 style='text-align: center; margin-top: 0;'>BMI RESULT</h3>", unsafe_allow_html=True)

    color = st.session_state.bmi_color
    score = st.session_state.bmi_score
    cat = st.session_state.bmi_category

    st.markdown(f"""
    <div style='background: white; border-radius: 30px; padding: 40px 20px; text-align: center; box-shadow: 0 5px 20px rgba(0,0,0,0.05);'>
        <div style='
            width: 200px; 
            height: 200px; 
            border-radius: 50%; 
            border: 15px solid {color};
            margin: 0 auto 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        '>
            <span style='font-size: 48px; font-weight: bold; color: #333;'>{score}</span>
        </div>
        <p style='font-size: 18px;'>You have <span style='color: {color}; font-weight: bold;'>{cat}</span> body weight!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Details"):
        navigate_to('details')
    st.markdown('</div>', unsafe_allow_html=True)

def show_details():
    if st.button("← Back", key='back_det'):
        navigate_to('result')
        
    st.markdown("<h3 style='text-align: center;'>SUMMARY</h3>", unsafe_allow_html=True)
    
    color = st.session_state.bmi_color
    score = st.session_state.bmi_score
    cat = st.session_state.bmi_category

    # User Result
    st.markdown(f"""
    <div style='background: white; border-radius: 20px; padding: 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);'>
        <span style='color: #888;'>Your BMI</span>
        <span style='font-size: 24px; font-weight: bold;'>{score}</span>
        <span style='background-color: {color}33; color: {color}; padding: 5px 15px; border-radius: 15px; font-weight: bold; font-size: 12px;'>{cat}</span>
    </div>
    """, unsafe_allow_html=True)

    # Reference Table
    st.markdown("""
    <div style='background: white; border-radius: 20px; padding: 25px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); font-size: 14px;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 15px;'>
            <span style='color: #888;'>Less than 18.5</span>
            <span style='color: #60A5FA; font-weight: bold;'>Underweight</span>
        </div>
        <div style='display: flex; justify-content: space-between; margin-bottom: 15px;'>
            <span style='color: #888;'>18.5 to 24.9</span>
            <span style='color: #4ADE80; font-weight: bold;'>Healthy</span>
        </div>
        <div style='display: flex; justify-content: space-between; margin-bottom: 15px;'>
            <span style='color: #888;'>25 to 29.9</span>
            <span style='color: #FACC15; font-weight: bold;'>Overweight</span>
        </div>
        <div style='display: flex; justify-content: space-between;'>
            <span style='color: #888;'>30 or above</span>
            <span style='color: #F87171; font-weight: bold;'>Obese</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Save Results & More"):
        navigate_to('more')
    st.markdown('</div>', unsafe_allow_html=True)

def show_more():
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <img src='https://images.unsplash.com/photo-1519052537078-e6302a4968ef?w=200' style='width: 150px; height: 150px; border-radius: 20px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.15);'>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ About Us")
    st.warning("★ Rate Us")
    
    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    if st.button("Sign Out"):
        # Reset state for clean exit
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = 'welcome'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        navigate_to('dashboard')

# --- MAIN CONTROLLER ---

if st.session_state.page == 'welcome':
    show_welcome()
elif st.session_state.page == 'signup':
    show_signup()
elif st.session_state.page == 'otp':
    show_otp()
elif st.session_state.page == 'profile':
    show_profile()
elif st.session_state.page == 'dashboard':
    show_dashboard()
elif st.session_state.page == 'calculator':
    show_calculator()
elif st.session_state.page == 'result':
    show_result()
elif st.session_state.page == 'details':
    show_details()
elif st.session_state.page == 'more':
    show_more()