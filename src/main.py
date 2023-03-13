import glob
import importlib
import os
import requests
import signal
import sys
from secrets_1 import auth_token

from client import Client

client = Client(auth_token)

jobs = []
job_files = os.listdir("src/jobs")

for job_file in job_files:
    name = os.path.splitext(os.path.basename(job_file))[0]
    module = importlib.import_module(f"jobs.{name}")
    job = getattr(module, 'job', None)
    
    if job is not None:
        jobs.append(job)
        job.init_data(client)
        job.start_job()


def signal_handler(sig, frame):
    print('Program interrupted. Exiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#signal.pause()
while True:
    pass