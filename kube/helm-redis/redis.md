helm repo add bitnami https://charts.bitnami.com/bitnami

takke@DESKTOP-GO0SQ8F:/mnt/c/Users/fbiag/GIT_REPOS/psychic-journey/kube/helm-redis$ helm install myredis bitnami/redis
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /home/takke/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /home/takke/.kube/config
NAME: myredis
LAST DEPLOYED: Mon Feb  7 01:06:17 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: redis
CHART VERSION: 16.2.1
APP VERSION: 6.2.6

** Please be patient while the chart is being deployed **

Redis can be accessed on the following DNS names from within your cluster:

    myredis-master.default.svc.cluster.local for read/write operations (port 6379)
    myredis-replicas.default.svc.cluster.local for read-only operations (port 6379)



To get your password run:

    export REDIS_PASSWORD=$(kubectl get secret --namespace default myredis -o jsonpath="{.data.redis-password}" | base64 --decode)

To connect to your Redis server:

1. Run a Redis pod that you can use as a client:

   kubectl run --namespace default redis-client --restart='Never'  --env REDIS_PASSWORD=$REDIS_PASSWORD  --image docker.io/bitnami/redis:6.2.6-debian-10-r103 --command -- sleep infinity

   Use the following command to attach to the pod:

   kubectl exec --tty -i redis-client \
   --namespace default -- bash

2. Connect using the Redis CLI:
   REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h myredis-master
   REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h myredis-replicas

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/myredis-master : &
    REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h 127.0.0.1 -p