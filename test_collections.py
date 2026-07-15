import unittest
from collections import deque, Counter, defaultdict
import heapq

class TestPythonCollections(unittest.TestCase):
    def test_lists(self):
        arr = [10, 20, 30]
        arr.append(40)
        self.assertEqual(arr, [10, 20, 30, 40])
        
        arr.insert(1, 15)
        self.assertEqual(arr, [10, 15, 20, 30, 40])
        
        arr.extend([50, 60])
        self.assertEqual(arr, [10, 15, 20, 30, 40, 50, 60])
        
        last = arr.pop()
        self.assertEqual(last, 60)
        
        popped = arr.pop(1)
        self.assertEqual(popped, 15)
        
        arr.remove(20)
        del arr[0]
        self.assertEqual(arr, [30, 40, 50])
        
        # Sorting
        unsorted_arr = [5, 2, 9, 1]
        new_arr = sorted(unsorted_arr)
        self.assertEqual(new_arr, [1, 2, 5, 9])
        self.assertEqual(unsorted_arr, [5, 2, 9, 1])
        
        unsorted_arr.sort()
        self.assertEqual(unsorted_arr, [1, 2, 5, 9])
        
    def test_tuples(self):
        point = (10, 20)
        single = (5,)
        self.assertEqual(len(single), 1)
        
        # Unpacking
        x, y = point
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)
        
        # Immutability Check
        with self.assertRaises(TypeError):
            point[0] = 15
            
    def test_dicts(self):
        map_ = {"Alice": 25, "Bob": 30}
        map_["Charlie"] = 35
        map_.update({"Dave": 40})
        
        self.assertEqual(map_["Alice"], 25)
        self.assertEqual(map_.get("Eve", 0), 0)
        
        del map_["Bob"]
        self.assertNotIn("Bob", map_)
        
        val = map_.pop("Alice")
        self.assertEqual(val, 25)
        
        safe_val = map_.pop("Zoe", None)
        self.assertIsNone(safe_val)
        
    def test_advanced_collections(self):
        # Counter
        counts = Counter([1, 1, 2, 3, 3, 3])
        self.assertEqual(counts[3], 3)
        self.assertEqual(counts[99], 0)
        
        # defaultdict
        graph = defaultdict(list)
        graph["node_A"].append("node_B")
        self.assertEqual(graph["node_A"], ["node_B"])
        self.assertEqual(graph["node_C"], []) # Returns empty list instantly
        
    def test_sets(self):
        seen = set([1, 2, 3])
        seen.add(4)
        self.assertTrue(2 in seen)
        
        seen.remove(4)
        seen.discard(99) # Safe removal
        
        setA = {1, 2, 3}
        setB = {3, 4, 5}
        self.assertEqual(setA & setB, {3})              # Intersection
        self.assertEqual(setA | setB, {1, 2, 3, 4, 5})  # Union
        self.assertEqual(setA - setB, {1, 2})           # Difference
        self.assertEqual(setA ^ setB, {1, 2, 4, 5})     # Symmetric Difference

if __name__ == '__main__':
    unittest.main()
