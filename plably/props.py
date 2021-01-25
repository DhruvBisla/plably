import plotly.graph_objects as go
import numpy as np

def splitName(name : str) -> (str, str):
        vertical, horizontal = name.split(" vs. ")
        return vertical, horizontal

def data(x : np.ndarray, y : np.ndarray, xuncert: np.ndarray, yuncert : np.ndarray) -> go.Scatter :
    return go.Scatter(
        x = x, 
        y = y,
        showlegend = False,
        marker = dict(
            color = '#F6E83E',
            size = 11,
        ),
        mode='markers',
        error_y = dict(
            type = 'data',
            symmetric = True,
            array = yuncert
        ),
        error_x = dict(
            type = 'data',
            symmetric = True,
            array = xuncert
        )
    )

def layout(title : str, trline : np.ndarray, corrcoef : np.float64, avx : np.float64, avy : np.float64, maxx : np.float64, maxy : np.float64) -> go.Layout:
    vtitle, htitle = splitName(title)
    return go.Layout(
        title = go.layout.Title(
            text = title,
            y = 0.9,
            x = 0.5,
            xanchor = 'center',
            yanchor = 'top',
            font=dict(family = 'Raleway', color = '#FFFFFF', size = 25),
        ),
        annotations = [go.layout.Annotation(
            showarrow = False,
            text = 'F(x) = {}x + {}  r²={}'.format(round(trline[0], 4), round(trline[1], 4), round(corrcoef, 4)),
            xanchor = 'center',
            x = avx,
            yanchor = 'top',
            y = maxy+(0.1 * avy),
            font=dict(family = 'Raleway', color = '#2DCEF7', size = 20)
        )],
        xaxis = dict(
            tickfont=dict(family = 'Raleway', color = '#BFBFBF', size = 14),
            title = htitle,
            showgrid = True,
            zeroline = True,
            showline = True,
            zerolinecolor = '#3F4148',
            zerolinewidth =  2.75,
            linecolor = '#1EA676',
            linewidth = 2.75,
            showticklabels = True,
            gridcolor = '#3F4148',
            gridwidth = 2,
            titlefont = dict(
                color = 'white'
            )
        ),
        yaxis = dict(
            zeroline = True,
            tickfont = dict(family = 'Raleway', color = '#BFBFBF', size = 14),
            gridcolor = '#3F4148',
            gridwidth = 2,
            linecolor = '#1EA676',
            linewidth = 2.75,
            zerolinecolor = '#3F4148',
            zerolinewidth =  2.75,
            title = vtitle,
            titlefont = dict(
                color = 'white'
            ),
        ),
        plot_bgcolor = 'rgba(42,45,53,100)',
        paper_bgcolor = 'rgba(42,45,53,100)'
    )

def trendline(rng : np.ndarray, trline : np.ndarray) -> go.Scatter:
    return go.Scatter(
        x = rng,
        y = ((trline[0] * rng) + trline[1]),
        mode = "lines",
        line = go.scatter.Line(color = "#2DCEF7"),
        showlegend = False
    )
