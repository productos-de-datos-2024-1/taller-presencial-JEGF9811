"""Autograding script"""

import os

# test code files
assert os.path.exists("src/7a_docker_server/config.json")
assert os.path.exists("src/7a_docker_server/server.py")
assert os.path.exists("src/7a_docker_server/Dockerfile")


# test run
assert os.path.exists("datalake/logs/api_server.log")
