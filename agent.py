from mesa import Agent
import random

class FarmerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crop_health = 100

    def step(self):
        # Move randomly
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

        # Update crop health
        if self.random.random() < 0.1:
            self.crop_health += 5
        
        self.crop_health -= self.model.weather_impact()
        self.crop_health -= self.model.pest_impact()
        self.crop_health = max(0, min(100, self.crop_health))


class PestAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.damage = 5

    def step(self):
        # Move randomly
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

        # Apply damage
        self.model.total_pest_damage += self.damage


class SensorAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Simulate weather data collection
        self.model.weather_data = self.random.randint(0, 5)


class MarketAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.price = 10

    def step(self):
        # Price adjusts based on crop health
        avg_health = self.model.avg_crop_health()
        if avg_health > 0:
            self.price = max(5, 15 - int(avg_health // 10))
        else:
            self.price = 15