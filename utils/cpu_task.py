import time


def sample_progress_thread(perf_start, array):

    dt = array[1, 0] - array[0, 0]

    while True:

        t = time.perf_counter_ns() - perf_start

        i = int(t / dt)

        if i >= len(array):
            break

        array[i, 1] += 1

    return array


def sample_progress_process(wall_start, perf_start, array):

    startup_delay = time.time() - wall_start

    dt = array[1, 0] - array[0, 0]

    while True:

        t = time.perf_counter_ns() - perf_start - startup_delay * 1e9

        i = int(t / dt)

        if i >= len(array):
            break

        array[i, 1] += 1

    return array
