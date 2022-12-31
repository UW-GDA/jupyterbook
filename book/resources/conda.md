# Conda and Jupyter Setup Instructions

UW Geospatial Data Analysis  
CEE467/CEWA567  
Friedrich Knuth and David Shean  

## [What is conda?](https://conda.io/en/latest/)
* See the first few sections of the User Guide:
  * https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
  * https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/

### What is mamba?
* https://mamba.readthedocs.io/en/latest/
>a Python-based CLI conceived as a drop-in replacement for conda, offering higher speed and more reliable environment solutions

## Basic terminology
#### package manager 
_helps you download and organize open-source software on your machine (conda is cross-platform, which is one of the reasons it is so great. There are also OS-specific package managers, like homebrew (MacOS), apt-get (Linux), chocolatey (Windows) etc...). The package manager installs/manages packages (Python, command-line utilities, etc.), resolves their dependencies, and creates a functional custom Python environment._

#### package
_includes Python module(s), binary executable machine instructions (e.g., libraries compiled from NumPy C/C++ source code), metadata, etc._  
https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html#what-is-a-conda-package

#### dependency
_another package required by a given package to function (e.g., `geopandas` depends on `fiona`, `shapely` and many other packages)_

#### environment
_collections of packages with self-consistent dependencies and versions, managed by conda so "everything just works together"_  
https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html

#### channel
_source for packages_  
https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html

## Why?

But I already have Python installed on my computer, why do I need this?

# How to reproduce the GDA JuptyerHub environment

## Install Conda
*Note: If you have an existing conda install, you can skip this section and go straight to 'Create the GDA environment' section.  You may want to `conda update conda` if it's been a while since you installed.*

Downloand and install the Python 3 version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/distribution/). 
* Miniconda gives you just the conda package manager, while Anaconda provides the same package manager along with a large set of common Python packages.
* While Anaconda may be easiest for beginners, we recommend miniconda for a more a lighter, faster, more customizable installation that requires less disk space.

Follow the instructions for installation: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

Select yes to initialize conda.  Close your terminal/shell, then open a new terminal session and type `conda` to verify a successfull installation. 

Run the following to see various useful info about your install:
`conda info`

Update to latest version of conda:
`conda update conda`

Install mamba:
`conda install mamba`

## Create the GDA environment

