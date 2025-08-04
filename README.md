### 1. Initialize MongoDB and Seed Data

Run the MongoDB setup script from the root of the project:

```bash
python mongo_setup.py
```

This script will:

* Create a `docker-compose.yml` file for the MongoDB service
* Launch the MongoDB container
* Connect to MongoDB using `pymongo`
* Create and populate the following collections with initial dummy data:

  * `inat_observations`
  * `weather_data`
  * `system_stats`

---

### 2. MongoDB Access Info

Once the script runs successfully:

* MongoDB will be running in Docker on port `27017`
* You can connect using MongoDB Compass with:

```
mongodb://localhost:27017
```

**Default database:** `invasive_db`

---

### Requirements

Ensure the following are installed:

* Docker & Docker Compose
* Python 3.8+
* Python dependencies:

  ```bash
  pip install pymongo
  ```
