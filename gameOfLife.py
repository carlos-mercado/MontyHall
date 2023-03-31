#Conway's Game of Life
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def transition(matrix):
    N = len(matrix)
    newMap = np.zeros((N, N))

    for row in range(N):
        for col in range(N):
            #getting all the adjacent cell indexes
            topCell = ((row - 1) % N, col)
            bottomCell = ((row + 1) % N, col)
            leftCell = (row, (col - 1) % N)
            rightCell = (row, (col + 1) % N)
            topLeftCell = ((row - 1) % N, (col - 1) % N)
            topRightCell = ((row - 1) % N, (col + 1) % N)
            bottomLeftCell = ((row + 1) % N, (col - 1) % N)
            bottomRightCell = ((row + 1) % N, (col + 1) % N)

            totalSurrounding = 0
            totalSurrounding = totalSurrounding + matrix[topCell[0], topCell[1]] \
                                                + matrix[bottomCell[0], bottomCell[1]] \
                                                + matrix[leftCell[0], leftCell[1]] \
                                                + matrix[rightCell[0], rightCell[1]] \
                                                + matrix[topLeftCell[0], topLeftCell[1]] \
                                                + matrix[topRightCell[0], topRightCell[1]] \
                                                + matrix[bottomLeftCell[0], bottomLeftCell[1]] \
                                                + matrix[bottomRightCell[0], bottomRightCell[1]]

            if matrix[row, col] == 1: #if the cell is alive
                if totalSurrounding < 2:
                    newMap[row, col] = 0 #cell dies
                elif totalSurrounding > 3:
                    newMap[row, col] = 0 #cell dies
                else:
                    newMap[row, col] = 1 #cell is alive
            else: #if the cell is dead
                if totalSurrounding == 3:
                    newMap[row, col] = 1 #cell is reborn
                else:
                    newMap[row, col] = 0 #cell dies
    return newMap

n = 50
map = np.zeros((n, n))

#putting in a glider
map[5,5] = 1
map[4,5] = 1
map[3,5] = 1
map[5,4] = 1
map[4,3] = 1

#bliker
map[8,8] = 1
map[7,8] = 1
map[6,8] = 1

fig, ax = plt.subplots()

# Plot the map as a heatmap
im = ax.imshow(map, cmap='viridis')

# Set the title and axis labels
ax.set_title('Game of Life')


# Animate the plot
def animate(frame):
    global map, im
    map = transition(map)  # update the matrix
    im.set_data(map)  # update the plot data
    ax.set_title(f'Game of Life (Frame {frame})')  # set the title to show the frame number
    return [im]

ani = animation.FuncAnimation(fig, animate, frames=10, interval=10)

plt.show()