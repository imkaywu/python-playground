"""
This demo is based on the tutorial 'threading vs multiprocessing in python'
(AZnGRKFUU0c)
"""

import threading
import time

import numpy as np

from utils.cpu_task import sample_progress_thread
from utils.visualize import TimelineVisualizer

NUM_WORKERS = 8
WORK_DURATION = 2.0
SAMPLE_INTERVAL_MS = 5.0


class ThreadingDemo:

    def __init__(
        self,
        num_workers=8,
        work_duration=2.0,
        sample_interval_ms=1.0,
    ):

        self.num_workers = num_workers

        dt = int(sample_interval_ms * 1e6)

        num_bins = int(work_duration * 1000 / sample_interval_ms)

        self.dt = dt
        self.num_bins = num_bins

        self.timeline = []

        for _ in range(num_workers):

            arr = np.zeros((num_bins, 2), dtype=np.int64)

            arr[:, 0] = np.arange(num_bins) * dt

            self.timeline.append(arr)

    def run(self):

        t0 = time.perf_counter_ns()

        threads = []

        for worker in range(self.num_workers):

            t = threading.Thread(
                target=sample_progress_thread,
                args=(
                    t0,
                    self.timeline[worker],
                ),
            )

            t.start()

            threads.append(t)

        for t in threads:
            t.join()

        elapsed = (time.perf_counter_ns() - t0) / 1e9

        return elapsed, self.timeline


def main():

    print("=" * 60)
    print("THREADING")
    print("=" * 60)

    thread_demo = ThreadingDemo(
        num_workers=NUM_WORKERS,
        work_duration=WORK_DURATION,
        sample_interval_ms=SAMPLE_INTERVAL_MS,
    )

    thread_time, thread_timelines = thread_demo.run()

    print(f"Completed in {thread_time:.3f} s")

    thread_vis = TimelineVisualizer(
        timelines=thread_timelines,
        total_time=thread_time,
        title=f"Threading ({NUM_WORKERS} threads)",
    )

    thread_vis.animate()

    print()
    print("=" * 60)
    print(f"Threading      : {thread_time:.3f} s")
    print("=" * 60)


if __name__ == "__main__":
    main()
