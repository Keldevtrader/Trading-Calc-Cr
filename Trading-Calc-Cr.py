import streamlit as st

def calculate_trading_scenario(total_investment, purchase_price, commission_percent, tp1_price, amount_taken_tp1, tp2_price, sl_price):
    # Convert commission percentage to a decimal
    commission_rate = commission_percent / 100
    
    # Break-even price (including buy and sell commissions)
    break_even_price = purchase_price * (1 + commission_rate) * (1 + commission_rate)

    # Value @ TP1
    Value_at_TP1 = total_investment * (1 - commission_rate) * (tp1_price / purchase_price)
    
    # Value @ TP1 including Sell Commission
    Sell_at_TP1 = Value_at_TP1 * (1 - commission_rate)
    
    # Profit @ TP1 if 100% sold @ TP1
    Profit_at_TP1 = Sell_at_TP1 - total_investment
    
    # Net Loss @ SL
    Net_Loss_SL = total_investment * (1 - commission_rate) * (sl_price / purchase_price)*(1 - commission_rate) - total_investment
    
    # Remaining Amount after taking out @ TP1 including Comm
    Amount_Remaining_Tp1 = Value_at_TP1 - (amount_taken_tp1 * (1 - commission_rate))
    
    # Total Amount Gained @ TP2
    Amount_gained_TP2 = Amount_Remaining_Tp1 * (tp2_price / tp1_price) * (1 - commission_rate) + amount_taken_tp1
    
    # Net Profit @ TP2
    net_profit_TP2 = Amount_gained_TP2 - total_investment
    
    # Return the results
    return break_even_price, net_profit_TP2, Profit_at_TP1, Net_Loss_SL

# Streamlit app interface
st.title("Trading Calculator with Commission Fee (%)")

# User inputs
total_investment = st.number_input("Total Investment", value=0)
purchase_price = st.number_input("Price per Share", value=0)
commission_percent = st.number_input("Commission Percentage (%)", value=0.25)
tp1_price = st.number_input("TP1 Price", value=0)
amount_taken_tp1 = st.number_input("Amount Withdrawn at TP1", value=0)
tp2_price = st.number_input("TP2 Price", value=0)
sl_price = st.number_input("SL Price", value=0)

# Calculate button
if st.button("Calculate"):
    break_even_price, net_profit_TP2, Profit_at_TP1, Net_Loss_SL = calculate_trading_scenario(
        total_investment, purchase_price, commission_percent, tp1_price, amount_taken_tp1, tp2_price, sl_price)
    
    # Display the results
    st.write(f"**Break-even Price (Including Commissions):** ${break_even_price:.2f}")
    st.write(f"**Net Profit (Partials @ TP1 + TP2):** ${net_profit_TP2:.2f}")
    st.write(f"**Profit If 100% Sold at TP1:** ${Profit_at_TP1:.2f}")
    st.write(f"**Net Loss @ SL:** ${Net_Loss_SL:.2f}")
