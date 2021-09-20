import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def print_simulation(simulation):
    """Print simulation to terminal. Uses 1 for live cells and 0 for dead cells."""
    for i, state in enumerate(simulation):
        print(f'Generation {i}')
        pprint(state)
        print()


def display_state(state, outfile=None, colors=['w', 'k'], grid=True):
    """Plot a specific state as a binary heatmap style plot."""
    fig, ax = plt.subplots()
    
    # Define the colors
    cmap = mpl.colors.ListedColormap(colors)

    # Create a normalize object the describes the limits of each color
    bounds = [0., 0.5, 1.]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # Plot
    im = ax.imshow(state, interpolation='none', cmap=cmap, norm=norm)

    # Format plot
    plt.xticks(np.arange(0 - 0.5, len(state[0]) - 0.5, 1.0))
    plt.yticks(np.arange(0 - 0.5, len(state) - 0.5, 1.0))
    plt.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        labelbottom=False,
        labelleft=False
    )
    if grid:
        plt.grid()

    if outfile:
        plt.savefig(outfile, bbox_inches='tight')
    

def animate_simulation(simulation):
    """Animate an entire simulation using binary heatmap style plots.
    Uses matplotlib.animation.FuncAnimation().
    """
    # Set up the figure
    fig, ax = plt.subplots()
    cmap = mpl.colors.ListedColormap(['w', 'k'])
    bounds = [0., 0.5, 1.]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    a = simulation[0]
    im = plt.imshow(a, interpolation='none', cmap=cmap, norm=norm)

    # Format plot
    plt.xticks(np.arange(0 - 0.5, len(simulation[0][0]) - 0.5, 1.0))
    plt.yticks(np.arange(0 - 0.5, len(simulation[0]) - 0.5, 1.0))
    plt.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        labelbottom=False,
        labelleft=False
    )
    plt.title("Generation 0")
    plt.grid()

    # Initialization function: plot the background of each frame
    def init():
        im.set_data(simulation[0])
        return [im]

    # Animation function. This is called sequentially
    def animate(i):
        plt.title(f"Generation {i}")
        im.set_array(simulation[i])
        return [im]

    # Call the animator.  blit=True means only re-draw the parts that have changed.
    anim = mpl.animation.FuncAnimation(fig, animate, init_func=init, frames=len(simulation), interval=1000, blit=True)
    anim.save('figures/animation.mp4', extra_args=['-vcodec', 'libx264'])


def animate_simulation_v2(simulation, outfile=None, colors=['w', 'k'], grid=True, frame_interval=1000):
    """Animate an entire simulation using binary heatmap style plots.
    Uses matplotlib.animation.ArtistAnimation().
    """
    fig, ax = plt.subplots()
    cmap = mpl.colors.ListedColormap(colors)
    bounds = [0., 0.5, 1.]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # Format plot
    plt.xticks(np.arange(0 - 0.5, len(simulation[0][0]) - 0.5, 1.0))
    plt.yticks(np.arange(0 - 0.5, len(simulation[0]) - 0.5, 1.0))
    plt.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        labelbottom=False,
        labelleft=False
    )
    if grid:
        plt.grid()
    
    frames = []
    for i in range(len(simulation)):
        title = ax.text(0.5,1.05,f"Generation {i}", 
                    size=plt.rcParams["axes.titlesize"], fontfamily="Serif", 
                    ha="center", transform=ax.transAxes)
        im = plt.imshow(simulation[i], interpolation='none', cmap=cmap, norm=norm, animated=True)
        frames.append([im, title])

    anim = mpl.animation.ArtistAnimation(fig, frames, interval=frame_interval, blit=True)

    if outfile:
        anim.save(outfile, extra_args=['-vcodec', 'libx264'])


if __name__ == '__main__':
    # Load data
    with open('data/result.json', 'r') as f:
        progress = json.load(f)

    # Print
    # print_simulation(progress)

    # Plot initial state
    # display_state(progress[0])
    # display_state(progress[1])

    # Animate simulation
    # anim_example()
    # animate_simulation(progress)
    # animate_simulation_v2(progress)

    animate_simulation_v2(progress, outfile='figures/animation_v2_grid.mp4', colors=['w', '#27ae60'], grid=False)

    plt.show()
