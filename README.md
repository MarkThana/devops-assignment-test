# DevOps Assignment – CI/CD, Kubernetes & Observability

## Overview

This repository demonstrates a production-ready DevOps setup covering:

- Dockerized frontend and backend applications
- CI/CD pipeline using GitHub Actions
- Kubernetes-based deployment
- Observability with Prometheus, Loki, Promtail, and Grafana
- Secure RBAC configuration
- Fully reproducible deployment steps

The goal is to reflect real-world DevOps practices rather than a minimal demo.

## Architecture

```
Developer
│
▼
GitHub Repository
│
▼
GitHub Actions (CI/CD)
	•	Build Docker images
	•	Push images to Docker Hub
	•	Deploy workloads to Kubernetes
│
▼
Kubernetes Cluster
├─ Namespace: devops-assignment
│   ├─ Frontend (Deployment + Service)
│   └─ Backend  (Deployment + Service)
│
└─ Namespace: observability
├─ Prometheus (Metrics)
├─ Loki (Logs)
├─ Promtail (Log Collector – DaemonSet)
└─ Grafana (Visualization)
```

Flow:

- Developer pushes code to GitHub
- GitHub Actions builds Docker images
- Images are pushed to Docker Hub
- Kubernetes workloads are updated
- Metrics and logs are collected and visualized

Namespaces:

- devops-assignment: application workloads
- observability: monitoring and logging stack

## Technology Stack

| Component | Technology |
|----------|-----------|
| CI/CD | GitHub Actions |
| Containers | Docker |
| Orchestration | Kubernetes |
| Metrics | Prometheus |
| Logging | Loki, Promtail |
| Visualization | Grafana |
| Registry | Docker Hub |

## Repository Structure

```
.
├── .github/workflows
│   └── ci.yml
├── k8s
│   ├── backend
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── frontend
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── observability
│       ├── namespace.yaml
│       ├── prometheus
│       │   ├── configmap.yaml
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   ├── serviceaccount.yaml
│       │   ├── clusterrole.yaml
│       │   └── clusterrolebinding.yaml
│       ├── loki
│       │   ├── configmap.yaml
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   ├── daemonset.yaml        # Promtail
│       │   ├── serviceaccount.yaml
│       │   ├── clusterrole.yaml
│       │   └── clusterrolebinding.yaml
│       └── grafana
│           ├── deployment.yaml
│           └── service.yaml
└── README.md
```

## CI/CD Pipeline

### Trigger

- Push to main branch

### Stages

1. Build backend Docker image
2. Push backend image to Docker Hub
3. Build frontend Docker image
4. Push frontend image to Docker Hub
5. Deploy updated images to Kubernetes

### Image Tagging

- latest
- Git commit SHA

### Deployment Method

- kubectl apply for manifests
- kubectl set image for runtime updates
- No manual changes on cluster nodes

## Kubernetes Deployment

### Namespaces

| Namespace | Purpose |
|----------|--------|
| devops-assignment | Frontend and backend applications |
| observability | Prometheus, Loki, Grafana, Promtail |

### Applications

- Deployed using Deployment
- Exposed using ClusterIP Service
- Health endpoint: /health
- imagePullPolicy set to Always

## Observability

### Prometheus

- Runs in observability namespace
- Uses kubernetes_sd_configs
- Scrapes pods using annotations

Required annotations:

```yaml
prometheus.io/scrape: "true"
prometheus.io/port: "8080"
prometheus.io/path: "/metrics"
```

RBAC:

- Dedicated ServiceAccount
- Dedicated ClusterRole
- Dedicated ClusterRoleBinding

Validation:

- /targets page shows healthy endpoints
- up query returns metrics

### Loki and Promtail

Loki:

- Deployment
- ClusterIP service
- Receives logs via HTTP push

Promtail:

- DaemonSet
- Reads logs from /var/log/containers/*.log
- Uses CRI pipeline stage
- Adds labels: job, namespace, pod, container, app

Promtail client configuration:

```yaml
clients:
  - url: http://loki.observability.svc.cluster.local:3100/loki/api/v1/push
```

Validation:

```bash
curl http://localhost:3100/loki/api/v1/labels
```

### Grafana

- Runs in observability namespace
- Used for metrics and log visualization

Datasources:

- Prometheus: http://prometheus.observability.svc.cluster.local:9090
- Loki: http://loki.observability.svc.cluster.local:3100

Example LogQL query:

```logql
{job="kubernetes-pods"}
```

## Security and RBAC

- No component uses default permissions
- Prometheus and Promtail use:
  - Dedicated ServiceAccount
  - Explicit ClusterRole
  - Explicit ClusterRoleBinding
- Principle of least privilege applied

## Deployment Steps

1. Create namespace

```bash
kubectl apply -f k8s/observability/namespace.yaml
```

2. Deploy observability stack

```bash
kubectl apply -f k8s/observability/prometheus
kubectl apply -f k8s/observability/loki
kubectl apply -f k8s/observability/grafana
```

3. Deploy applications

```bash
kubectl apply -f k8s/backend
kubectl apply -f k8s/frontend
```

4. Verify

```bash
kubectl get pods -A
kubectl get svc -A
```

## Demo and Validation Checklist

Prometheus:

- Targets page shows healthy endpoints
- up query returns data

Grafana:

- Metrics dashboards load
- Logs visible from Loki

Loki:

- Logs ingested from all namespaces
- Labels available for querying

## Conclusion

This project provides a complete DevOps workflow including CI/CD, Kubernetes deployment, observability, and security best practices suitable for production environments.