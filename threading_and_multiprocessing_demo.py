import numpy as np

from utils.process_demo import ProcessDemo
from utils.thread_demo import ThreadDemo
from utils.visualize import TimelineVisualizer

NUM_WORKERS = 8
WORK_DURATION = 2.0
SAMPLE_INTERVAL_MS = 5.0


def main():

    print("=" * 60)
    print("THREADING")
    print("=" * 60)

    thread_demo = ThreadDemo(
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

    print("=" * 60)
    print("MULTIPROCESSING")
    print("=" * 60)

    process_demo = ProcessDemo(
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
    print(f"Threading      : {thread_time:.3f} s")
    print(f"Multiprocessing: {process_time:.3f} s")
    print(f"Speedup        : {thread_time / process_time:.2f}x")
    print("=" * 60)


if __name__ == "__main__":
    main()
