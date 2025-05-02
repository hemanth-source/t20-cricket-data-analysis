# t20-cricket-data-analysis
building a best t20 squad among all players from every country

Sure! Here's the complete text you can directly copy and paste into your `README.md` file:


🏏 Cricket Player Data Analysis

This repository contains a complete data pipeline for scraping cricket player data from the web, performing data preprocessing and transformation, and visualizing key insights using Power BI.

📌 Project Overview

This project aims to automate the process of collecting cricket player statistics from the web, cleaning and transforming the data, and presenting meaningful visualizations to analyze player performance, trends, and comparisons.

🔧 Components
Web Scraping: Automated data extraction from websites containing cricket player statistics using Python libraries like `requests`, `BeautifulSoup`.
Data Preprocessing: Cleaning null values, handling data types, removing duplicates, and normalizing data.
Data Transformation: Aggregating, encoding, and restructuring the data for analytical purposes.
Data Visualization: Creating interactive dashboards and charts using **Power BI** to visualize trends, comparisons, and insights.






 🧪 Requirements

- Python 3.8+
- pandas
- numpy
- BeautifulSoup / Selenium
- Power BI Desktop

🚀 How to Run

1. Web Scraping

    Navigate to the `webscraper/` directory and run `scraper.py` to collect the latest player data.
     The scraped data will be saved as `raw_data.csv` in the `data/` folder.

2. Data Preprocessing

    Open `notebooks/data_cleaning.ipynb` and follow the steps to clean and transform the raw data.
     The final output will be saved as `cleaned_data.csv`.

3. Power BI Visualization

    Open `powerbi/CricketDashboard.pbix` in Power BI Desktop.
    Load the `cleaned_data.csv` dataset and refresh the visuals to explore the dashboard.



 📊 Power BI Dashboard Features

1.Player performance comparison (e.g., batting average, strike rate)
2.Top players by total runs, wickets, etc.
3.Filters for teams, years, player roles (batsman, bowler, all-rounder)
4. Match-wise or tournament-wise performance insights



## 📌 Future Enhancements

1.Integrate live data fetching using official cricket APIs
2.add player ranking and team performance analytics
3.Deploy dashboard to the web using Power BI Service or Streamlit



 🤝 Contributions

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.



