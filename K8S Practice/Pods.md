# Using Kubernetes Imperative Command to Create a Pod
A quick refeerence for manageing pods imperatively in Kubernetes
## Create an Nginx Pod
''' bash kubectl run nginx-pod --image=nginx --restart=Never
## REplace nginx-pod with your preferred name, Image Uses official Nginx Docker Image

## Verify Pod 
'''bash kubectl get pods

## Export Configuration to YAML
'''bash kubectl get pod nginx-pod -o yaml > ngnix-pod.yaml

## This can then be edited using:
'''bash vim nginx-pod.yaml 

## Apply Changes
'''bash kubectl apply -f nginx-pod.yaml
