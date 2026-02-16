import streamlit as st
import pandas as pd
from datetime import date

# 1. Database
FOOD_DB = {
    "Dairy & Grains": {
        "Whole Milk (8oz)": {"cal": 150, "iron": 0.07},
        "Small Dosa (1 pc)": {"cal": 74, "iron": 0.77},
        "Ragi (1/4 cup cooked)": {"cal": 110, "iron": 0.90},
        "Cheese Slice (1 pc)": {"cal": 80, "iron": 0.0},
    },
    "Legumes (1/4 cup cooked)": {
        "Yellow Moong Dal": {"cal": 45, "iron": 0.80},
        "Green Moong Dal": {"cal": 53, "iron": 0.71},
        "Rajma (Kidney Beans)": {"cal": 53, "iron": 0.95},
        "Chickpeas (Chole)": {"cal": 67, "iron": 1.18},
    },
    "Fruits & Veggies": {
        "Green Peas (1/4 cup)": {"cal": 31, "iron": 0.30},
        "Broccoli (1/2 cup)": {"cal": 15, "iron": 0.35},
        "Banana (1 medium)": {"cal": 105, "iron": 0.30},
        "Apple (1 medium)": {"cal": 95, "iron": 0.20},
    }
}

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# --- SIDEBAR ---
st.sidebar.header("📏 Portion Guide")
st.sidebar.info("1/4 Cup = Golf Ball | 1/2 Cup = Tennis Ball")
st.sidebar.markdown("---")
st.sidebar.header("💡 Pro-Tip")
st.sidebar.write("Limit milk to 16oz/day to prevent 'Milk Anemia' (where calcium blocks iron).")

# --- MAIN APP ---
st.title("👶 Toddler Nutrition Log")

tab1, tab2 = st.tabs(["Daily Tracker", "View History & Save"])

with tab1:
    st.subheader(f"Today: {date.today().strftime('%B %d, %Y')}")
    total_cal, total_iron = 0.0, 0.0

    for category, items in FOOD_DB.items():
        with st.expander(category, expanded=True):
            for name, stats in items.items():
                qty = st.number_input(f"{name}", min_value=0.0, step=0.5, key=f"in_{name}")
                total_cal += stats["cal"] * qty
                total_iron += stats["iron"] * qty

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Calories", f"{int(total_cal)}")
    c2.metric("Iron (mg)", f"{total_iron:.2f}/7.0")

    if st.button("💾 Log Today's Totals"):
        new_entry = {"Date": date.today(), "Calories": int(total_cal), "Iron (mg)": round(total_iron, 2)}
        st.session_state.history.append(new_entry)
        st.success("Day saved to history!")

with tab2:
    st.header("Weekly Overview")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)
        
        # Download Button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Log as CSV",
            data=csv,
            file_name=f'toddler_nutrition_{date.today()}.csv',
            mime='text/csv',
        )
        
        avg_iron = df["Iron (mg)"].mean()
        st.info(f"**Average Daily Iron:** {avg_iron:.2f} mg")
    else:
        st.info("No logs saved yet. Add data in the Daily Tracker tab.")
