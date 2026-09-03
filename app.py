import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meesho Seller P&L Dashboard", layout="wide")

st.title("📦 Meesho Seller P&L Dashboard")
st.write("Upload your Meesho Order report CSV to analyze your true net profit.")

uploaded_file = st.file_uploader("Upload Meesho CSV Report", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.sidebar.header("Cost Inputs (Per Unit)")
    avg_cogs = st.sidebar.number_input("Average Product Cost (COGS ₹)", value=150)
    avg_pkg = st.sidebar.number_input("Packaging & Label Cost (₹)", value=10)
    
    total_orders = len(df)
    
    if 'Selling Price' in df.columns:
        total_revenue = df['Selling Price'].sum()
    else:
        total_revenue = st.sidebar.number_input("Manual Total Revenue Override (₹)", value=50000)

    total_cogs = total_orders * avg_cogs
    total_pkg = total_orders * avg_pkg
    net_profit = total_revenue - total_cogs - total_pkg
    profit_margin = (net_profit / total_revenue * 100) if total_revenue > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Orders", f"{total_orders:,}")
    col2.metric("Total Revenue", f"₹{total_revenue:,.2f}")
    col3.metric("Net Profit", f"₹{net_profit:,.2f}")
    col4.metric("Profit Margin", f"{profit_margin:.1f}%")

    st.divider()
    st.subheader("Order Data Preview")
    st.dataframe(df.head(10))

else:
    st.info("Please upload a CSV file to view your P&L breakdown.")
