
import time
from job_template import Job

def init_data(client):
    page = client.get_page("791923b871ad415c9454bdd385edb727")
    return client, page

def routine(client, *args):
    localtime = time.localtime()
    # in this case we could also call client.change_page_title
    args[0].title = time.strftime("%H:%M:%S", localtime)

job = Job(init_data=init_data, routine=routine, refreshRate=10)