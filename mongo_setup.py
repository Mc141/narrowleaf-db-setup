from pathlib import Path
from pymongo import MongoClient
from datetime import datetime
import subprocess

# Define Docker Compose file
docker_compose = """
services:
  mongo:
    image: mongo:6.0
    container_name: mongo_invasive
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
volumes:
  mongo_data:
"""

# Get script directory
script_dir = Path(__file__).parent

# Write docker-compose.yml
compose_path = script_dir / "docker-compose.yml"
compose_path.write_text(docker_compose)
print(f"Created file: {compose_path}")

# Start MongoDB container
try:
    subprocess.run(["docker-compose", "up", "-d"], cwd=str(script_dir), check=True)
    print("MongoDB container started successfully.")
except Exception as e:
    print(f"Failed to start MongoDB container: {e}")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["invasive_db"]

# Drop collections to reset (optional)
db.drop_collection("inat_observations")
db.drop_collection("weather_data")
db.drop_collection("system_stats")

# Insert iNaturalist sample data
db.inat_observations.insert_one({
    "id": 123456,
    "uuid": "abc-uuid",
    "time_observed_at": datetime(2021, 9, 1, 12, 0, 0),
    "created_at": datetime(2021, 9, 1, 12, 30, 0),
    "latitude": -33.927,
    "longitude": 18.417,
    "positional_accuracy": 25,
    "place_guess": "Table Mountain, Cape Town",
    "scientific_name": "Pyracantha angustifolia",
    "common_name": "Narrow-leaf Firethorn",
    "quality_grade": "research",
    "image_url": "https://example.com/image.jpg",
    "user_id": 101
})

# Insert linked weather data
db.weather_data.insert_one({
    "inat_id": 123456,
    "date": datetime(2021, 9, 1),
    "T2M": 18.3,
    "T2M_MAX": 24.1,
    "T2M_MIN": 12.8,
    "PRECTOT": 0.0,
    "RH2M": 65.2,
    "WS2M": 3.1,
    "ALLSKY_SFC_SW_DWN": 210.5,
    "CLRSKY_SFC_SW_DWN": 250.0,
    "TQV": 1.2,
    "TS": 19.0,
    "GDD": 8.1,
    "temperature_anomaly": 1.3,
    "cloud_cover_index": 15.8,
    "heat_stress_days": 0,
    "frost_days": 0,
    "evapotranspiration_proxy": 2.1,
    "cumulative_rainfall": 0.0,
    "elevation": 450,
    "slope": 12.3,
    "aspect": "southwest",
    "distance_to_urban": 3.5,
    "distance_to_water": 1.0,
    "land_cover": "shrubland",
    "season": "spring",
    "month": 9,
    "year": 2021
})

# Insert system stats
db.system_stats.insert_one({
    "last_refresh": datetime(2025, 8, 3, 23, 59, 0),
    "total_observations": 1,
    "total_weather_records": 1,
    "last_inat_pull": datetime(2025, 8, 3, 23, 0, 0),
    "last_weather_pull": datetime(2025, 8, 3, 23, 30, 0)
})

print("MongoDB collections and data initialized.")
