from pathlib import Path

import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

model_path = Path(__file__).resolve().parent / "model" / "iris_model.joblib"
artifact = joblib.load(model_path)
model = artifact["model"]
target_names = artifact["target_names"]
feature_names = artifact["feature_names"]
validation_accuracy = artifact["accuracy"]


@app.get("/")
def index():
    return render_template(
        "index.html",
        prediction=None,
        probability=None,
        values=["", "", "", ""],
        error=None,
        feature_names=feature_names,
        validation_accuracy=validation_accuracy,
    )


@app.post("/predict")
def predict():
    values = [request.form.get(f"feature_{idx}", "").strip() for idx in range(4)]

    try:
        features = [[float(value) for value in values]]
    except ValueError:
        return render_template(
            "index.html",
            prediction=None,
            probability=None,
            values=values,
            error="Please enter valid numeric values for all fields.",
            feature_names=feature_names,
            validation_accuracy=validation_accuracy,
        )

    pred_index = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    confidence = float(probabilities[pred_index])

    return render_template(
        "index.html",
        prediction=target_names[pred_index],
        probability=confidence,
        values=values,
        error=None,
        feature_names=feature_names,
        validation_accuracy=validation_accuracy,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
