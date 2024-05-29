from collections import UserDict


class BidirectionalDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __len__(self):
        return super().__len__() // 2

    def __delitem__(self, key):
        try:
            super().__delitem__(key)
            super().__delitem__(self[key])
        except KeyError:
            return


bd = BidirectionalDict({"one":"two", "two":"three", "three": "twoo"})
print(bd.__len__())
bd["five"] = "three"
print(bd)
print(len(bd))
print(bd.pop("three"))
print(bd)
bd.update([("seven", "eight")])
print(bd)
