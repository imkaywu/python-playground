import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

step = 10


class TimelineVisualizer:

    def __init__(
        self,
        timelines,
        total_time,
        title,
        interval=20,
    ):
        """
        timelines:
            list of numpy arrays
            each array has shape (N,2)

            column0 = timestamp(ns)
            column1 = progress counter
        """

        self.timelines = timelines
        self.total_time = total_time
        self.title = title
        self.interval = interval

        self.num_workers = len(timelines)
        self.num_bins = timelines[0].shape[0]

        #
        # Convert into image
        #

        self.image = np.stack([t[:, 1] for t in timelines]).astype(np.float32)

        #
        # Normalize each column
        #

        col_max = self.image.max(axis=0)
        col_max[col_max == 0] = 1

        self.image /= col_max

        #
        # Figure
        #

        self.fig, self.ax = plt.subplots(figsize=(14, 5))

        self.im = self.ax.imshow(
            np.zeros_like(self.image),
            origin="lower",
            aspect="auto",
            interpolation="nearest",
            cmap="viridis",
            vmin=0,
            vmax=1,
        )

        self.cursor = self.ax.axvline(
            0,
            color="red",
            linewidth=2,
        )

        self.ax.set_title(title)

        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Worker")

        ticks = np.linspace(
            0,
            self.num_bins - 1,
            6,
            dtype=int,
        )

        labels = [
            f"{i * total_time / (len(ticks)-1):.1f}" for i in range(len(ticks))
        ]

        self.ax.set_xticks(ticks)
        self.ax.set_xticklabels(labels)

        self.ax.set_yticks(range(self.num_workers))

        self.fig.colorbar(
            self.im,
            ax=self.ax,
            label="Relative CPU Progress",
        )

    def update(self, frame):

        visible = np.zeros_like(self.image)

        visible[:, :frame] = self.image[:, :frame]

        self.im.set_data(visible)

        self.cursor.set_xdata([frame, frame])

        return self.im, self.cursor

    def animate(self):

        anim = FuncAnimation(
            self.fig,
            self.update,
            frames=range(0, self.num_bins, step),
            interval=self.interval,
            repeat=False,
            blit=False,
        )

        plt.tight_layout()
        plt.show()

        return anim
