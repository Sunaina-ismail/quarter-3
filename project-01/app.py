import streamlit as st


st.markdown("""
    <style>
        .title {
            font-size:  30px;
            font-weight: bold;
            color: #202124;
            text-align: center;
            padding-bottom: 10px;
        }
        .convert-button {
            background-color: #1A73E8 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 8px !important;
            padding: 10px !important;
            width: 100%;
        }
        .convert-button:hover {
            background-color: #1257A0 !important;
        }
        .result-box {
            background: #E8F0FE;
            padding: 12px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            border-radius: 8px;
            margin-top: 15px;
            color: #1A73E8;
        }
    </style>
""", unsafe_allow_html=True)

conversion_factors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 0.000001, "Square Mile": 3.861e-7, "Acre": 0.000247105, "Hectare": 0.0001
    },
    "Time": {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
    },
    "Volume": {
        "Liter": 1, "Milliliter": 1000, "Gallon": 0.264172, "Cubic Meter": 0.001, "Cup": 4.16667
    }
}


st.markdown("<div class='title'>🔄 Simple Unit Converter </div>", unsafe_allow_html=True)


category = st.selectbox("🔹 Select Conversion Type", list(conversion_factors.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("📥 From", list(conversion_factors[category].keys()))
with col2:
    to_unit = st.selectbox("📤 To", list(conversion_factors[category].keys()))

value = st.number_input("📝 Enter Value", min_value=0.0, step=0.1, format="%.2f")

if st.button("Convert", key="convert", help="Click to convert the value"):
    if category == "Temperature":
        if from_unit == "Celsius":
            result = conversion_factors["Temperature"][to_unit](value)
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            result = conversion_factors["Temperature"][to_unit](celsius)
        elif from_unit == "Kelvin":
            celsius = value - 273.15
            result = conversion_factors["Temperature"][to_unit](celsius)
    else:
        result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    

    st.markdown(f"<div class='result-box'>✅ Result: {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
