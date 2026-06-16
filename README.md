# Homelab Infrastructure Dashboard

A self-hosted homelab environment orchestrated via Docker Compose.
This repository contains the configuration files required to deploy a
centralized homepage alongside infrastructure management, monitoring,
and utility tools.

## Architecture & Services

The stack consists of the following components:

* **Dashboard (`homepage`)**: The primary application portal providing
  centralized access to all deployed services and real-time infrastructure status.
* **Infrastructure Management (`Portainer`)**: Container management interface
  used for monitoring stacks, container lifecycles, and docker volumes.
* **Monitoring & Analytics (`Grafana`, `Prometheus`, `Node Exporter`)**:
  * **Node Exporter**: Collects hardware and OS metrics from the host system.
  * **Prometheus**: Acts as the time-series database to ingest and store metrics.
  * **Grafana**: Visualizes the collected data via infrastructure dashboards.
* **Development Utilities (`IT-Tools`)**: A collection of aggregated web-based
  tools for developers and system administrators.
* **Deployment Automation (`VERT.sh`)**: Scripting/automation tooling
  utilized for environment verification and deployment lifecycles.

## Prerequisites

* Docker Engine 20.10+
* Docker Compose v2.0+
* Supported Linux-based Host Engine (Ubuntu/Debian recommended)

## Deployment

1. Clone the repository:

```bash
git clone git@github.com:Kaboupi/homepage-config.git
cd homepage-config
```

2. Configure environment variables (copy the template and adjust system IPs/ports):

```bash
cp .env.example .env
```

3. Initialize the stack

```bash
docker compose up -d
```
