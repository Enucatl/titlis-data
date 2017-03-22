import matplotlib.pyplot as plt
import numpy as np
import h5py
import click


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
def main(input_file, output_file):
    h5file = h5py.File(input_file)
    datasets0 = [np.median(d) for d in h5file["/entry/data/th_0"].values()]
    datasets1 = [np.median(d) for d in h5file["/entry/data/th_1"].values()]
    xs = np.arange(len(datasets0))
    plt.figure()
    plt.plot(xs, datasets0, xs, datasets1)
    plt.savefig(output_file, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
