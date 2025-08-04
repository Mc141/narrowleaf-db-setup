## **Full List of Parameters for Spread Prediction**

### **Core NASA POWER Parameters** (Direct from the API)

| NASA Code           | Description                                             | Importance                                         |
| ------------------- | ------------------------------------------------------- | -------------------------------------------------- |
| `T2M`               | Mean Air Temperature at 2 meters                        | Crucial for general growth behavior                |
| `T2M_MAX`           | Maximum Daily Air Temperature                           | Identifies heat stress periods                     |
| `T2M_MIN`           | Minimum Daily Air Temperature                           | Indicates frost risk                               |
| `PRECTOT`           | Precipitation (mm/day)                                  | Drives soil moisture and establishment             |
| `RH2M`              | Relative Humidity at 2m                                 | Affects evapotranspiration and seedling survival   |
| `WS2M`              | Wind Speed at 2 meters                                  | Affects seed dispersal and evapotranspiration      |
| `ALLSKY_SFC_SW_DWN` | Total Solar Radiation on Horizontal Surface (shortwave) | Proxy for photosynthetic activity                  |
| `CLRSKY_SFC_SW_DWN` | Clear Sky Radiation                                     | Used to compute cloud cover                        |
| `TQV`               | Total Precipitable Water Vapor                          | Indicates available moisture in atmosphere         |
| `TS`                | Surface Temperature                                     | Supplement to air temperature (microclimate proxy) |

---

### **Derived / Calculated Parameters**

| Name                          | Description                                             | Source                             |
| ----------------------------- | ------------------------------------------------------- | ---------------------------------- |
| **Growing Degree Days (GDD)** | Sum of heat units above a base threshold (e.g. 10°C)    | Derived from `T2M_MIN` & `T2M_MAX` |
| **Temperature Anomaly**       | Deviation from long-term seasonal average               | Derived                            |
| **Cloud Cover Index**         | Percent difference between `ALLSKY` and `CLRSKY` values | Derived                            |
| **Heat Stress Days**          | Days above 30–35°C (species-dependent threshold)        | Derived                            |
| **Frost Days**                | Days below 0°C or 5°C                                   | Derived                            |
| **Evapotranspiration Proxy**  | Combination of `T2M`, `RH2M`, `WS2M`, and radiation     | Derived                            |
| **Cumulative Rainfall**       | Total over season or month                              | Aggregated `PRECTOT`               |

---

### **Optional Geospatial Variables (if available from other sources)**

| Variable                     | Description                                     | Source                 |
| ---------------------------- | ----------------------------------------------- | ---------------------- |
| **Elevation (DEM)**          | Influences temperature, humidity, microclimates | SRTM, OpenTopography   |
| **Slope & Aspect**           | Affects runoff and sun exposure                 | Derived from elevation |
| **Distance to Urban Areas**  | Affects spread patterns (human interaction)     | OpenStreetMap, QGIS    |
| **Distance to Water Bodies** | Influences humidity and suitability             | GIS tools              |
| **Land Cover Type**          | Forest, shrubland, urban, etc.                  | MODIS, Copernicus      |

---

### **Temporal Metadata**

| Field                      | Description                 | Importance                        |
| -------------------------- | --------------------------- | --------------------------------- |
| `time_observed_at`         | Exact timestamp of sighting | Needed for temporal join          |
| `month`, `season`, `year`  | Derived temporal buckets    | Used in time-based trend analysis |
| `days_since_last_sighting` | Spread dynamics feature     | Derived                           |
| `recent_sighting_count`    | Count in nearby regions     | Derived                           |

---

### **Model-Friendly Aggregated Features**

| Feature                  | Description                                    |
| ------------------------ | ---------------------------------------------- |
| `avg_temp_monthly`       | Monthly average of `T2M`                       |
| `total_rainfall_monthly` | Sum of `PRECTOT` per month                     |
| `max_temp_3_day_avg`     | Max heat event estimate                        |
| `gdd_accumulated`        | Growing degree days per month                  |
| `env_suitability_score`  | Composite of temp + rainfall + NDVI (optional) |

---

## Grouped by Type

### Weather (NASA POWER):

* `T2M`, `T2M_MAX`, `T2M_MIN`
* `PRECTOT`, `RH2M`
* `WS2M`
* `ALLSKY_SFC_SW_DWN`, `CLRSKY_SFC_SW_DWN`
* `TQV`, `TS`

### Derived:

* GDD
* Heat/frost days
* Cloud index
* Cumulative rainfall
* Temperature anomaly

### Geospatial:

* Elevation
* Slope/Aspect
* Distance to urban areas / water bodies
* Land cover

### Temporal:

* Season / Month / Year
* Spread rate over time