The environment used for the GDA course is in [uwgda-image-2022 repo](https://github.com/UW-GDA/uwgda-image-2022) in the UW-GDA Github organization:  
https://github.com/UW-GDA/uwgda-image-2022/blob/main/environment.yml

This configuration file contains all of the packages/versions we used on the Jupyterhub this quarter.

1. Download (or copy the content of) this text file to your computer. On Github, you can right-click on the "RAW" button in your browser, and "save link as" to save locally.
    * View it with a text editor and note that it is basically just a list of package names (many you will recognize from this course).
    * The first line `uwgda2022` defines the conda environment name.
    * Note that we may have "pinned" version numbers for some packages (e.g., `- python=3.9`).
      * This is not necessary, but is a best practice for our classroom situation. Because many of these projects are under active development, new versions are released during the quarter, potentially changing/breaking some functionality. 
      * For your personal setup, you can remove the version numbers, so conda will automatically fetch the latest version of each package, and you can access latest features (but no guarantee that the existing GDA notebooks will run out of the box).
1. Create the `uwgda2022` conda environment on your local machine
    * Open a terminal on your machine, and run the following: `conda env create -f environment.yml`
    * This will take a few minutes to download and unzip all of the packages.
    * If this fails, please post the error message to the #it_help Slack channel
    * You can try installing with mamba: `mamba env create -f environment.yml`
1. Activate the `uwgda2022` environment, 
    * `conda activate uwgda2022`
    * You should see a slightly different terminal prompt display with `(uwgda2022)`
    * Now when you type `python` it should run the python executable in the new conda environment, and all of the GDA packages will be available!  Try it, run `python`, then `import geopandas` (shouldn't see any errors), then `exit()`
1. Configure the Jupyterlab extensions
    * Latest version of these extentions don't require additional configuration after install.
    * Can verify everything with `jupyter labextension list` (should see "enabled OK" for at least 6 extensions)

Note that once this setup is complete, you will need to `conda activate uwgda2022` when you start a new terminal (including after you restart your computer), but you don't need to recreate the environment.  You can consider adding `conda activate uwgda2022` to your `~/.bashrc` or '~/.bash_profile` files.

## Starting Jupyter lab

Once you have created the environment, activated the environment, and installed Jupyter lab extensions, open a terminal and navigate to the local directory where you store your notebooks/code (either lab/project repos from class that you `git clone` to local directory, or location where you will create new notebooks locally).  This could be something like `~/Documents/gda_course_2022/`.

Then from the terminal, start Jupyter lab with the command: `jupyter lab`

This should automatically open a new window/tab in your local browser and bring up the jupyter lab interface. Now, you can open and run the GDA course notebooks, or create your own notebooks with the GDA environment!

Note that the corresponding url will be printed in your terminal.  Something like `http://localhost:8888/?token=8c2ec9dc22517fac7323334fec7224e7eff07275c2f648e8`.  If you accidentally close the tab, you can just paste this url in the browser (no need to restart jupyter).

To end your jupyter lab session, you can close the tab, but the Jupyter lab server is still running.  To stop the server, on the command line you can `Ctrl-C` in the same window/terminal where you ran `jupyter lab`, then select 'y' to shut down the server.  From the open Jupyter lab tab, you can also "File -> Shut Down".

## Removing or starting over

See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Most of the time, you should be able to `conda update`, or manage environments to add/remove packages.

One of the best things about conda is the fact that it creates isolated environments, separate from your system Python. So if you no longer need it, or you have unresolvable issues, you can always just delete and start over with a fresh install.

https://docs.anaconda.com/anaconda/install/uninstall/

# Creating a custom setup from scratch

## Conda channels

Sometimes, certain packages or newer versions aren't available through the default conda package distribution source. Fortunately, you can point conda to other "channels" which have different packages available, and maybe more up to date versions. 

https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html

The `conda-forge` channel is user-supported, and has largely superseded the main anaconda package channel

For example, this package called [RISE](https://github.com/damianavila/RISE), which is a jupyter notebook extention that let's you turn your notebook into a presentation, is only available through the conda-forge channel. Note that the author specifies installation as:

`conda install -c conda-forge rise`

This means _conda, please install the package called "rise" from the conda-forge channel_. 

Generally, it is safe to grab the latest packages from conda-forge, which is usually somewhat ahead of the default channel. If you find yourself on shaky ground, you can always specify a previous, more stable version of the package you are looking to install. This is one reason why we use a package manager.

Let's add the conda-forge channel, by typing the following into your terminal:

`conda config --add channels conda-forge`
`conda config --set channel_priority strict`

This adds the conda-forge channel to your conda configuration file located in your home directory (`~/.condarc`). You only need to do this once. Now, when creating a new environment conda will first look for a package on conda-forge, then on the default anaconda distribution channel.

When shopping around for packages, a useful resource to check is the anaconda [repository](https://anaconda.org/anaconda/repo). Search "geopandas", for example and you will see that it is most popular through the conda-forge channel. The package repository is a great way to guage how popular and well supported a specific package is within the community.

## Creating a custom Conda environment

Let's create a new custom envornment called `my_favorite_env` with geopandas and matplotlib.

`conda create -n my_favorite_env geopandas matplotlib`

Notice that conda lists a number of other packages to be installed. These are the dependencies for geopandas and matplotlib. Some of them include seaborn, pandas, numpy etc. which means you don't always have to specify those if you know they will be installed as dependencies for the main packages you want in your environment (in this case, geopandas and matplotlib). If you aren't sure, you can always add them to the installation call, just to be safe.

## Useful commands

<b>List all your environments</b>

`conda env list`

<b>Delete an environment</b>

`conda env remove -n my_favorite_env`

<b>Activate an environment</b>

`conda activate my_favorite_env`

<b>Deactivate a loaded environment</b>

`conda deactivate`

<b>List all installed packages for an environment</b>

`conda list -n my_favorite_env`

<b>Add a package to an environment</b>
In this case we are adding 'xarray'.

`conda install -n my_favorite_env xarray`

<b>Add a package with specific version to an environment</b>
In this case we are adding 'geopandas' with version 0.3.0.

`conda install -n my_favorite_env geopandas==0.3.0`

<b>Remove a package from an environment</b>
In this case we are removing 'geopandas'.

`conda remove -n my_favorite_env geopandas`

<b>Upgrade a installed package from an environment</b>
In this case we are updating 'geopandas' to the latest version.

`conda upgrade -n my_favorite_env geopandas`

<b>Create an environment with specific version of a package</b>

`conda create -n my_favorite_env geopandas==0.3.0 matplotlib`

<b>Create an environment with a specific version of Python</b>

`conda create -n my_favorite_env python=2.7 geopandas matplotlib`

## Jupyter integration

To create a Python environment that can handle jupyter notebooks, add `jupyterlab` to the environment install. 

For example:  
`conda create -n my_favorite_env geopandas matplotlib jupyterlab`

Activate your envornment:  
`conda activate my_favorite_env`

You can then start the jupyter lab environment in your local browser:  
`jupyter lab` 

## Running a Jupyter notebook on a remote machine

Some additional notes (thanks to @ShashankBice!) on how to launch a Jupyter notebook server on a remote machine:

1. Open a terminal
1. Log in to the remote machine: `ssh username@serverIP`
1. `cd` into directory where your notebooks/data are stored
1. `conda activate` your environment
1. Start the jupyter lab/notebook `jupyter lab --port=8888 --no-browser`
1. Open a new terminal on your local machine
1. Open an ssh tunnel to the remote machine: `ssh -f -L 8888:localhost:8888 -N your_user@serverIP`
1. Open your local browser and paste the address `http://localhost:8888`, which should bring up the remote jupyter lab interface
1. :tada:
