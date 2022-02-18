from datetime import timedelta

from feast import BigQuerySource, Entity, Feature, FeatureView, ValueType

# Define an entity for the Customer.
customer = Entity(
    # Name of the entity. Must be unique within a project
    name="CustomerID",
    # The join key of an entity describes the storage level field/column on which
    # features can be looked up. The join key is also used to join feature
    # tables/views when building feature vectors
    join_key="CustomerID",
    # The storage level type for an entity
    value_type=ValueType.STRING,
)

# Data Sources

# Cust Churn Flag
cust_churn_flag_source = BigQuerySource(
    # The BigQuery table where features can be found
    table_ref="vj-feat-ml.feature_store.cust_churn_flag",
    # The event timestamp is used for point-in-time joins and for ensuring only
    # features within the TTL are returned
    event_timestamp_column="feature_creation_date",
    created_timestamp_column="record_creation_date",
)

# Cust Connection Details
cust_conn_details_source = BigQuerySource(
    # The BigQuery table where features can be found
    table_ref="vj-feat-ml.feature_store.cust_conn_det",
    # The event timestamp is used for point-in-time joins and for ensuring only
    # features within the TTL are returned
    event_timestamp_column="feature_creation_date",
    created_timestamp_column="record_creation_date",
)

# Cust Payment Details
cust_pay_details_source = BigQuerySource(
    # The BigQuery table where features can be found
    table_ref="vj-feat-ml.feature_store.cust_pay_det",
    # The event timestamp is used for point-in-time joins and for ensuring only
    # features within the TTL are returned
    event_timestamp_column="feature_creation_date",
    created_timestamp_column="record_creation_date",
)

# Feature views

# Churn Feature View
cust_churn_fv = FeatureView(
    name="customer_churn_flag",
    entities=["CustomerID"],
    ttl=timedelta(days=365),
    features=[Feature(name="Churn", dtype=ValueType.INT32),],
    input=cust_churn_flag_source,
    tags={"churn": "churn_data"},
)

# Connection Feature View
cust_conn_fv = FeatureView(
    name="customer_conn_det",
    entities=["CustomerID"],
    ttl=timedelta(days=365),
    features=[
        Feature(name="Tenure", dtype=ValueType.INT64),
        Feature(name="PhoneService", dtype=ValueType.INT32),
        Feature(name="MultipleLines", dtype=ValueType.INT32),
        Feature(name="InternetService", dtype=ValueType.INT32),
        Feature(name="OnlineSecurity", dtype=ValueType.INT32),
        Feature(name="OnlineBackup", dtype=ValueType.INT32),
        Feature(name="DeviceProtection", dtype=ValueType.INT32),
        Feature(name="TechSupport", dtype=ValueType.INT32),
        Feature(name="StreamingTV", dtype=ValueType.INT32),
        Feature(name="StreamingMovies", dtype=ValueType.INT32),
    ],
    input=cust_conn_details_source,
    tags={"churn": "churn_data"},
)
# Payment Feature View
cust_pay_fv = FeatureView(
    name="customer_pay_det",
    entities=["CustomerID"],
    ttl=timedelta(days=365),
    features=[
        Feature(name="Contract", dtype=ValueType.INT32),
        Feature(name="PaperlessBilling", dtype=ValueType.INT32),
        Feature(name="PaymentMethod", dtype=ValueType.INT32),
        Feature(name="MonthlyCharges", dtype=ValueType.FLOAT),
        Feature(name="TotalCharges", dtype=ValueType.FLOAT),
    ],
    input=cust_pay_details_source,
    tags={"churn": "churn_data"},
)

