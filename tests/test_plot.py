import plably
import os
import utils

class TestPlot():
    @staticmethod
    def instantiate_plot():
        utils.create_fake_data()
        return plably.Plot("Test vs. Test", "tests/data.csv", "tests/output.png")
    def test_parseData(self):
        graph = TestPlot.instantiate_plot()
        graph.parseData()
        try:
            graph.x
            graph.y
            graph.xuncert
            graph.yuncert
            graph.avx
            graph.avy
            graph.maxx
            graph.maxy
            graph.trline
            graph.rng
            graph.corrcoef
        except Exception as error:
            assert(False)
    def test_createGraph(self):
        graph = TestPlot.instantiate_plot()
        graph.createGraph()
        assert(os.path.isfile("tests/output.png"))
