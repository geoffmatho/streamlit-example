import altair as alt
import pandas as pd
import streamlit as st
from pyAFL.teams import ALL_TEAMS, CURRENT_TEAMS


team1 = st.selectbox("Team 1", CURRENT_TEAMS)

team2 = st.selectbox("Team 2", CURRENT_TEAMS)

st.write(team1, team2)


filteredPlayers = list(set(team1.players).intersection(team2.players))
st.write(filteredPlayers)