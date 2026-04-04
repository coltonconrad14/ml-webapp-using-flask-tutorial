from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Iterable

import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "iris_model.joblib"


@lru_cache(maxsize=1)
def load_model_artifact() -> dict:
    artifact = joblib.load(MODEL_PATH)
    return {
        "model": artifact["model"],
        "target_names": list(artifact["target_names"]),
        "feature_names": list(artifact["feature_names"]),
        "accuracy": float(artifact["accuracy"]),
    }


def get_model_metadata() -> dict:
    artifact = load_model_artifact()
    return {
        "feature_names": artifact["feature_names"],
        "accuracy": artifact["accuracy"],
        "target_names": artifact["target_names"],
    }


def predict_iris(values: Iterable[object]) -> dict:
    cleaned_values = [str(value).strip() for value in values]

    if len(cleaned_values) != 4 or any(value == "" for value in cleaned_values):
        raise ValueError("Please provide all four flower measurements.")

    try:
        features = [[float(value) for value in cleaned_values]]
    except ValueError as exc:
        raise ValueError("Please enter valid numeric values for all fields.") from exc

    artifact = load_model_artifact()
    model = artifact["model"]
    target_names = artifact["target_names"]

    pred_index = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    confidence = float(probabilities[pred_index])

    return {
        "prediction": target_names[pred_index],
        "confidence": confidence,
        "values": cleaned_values,
        "probabilities": {
            str(target_names[index]): float(probability)
            for index, probability in enumerate(probabilities)
        },
    }
