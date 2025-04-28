#!/bin/sh

K8S_DEPLOYMENT_FOLDER="k8s_deployment_files";

kubectl apply -f ${K8S_DEPLOYMENT_FOLDER}/daemonset_ollama-model-init.yaml;
# wait for daemonset to initialize
kubectl rollout status daemonset ollama-model-init;
kubectl create cm pymaker-config --from-file config -o yaml --dry-run=client | kubectl apply -f -

kubectl apply -f ${K8S_DEPLOYMENT_FOLDER}/deployment_ollama.yaml;
kubectl apply -f ${K8S_DEPLOYMENT_FOLDER}/service_ollama.yaml;
kubectl apply -f ${K8S_DEPLOYMENT_FOLDER}/deployment_pymaker-web.yaml;
kubectl apply -f ${K8S_DEPLOYMENT_FOLDER}/service_pymaker-web.yaml;
