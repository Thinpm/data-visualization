# **Real-time Dubai Temperature Tracker**

## **1\. Introduction**

This is a real-time tracking tool for monitoring the temperature in Dubai using OpenWeatherMap API. The tool displays an intuitive chart with real-time temperature updates and logs data into a CSV file.

## **2\. System Requirements**

* Operating Systems: Windows, Linux, macOS (compatible with all platforms)  
* Python 3.8+

## **3\. Installation**

First, ensure that Python is installed on your system. Then, install the required libraries by running:

pip install \-r requirements.txt

## **4\. Usage Instructions**

1. Open a terminal or command prompt.  
2. Run the application using the command:  
   python temperature\_tracker.py  
3. The tool will start fetching and displaying real-time temperature data for Dubai.  
4. To stop the program, press `Ctrl + C`.

## **5\. Key Features**

* Displays a **real-time line chart** to track Dubai's temperature.  
* Updates data every **60 seconds**.  
* Automatically saves data to a CSV file for later analysis.  
* Keeps only the last **100 records** for efficient tracking.

## **6\. Data Storage**

* Data is saved in a CSV file (`temperature_data.csv`).  
* The dataset contains two columns:  
  * **Time (Dubai timezone)**  
  * **Temperature (°C)**  
* When the dataset reaches **100 entries**, the oldest data is removed to maintain efficiency.

## **7\. Authors**

**Phan Minh Thuy\_ 2202079**  
**Ha Minh ChieChien\_2202095**

