import os

from flask import Flask, render_template, request

from src.predictor import get_model_metadata, predict_iris

app = Flask(__name__)

metadata = get_model_metadata()
feature_names = metadata["feature_names"]
validation_accuracy = metadata["accuracy"]


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
        result = predict_iris(values)
    except ValueError as exc:
        return render_template(
            "index.html",
            prediction=None,
            probability=None,
            values=values,
            error=str(exc),
            feature_names=feature_names,
            validation_accuracy=validation_accuracy,
        )

    return render_template(
        "index.html",
        prediction=result["prediction"],
        probability=result["confidence"],
        values=result["values"],
        error=None,
        feature_names=feature_names,
        validation_accuracy=validation_accuracy,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "3000")), debug=True)
