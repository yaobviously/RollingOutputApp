# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:32:06 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as seaborn

players = pd.read_csv(r'C:\Learning to Code\code\DailyFantasyCSV\boxscoreappdata.csv')
todaysp = pd.read_csv(r'https://raw.githubusercontent.com/yaobviously/playerplotter/main/slatetoday.csv')
todaysp = todaysp.sort_values(by='Salary', ascending=False)

playerlist = todaysp['Player'].unique().tolist()

default = playerlist[0]

st.sidebar.header('Select Players')
st.write("Player Performance")

player = st.sidebar.selectbox('Player', playerlist)


def rollingplayer(x):
    _df = players[players['Player'] == x].reset_index()
    _df['rollingfp'] = _df['GameFP/36'].rolling(8, min_periods =3).mean()
    _df['rollingusage'] = _df['Usage'].rolling(8, min_periods = 3).mean()
    
    return sb.lineplot(data= _df[['MIN', 'rollingusage', 'PlayerFP', 'rollingfp']], legend= 'brief')

rollingplayer('Isaiah Roby')


