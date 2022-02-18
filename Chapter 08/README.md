# Feast
### MLOps Book Example for Feature Store

The rep contains the data and code used to create the Feast feature store on GCP. Please change the table names in source in **cust_repo.py** and the GCP bucket in **feature_store.yaml**.

Data source contains two files **new_cust_conn_details.csv** and **new_cust_pay_det.csv** which is the only data that is made available in online store using feast materialize. All other data is treated as historical data.

Two additional files offline.py and online.py is shared to show how data can be pulled from feature store for training and scoring respectively. We have not used all the features, but code can be modified to do that.

In case you want to import module directly from GitHub you can refer https://gist.github.com/MineRobber9000/998fe8c5a183fa2649f937c9d2e0b8b0