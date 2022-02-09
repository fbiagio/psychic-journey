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

eyJhbGciOiJSUzI1NiIsImtpZCI6IjVfNk54R3A4YW9wd2hjTHFvaXdLNk90OTQ5V2lVck9PRENQZDNISzdYS2MifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWxnOXZ3Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJiNDk3ZDAyMC0yYWZlLTRlNjUtYjg2NC0xZjAzM2M4YTJkNDMiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.dv1S76eFE5pzwZl_uvO20raFOGmsLz7-etknU8yPgE_CQoOs6kbnINFj_p2NaoDKd9WNuSmuCASJ9qVXlAbwoaAJeYuE9SRrgY0818hytjH41VO7J_Iw5_e7JXOPI2hMZCeQORGfGeKpcLH192EYZtvInamIFPI-xM0uJqXvz98sLj5q3vOss437AAbAwOiURd_smIEtetuv3ZL_-PF5_tDrVg0s1P1xP4OawID8Vj5t5Sl82Aj_VLfviDItGwCEJ1YZx_vPR9LCb1ZGNj8fB_2HV19uxW6nfjV09jg7_z5D-WzO50TnsUh7wvRbPT-8iOGD8WBu1wc_tOYFviMnHw

