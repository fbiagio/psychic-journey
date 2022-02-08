FROM busybox

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
COPY requirements.txt ./

WORKDIR / 


COPY . .


CMD [ "sh" ]

# nerdctl build . -f Dockerfile -t takke/busybox
# nerdctl run -it --rm takke/busybox
# nerdctl rmi takke/busybox

## TO TEST BUILD 
# nerdctl rmi takke/busybox ; nerdctl build . -f Dockerfile -t takke/busybox && nerdctl run -it --rm takke/busybox


## TO PULL for kube
# nerdctl -n k8s.io run -d -exec local/takke/busybox:latest
# nerdctl -n k8s.io pull local/takke/busybox:v1.2

