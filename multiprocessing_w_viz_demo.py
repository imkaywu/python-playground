"""
This demo is based on the tutorial 'threading vs multiprocessing in python'
(AZnGRKFUU0c)
"""

import multiprocessing as mp
import time

import numpy as np

from utils.cpu_task import sample_progress_process
from utils.visualize import TimelineVisualizer

NUM_WORKERS = 8
WORK_DURATION = 2.0
SAMPLE_INTERVAL_MS = 5.0


class MultiProcessingDemo:

    def __init__(
        self,
        num_workers=8,
        work_duration=2.0,
        sample_interval_ms=1.0,
    ):
        self.num_workers = num_workers
        self.work_duration = work_duration
        self.sample_interval_ms = sample_interval_ms

        self.dt = int(sample_interval_ms * 1e6)

        self.num_bins = int(work_duration * 1000 / sample_interval_ms)

        # Base timeline.
        # Every worker receives its own copy.

        self.template = np.zeros(
            (self.num_bins, 2),
            dtype=np.int64,
        )

        self.template[:, 0] = np.arange(self.num_bins) * self.dt

    def run(self):

        # Create one copy per process.

        arrays = [np.copy(self.template) for _ in range(self.num_workers)]

        # Pool

        with mp.Pool(self.num_workers) as pool:

            # Warm up all workers first.
            pool.map(int, range(self.num_workers))

            t0 = time.time()
            t1 = time.perf_counter_ns()

            timelines = pool.starmap(
                sample_progress_process,
                [(t0, t1, arr) for arr in arrays],
            )

        return self.work_duration, timelines


def main():

    process_demo = MultiProcessingDemo(
        num_workers=NUM_WORKERS,
        work_duration=WORK_DURATION,
        sample_interval_ms=SAMPLE_INTERVAL_MS,
    )

    process_time, process_timelines = process_demo.run()

    print(f"Completed in {process_time:.3f} s")

    process_vis = TimelineVisualizer(
        timelines=process_timelines,
        total_time=process_time,
        title=f"Multiprocessing ({NUM_WORKERS} processes)",
    )

    process_vis.animate()

    print()
    print("=" * 60)
    print(f"Multiprocessing: {process_time:.3f} s")
    print("=" * 60)


if __name__ == "__main__":
    main()
