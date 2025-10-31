from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider
from model import SmartAgriModel
from agent import FarmerAgent, PestAgent, SensorAgent, MarketAgent


def agent_portrayal(agent):
    if agent is None:
        return None

    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5, "Layer": 0}

    if isinstance(agent, FarmerAgent):
        portrayal["Color"] = "green"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.5
    elif isinstance(agent, PestAgent):
        portrayal["Color"] = "red"
        portrayal["Layer"] = 3
        portrayal["r"] = 0.4
    elif isinstance(agent, SensorAgent):
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 5
        portrayal["r"] = 0.3
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.6
        portrayal["h"] = 0.6
    elif isinstance(agent, MarketAgent):
        portrayal["Color"] = "orange"
        portrayal["Layer"] = 4
        portrayal["r"] = 0.6

    return portrayal


# Grid
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

# Chart
chart = ChartModule(
    [
        {"Label": "Avg Crop Health", "Color": "green"},
        {"Label": "Total Pest Damage", "Color": "red"}
    ],
    data_collector_name='datacollector'
)

# Model parameters
model_params = {
    "num_farmers": Slider("Number of Farmers", 5, 1, 20, 1),
    "num_pests": Slider("Number of Pests", 3, 1, 10, 1),
    "num_sensors": Slider("Number of Sensors", 2, 1, 5, 1),
    "width": 10,
    "height": 10
}

# Server
server = ModularServer(
    SmartAgriModel,
    [grid, chart],
    "Smart Agriculture Real-Time Model",
    model_params
)

server.port = 8521

if __name__ == "__main__":
    server.launch()