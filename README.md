# Docker Learning Docker Module

This repository documents my journey into the world of Docker, from building and running containers to managing multi-container applications using Docker Compose and pushing images to AWS ECR. My approach has been hands-on, building small projects to consolidate learning and applying real-world DevOps concepts.

# What I learnt
- **Introduction to Docker:** Understanding what containers are, how they differ from virtual machines, and why Docker is a critical tool in modern DevOps workflows.

- **Container Lifecycle:** How to build images (docker build), run containers (docker run), inspect them (docker inspect), and manage their lifecycle (docker stop, docker rm).

- **Networking and Volumes:** Connecting containers on the same network for inter-service communication and using volumes to persist data beyond container lifecycles.

- **Docker Hub & AWS ECR:** Pushing and pulling Docker images to public (Docker Hub) and private registries (AWS ECR), including authentication and tagging workflows.

- **Docker Compose:** Managing multi-container applications with a single docker-compose.yml file, defining services, ports, dependencies, and networks.

- **Optimizing Docker Images:** Using multi-stage builds to reduce image size, remove unnecessary build dependencies and create efficient production-ready containers.

- **Debugging & Logs:** Inspecting containers, reviewing logs and troubleshooting networking issues between containers.

- **System Cleanup:** Keeping the Docker environment clean by removing unused images, stopping containers and dangling volumes using commands like docker system prune.

- **Container Orchestration Overview:** Learning why tools like Kubernetes and Docker Swarm are used for scaling and managing containers across multiple machines and understanding their differences.

# Docker Challenge: Flask + Redis Multi-Container App

As a practical exercise, I built a multi-container application consisting of:

- A Python Flask web application that serves a welcome page and tracks visit counts.
- A Redis database to store visit counts using persistent storage.

Key concepts applied in this challenge:

- Using a **Dockerfile** to containerize the Flask application.
- Using the official **Redis** Docker image and connecting it to Flask.
- Managing both services with **Docker Compose**, ensuring proper networking and dependencies.
- Implementing **persistent storage** with Docker volumes, so Redis data survives container restarts.
- Experimenting with **environment variables** and **scaling services** (bonus challenge).

By completing this challenge, I was able to understand how Docker allows consistent application deployment across environments and how containerisation simplifies development, testing and production workflows.