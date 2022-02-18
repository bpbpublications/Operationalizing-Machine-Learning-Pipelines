from datetime import datetime, timedelta
import pandas as pd
from google.cloud import bigquery
from feast import FeatureStore, RepoConfig

# Creating Entity DataFrame
client = bigquery.Client()
query = """SELECT * FROM vj-feat-ml.feature_store.cust_demo_det"""
df_entity = client.query(query).to_dataframe()
df_entity["event_timestamp"] = pd.Timestamp("2021-07-31", tz="UTC")

# Initializing Feature Store
fs = FeatureStore(
    config=RepoConfig(
        registry="gs://cust_feat_new/custfeat.db",
        project="Customer_Feature",
        provider="gcp",
    )
)
# Features to be imported
features = ["customer_churn_flag:Churn"]

# Training DataFrame
training_df = fs.get_historical_features(features=features, entity_df=df_entity).to_df()
