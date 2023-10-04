import altair as alt
import pandas as pd
import streamlit as st
from pyAFL.teams import ALL_TEAMS, CURRENT_TEAMS


team1 = st.selectbox("Team 1", CURRENT_TEAMS)

team2 = st.selectbox("Team 2", CURRENT_TEAMS)

st.write(team1, team2)
runIt = st.checkbox("Ready to run?")

if runIt:
    players1 = [p.name for p in team1.players]
    players2 = [p.name for p in team2.players]
    filteredPlayers = list(set(players1).intersection(players2))
    st.write(filteredPlayers)