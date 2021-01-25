import numpy as np
import plotly.graph_objects as go
from plably import props

class TestProps():
    def test_splitName(self):
        vtitle, htitle = props.splitName("Vertical vs. Horizontal")
        assert(vtitle == "Vertical")
        assert(htitle == "Horizontal")
    def test_data(self):
        data = props.data(np.array([1, 2]), np.array([1, 2]), np.array([0.5, 0.5]), np.array([0.5, 0.5]))
        assert(type(data) == go.Scatter)
    def test_layout(self):
        layout = props.layout("Test vs. Test", np.array([1,0]), np.float64(1.0), np.float64(1.5), np.float64(1.5), np.float64(2.0), np.float64(2.0))
        assert(type(layout) == go.Layout)
    def test_trendline(self):
        trendline = props.trendline(np.array([1,2]), np.array([1,0]))
        assert(type(trendline) == go.Scatter)