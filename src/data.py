import pandas as pd
from sklearn.datasets import load_iris


def load_dataset(cfg: dict):
    """Baseline : Iris.
    Extension : CSV si cfg["data"]["kind"] == "csv".
    """
    kind = cfg["data"].get("kind", "iris")

    if kind == "iris":
        X, y = load_iris(return_X_y=True, as_frame=True)
        return X, y

    # Extension CSV pour un futur dataset
    df = pd.read_csv(cfg["data"]["path"])
    target = cfg["data"]["target"]

    y = df[target]
    X = df.drop(columns=[target])

    return X, y