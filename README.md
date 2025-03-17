📌 Introduction

This project demonstrates the implementation of Stack and Queue data structures using an array (Python list). It includes basic operations such as push, pop, enqueue, and dequeue.

🚀 Features

🗂️ Stack Operations:

📌 push(value): Insert an element at the top

❌ pop(): Remove an element from the top

🔍 peek(): View the top element without removing it

❓ is_empty(): Check if the stack is empty

📦 Queue Operations:

➕ enqueue(value): Insert an element at the rear

❌ dequeue(): Remove an element from the front

🔍 peek(): View the front element without removing it

❓ is_empty(): Check if the queue is empty
🔍 Implementation Details

🗂️ Stack Implementation (Using List)

📌 Uses Python's built-in list as an array.

➕ push() appends an element to the end of the list.

❌ pop() removes and returns the last element.

🔍 peek() returns the last element without removing it.

📦 Queue Implementation (Using List)

📌 Uses Python's built-in list as an array.

➕ enqueue() appends an element to the end of the list.

❌ dequeue() removes and returns the first element.

🔍 peek() returns the first element without removing it.

⚠️ Limitations

⏳ The pop() and dequeue() operations have O(1) and O(n) complexity respectively due to Python's list behavior.

🏎️ For a more efficient queue, consider using collections.deque.
