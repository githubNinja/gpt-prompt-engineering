import streamlit as st

# Simulated data for demo
summaries = [
    "Customer faced login difficulties due to 'Invalid credentials'. Agent resolved by resetting the password.",
    "Customer had billing queries about incorrect charges. Agent clarified and escalated the issue."
]

insights = {
    "Sentiment Distribution": {"Positive": 10, "Neutral": 15, "Negative": 5},
    "Top Issues": {"Login": 12, "Billing": 8, "Account Updates": 5}
}

# Streamlit app
st.title("Customer Behavior Analysis Dashboard")
st.header("Summarized Conversations")
for summary in summaries:
    st.write("- " + summary)

st.header("Behavioral Insights")
st.bar_chart(insights["Sentiment Distribution"])
st.bar_chart(insights["Top Issues"])
