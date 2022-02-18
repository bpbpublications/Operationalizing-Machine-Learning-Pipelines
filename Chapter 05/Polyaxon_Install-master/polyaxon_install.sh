#Install polyaxon python library 
#Running from local might need changing pip3 to pip
sudo pip3 install polyaxon 
#Set env varaibles
#Project ID
export PROJECT_ID=$1
#Computation Zone
export ZONE=$2
#K8 cluster name
export CLUSTER_NAME=$3
#Maximum number of node in autoscale
export NUM_NODES=$4

#Installing Kubernetes Cluster
gcloud config set project $PROJECT_ID
gcloud config set compute/zone $ZONE
gcloud container clusters create $CLUSTER_NAME --num-nodes 3 --enable-autoscaling --min-nodes 3 --max-nodes $NUM_NODES  
gcloud container clusters get-credentials $CLUSTER_NAME

#If excuting from cloud shell comment below line
gcloud container clusters get-credentials $CLUSTER_NAME

#Create name space for Polyaxon
kubectl create namespace polyaxon
#Add polyaxon to repositories
helm repo add polyaxon https://charts.polyaxon.com
#Install Polyaxon
polyaxon admin deploy 