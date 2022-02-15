# https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml

# create user and roles

kubectl apply -n kubernetes-dashboard -f dashboard-adminuser.yaml


# get secret for access gui

kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"


# kubectl proxy
# http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

# to remove login password (only for dev env)
# kubectl patch deployment kubernetes-dashboard -n kubernetes-dashboard --type 'json' -p '[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--enable-skip-login"}]'

yJhbGciOiJSUzI1NiIsImtpZCI6IlNmM2dnOUloN0RrT1ZJWWZOTmpfSEpDVVpQdTBWdDJQN3pabzlZb05ybmcifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXc1dnJzIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIzYmM5MDc2OS01M2ZjLTQ1ZWItODNhNC04YzUyYjBkM2VjMWEiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.CzHJwKuhsiZykaspeDVgQk3W8gdpUtyyKr942gncndl5l4Raf-ZtBYisPyh3QkYluALzcTAwCZYG3qZ-R-D6lFSolCc3i--s_TA6DaYxRhv_XM5Xn2BiwnVCCvBKWFOTXH8QPHTrc-EaJR7JK7PfWiJ65LnplGEVEn6llAqoWKBV55uHVxgn2dPFeiGZZ9H0wgfHMVijmd9D00fpQtYIU5ItPTa_DVTHApfiBX_LjMwlOyMqzXYbywyng8L_FX4lB7cWR5pdsmbcgTUbHwzQsYAjYsTPUMBso7moIVE5nOP4BrOg8aoczSp8umh3YliPFirMK6iRRLcnEQX8MnBRWQ
