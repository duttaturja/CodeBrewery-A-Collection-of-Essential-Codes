class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, None)

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def contains(self, key):
        return key in self.map

# Example Usage
hash_map = HashMap()
hash_map.put("name", "Alice")
print(hash_map.get("name"))  # Output: Alice
hash_map.remove("name")
print(hash_map.contains("name"))  # Output: False
