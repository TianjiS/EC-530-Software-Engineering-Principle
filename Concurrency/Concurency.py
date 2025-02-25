import numpy as np
import multiprocessing
import time
import random
from multiprocessing import Queue
import micropip


class MatrixQueueSystem:
    def __init__(self, queue_size=10):
        self.queue = Queue(maxsize=queue_size)
        self.running = multiprocessing.Value('b', True)
        self.processes = []
        self.start_time = time.time()
        self.processed_tasks = multiprocessing.Value('i', 0)

    def process_request(self):
        """ Worker function to process matrix multiplications """
        while self.running.value:
            if not self.queue.empty():
                matrices = self.queue.get()
                result = np.matmul(matrices[0], matrices[1])  # matrix multiplication
                with self.processed_tasks.get_lock():
                    self.processed_tasks.value += 1
                print(f"Processed matrix multiplication with shape {matrices[0].shape}")
            else:
                time.sleep(0.1)
    
    def start_workers(self, num_workers=2):
        """ Start worker processes """
        for _ in range(num_workers):
            p = multiprocessing.Process(target=self.process_request)
            p.start()
            self.processes.append(p)

    def stop_workers(self):
        """ Stop all worker processes """
        self.running.value = False
        for p in self.processes:
            p.join()

    def add_request(self, matrix_a, matrix_b):
        """ Add a request to the queue """
        if not self.queue.full():
            self.queue.put((matrix_a, matrix_b))
        else:
            print("Queue is full! Dropping request.")
    
    def simulate_requests(self, mode='slow', duration=5, interval=1, batch_size=100):
        """ Simulate incoming requests at different rates """
        start_time = time.time()
        while time.time() - start_time < duration:
            if mode == 'slow':
                matrix_a = np.random.rand(100, 100)
                matrix_b = np.random.rand(100, 100)
                self.add_request(matrix_a, matrix_b)
                time.sleep(interval)
            elif mode == 'burst':
                for _ in range(batch_size):
                    matrix_a = np.random.rand(100, 100)
                    matrix_b = np.random.rand(100, 100)
                    self.add_request(matrix_a, matrix_b)
                time.sleep(interval)

    def print_metrics(self):
        """ Print performance metrics """
        elapsed_time = time.time() - self.start_time
        print(f"Total processed tasks: {self.processed_tasks.value}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Throughput: {self.processed_tasks.value / elapsed_time:.2f} tasks per second")
        
# Example Usage
if __name__ == "__main__":
    queue_size = 50  # Configurable queue size
    system = MatrixQueueSystem(queue_size=queue_size)
    system.start_workers(num_workers=4)  # Start 4 worker processes
    
    try:
        # Test different call flooding scenarios
        print("Running slow request test: 1 request every 2 seconds")
        system.simulate_requests(mode='slow', duration=10, interval=2)
        
        print("Running burst request test: 100 requests every 5 seconds")
        system.simulate_requests(mode='burst', duration=10, interval=5, batch_size=100)
        
    except KeyboardInterrupt:
        print("Stopping simulation...")
    
    system.stop_workers()
    system.print_metrics()
