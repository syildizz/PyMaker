
# PyMaker

## About

PyMaker is a web service that allows people to generate Python code using AI. 
For the webserver, FastAPI is used and for the code generation Ollama is used. 
The service can be deployed to a single server using a Docker compose file or 
to a cluster of computers using Kubernetes.

The Ollama instance is deployed locally and uses the llama3.2 model by default. 

## Deployment

### Docker Compose

The service can be installed using docker compose.

```bash
docker compose up -d;
```

Before the service can work however, the llama3.2 model has to be installed to the container. 

```bash
docker exec -it <your-ollama-docker-id> ollama pull llama3.2;
```

After the model is pulled the service can be used. 

The model does not have to be pulled again if the containers are taken down as it persists.

```bash
docker compose down;
```

The web-server will be hosted on localhost:80.

### Kubernetes

The service can also be installed on Kubernetes. 
To install on kubernetes, the deploy_k8s.sh can be used.

```bash
. deploy_k8s.sh;
```

The model will be automatically pulled. 
However, the model being pulled takes time. 
If you want to check on the progress of the model being pulled, 
you can use model_pull_status_k8s.sh.

```bash
. model_pull_status_k8s.sh;
```


The cluster can be taken down using takedown_k8s.sh

```bash
. takedown_k8s.sh;
```
