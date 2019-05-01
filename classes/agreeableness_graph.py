import matplotlib as mil
mil.use("TkAgg")
import matplotlib.pyplot as plt
from .base_graph import BaseGraph


class AgreeablenessGraph(BaseGraph):
    
    def __init__(self):
        super().__init__()
        self.title = "Nice people live in the countryside"
        self.x_label = "Population density"
        self.y_label = "Agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values
