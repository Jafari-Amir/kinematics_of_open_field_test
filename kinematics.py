import matplotlib.pyplot as plt
import pandas as pd
import imageio
# Read the CSV file  to DataFrame
df = pd.read_csv('/Users/directory path/example.csv')
#get the x and y columns from the DataFrame and it starts from b2 position(at lease in our case)
x = df['X']
y = df['Y']
# define a figure and axes
fig, axs = plt.subplots(1, 2, figsize=(8, 5), gridspec_kw={'wspace':0.3, 'hspace':3})
# Set the title for the figure
fig.suptitle('X and Y Coordinations')
#set labels for open field test axis
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
#set the minimum and maximum values for the x-axis and y-axis, which usually came from csv file which contains number and locations (EZ track software)
axs[0].set_xlim(0, 800)
axs[0].set_ylim(0, 800)
# You case chage into true or false the x-axis and y-axis labels with this
axs[0].xaxis.set_visible(True)
axs[0].yaxis.set_visible(True)
# Set the height and width of the first subplot
fig.set_figheight(4)
fig.set_figwidth(8)
#this plots the x and y coordinates as rows increase in the first subplot
axs[0].plot(y, x)
# box plot of the x and y coordinates in the second subplot
axs[1].boxplot([x, y])
##################################
axs[0].grid(True, which='both', axis='both', linestyle='--', color='grey', alpha=1)
num_rows = len(df)
#imageio writer object makes a gif with following fps for each frame in term of milisecond
writer = imageio.get_writer('plot.gif', mode='I', duration=0.001)  # Set the duration of each frame
# we need an empty list to store list of the dots
dots = []
#loop rows of the data and add each frame to the GIF from 10 row and jump to another 10th data, to make shorter gif
for i in range(0, num_rows, 10):
    # his makes an updated  x and y values for the current row
    x_val = x[i]
    y_val = y[i]
#add the current dot to the list of dots
    dots.append((x_val, y_val)) 
       #clear current plot
    axs[0].clear()
     # this helps the title for the figure
    fig.suptitle('X and Y Coordinates')
    # Set the x and y axis labels
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].set_xlim(x.min(), x.max())
    axs[0].set_ylim(y.min(), y.max())
    axs[1].set_xticklabels(['X', 'Y'])
    # Plot all the dots in the list, with the current dot in red and all the previous dots in black
    axs[0].scatter([dot[0] for dot in dots], [dot[1] for dot in dots], c=range(len(dots)), cmap='Wistia', s=18, alpha=1)
       # to add constant updates of formed plots as a PNG image
    plt.savefig('plot.png')
     # this adds following updated plot to form the GIF
    image = imageio.imread('plot.png')
    writer.append_data(image)
# In the end the writer object must be ended
writer.close()
# shows GIF using matplotlib imshow function
plt.imshow(imageio.imread('plot.gif'))
plt.show()
#you could manipulate your data with following lines too, in its right palce
#df2 = df1.drop(df1.index[np.where(df1.index > 9000)])
#df = df2.iloc[::60, :]