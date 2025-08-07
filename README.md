📦 Vendor Performance Analysis using Python & Power BI

This project performs an in-depth Vendor Performance Analysis by consolidating data from multiple SQL sources, analyzing key performance metrics, and visualizing actionable business insights using Power BI. It aims to help decision-makers identify underperforming vendors, optimize procurement strategies, and enhance vendor management efficiency.

📌 Objective
	The primary goal of this project is to automate and streamline the analysis of vendor performance data by:
		Extracting and merging data from multiple relational tables
		Performing Exploratory Data Analysis (EDA)
		Classifying vendors based on business rules
		Creating a dynamic and interactive Power BI dashboard for decision-making

🛠️ Tools & Technologies
	Tool	Purpose
        Python 3.x	Data extraction, transformation & logic
        Pandas	Data manipulation
        SQLite3	Querying relational data
        Power BI	Data visualization
        Matplotlib / Seaborn	Optional EDA plotting
        Logging	Debugging and traceability

🧩 Project Workflow
1. 🧠 Data Ingestion & Transformation
		Script: get_vendor_summary.py
		Connects to the SQLite database
		Joins relevant tables to create a consolidated vendor summary
		Cleans and formats data for analysis
		Outputs a CSV or DataFrame for Power BI

2. 📊 Exploratory Data Analysis (EDA)
	Performed initial data exploration using Python:
		Checked for null values, outliers, and duplicates
		Grouped vendors by category and calculated key metrics
		Generated summary statistics to understand data distribution
		(Optional) Plotted charts like bar graphs, box plots using Matplotlib/Seaborn

3. 📈 Vendor Performance Analysis – Business Questions Answered
	This project helps answer crucial business questions such as:
		🔍 Which vendors and brands demonstrate the highest sales performance?
		💰 Which vendors contribute the most to total purchase spend?
		📉 Which brands need promotional or pricing adjustments due to low sales but high profit margins?
		📦 How much capital is locked in unsold inventory per vendor?
		🏷️ What is the cost impact of bulk purchasing – is there an optimal purchase volume?
		🥇 How dependent is procurement on top vendors – what’s their share?

5. 📉 Power BI Dashboard
  	The final interactive dashboard was created using Power BI and includes:
		Top Vendor Performance (Sales, Profits, Units Sold)
		Profitability vs. Sales Matrix
		Unsold Inventory Value by Vendor
		Bulk Purchase Impact on Unit Cost
		Vendor Category Distribution
		Procurement Dependence on Top Vendors

	The dashboard enables procurement teams and managers to:
		Take data-driven decisions
		Improve vendor negotiations
		Reduce inventory holding costs
		Optimize procurement strategies

