# Polyaxon Installation

__Execute the _"polyaxon_install.sh"_  script for installing polyaxon open source. Below are the parameters that need to be passed in sequence:__

1. Google Project ID for the project under which polyaxon will be installed.
2. Computaion Zone under which K8s cluster will be installed.
3. K8s cluster name the user wants to assign
4. Maximum number of autoscale nodes of K8s cluster, minimum is alredy given as 3.

# Polyaxon Dashboard
__This needs to be run from GCP cloud shell, either by running the _"polyaxon_dashboard.sh"_ script or run the individual command one by one in the script. The script takes two parameters the _2 & 3_ used in above script__ 