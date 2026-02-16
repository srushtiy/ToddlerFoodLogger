import streamlit as st
import pandas as pd
from datetime import date

# 1. Database with Trace Labels
# Updated Database including Oatmeal with Chia & Jaggery
FOOD_DB = {
    "Dairy & Grains": {
        "Whole Milk (8oz)": {"cal": 150, "iron": 0.07, "trace": True},
        "Small Dosa (1 pc)": {"cal": 74, "iron": 0.77, "trace": False},
        "Ragi (1/4 cup cooked)": {"cal": 110, "iron": 0.90, "trace": False},
        "Cheese Slice (1 pc)": {"cal": 80, "iron": 0.0, "trace": True},
    },
    "Snacks & Breakfast": {
        "Oatmeal w/ Chia & Jaggery": {"cal": 116, "iron": 2.13, "trace": False}, # <--- ADDED
        "Almond Butter Toast w/ Berry": {"cal": 186, "iron": 1.58, "trace": False},
        "Banana (1 medium)": {"cal": 105, "iron": 0.30, "trace": True},
        "Apple (1 medium)": {"cal": 95, "iron": 0.20, "trace": True},
    },
    "Legumes (1/4 cup cooked)": {
        "Yellow Moong Dal": {"cal": 45, "iron": 0.80, "trace": False},
        "Green Moong Dal": {"cal": 53, "iron": 0.71, "trace": False},
        "Rajma (Kidney Beans)": {"cal": 53, "iron": 0.95, "trace": False},
        "Chickpeas (Chole)": {"cal": 67, "iron": 1.18, "trace": False},
    },
    "Fruits & Veggies (1/4 cup)": {
        "Strawberries": {"cal": 13, "iron": 0.17, "trace": True},
        "Blueberries": {"cal": 21, "iron": 0.10, "trace": True},
        "Green Peas": {"cal": 31, "iron": 0.30, "trace": True},
        "Broccoli (1/2 cup)": {"cal": 15, "iron": 0.35, "trace": True},
    }
}


if 'history' not in st.session_state:
    st.session_state.history = []

# --- SIDEBAR ---
st.sidebar.header("📏 Portion Guide")
st.sidebar.info("1/4 Cup = Golf Ball | 1/2 Cup = Tennis Ball")
st.sidebar.markdown("---")
st.sidebar.warning("⚠️ **Trace Iron**: These items have small amounts. Pair them with high-iron legumes to reach the 7mg goal!")

# --- MAIN APP ---
st.title("👶 Toddler Nutrition Log")

tab1, tab2 = st.tabs(["Daily Tracker", "View History & Save"])

with tab1:
    st.subheader(f"Today: {date.today().strftime('%B %d, %Y')}")
    total_cal, total_iron = 0.0, 0.0

    for category, items in FOOD_DB.items():
        with st.expander(category, expanded=True):
            for name, stats in items.items():
                # Append label if it's a trace food
                display_name = f"{name} (Trace Iron)" if stats["trace"] else name
                qty = st.number_input(display_name, min_value=0.0, step=0.5, key=f"in_{name}")
                
                total_cal += stats["cal"] * qty
                total_iron += stats["iron"] * qty

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Calories", f"{int(total_cal)}")
    c2.metric("Iron (mg)", f"{total_iron:.2f}/7.0")

    if st.button("💾 Log Today's Totals"):
        new_entry = {"Date": date.today(), "Calories": int(total_cal), "Iron (mg)": round(total_iron, 2)}
        st.session_state.history.append(new_entry)
        st.success("Day saved!")

with tab2:
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Log as CSV", data=csv, file_name='toddler_log.csv', mime='text/csv')
    else:
        st.info("No logs yet.")
