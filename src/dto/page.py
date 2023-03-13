from collections import defaultdict

from dto.property_map import property_map

class Record(object):
    def __init__(self, client, values = defaultdict(lambda: "KeyNotFound")):
        self.client = client
        self.values = values

    def get_property(self, name):
        return self.values[name][name][0]["text"]["content"]

    def set_property(self, name, value):
        # internal setting
        # refacto the dictionnary to store more easily accessible data
        self.values[name][name][0]["text"]["content"] = value
        # api update - only update title for now
        self.client.change_page_title(self.id, value)

class Page(Record):
    def __init__(self, id, client, value):
        self.id = id
        super().__init__(client, value)

    title = property_map("title")
