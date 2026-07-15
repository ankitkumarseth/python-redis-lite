class RedisLite:
    """
    An in-memory Key-Value store to practice Python Data Structures and OOP.
    """
    
    def __init__(self):
        # TODO: Initialize a dictionary to store your key-value pairs
        # TODO: Initialize a dictionary to store expiry times (optional challenge)
        pass

    def set(self, key: str, value: str) -> None:
        """
        Store the key-value pair.
        """
        # TODO: Implement this method
        pass

    def get(self, key: str) -> str:
        """
        Retrieve the value for a given key.
        If the key doesn't exist, raise a KeyError with a custom message.
        """
        # TODO: Implement this method using a try/except or an if statement
        pass

    def delete(self, key: str) -> bool:
        """
        Delete a key from the store. 
        Return True if deleted, False if the key didn't exist.
        """
        # TODO: Implement this method
        pass

    # --- QUEUE OPERATIONS (Simulating Redis Lists) ---

    def lpush(self, key: str, value: str) -> None:
        """
        Push a value to the 'left' (start) of a list stored at the key.
        If the key doesn't exist, create a new collections.deque.
        HINT: Use collections.deque for O(1) left insertions!
        """
        # TODO: Implement this method
        pass

    def rpop(self, key: str) -> str:
        """
        Pop and return a value from the 'right' (end) of a list stored at the key.
        If the key doesn't exist or is empty, return None.
        """
        # TODO: Implement this method
        pass

    # --- BITWISE CHALLENGE ---

    def basic_hash(self, key: str) -> int:
        """
        A simple hashing function using bitwise XOR.
        For each character in the string, XOR its ASCII value (using ord()) 
        with a running hash value.
        Return the final integer hash.
        """
        # TODO: Implement this method using a for loop and the ^ operator.
        # Initialize hash_val = 0
        pass

    # --- FILE HANDLING (Simulating Redis Snapshots) ---

    def save_to_disk(self, filename: str) -> None:
        """
        Save the current key-value store to a file.
        Write each key-value pair as "key,value\\n" on a new line.
        """
        # TODO: Open the file in 'w' mode and write the contents of your dictionary.
        pass

    def load_from_disk(self, filename: str) -> None:
        """
        Load key-value pairs from a file, overwriting the current store.
        Assume the file format is "key,value\\n" on each line.
        """
        # TODO: Open the file in 'r' mode, read line by line, split by comma, and store in the dictionary.
        pass
