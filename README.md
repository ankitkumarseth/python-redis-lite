# Python Redis-Lite Tutorial

Welcome to **Redis-Lite**, an interactive, test-driven tutorial designed to teach foundational Python, Object-Oriented Programming (OOP), and core Data Structures & Algorithms (DSA).

This project was built for experienced developers (specifically those transitioning from Java) to rapidly master Python without slogging through beginner tutorials.

## What is this?

Instead of solving random algorithmic puzzles, you will build a functional, in-memory Key-Value store modeled after Redis. By completing this project, you will master:
- **Core Syntax & Exceptions:** `try/except`, `KeyError` handling.
- **Data Structures:** Dictionaries (Hash Maps) and `collections.deque` (Queues).
- **File Handling:** Serializing and deserializing data to disk (simulating RDB snapshots).
- **Bitwise Operations:** Implementing a basic XOR hashing function.

## How to use this project

1. **The Reference Guide:** Keep `python_master_cheatsheet.md` open. It contains everything you need to know about Python syntax, mapped directly to Java concepts.
2. **The Code:** Open `redis_lite.py`. You will see several empty methods with `TODO` comments.
3. **The Tests:** Open your terminal and run the test suite:
   ```bash
   python3 test_redis_lite.py
   ```
4. **The Goal:** The tests will fail initially. Use the cheatsheet to write the Python code in `redis_lite.py` until every single test in `test_redis_lite.py` passes!

## Project Structure

- `redis_lite.py`: The main class you need to implement.
- `test_redis_lite.py`: The test suite that validates your implementation.
- `python_master_cheatsheet.md`: The ultimate Python reference guide for Java developers.

Happy Coding! 🚀
