import plotly.graph_objects as go
import numpy as np
import pandas as pd
from . import props

class Plot():
    def __init__(self, name : str, data : str, out : str):
        self.name = name
        self.data : str = data
        self.out : str = out
        self.x : np.array
        self.y : np.array
        self.xuncert : np.ndarray
        self.yuncert : np.ndarray
        self.avx : np.float64
        self.avy : np.float64
        self.maxx : np.float64
        self.maxy : np.float64
        self.trline : np.ndarray
        self.rng : np.ndarray
        self.corrcoef : np.float64
        
    def createGraph(self):
        self.parseData()
        fig = go.Figure(data=props.data(self.x, self.y, self.xuncert, self.yuncert), layout=props.layout(self.name, self.trline, self.corrcoef, self.avx, self.avy, self.maxx, self.maxy))
        fig.add_trace(props.trendline(self.rng, self.trline))
        fig.write_image(self.out)

    def parseData(self):
        df = pd.read_csv(self.data)
        self.x = np.array(df['x'])
        self.y = np.array(df['y'])
        self.xuncert = np.array(df['x±'])
        self.yuncert = np.array(df['y±'])
        self.avx = np.average(self.x)
        self.avy = np.average(self.y)
        self.maxx = np.max(self.x) + np.max(self.xuncert)
        self.maxy = np.max(self.y) + np.max(self.yuncert)
        self.trline = np.polyfit(self.x, self.y, 1)
        self.rng = np.linspace(np.amin(self.x), np.amax(self.x), 2)
        self.corrcoef = np.corrcoef(self.x, self.y)[0, 1]**2

    
