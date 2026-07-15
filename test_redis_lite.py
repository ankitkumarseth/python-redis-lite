import traceback
from redis_lite import RedisLite

def run_tests():
    try:
        db = RedisLite()
        
        print("Test 1: Basic Key-Value Storage (set & get)")
        db.set("name", "Ankit")
        assert db.get("name") == "Ankit", "Expected get('name') to return 'Ankit'"
        
        print("Test 2: Overwriting a key")
        db.set("name", "Principal Engineer")
        assert db.get("name") == "Principal Engineer", "Expected 'name' to be overwritten"
        
        print("Test 3: KeyError on missing key")
        try:
            db.get("missing_key")
            assert False, "Expected KeyError to be raised for missing key"
        except KeyError:
            pass # Success!
            
        print("Test 4: Deleting a key")
        assert db.delete("name") == True, "Expected delete to return True on success"
        try:
            db.get("name")
            assert False, "Key should have been deleted!"
        except KeyError:
            pass # Success!
        assert db.delete("name") == False, "Expected delete to return False if key doesn't exist"

        print("Test 5: Queue Operations (lpush & rpop)")
        db.lpush("tasks", "task3")
        db.lpush("tasks", "task2")
        db.lpush("tasks", "task1")
        # List should look like: [task1, task2, task3]
        
        assert db.rpop("tasks") == "task3", "Expected rpop to return 'task3'"
        assert db.rpop("tasks") == "task2", "Expected rpop to return 'task2'"
        assert db.rpop("tasks") == "task1", "Expected rpop to return 'task1'"
        assert db.rpop("tasks") == None, "Expected None when popping from an empty list"

        print("Test 6: Bitwise Hash")
        # Hash of "abc" -> ord('a') ^ ord('b') ^ ord('c') = 97 ^ 98 ^ 99 = 96
        h = db.basic_hash("abc")
        assert h == 96, f"Expected basic_hash('abc') to be 96, but got {h}"

        print("Test 7: File Handling (Snapshots)")
        db.set("persistent_key", "survives_crash")
        db.save_to_disk("dump.rdb")
        
        # Create a completely new database instance
        new_db = RedisLite()
        new_db.load_from_disk("dump.rdb")
        assert new_db.get("persistent_key") == "survives_crash", "Expected loaded db to have 'persistent_key'"
        import os
        if os.path.exists("dump.rdb"):
            os.remove("dump.rdb")

        print("Test 8: Dunder Methods (__len__ and __str__)")
        db.set("a", "1")
        db.set("b", "2")
        assert len(db) >= 2, f"Expected len(db) to work, got {len(db)}"
        assert "RedisLite" in str(db), f"Expected str(db) to return a descriptive string, got: {str(db)}"

        print("Test 9: Packing/Unpacking (*args)")
        db.mset("key1", "val1", "key2", "val2")
        assert db.get("key1") == "val1"
        assert db.get("key2") == "val2"

        print("Test 10: List Comprehensions")
        db.set("user:1", "Ankit")
        db.set("user:2", "John")
        db.set("admin:1", "Alice")
        res = db.keys("user:")
        assert len(res) == 2 and "user:1" in res and "user:2" in res, f"Expected keys('user:') to return 2 matching keys, got {res}"

        print("\n🎉 ALL TESTS PASSED! You have successfully implemented Redis-Lite!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except NotImplementedError:
        print("\n❌ TEST FAILED: You have a method that is not implemented yet!")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run_tests()
