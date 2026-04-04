import streamlit as st

from src.predictor import get_model_metadata, predict_iris

metadata = get_model_metadata()
default_values = [5.1, 3.5, 1.4, 0.2]

st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🌸",
    layout="centered",
)

st.title("🌸 Iris Species Predictor")
st.caption("Streamlit + Scikit-learn")
st.write(
    "Enter four flower measurements to predict the iris species with the trained machine learning model."
)

left_col, right_col = st.columns(2)
left_col.metric("Validation accuracy", f"{metadata['accuracy'] * 100:.2f}%")
right_col.info("The original Flask app is still available in `app.py`.")

with st.form("prediction_form"):
    st.subheader("Flower measurements")
    columns = st.columns(2)
    values = []

    for index, feature_name in enumerate(metadata["feature_names"]):
        with columns[index % 2]:
            value = st.number_input(
                feature_name,
                min_value=0.0,
                value=float(default_values[index]),
                step=0.1,
                format="%.2f",
            )
            values.append(value)

    submitted = st.form_submit_button("Predict species")

if submitted:
    result = predict_iris(values)
    st.success(
        f"Prediction: **{result['prediction']}** ({result['confidence'] * 100:.2f}% confidence)"
    )

    st.subheader("Class probabilities")
    for species, probability in result["probabilities"].items():
        st.write(f"**{species}**")
        st.progress(probability, text=f"{probability * 100:.2f}%")

    st.json(
        {
            "prediction": result["prediction"],
            "confidence": round(result["confidence"], 4),
            "inputs": {
                feature: value
                for feature, value in zip(metadata["feature_names"], result["values"])
            },
        }
    )
else:
    st.info("Submit the form to get a prediction.")
