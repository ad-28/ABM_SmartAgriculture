# Smart Agriculture Agent-Based Model

Agent-Based Model simulating smart agriculture with farmers, pests, sensors, and market dynamics using Mesa framework.

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install mesa
```

## Project Structure

```
smart-agriculture-abm/
├── agent.py      # Agent definitions (Farmer, Pest, Sensor, Market)
├── model.py      # Model class with grid and scheduling
└── server.py     # Visualization server
```

## Usage

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run simulation
python server.py

# Open browser at http://localhost:8521
```

## Agents

- **Farmer** (Green): Manages crops, health 0-100
- **Pest** (Red): Damages crops, 5 damage/step
- **Sensor** (Blue): Collects weather data
- **Market** (Orange): Adjusts prices based on crop health

## Requirements

```txt
mesa>=2.1.0
```
