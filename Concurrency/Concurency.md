# Concurrency: Matrix Multiplication Queue System

## Introduction
This project implements a **concurrent queue system** designed to process requests for matrix multiplications efficiently. The system utilizes both **multi-processing** for parallel execution and **configurable queue sizes** to handle varying workloads. The queue processes tasks using multiple worker processes, ensuring optimized handling of different request flooding scenarios.

### Features
- **Concurrent Execution**: Uses multi-processing to process tasks efficiently.
- **Configurable Queue Size**: Users can set the queue size dynamically.
- **Different Request Flooding Modes**:
  - Slow Mode: 1 request every _x_ seconds.
  - Burst Mode: 100 requests per _x_ seconds.
- **Performance Metrics**: Tracks total tasks processed, elapsed time, and throughput.

## Guidelines for the Homework
### 1. Implementing a Queue System
- The system uses **multiprocessing.Manager().Queue()** to manage queued tasks.
- Worker processes retrieve and process tasks asynchronously.
- Matrix multiplication (`numpy.matmul()`) is performed on large matrices to stress the system.

### 2. Configurable Queue Size
- Users can define the queue size via the `queue_size` parameter.
- The queue will drop requests if full, simulating real-world load handling.

### 3. Testing with Different Call Flooding Scenarios
- **Slow Mode**: Generates one request every `interval` seconds.
- **Burst Mode**: Generates 100 requests at a time, with a delay between bursts.
- **Duration is configurable** to observe the system under different workloads.

### 4. Multi-Threading vs Multi-Processing
- This implementation **uses multi-processing** for better performance on CPU-bound tasks.
- Worker processes handle matrix multiplications concurrently, avoiding Python's GIL limitations.


##### Acknowledgment:
##### This project was developed with guidance and assistance from professor Osama's lecture materials and ChatGPT by OpenAI


