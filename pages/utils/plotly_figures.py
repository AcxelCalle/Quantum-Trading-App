import plotly.graph_objects as go
import pandas as pd
import dateutil
import ta
import datetime as dt


import plotly.graph_objects as go

def plotly_table(dataframe):
    headerColor = "#1f8ab4"
    rowEvenColor = 'lightgrey'
    rowOddColor = "#5ab5da"
    row_colors = [rowOddColor if i % 2 == 0 else rowEvenColor for i in range(len(dataframe))]
    
    headers = [""] + list(dataframe.columns.get_level_values(0).unique())
    cell_values = [dataframe.index] + [dataframe[i] for i in dataframe.columns]
    cantidad_columnas = len(dataframe.columns)
    fuentes_celdas = ["Arial Black"] + ["Arial"] * cantidad_columnas
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=headers,
            line_color='darkslategray',
            fill_color=headerColor,
            align=["left", "center"],
            font=dict(color='white', size=12, family="Arial Black"),
            height=30,
        ),
        cells=dict(
            values=cell_values,
            line_color='darkslategray',
            fill_color=[row_colors],
            align=["left", "center"],
            font=dict(color="#0c0c0c", size=13, family=fuentes_celdas), 
            height=30,
        )
    )])
    
    fig.update_layout(
        autosize=False,
        width=1000,
        height=400,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig

def filter_data(dataframe, num_period):
    if num_period == '1m':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6m':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1a':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5a':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = dt.datetime(dataframe.index[-1].year, 1, 1, tzinfo=dataframe.index[-1].tzinfo)
    else:
        date = dataframe.index[0]
        
    return dataframe.reset_index()[dataframe.reset_index()['Date']>date]

def close_chart(dataframe, num_period = False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
                             mode='lines',
                             name='Open',
                             line=dict(width=2, color = "#06be00"))
                  )
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
                                 mode='lines',
                                 name='Close',
                                 line=dict(width=2, color = "#d10000"))
                      )
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
                                 mode='lines',
                                 name='High',
                                 line=dict(width=2, color = "#d3d3d3"))
                      )
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
                                 mode='lines',
                                 name='Low',
                                 line=dict(width=2, color = "#e5ff00"))
                      )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(dict(height =500, margin=dict(l=0,r=20, t=20, b=0), plot_bgcolor = 'black', paper_bgcolor='gray',
                           legend=dict(yanchor='top', xanchor='right')))

    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe['Date'],
                                 open = dataframe['Open'],
                                 high=dataframe['High'],
                                 low=dataframe['Low'],
                                 close=dataframe['Close'])
                  )
    fig.update_layout(showlegend =False, height =500, 
                      margin=dict(l=0, r=20, t=20, b=0),
                      plot_bgcolor='black',
                      paper_bgcolor='gray')
    
    return fig

import plotly.graph_objects as go
import ta

def RSI(dataframe, num_period):
    dataframe['RSI'] = ta.momentum.RSIIndicator(close=dataframe['Close'], window=14).rsi()
    dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['RSI'], 
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70] * len(dataframe),
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30] * len(dataframe),
        fill='tonexty',
        name='Oversold',
        marker_color="#ffffff",
        line=dict(width=2, color="#0f0f0f", dash='dash')
    ))
    
    fig.update_layout(
        yaxis_range=[0, 100],
        height=200, # Corregido: height
        plot_bgcolor='black',
        paper_bgcolor="#0f0f0f",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right', x=1)
    )
    return fig

def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = ta.trend.SMAIndicator(close=dataframe['Close'], window=50).sma_indicator()
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
            x=dataframe['Date'],
            y=dataframe['Open'],
            mode='lines', name='Open', line=dict(width=2, color= "#FDFDFD")
        ))
    fig.add_trace(go.Scatter(
            x=dataframe['Date'],
            y=dataframe['Close'],
            mode='lines', name='Close', line=dict(width=2, color= "#B42222")
        ))
    fig.add_trace(go.Scatter(
            x=dataframe['Date'],
            y=dataframe['High'],
            mode='lines', name='High', line=dict(width=2, color= "#100E85")
        ))
    fig.add_trace(go.Scatter(
            x=dataframe['Date'],
            y=dataframe['Low'],
            mode='lines', name='Low', line=dict(width=2, color= "#FF0000")
        ))
    fig.add_trace(go.Scatter(
            x=dataframe['Date'],
            y=dataframe['SMA_50'],
            mode='lines', name='SMA_50', line=dict(width=2, color= "#E900D5")
        ))
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500, margin=dict(l=0, r=20,t=20,b=0), plot_bgcolor='black', paper_bgcolor="#333634",
                      legend=dict(yanchor='top', xanchor='right')
                      )
    
    return fig

def MACD(dataframe, num_period):
    macd_indicator = ta.trend.MACD(close=dataframe['Close'])
    macd = macd_indicator.macd()               
    macd_signal = macd_indicator.macd_signal() 
    macd_hist = macd_indicator.macd_diff()     
    dataframe['MACD'] = macd
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist
    dataframe = filter_data(dataframe, num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD'],
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD Signal'],
        name='Overbough',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))
    
    c = ['red' if cl < 0 else 'green' for cl in macd_hist]
    
    fig.update_layout(
        height=200, plot_bgcolor='black', paper_bgcolor="#595A53",
        margin = dict(l=0,r=0,t=0,b=0),
        legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right',x=1)
    )
    
    return fig