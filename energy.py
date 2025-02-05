import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
def load_data():
    file_path = r"C:\Users\Admin\Downloads\Energy_consumption.csv"
    df = pd.read_csv(file_path, parse_dates=["Timestamp"])
    return df

def predict_energy(input_data):
    # Placeholder prediction logic (Replace with a trained ML model)
    return sum(input_data) * 0.1

def main():
    st.title("Energy Consumption Alert & Prediction System")
    
    df = load_data()
    
    # Sidebar for threshold selection
    st.sidebar.header("Settings")
    threshold = st.sidebar.slider("Energy Consumption Alert Threshold", min_value=int(df['EnergyConsumption'].min()), 
                                  max_value=int(df['EnergyConsumption'].max()), value=80)
    
    # Display dataset
    st.subheader("Dataset Overview")
    st.dataframe(df.head())
    
    # Plot energy consumption over time
    st.subheader("Energy Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Timestamp'], df['EnergyConsumption'], label='Energy Consumption', color='b')
    ax.axhline(y=threshold, color='r', linestyle='--', label='Alert Threshold')
    ax.set_xlabel("Time")
    ax.set_ylabel("Energy Consumption")
    ax.legend()
    st.pyplot(fig)
    
    # Alert System
    st.subheader("Consumption Alerts")
    high_usage = df[df['EnergyConsumption'] > threshold]
    if not high_usage.empty:
        st.warning("High energy consumption detected at the following times:")
        st.dataframe(high_usage[['Timestamp', 'EnergyConsumption']])
    else:
        st.success("Energy consumption is within normal limits.")
    
    # Energy Consumption Prediction
    st.subheader("Energy Consumption Prediction")
    st.write("Enter the following details to predict energy consumption:")

    temperature = st.number_input("Temperature (°C)", value=25)
    humidity = st.number_input("Humidity (%)", value=50)
    square_footage = st.number_input("Square Footage", value=1500)
    occupancy = st.number_input("Occupancy (people)", value=3)
    hvac_usage = st.radio("HVAC Usage", ["On", "Off"])
    lighting_usage = st.radio("Lighting Usage", ["On", "Off"])
    renewable_energy = st.number_input("Renewable Energy Generated (kWh)", value=5.0)
    holiday = st.number_input("Holiday (0 = No, 1 = Yes)", value=0)
    energyconsumption = st.number_input("Previous Energy Consumption (kWh)", value=50)

    hvac_usage = 1 if hvac_usage == "On" else 0
    lighting_usage = 1 if lighting_usage == "On" else 0

    input_data = [temperature, humidity, square_footage, occupancy, hvac_usage, lighting_usage, renewable_energy, holiday, energyconsumption]
    prediction = predict_energy(input_data)

    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")
    
    # Recommendations
    st.subheader("Energy Saving Tips")
    st.write("- Optimize HVAC usage by maintaining a moderate temperature.")
    st.write("- Reduce lighting usage when not necessary.")
    st.write("- Increase reliance on renewable energy sources where possible.")
    
if __name__ == "__main__":
    main()
