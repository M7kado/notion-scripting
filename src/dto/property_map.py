
def property_map(name):
    def fget(self):
        return self.get_property(name)

    def fset(self, value):
        self.set_property(name, value)

    return property(
        fget=fget,
        fset=fset,
    )