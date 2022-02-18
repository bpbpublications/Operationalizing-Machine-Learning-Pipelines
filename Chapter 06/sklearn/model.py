import argparse
import os

import joblib
from polyaxon import tracking
from polyaxon.tracking.contrib.scikit import log_regressor

from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--max_depth", type=int, default=5)
    args = parser.parse_args()

    tracking.init()

    X, y = datasets.load_boston(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    tracking.log_data_ref(content=X_train, name="x_train")
    tracking.log_data_ref(content=y_train, name="y_train")
    tracking.log_data_ref(content=X_test, name="x_test")
    tracking.log_data_ref(content=y_test, name="y_test")

    rfr = RandomForestRegressor(n_estimators=args.n_estimators, max_depth=args.max_depth)
    rfr.fit(X_train, y_train)

    # Polyaxon
    # This automatically logs metrics relevant to regression
    log_regressor(rfr, X_test, y_test)

    # Logging the model as joblib
    model_path = os.path.join(tracking.get_outputs_path(), "model.joblib")
    joblib.dump(rfr, model_path)
    tracking.log_model(model_path, name="model", framework="scikit-learn")
