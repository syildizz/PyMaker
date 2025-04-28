
#!/bin/sh

K8S_DEPLOYMENT_FOLDER="k8s_deployment_files";

kubectl delete -f ${K8S_DEPLOYMENT_FOLDER}/service_pymaker-web.yaml;
kubectl delete -f ${K8S_DEPLOYMENT_FOLDER}/deployment_pymaker-web.yaml;
kubectl delete -f ${K8S_DEPLOYMENT_FOLDER}/service_ollama.yaml;
kubectl delete -f ${K8S_DEPLOYMENT_FOLDER}/deployment_ollama.yaml;

kubectl create cm pymaker-config --from-file config -o yaml --dry-run=client | kubectl delete -f -
kubectl delete -f ${K8S_DEPLOYMENT_FOLDER}/daemonset_ollama-model-init.yaml;
