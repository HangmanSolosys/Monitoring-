#!/bin/python3
import os
import subprocess
import time

var1 = "waaazzaaap"

def my_function():
    try:
        print("Checking if Docker is installed")
        subprocess.run(["docker", "--version"], check=True, text=True)
        print("Docker is installed.\n")

    except FileNotFoundError:
        print("Docker is not installed. Please install Docker first.")

    except subprocess.CalledProcessError:  
        print("Docker is installed but not functioning correctly.")
        return

    try:
        print("Checking if Docker service is running...")

        result = subprocess.run(["sudo", "systemctl", "is-active", "docker"], check=True, text=True, capture_output=True)
        
        if result.stdout.strip() == "active":
            print("Docker service is running.")
        else:
            print("Docker service is not running.")

    except subprocess.CalledProcessError:
        print("Docker service is not running or there's an issue with the service.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    my_function()

