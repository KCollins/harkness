# harkness
A python library for generating VR-friendly visualization files from pandas dataframes. 

## How to Use:
- **Identify an appropriate dataframe.**

- **Generate .ply file.** Run `create_ply()` on your dataframe, identifying the columns X, Y, Z, and C (for color).

- **Visualize on desktop.** You can use a program like [Autodesk MeshMixer](https://meshmixer.com/) or [Cloud Compare](https://www.danielgm.net/cc/).

- **Visualize in VR.** You can open the resulting file in a VR viewer like [VRifier](https://store.steampowered.com/app/640080/Vrifier/).



### Notes and Acknowledgments
Named for Ruth Harkness, who with Quentin Young and Gerald Russell brought the first live giant panda cub to the United States. (For more on this, read her memoir, _The Lady and the Panda._) Name chosen because (1) "harkness" did not appear for related topics on a search of pypi, and (2) it's a library for displaying pandas. Some assistance by Google Bard.
