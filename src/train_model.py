from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_and_save_model() -> None:
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )

    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=500, random_state=42)),
        ]
    )

    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)

    artifact = {
        "model": model,
        "target_names": iris.target_names,
        "feature_names": iris.feature_names,
        "accuracy": float(accuracy),
    }

    output_path = Path(__file__).resolve().parents[1] / "model" / "iris_model.joblib"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, output_path)

    print(f"Model saved to: {output_path}")
    print(f"Validation accuracy: {accuracy:.3f}")


if __name__ == "__main__":
    train_and_save_model()
