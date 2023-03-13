from threading import Thread
import time


class Job:
    def __init__(self, init_data, routine=None, callback=None, refreshRate=60):
        self._init = init_data
        self.routine = routine
        self.callback = callback
        self.refreshRate = refreshRate
        assert self.routine or self.callback, "Job must have a routine or callback"

    def init_data(self, client):
        self.client, self.data = self._init(client)

    def start_job(self):
        thread = Thread(target=self.run, args=(), daemon=True)
        thread.start()

    def run(self):
        while True:
            #fetch data
            if self.routine: self.routine(self.client, self.data)
            #if data changed, call callback
            if self.callback: self.callback(self.client, self.data)
            time.sleep(self.refreshRate)
