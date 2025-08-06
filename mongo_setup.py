from pathlib import Path
from pymongo import MongoClient
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

# Create empty collections
db.create_collection("inat_observations")
db.create_collection("weather_data")
db.create_collection("system_stats")

print("MongoDB collections created successfully.")
