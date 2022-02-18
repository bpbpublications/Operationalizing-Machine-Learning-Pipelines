from datetime import datetime, timedelta
import pandas as pd
from google.cloud import bigquery
from feast import FeatureStore, RepoConfig

fs = FeatureStore(
    config=RepoConfig(
        registry="gs://cust_feat_new/custfeat.db",
        project="Customer_Feature",
        provider="gcp",
    )
)

features = ["customer_conn_det:Tenure", "customer_pay_det:Contract"]

online_features_df = fs.get_online_features(
    features=features,
    entity_rows=[
        {"CustomerID": "3115-CZMZD"},
        {"CustomerID": "4367-NUYAO"},
        {"CustomerID": "2520-SGTTA"},
    ],
).to_df()

