# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:32:06 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


players = pd.read_csv(r'https://github.com/yaobviously/playerplotter/blob/main/stacked2019to2021.csv?raw=true')
todaysp = pd.read_csv(r'https://github.com/yaobviously/playerplotter/blob/main/fctodayd.csv?raw=true')

playerlist = todaysp['Player'].unique().tolist()


st.sidebar.header('Select Players')
st.write("Player Output Comparisons")

player1 = st.sidebar.selectbox('Player 1', playerlist)
player2 = st.sidebar.selectbox('Player 2', playerlist)
player3 = st.sidebar.selectbox('Player 3', playerlist)


def ecdf(data):
    x = np.sort(data)
    n = np.size(x)
    y = np.arange(1, n+1) / n
    return (x,y)

fig, ax = plt.subplots()

x, y = ecdf(players[players['Player'] == player1]['PlayerFP'])
a, b = ecdf(players[players['Player'] == player2]['PlayerFP'])
c, d = ecdf(players[players['Player'] == player3]['PlayerFP'])
ax.scatter(x=x, y=y, label= player1)
ax.scatter(x=a, y=b, label= player2)
ax.scatter(x=c, y= d, label= player3)
ax.legend(loc='best')


st.pyplot(fig)
