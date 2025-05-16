# Creatiing a Pod imperatively with Nginx
kubectl run nginx-pod --image=nginx --restart=Never
# Where i inputed "nginx-pod" can be whatever name you choose for your pod
# To verify if the pod is running you would type the command
kubectl get pods
# To Export a YAML file from the pod you created you would:
kubectl get pod nginx-pod -o yaml > ngnix-pod.yaml
# This can then be edited using:
vim nginx-pod.yaml 
# when the configuration are made then you can use
esc wq: 
#then
kubectl apply -f nginx-pod.yaml
