#Set Path and enable dashboard - This needs to run from GCP cloud shell
#Install polyaxon python library
sudo pip3 install polyaxon
#Name of the K8s cluster installed for polyaxon
CLUSTER_NAME = $2
#Computaion Zone under which K8s cluster is installed
ZONE = $1
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE
polyaxon config set --host=http://localhost:8000
kubectl port-forward -n polyaxon svc/polyaxon-polyaxon-gateway 8000:80