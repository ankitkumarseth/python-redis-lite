import collections

class RedisLite:
    """
    An in-memory Key-Value store to practice Python Data Structures and OOP.
    """
    
    def __init__(self):
        # Initialize a dictionary to store your key-value pairs
        self.store = {}

    def set(self, key: str, value: str) -> None:
        """
        Store the key-value pair.
        """
        self.store[key] = value

    def get(self, key: str) -> str:
        """
        Retrieve the value for a given key.
        If the key doesn't exist, raise a KeyError with a custom message.
        """
        try:
            return self.store[key]
        except KeyError:
            raise KeyError(f"Key '{key}' does not exist in RedisLite.")

    def delete(self, key: str) -> bool:
        """
        Delete a key from the store. 
        Return True if deleted, False if the key didn't exist.
        """
        if key in self.store:
            del self.store[key]
            return True
        return False

    # --- QUEUE OPERATIONS (Simulating Redis Lists) ---

    def lpush(self, key: str, value: str) -> None:
        """
        Push a value to the 'left' (start) of a list stored at the key.
        If the key doesn't exist, create a new collections.deque.
        """
        if key not in self.store:
            self.store[key] = collections.deque()
        self.store[key].appendleft(value)

    def rpop(self, key: str) -> str:
        """
        Pop and return a value from the 'right' (end) of a list stored at the key.
        If the key doesn't exist or is empty, return None.
        """
        if key not in self.store or not self.store[key]:
            return None
        return self.store[key].pop()

    # --- BITWISE CHALLENGE ---

    def basic_hash(self, key: str) -> int:
        """
        A simple hashing function using bitwise XOR.
        For each character in the string, XOR its ASCII value (using ord()) 
        with a running hash value.
        Return the final integer hash.
        """
        hash_val = 0
        for char in key:
            hash_val ^= ord(char)
        return hash_val

    # --- FILE HANDLING (Simulating Redis Snapshots) ---

    def save_to_disk(self, filename: str) -> None:
        """
        Save the current key-value store to a file.
        Write each key-value pair as "key,value\\n" on a new line.
        """
        with open(filename, 'w') as f:
            for k, v in self.store.items():
                if isinstance(v, str):
                    f.write(f"{k},{v}\n")

    def load_from_disk(self, filename: str) -> None:
        """
        Load key-value pairs from a file, overwriting the current store.
        Assume the file format is "key,value\\n" on each line.
        """
        self.store.clear()
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    self.store[parts[0]] = parts[1]

    # --- PURE PYTHON SKILLS (Dunder, *args, Comprehensions) ---

    def __len__(self) -> int:
        """
        Return the total number of keys currently in the store.
        """
        return len(self.store)

    def __str__(self) -> str:
        """
        Return a string representation of the database.
        """
        return f"RedisLite with {len(self)} keys"

    def mset(self, *args) -> None:
        """
        Set multiple key-value pairs at once. 
        `args` will be a tuple like ("key1", "val1", "key2", "val2").
        """
        for i in range(0, len(args), 2):
            if i + 1 < len(args):
                self.set(args[i], args[i+1])

    def keys(self, pattern: str) -> list:
        """
        Return a list of all keys that contain the given pattern.
        """
        return [k for k in self.store.keys() if pattern in k]
