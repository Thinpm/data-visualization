# Crime Map Visualization

## Overview

This project visualizes crime incidents in San Francisco using **Folium** and **Pandas**. It clusters crime locations on an interactive map, making it easier to analyze crime distribution across the city.

## Features

- Interactive map with crime clusters
- Categorized crime markers with custom icons
- Scalable visualization based on the number of incidents
- Easy-to-use and lightweight implementation

## Installation

Ensure you have Python installed (version 3.7+ recommended). Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### **Running in Jupyter Notebook**

Execute the Jupyter Notebook to generate the crime map:

```bash
jupyter notebook CrimeMapAnalysis.ipynb
```

### **Viewing the Pre-generated Map**

If you have already run the script and saved the map, open `crime_map.html` in your browser to view the interactive visualization.

## Data

The dataset used in this project is stored in the `data/` directory. Ensure that the dataset file is placed inside before running the script:

```
data/
 ├── Police_Incidents_2016.csv
```

## File Structure

```
Crime-Map-Project/
 ├── CrimeMapAnalysis.ipynb   # Jupyter Notebook for crime mapping
 ├── README.md                # Project documentation
 ├── requirements.txt         # Required dependencies
 ├── data/                    # Folder containing dataset
 │   ├── Police_Incidents_2016.csv
```

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or contributions, reach out via GitHub issues or email.

