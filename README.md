# DevOps Assignment — Production-Grade Microservice Deployment on AWS

## Overview
This project demonstrates how to design, deploy, and manage a **production-grade microservice-based application** on AWS using modern DevOps practices and tools.

The focus of this assignment is on **infrastructure design, deployment automation, and operational readiness**, rather than application complexity or business features.

The system consists of **two independently deployable services**:
- **Frontend Service** — a web application
- **Backend Service** — a REST API

Both services are containerized and communicate over HTTP.

---

## Architecture Decision

### High-Level Architecture
Client  
↓  
Nginx (Reverse Proxy)  
├─ Frontend Service (Container)  
└─ Backend API Service (Container)

### Why Frontend + Backend?
- Demonstrates clear **service boundaries**
- Each service can be **built, deployed, and updated independently**
- Aligns with **microservice architecture principles**
- Keeps the application simple while highlighting DevOps capabilities

Although the backend is a single API service, the overall system qualifies as a **microservice-based architecture** because services are isolated, networked, and independently deployable.

---

## Technology Stack & Rationale

### Application Layer
| Component | Technology | Rationale |
|----------|------------|-----------|
| Frontend | Static Web (HTML / JS or SPA) | Lightweight and fast to deploy |
| Backend | REST API | Stateless and easy to containerize |
| Communication | HTTP | Standard service-to-service communication |

---

### Containerization
| Tool | Rationale |
|-----|-----------|
| Docker | Industry-standard container platform |
| Separate Dockerfiles | Enables independent service lifecycle |

---

### Cloud Platform
| Service | Rationale |
|--------|-----------|
| AWS EC2 | Simple, cost-efficient, Free Tier friendly |
| Nginx | Reverse proxy instead of managed load balancer |
| Amazon ECR (optional) | Container image registry |

> Kubernetes (EKS) is intentionally not used to avoid unnecessary operational complexity for the scope of this assignment.  
> In a larger-scale production environment, ECS or EKS would be considered.

---

### Infrastructure as Code (IaC)
| Tool | Rationale |
|------|-----------|
| Terraform | Declarative, repeatable, and widely adopted IaC tool |

All infrastructure is provisioned using code to ensure consistency and reproducibility.

---

### CI/CD
| Tool | Rationale |
|------|-----------|
| GitHub Actions | Native GitHub integration and simple automation |

The CI/CD pipeline automates:
1. Docker image builds
2. Image publishing
3. Deployment to AWS EC2

---

### Observability & Operations
| Area | Approach |
|------|----------|
| Logging | Amazon CloudWatch Logs |
| Metrics | Amazon CloudWatch Metrics |
| Health Checks | `/health` endpoint on backend |
| Resilience | Docker restart policies |

These practices ensure the system is observable and manageable in a production-like environment.

---

## Microservice Definition
This system follows microservice principles by ensuring:
- Independent service deployment
- Container isolation
- Network-based communication
- Stateless application design

Future improvements may include decomposing the backend into multiple domain-based services (e.g., user-service, order-service).

---

## Local Development

### Run Backend
```bash
docker build -t backend ./backend
docker run -p 8080:8080 backend `

###Run Frontend
```bash
docker build -t frontend ./frontend
docker run -p 3000:80 frontend `

---

##Deployment Workflow (High-Level)

Git Commit
↓
GitHub Actions (CI)
↓
Build Docker Images
↓
Push Images
↓
Deploy to AWS EC2
↓
Run Containers
↓
Nginx Routes Traffic

---

## Cost Consideration

This project is designed to operate within AWS Free Tier constraints by:
- Using a single EC2 instance
- Avoiding managed load balancers
- Not using Kubernetes control plane services

This approach minimizes cost while still demonstrating production-grade DevOps practices.

---

## Future Improvements
- Introduce ECS or EKS for container orchestration
- Add auto-scaling and load balancing
- Implement centralized monitoring dashboards
- Add a staging environment

---

## Conclusion

This project showcases how a production-grade microservice deployment can be achieved using simple, well-reasoned architectural decisions and modern DevOps practices on AWS.

**Full Changelog**: https://github.com/MarkThana/devops-assignment-test/commits/readme-v1.0.0
