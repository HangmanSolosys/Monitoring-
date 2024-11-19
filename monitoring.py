#!/bin/python3

import time
import os

def docker_compose():

#I'm adding the docker-compose content in a variable as a string
    docker_content= """

version: '3.8'

services:

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus_container
    restart: unless-stopped
    volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
    - "9090:9090"

  grafana:

    image: grafana/grafana:latest
    container_name: grafana_container
    restart: unless-stopped
    depends_on:
    - prometheus
    ports:
    - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: "admin"
    volumes:
      - grafana-storage:/var/lib/grafana

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter-container
    restart: unless-stopped
    ports:
    - "9100:9100"
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/host'

volumes:
  grafana-storage:

  """


#open the file and write the docker-compose content in it

    with open("docker-compose.yml", "w") as file:
        file.write(docker_content)

    print("The docker-compose.yml file as been created")


    os.system('docker-compose up -d')

    print("The containers have started!")


docker_compose()
