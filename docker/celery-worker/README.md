




## TO TEST BUILD 
# nerdctl rmi takke/flower ; nerdctl build . -f DockerfileFlower -t takke/flower && nerdctl run -it --rm takke/flower
# nerdctl rmi takke/celery ;  nerdctl build . -f Dockerfile -t takke/celery ;  nerdctl run -it --rm takke/celery 


## TO PULL for kube
# nerdctl -n k8s.io build . -f DockerfileFlower -t local/takke/flower:v1.0
# nerdctl -n k8s.io run -d -exec local/takke/flower:v1.0

## TO PULL for kube
# nerdctl -n k8s.io build . -f Dockerfile -t local/takke/celery:v2.0
# nerdctl -n k8s.io run -d -exec local/takke/celery:v1.0