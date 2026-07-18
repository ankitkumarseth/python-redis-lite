import re
from collections import deque


class RedisLite:
    """
    An in-memory Key-Value store to practice Python Data Structures and OOP.
    """
    
    def __init__(self):
        self.redis_dict = {}
        self.expiry_dict = {}

    def set(self, key: str, value: str) -> None:
        """
        Store the key-value pair.
        """
        self.redis_dict[key] = value

    def get(self, key: str) -> str:
        """
        Retrieve the value for a given key.
        If the key doesn't exist, raise a KeyError with a custom message.
        """
        try:
            return self.redis_dict[key]
        except KeyError as e:
            raise KeyError(f"Key {key} does not exist in Redis datastore")

    def delete(self, key: str) -> bool:
        """
        Delete a key from the store. 
        Return True if deleted, False if the key didn't exist.
        """
        result = self.redis_dict.pop(key, None)
        return bool(result)

    # --- QUEUE OPERATIONS (Simulating Redis Lists) ---

    def lpush(self, key: str, value: str) -> None:
        """
        Push a value to the 'left' (start) of a list stored at the key.
        If the key doesn't exist, create a new collections.deque.
        HINT: Use collections.deque for O(1) left insertions!
        """
        if key in  self.redis_dict.keys():
            self.redis_dict[key].appendleft(value)
        else:
            self.redis_dict[key] = deque([value])

    def rpop(self, key: str) -> str | None:
        """
        Pop and return a value from the 'right' (end) of a list stored at the key.
        If the key doesn't exist or is empty, return None.
        """
        if key in self.redis_dict.keys() and len(self.redis_dict[key]) > 0:
            return self.redis_dict[key].pop()
        else: return None

    # --- BITWISE CHALLENGE ---

    def basic_hash(self, key: str) -> int:
        """
        A simple hashing function using bitwise XOR.
        For each character in the string, XOR its ASCII value (using ord()) 
        with a running hash value.
        Return the final integer hash.
        """
        # Initialize hash_val = 0
        hash_value = 0
        for char in key:
            hash_value ^= ord(char)
        return hash_value

    # --- FILE HANDLING (Simulating Redis Snapshots) ---

    def save_to_disk(self, filename: str) -> None:
        """
        Save the current key-value store to a file.
        Write each key-value pair as "key,value\\n" on a new line.
        """
        with open(filename, 'w') as file:
            for key,value in self.redis_dict.items():
                file.write(f"{key},{value}\n")

    def load_from_disk(self, filename: str) -> None:
        """
        Load key-value pairs from a file, overwriting the current store.
        Assume the file format is "key,value\\n" on each line.
        """
        # TODO: Open the file in 'r' mode, read line by line, split by comma, and store in the dictionary.
        with open(filename, 'r') as file:
            for line in file:
                key_value = line.strip().split(',')
                self.set(key_value[0], key_value[1])

    # --- PURE PYTHON SKILLS (Dunder, *args, Comprehensions) ---

    def __len__(self) -> int:
        """
        Return the total number of keys currently in the store.
        This allows the user to call `len(db)` directly.
        """
        return len(self.redis_dict)

    def __str__(self) -> str:
        """
        Return a string representation of the database, e.g., "RedisLite with X keys".
        This allows the user to call `print(db)`.
        """
        return f"RedisLite data store with {len(self)} items"

    def mset(self, *args) -> None:
        """
        Set multiple key-value pairs at once. 
        `args` will be a tuple like ("key1", "val1", "key2", "val2").
        """
        # Hint: self.set(args[i], args[i+1])
        for i in range(0, len(args), 2):
            self.set(args[i], args[i+1])

    def keys(self, pattern: str) -> list:
        """
        Return a list of all keys that contain the given pattern.
        """
        # TODO: Implement this using a one-line list comprehension!
        keys =  [key for key in self.redis_dict if pattern in key]
        return keys

