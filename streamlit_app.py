import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

# Simulated S&P 500 total return multipliers (2000–2023)
# These include dividend reinvestment, approximate values
sp500_total_return_multipliers = {
    2000: 7.54, 2001: 6.94, 2002: 6.46, 2003: 5.28, 2004: 4.82,
    2005: 4.42, 2006: 3.92, 2007: 3.44, 2008: 2.26, 2009: 3.47,
    2010: 3.02, 2011: 2.73, 2012: 2.35, 2013: 1.98, 2014: 1.80,
    2015: 1.63, 2016: 1.47, 2017: 1.31, 2018: 1.21, 2019: 1.12,
    2020: 1.00, 2021: 0.90, 2022: 0.80, 2023: 0.75
}

# Streamlit UI
st.set_page_config(page_title="What If I Invested?", layout="centered")
st.title("📈 What If I Invested in the S&P 500?")
st.caption("See how much your investment would be worth today.")

# Inputs
amount = st.number_input("💵 Amount Invested ($)", min_value=100, value=1000, step=100)
year = st.selectbox("📅 Year of Investment", sorted(sp500_total_return_multipliers.keys()))
show_chart = st.checkbox("📊 Show Growth Chart", value=True)

# Calculation
today = datetime.now().year
if year in sp500_total_return_multipliers:
    multiplier = sp500_total_return_multipliers[year]
    current_value = round(amount * multiplier, 2)
    st.subheader(f"💰 Your investment would be worth: **${current_value:,.2f}**")
    st.caption(f"Based on an approximate total return multiplier of {multiplier} since {year}.")

    # Chart
    if show_chart:
        years = list(range(year, today + 1))
        values = [amount * (multiplier * ((i - year + 1)/len(years))) for i in years]
        fig, ax = plt.subplots()
        ax.plot(years, values, marker='o')
        ax.set_title("Investment Growth Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("Value ($)")
        st.pyplot(fig)
else:
    st.warning("Data not available for that year.")

