import threading
import time

import numpy as np

from utils.cpu_task import sample_progress_thread


class ThreadDemo:

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
