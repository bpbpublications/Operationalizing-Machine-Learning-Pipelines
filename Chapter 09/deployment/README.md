# Deployment

## Install KServe

To install kserve for experimentation/prototyping purposes, run `kserve_install.sh`.

```bash
bash kserve_install.sh
```

To install kserve for a production scenario, follow [this link](https://kserve.github.io/website/admin/serverless/).

## Deploying the model

To deploy the model, run the `deploy_model.sh` script.

```sh
bash deploy_model.sh <uuid> <experiment_bucket> <prod_bucket>
```

**uuid**: uuid of the Polyaxon run containing the model to be deployed. (You can use the `get_best_model.py` script to get the model with the best accuracy)

**experiment_bucket**: GCS bucket being used as the Polyaxon artifact store.

**prod_bucket**: GCS bucket containing models being used for production. The model and training data will be copied from the experiment bucket to the production bucket.

**NOTE**: Before executing the deployment script, please change the model name parameter in `deployment.yaml`.
