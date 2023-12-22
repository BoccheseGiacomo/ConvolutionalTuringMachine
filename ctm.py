import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

#edge padding 
def edge_pad_3x3(arr):
    """
    Pad an array for a 3x3 kernel. This function adds one layer of padding around the array.
    """
    # Pad top and bottom with 1 row
    top_bottom_padded = np.vstack([arr[0, :], arr, arr[-1, :]])
    # Pad left and right with 1 column
    fully_padded = np.hstack([top_bottom_padded[:, 0:1], top_bottom_padded, top_bottom_padded[:, -1:]])
    return fully_padded

def edge_pad_5x5(arr):
    """
    Pad an array for a 5x5 kernel. This function adds two layers of padding around the array.
    """
    # Pad top and bottom with 2 rows
    top_bottom_padded = np.vstack([arr[0, :], arr[0, :], arr, arr[-1, :], arr[-1, :]])
    # Pad left and right with 2 columns
    fully_padded = np.hstack([top_bottom_padded[:, 0:1], top_bottom_padded[:, 0:1], 
                              top_bottom_padded, top_bottom_padded[:, -1:], top_bottom_padded[:, -1:]])
    return fully_padded


class CTM:
    def __init__(self):
        # Configurations
        self.dim = (20, 20)
        self.max_steps = 100  # Maximum number of steps in the simulation
        self.state = np.zeros(self.dim)  # Initialize the state grid
        self.kernel = np.random.rand(3, 3)*2-1  # Initialize the kernel
        self.halting_threshold = 0.7
        self.dt=0.1
        self.time_idx=0

        self.state_history=[]

        # Significant cells
        self.input_indexes = [(3, 0), (6, 0)]
        self.output_indexes = [(3, 19), (6, 19)]
        self.halting_index = (10, 19)
        self.reward_index = (15, 19)

    def set_input(self,input_values):
        for idx, value in zip(self.input_indexes, input_values):
            self.state[idx] = value

    def set_reward(self,reward):
        self.state[self.reward_index] = reward

    def get_output(self):
        return [self.state[idx] for idx in self.output_indexes]
    
    def get_halting(self):
        return self.state[self.halting_index]
    
    def reset_halting(self):
        # Reset the halting cell
        self.state[self.halting_index] = 0

        # Define the halving kernel
        halving_kernel = np.array([[0.3, 0.3, 0.3],
                                   [0.3, 0.0, 0.3],
                                   [0.3, 0.3, 0.3]])

        # Get the coordinates of the halting cell
        y, x = self.halting_index

        # Determine the slicing bounds, ensuring they are within the grid boundaries
        y_start, y_end = max(y - 1, 0), min(y + 2, self.dim[0])
        x_start, x_end = max(x - 1, 0), min(x + 2, self.dim[1])

        # Adjust the kernel size if slicing bounds are at the edges
        kernel_y_start, kernel_x_start = max(1 - y, 0), max(1 - x, 0)
        kernel_y_end, kernel_x_end = 3 - max(y + 2 - self.dim[0], 0), 3 - max(x + 2 - self.dim[1], 0)

        # Apply the halving kernel to the surrounding cells
        self.state[y_start:y_end, x_start:x_end] *= halving_kernel[kernel_y_start:kernel_y_end, kernel_x_start:kernel_x_end]


    def reset_recording(self):
        self.state_history=[]

    def save_state(self):
        self.state_history.append(self.state.copy())


    def forward(self, input_values, reward):
            if len(input_values) != len(self.input_indexes):
                raise ValueError("Input values size does not match input indexes size.")

            #reset halting
            self.reset_halting()

        
            for step in range(self.max_steps):
                
                self.set_input(input_values)
                self.set_reward(reward)

                # Add the current state
                self.save_state()

                # Apply convolution with edge padding
                padded_state = edge_pad_3x3(self.state)
                ds = convolve2d(padded_state, self.kernel, mode='valid')
                self.state += ds * self.dt

                # Check halting condition
                if self.get_halting() >= self.halting_threshold:
                    self.save_state()
                    break

            # Retrieve output values
            outputs = self.get_output()
            
            return outputs
    
    def visualize(self):
        # Set up the figure for animation
        fig, ax = plt.subplots()
        ims = []

        for state in self.state_history:
            # Create the heatmap from the state
            im = ax.imshow(state, animated=True, cmap='jet', vmin=-3, vmax=3)

            # Function to draw border around a cell
            def draw_border(y, x, color):
                rect = plt.Rectangle((x-0.5, y-0.5), 1, 1, fill=False, edgecolor=color, lw=4)
                ax.add_patch(rect)

            # Draw borders around the special cells
            for y, x in self.input_indexes:
                draw_border(y, x, 'green')  # Green for input
            for y, x in self.output_indexes:
                draw_border(y, x, 'blue')  # Blue for output
            y, x = self.halting_index
            draw_border(y, x, 'red')  # Red for halting
            y, x = self.reward_index
            draw_border(y, x, 'orange')  # Orange for reward

            ims.append([im])

        # Create the animation
        ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)

        # Add a colorbar
        fig.colorbar(im, ax=ax)

        # Save the animation to a file
        ani.save('simulation.mp4', writer='ffmpeg')

        # Close the plot to prevent it from displaying inline or in a new window
        plt.close(fig)