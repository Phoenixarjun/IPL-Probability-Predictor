import streamlit as st 
import pickle as pkl 
import pandas as pd 
from PIL import Image
import requests
from io import BytesIO

# Set wide page layout
st.set_page_config(layout="wide", page_title="IPL Win Predictor", page_icon="🏏")

# Custom CSS for styling
st.markdown("""
<style>
    .title {
        color: #FFD700;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .team-card {
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s;
        text-align: center;
    }
    .team-card:hover {
        transform: translateY(-5px);
    }
    .progress-container {
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .progress-bar {
        height: 30px;
        border-radius: 15px;
        margin-bottom: 10px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .progress-fill {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
        font-weight: bold;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .team-logo {
        width: 80px;
        height: 80px;
        object-fit: contain;
        margin: 0 auto 10px;
        display: block;
    }
    .prediction-result {
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FFA500, #FF8C00);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: bold;
        transition: all 0.3s;
        width: auto;
        margin: 0 auto;
        display: block;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255,165,0,0.4);
    }
    .stNumberInput>div>div>input {
        text-align: center;
    }
    .result-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
    }
    .team-result {
        flex: 1;
        text-align: center;
        padding: 20px;
    }
    .win-message {
        background: linear-gradient(45deg, #4CAF50, #2E7D32);
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .match-info {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title of the page
st.markdown('<div class="title">🏏 IPL Win Predictor</div>', unsafe_allow_html=True)

# Team logos mapping
team_logos = {
    "Chennai Super Kings": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/1200px-Chennai_Super_Kings_Logo.svg.png",
    "Mumbai Indians": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/1200px-Mumbai_Indians_Logo.svg.png",
    "Royal Challengers Bangalore": "https://www.royalchallengers.com/themes/custom/rcbbase/images/rcb-logo-new.png",
    "Kolkata Knight Riders": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Kolkata_Knight_Riders_Logo.svg/1200px-Kolkata_Knight_Riders_Logo.svg.png",
    "Delhi Capitals": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Delhi_Capitals.svg/1200px-Delhi_Capitals.svg.png",
    "Punjab Kings": "https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg",
    "Rajasthan Royals": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/This_is_the_logo_for_Rajasthan_Royals%2C_a_cricket_team_playing_in_the_Indian_Premier_League_%28IPL%29.svg/1024px-This_is_the_logo_for_Rajasthan_Royals%2C_a_cricket_team_playing_in_the_Indian_Premier_League_%28IPL%29.svg.png",
    "Sunrisers Hyderabad": "https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Sunrisers_Hyderabad_Logo.svg/1280px-Sunrisers_Hyderabad_Logo.svg.png",
    "Gujarat Titans": "https://images.seeklogo.com/logo-png/43/1/gujarat-titans-ipl-logo-png_seeklogo-431226.png",
}

# Team colors mapping
team_colors = {
    "Chennai Super Kings": "#FDB913",
    "Mumbai Indians": "#004BA0",
    "Royal Challengers Bangalore": "#EC1C24",
    "Kolkata Knight Riders": "#3A225D",
    "Delhi Capitals": "#004C93",
    "Punjab Kings": "#AA4545",
    "Rajasthan Royals": "#FF5DA2",
    "Sunrisers Hyderabad": "#FB643E",
    "Gujarat Titans": "#008C45",
}

# Importing data and model from pickle
teams = pkl.load(open('./Models/team.pkl','rb'))
cities = pkl.load(open('./Models/city.pkl','rb'))
model = pkl.load(open('./Models/model.pkl','rb'))

# First Row - Team Selection
col1, col2, col3 = st.columns(3)
with col1: 
    batting_team = st.selectbox('Select the batting team', sorted(teams))
    try:
        batting_logo = Image.open(BytesIO(requests.get(team_logos[batting_team]).content))
        st.image(batting_logo, width=100)
    except:
        st.write("")

with col2: 
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))
    try:
        bowling_logo = Image.open(BytesIO(requests.get(team_logos[bowling_team]).content))
        st.image(bowling_logo, width=100)
    except:
        st.write("")

with col3: 
    selected_city = st.selectbox('Select the host city', sorted(cities))

# Second Row - Match Situation
st.subheader("Match Situation")
target = st.number_input('Target Score', min_value=0, max_value=720, step=1)

col4, col5, col6 = st.columns(3)
with col4:
    score = st.number_input('Current Score', min_value=0, max_value=720, step=1)
with col5:
    overs = st.number_input('Overs Completed', min_value=0, max_value=20, step=1)
with col6: 
    wickets = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1)

# Prediction Button (smaller size)
if st.button('Predict Win Probabilities'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score/overs if overs > 0 else 0
    rrr = (runs_left*6)/balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team], 
        'bowling_team': [bowling_team], 
        'city': [selected_city], 
        'Score': [score],
        'Wickets': [wickets_left],
        'Remaining Balls': [balls_left], 
        'target_left': [runs_left], 
        'crr': [crr], 
        'rrr': [rrr]
    })
    
    result = model.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    # Display results with team logos and progress bars
    st.markdown("---")
    st.markdown('<div class="prediction-result">🏆 Win Probability</div>', unsafe_allow_html=True)
    
    # Result container with team logos and progress bars
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    
    # Batting team result
    st.markdown(f"""
    <div class="team-result">
        <h3>{batting_team}</h3>
        <img src="{team_logos[batting_team]}" class="team-logo" width="100">
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {win*100}%; background: {team_colors.get(batting_team, '#4CAF50')};">
                    {round(win*100)}%
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Bowling team result
    st.markdown(f"""
    <div class="team-result">
        <h3>{bowling_team}</h3>
        <img src="{team_logos[bowling_team]}" class="team-logo" width="100">
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {loss*100}%; background: {team_colors.get(bowling_team, '#F44336')};">
                    {round(loss*100)}%
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Win message with animation
    winning_team = batting_team if win > loss else bowling_team
    winning_percent = max(win, loss) * 100
    
    st.markdown(f"""
    <div class="win-message">
        🎉 Hooray! {winning_team} has {round(winning_percent)}% chance to win! 🎉
    </div>
    """, unsafe_allow_html=True)
    
    # Additional match info
    st.markdown('<div class="match-info">', unsafe_allow_html=True)
    st.subheader("Match Statistics")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("Runs Needed", runs_left)
    with col8:
        st.metric("Balls Remaining", balls_left)
    with col9:
        st.metric("Required Run Rate", f"{rrr:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)