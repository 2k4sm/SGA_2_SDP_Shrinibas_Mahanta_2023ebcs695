#!/usr/bin/env python3
"""
Name: Shrinibas Mahanta
ID: 2023ebcs695
"""

import datetime
import platform

def main():
    print("Docker Containerization Demo")
    print()
    print(f"Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print()
    print("This application is running inside a Docker container!")
    print()

if __name__ == "__main__":
    main()

