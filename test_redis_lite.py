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

        print("\\n🎉 ALL TESTS PASSED! You have successfully implemented Redis-Lite!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except NotImplementedError:
        print("\n❌ TEST FAILED: You have a method that is not implemented yet!")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run_tests()
