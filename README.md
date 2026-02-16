👶 Toddler Nutrition Tracker
A lightweight Python web application built with Streamlit to help parents track daily iron and calorie intake for toddlers (specifically optimized for an 18-month-old's needs).
🚀 Quick Start
1. Install Requirements
You will need Python installed. Install the necessary library using pip:
bash
pip install streamlit pandas
Use code with caution.

2. Run the App
Save the code provided in our conversation as app.py and run:
bash
streamlit run app.py
Use code with caution.

📋 Features
Custom Food Database: Pre-loaded with toddler favorites like Dosa, Ragi, Rajma, Chickpeas, and Yellow Moong Dal.
Real-time Calculations: Instantly calculates total calories and iron (mg) as you adjust portions.
Visual Progress: A dynamic progress bar tracks the daily 7mg iron goal.
Portion Guide: A built-in sidebar guide translates "cups" into "visual objects" (e.g., 1/4 cup = a golf ball).
Data Logging: Save daily totals to a "History" tab and export them to a CSV/Excel file for your pediatrician.
🥗 Nutritional Targets
The app is calibrated to standard pediatric guidelines for an 18-month-old:
Iron: 7 mg / day.
Calories: 1,000 – 1,400 kcal / day.
Milk Limit: 16 oz / day (to prevent calcium from blocking iron absorption).
🛠️ Customization
To add more foods, simply locate the FOOD_DB dictionary in the code and add a new entry:
python
"New Food Name": {"cal": 100, "iron": 1.5},
Use code with caution.

📝 License
This project is for personal educational use. Always consult with a pediatrician or registered dietitian regarding your child's specific nutritional needs.
Would you like me to show you how to deploy this for free on Streamlit Cloud so you can access it from your phone's home screen like a real app?



