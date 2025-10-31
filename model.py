from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agent import FarmerAgent, PestAgent, SensorAgent, MarketAgent


class SmartAgriModel(Model):
    def __init__(self, width=10, height=10, num_farmers=5, num_pests=3, num_sensors=2):
        super().__init__()
        self.grid = MultiGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.num_farmers = num_farmers
        self.total_pest_damage = 0
        self.weather_data = 0

        # Add farmers
        for i in range(num_farmers):
            a = FarmerAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(a, (x, y))

        # Add pests
        for i in range(num_farmers, num_farmers + num_pests):
            a = PestAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(a, (x, y))

        # Add sensors
        for i in range(num_farmers + num_pests, num_farmers + num_pests + num_sensors):
            a = SensorAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(a, (x, y))

        # Market agent
        self.market = MarketAgent(999, self)
        self.schedule.add(self.market)
        x = self.random.randrange(width)
        y = self.random.randrange(height)
        self.grid.place_agent(self.market, (x, y))

        self.datacollector = DataCollector(
            model_reporters={
                "Avg Crop Health": self.avg_crop_health,
                "Total Pest Damage": lambda m: m.total_pest_damage
            }
        )

    def step(self):
        self.total_pest_damage = 0
        self.schedule.step()
        self.datacollector.collect(self)

    def weather_impact(self):
        return self.weather_data

    def pest_impact(self):
        return self.total_pest_damage // max(1, self.num_farmers)

    def avg_crop_health(self):
        farmers = [a for a in self.schedule.agents if isinstance(a, FarmerAgent)]
        if len(farmers) == 0:
            return 0
        return sum(f.crop_health for f in farmers) / len(farmers)