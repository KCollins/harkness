# functions for visualization of data from pandas dataframes

# Importing packages
import pandas as pd
import matplotlib.pyplot as plt



def create_ply(df, filename, C = 'C',  X = 'X', Y = 'Y', Z = 'Z', cmap = 'viridis'):
   
    """
    Create a PLY file from a pandas DataFrame with columns X, Y, Z, and C.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the point cloud data.
        filename (str): The filename for the PLY file.
        C: The column of df associated with color
        X, Y, Z: column names associated with X, Y and Z. XYZ by default.
        cmap: The matplotlib colormap used for the .ply file. 'viridis' by default.
    """

    with open(filename, 'w') as f:
        f.write('ply\n')
        f.write('format ascii 1.0\n')
        f.write('element vertex %d\n' % len(df))
        f.write('property float x\n')
        f.write('property float y\n')
        f.write('property float z\n')
        f.write('property uchar red\n')
        f.write('property uchar green\n')
        f.write('property uchar blue\n')
        f.write('end_header\n')

        for i in range(len(df)):
            row = df.iloc[i]
            # from matplotlib.colors import cmap
            cmap = plt.get_cmap(cmap)
            norm = plt.Normalize(min(df[C]), max(df[C]))
            color = cmap(norm(row[C]))

            # Calculate the RGB color
            # color = cmap(norm(row[C]))[:3] * 255
            color = [int(x * 255) for x in cmap(norm(row[C]))[:3]]

            # Write the coordinates and color values to the PLY file
            f.write('%f %f %f %d %d %d\n' % (row[X], row[Y], row[Z], int(color[0]), int(color[1]), int(color[2])))
