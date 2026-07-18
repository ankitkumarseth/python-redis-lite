class Database:
    def __init__(self):
        self.store = {"A": 1, "B": 2}

    def __len__(self):
        # Allows you to call `len(db)`!
        return len(self.store)

    def __str__(self):
        # Equivalent to Java's `toString()`
        return f"Database with {len(self)} items"


db = Database()
print(len(db))  # 2
print(db)  # "Database with 2 items"