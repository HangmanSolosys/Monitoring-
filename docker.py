#!/bin/python3

import time
import subprocess
import os


def execute_docker():

    compose_file_dir="/home/solosys/containers"

    os.chdir(compose_file_dir)

    os.system("docker-compose up -d")

    time.sleep(2)

    print("The images have been pulled and the containers are started...")


execute_docker()
