import pandas as pd

def load_dataset():
    data = {
        "mission_name": [
            "Apollo 11", "Voyager 1", "Curiosity Rover", "James Webb",
            "Artemis I", "Pioneer 10", "Cassini", "Hubble Telescope",
            "Mars Pathfinder", "New Horizons"
        ],
        "launch_year": [1969, 1977, 2011, 2021, 2022, 1972, 1997, 1990, 1996, 2006],
        "destination": [
            "Moon", "Interstellar", "Mars", "Deep Space",
            "Moon", "Jupiter", "Saturn", "Low Earth Orbit",
            "Mars", "Pluto"
        ],
        "mission_goal": [
            "Human Landing", "Exploration", "Surface Analysis", "Infrared Imaging",
            "Test Flight", "Exploration", "Atmosphere Study", "Imaging",
            "Surface Analysis", "Flyby"
        ],
        "mission_type": [
            "Manned", "Unmanned", "Unmanned", "Unmanned",
            "Unmanned", "Unmanned", "Unmanned", "Unmanned",
            "Unmanned", "Unmanned"
        ]
    }

    df = pd.DataFrame(data)
    return df
