import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime as dt
import numpy as np
#import ta
from pages.utils.plotly_figures import *

# Set page configuration
st.set_page_config(
    page_title="Análisis de Acciones",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Anális de acciones")
col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Ingrese el ticker de la acción (por ejemplo, AAPL, MSFT, GOOGL):", "AAPL")
with col2:
    start_date = st.date_input("Fecha de inicio:", dt.date(2020, 1, 1))
with col3:
    end_date = st.date_input("Fecha de fin:", dt.date.today())

st.subheader(ticker)
 
stock = yf.Ticker(ticker)

st.write(stock.info['longBusinessSummary'])
st.write("**Sector:**",stock.info['sector'])
st.write("**Industria**",stock.info['industry'])
st.write("**País**",stock.info['country'])
st.write("**Página web**",stock.info['website'])

col1, col2 = st.columns(2)
with col1:
    df = pd.DataFrame(index=['Cap. Bursátil', 'Beta', 'Beneficio por Acción (BPA)', 'Ratio PER', 'Rendimiento por Dividendo'])
    df[''] = [stock.info.get('marketCap'), stock.info.get('beta'),
              stock.info.get('trailingEps'), stock.info.get('trailingPE'),
              stock.info.get('dividendYield')]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, width='stretch')
with col2:
    df = pd.DataFrame(index=['Prueba Ácida', 'Ingresos por Acción',
                             'Margen Neto', 'Ratio Deuda/Capital', 'ROE (Retorno sobre el Capital Financiero'])
    df[''] = [stock.info.get('quickRatio'), stock.info.get('revenuePerShare'),
              stock.info.get('profitMargins'), stock.info.get('debtToEquity'),
              stock.info.get('returnOnEquity')]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, width='stretch')

data = yf.download(ticker, start=start_date, end=end_date)

col1, col2, col3 = st.columns(3)
daily_change = data['Close'].iloc[-1].get(ticker) - data['Close'].iloc[-2].get(ticker)
col1.metric("Cambio Diario", str(round(data['Close'].iloc[-1].get(ticker), 2)), str(round(daily_change, 2)))

last_10_df = data.tail(10).sort_index(ascending=False).round(3)
last_10_df.rename(columns={
    'Close': 'Cierre',
    'High': 'Máximo',
    'Low': 'Mínimo',
    'Open': 'Apertura',
    'Volume': 'Volumen'
}, inplace=True)
fig_df = plotly_table(last_10_df)

st.divider()

st.write('#### Datos de los últimos 10 días')
st.plotly_chart(fig_df, width='stretch')

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)

num_period = ''
with col1:
    if st.button("5D"):
        num_period = '5d'
with col2:
    if st.button("1M"):
        num_period = '1m'
with col3:
    if st.button("6M"):
        num_period = '6m'
with col4:
    if st.button("YTD"):
        num_period = 'ytd'
with col5:
    if st.button("1A"):
        num_period = '1a'
with col6:
    if st.button("5A"):
        num_period = '5a'
with col7:
    if st.button("MAX"):
        num_period = 'max'
        
col1, col2, col3 = st.columns(3)

with col1:
    chart_type = st.selectbox("Tipo de gráfico:", ["Candela", "Línea"])
with col2:
    if chart_type == 'Candela':
        indicators = st.selectbox('', ('RSI','MACD'))
    else:
        indicators = st.selectbox('', ('RSI', 'Moving Average', 'MACD'))

ticker = yf.Ticker(ticker)
new_df1 = ticker.history(period='max')
data1 = ticker.history(period='max')
if num_period == '':
    if chart_type == 'Candela' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1, '1a'), width='stretch')
        st.plotly_chart(RSI(data1, '1a'), width='stretch')
    if chart_type == 'Candela' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1, '1a'), width='stretch')
        st.plotly_chart(MACD(data1, '1a'), width='stretch')
    if chart_type == 'Línea' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, '1a'), width='stretch')
        st.plotly_chart(RSI(data1, '1a'), width='stretch')
    if chart_type == 'Línea' and indicators == 'Moving Average':
        st.plotly_chart(close_chart(data1, '1a'), width='stretch')
        st.plotly_chart(Moving_average(data1, '1a'), width='stretch')
    if chart_type == 'Línea' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1, '1a'), width='stretch')
        st.plotly_chart(MACD(data1, '1a'), width='stretch')
    
else:
    if chart_type == 'Candela' and indicators == 'RSI':
        st.plotly_chart(candlestick(new_df1, num_period), width='stretch')
        st.plotly_chart(RSI(new_df1, num_period), width='stretch')
    if chart_type == 'Candela' and indicators == 'MACD':
        st.plotly_chart(candlestick(new_df1, num_period), width='stretch')
        st.plotly_chart(MACD(new_df1, num_period), width='stretch')
    if chart_type == 'Línea' and indicators == 'RSI':
        st.plotly_chart(close_chart(new_df1, num_period), width='stretch')
        st.plotly_chart(RSI(new_df1, num_period), width='stretch')
    if chart_type == 'Línea' and indicators == 'Moving Average':
        st.plotly_chart(close_chart(new_df1, num_period), width='stretch')
        st.plotly_chart(Moving_average(new_df1, num_period), width='stretch')
    if chart_type == 'Línea' and indicators == 'MACD':
        st.plotly_chart(close_chart(new_df1, num_period), width='stretch')
        st.plotly_chart(MACD(new_df1, num_period), width='stretch')