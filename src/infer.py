from src.model import Input
import pandas as pd
import numpy as np
import pickle
import xgboost
import sklearn


def infer(detail_in: dict) -> float:
    model_lgbm = pickle.load(open("src/model_lgbm.pkl", "rb"))
    pipeline = pickle.load(open("src/pipeline.pkl", "rb"))
    detail = pd.DataFrame(
        detail_in,
        index=[
            "i",
        ],
    )

    test_processed = pd.DataFrame(
        pipeline.transform(detail), columns=pipeline.get_feature_names_out()
    )

    y_pred = np.expm1(model_lgbm.predict(test_processed))

    return np.round(np.maximum(y_pred, 0).item(), decimals=2)
