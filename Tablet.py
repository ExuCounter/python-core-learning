models = ("lite", "pro", "max")

memory_amount = {
    "lite": 2,
    "pro": 3,
    "max": 4
}

storage_capacity = {
    "lite": 32,
    "pro": 64,
    "max": 128
}

max_storage_amount = 1024


class Tablet:
    def __init__(self, model):
        if not isinstance(model, str) or model not in models:
            return TypeError("Wrong model type")

        self._base_storage = storage_capacity[model]
        self._memory = memory_amount[model]
        self._added_storage = 0

    @property
    def base_storage(self):
        return self._base_storage

    @property
    def added_storage(self):
        return self._added_storage

    @property
    def memory(self):
        return self._memory

    @property
    def storage(self):
        return self.base_storage + self.added_storage

    def add_storage(self, amount):
        if self.added_storage + amount > max_storage_amount:
            return "Max storage amount exceeded"

        self._added_storage = amount


pro = Tablet("pro")
lite = Tablet("lite")
max = Tablet("max")

print(lite.storage)
print(pro.storage)
max.add_storage(500)
print(max.storage)
print(max.add_storage(1000))
print(max.storage)
print(max.base_storage)
print(max.memory)
