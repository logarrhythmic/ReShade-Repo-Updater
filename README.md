# ReShade-Repo-Updater
Python script to git clone a list of repositories, keep them updated, and copy ReShade shaders and textures into a directory structure similar to that created by the ReShade installer.
## Requirements
1. Python 3
2. git installed in PATH
## Usage
Add links to the repos you want to clone/keep updated in `repolist.txt`. Run update.py. 

To use the shaders in ReShade, add the Shaders folder to `Effect search paths` as `<Reshade-Repo-Updater path>\Shaders\**` and the Textures folder to `Texture search paths` as `<Reshade-Repo-Updater path>\Textures\**`.
### Default repolist.txt contents
The included repolist.txt contains links to all repos listed in https://www.pcgamingwiki.com/wiki/ReShade#List_of_known_shader_repositories that are not included in the default selection in the ReShade 5.9.2 installer, and additionally https://github.com/GarrettGunnell/AcerolaFX/.
