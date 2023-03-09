# Environment Setup and Package Management

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean and Friedrich Knuth  

## How to install a Python package on the hub
As you research your projects, you will likely discover some useful packages are not available in the default environment on the Jupyterhub. You can easily install new packages from the shell or directly in a notebook. 

Start by reading the install instructions for the package - if conda/mamba is listed as an option, use that instead of pip (see more below).

> **_NOTE:_** This following is not a permanent installation, and the package will only be available during the current session. You will need to reinstall each time your Jupyterhub server restarts. Slightly inconvenient, but reproducible. We will talk more about permanent installs and creating environments later in the quarter.

### Install a package named `coolpackage` in the notebook with current kernel
Create a new cell near the top of the notebook before `import` statements, and add the following:

#### using conda:
```
import sys
!conda install --yes --prefix {sys.prefix} coolpackage
```
Note: the `--yes` will automatically answer "yes" to the interactive prompt about whether to proceed with the install.

#### using pip:
```
import sys
!{sys.executable} -m pip install coolpackage
```

Assuming this was successful, in a subsequent cell, you should be able to use the recommended syntax from the package documentation to start using the package (e.g., `import coolpackage` or `from coolpackage import coolfunction`). 

### Install a package named `coolpackage` from the command line
Use an open Terminal or launch a new Terminal and run the following command:
```
conda install mypackage
```
or
```
pip install mypackage
```

You can then launch a new notebook or restart the kernel in an open notebook, and start using.

### More information
* [https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/#How-to-use-Conda-from-the-Jupyter-Notebook)

## Conda, mamba, pip
### What is [`conda`](https://conda.io/en/latest/)?
>Conda is a cross-platform, language-agnostic binary package manager.
* See the first few sections of the User Guide:
  * https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
  * https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/

### What is [`mamba`](https://mamba.readthedocs.io/en/latest/)?
>a Python-based CLI conceived as a drop-in replacement for conda , offering higher speed and more reliable environment solutions.
>Mamba is a fast, robust, and cross-platform package manager

### What is [`pip`](https://pip.pypa.io/en/stable/)?
>pip is the package installer for Python. You can use it to install packages from the Python Package Index and other indexes.

### How to choose?
Approaches for Python package management are constantly improving, and there is outdated documentation on the web, which can be confusing.

In general, we recommend using `mamba` or `canda` rather than `pip` to install packages, unless they are only available on `pip`. 

A good resource: https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/#pip-vs.-conda

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

Downloand and install the Python 3 version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/distribution/) for your operating system and architecture. 
* Miniconda installs just the conda package manager, while Anaconda provides the same package manager along with a large set of common Python packages.
* While Anaconda may be easiest for beginners, we recommend miniconda for a more a lighter, faster, more customizable installation that requires less disk space.
  * Read more: https://conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda 
  * For Windows users, it seems 

1. Follow the official instructions for installation: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
  * Make sure you select the appropriate architecture for your local system (64-bit, Intel vs M1/AMD processor for mac)
  * Accept the license and select `yes` to initialize conda.
2. Open a new terminal session and run `conda` to verify a successfull installation. You should see `usage: conda [-h] [-V] command ...` followed by a bunch of options
3. Run the following to see useful info about your install: 
```
conda info
```
4. Update to latest version of conda: 
```
conda update conda
```
5. Add the `conda-forge` channel: 
```
conda config --add channels conda-forge
conda config --set channel_priority strict
```
6. Install mamba: 
```
conda install mamba
```

## Create the GDA environment

The environment used for the GDA course is in [uwgda-image-2023 repo](https://github.com/UW-GDA/uwgda-image-2023) in the UW-GDA Github organization:  
https://github.com/UW-GDA/uwgda-image-2023/blob/main/environment.yml

This configuration file contains all of the packages/versions we used on the Jupyterhub this quarter.

1. Download (or copy the content of) this text file to your computer. On Github, you can right-click on the "RAW" button in your browser, and "save link as" to save locally.
    * View it with a text editor and note that it is basically just a list of package names (many you will recognize from this course).
    * The first line `uwgda2023` defines the conda environment name.
    * Note that we may have "pinned" version numbers for some packages (e.g., `- python=3.9`).
        * This is not necessary, but is a best practice for our classroom situation. Because many of these projects are under active development, new versions are released during the quarter, potentially changing/breaking some functionality. 
        * For your personal setup, you can remove the version numbers, so conda will automatically fetch the latest version of each package, and you can access latest features (but no guarantee that the existing GDA notebooks will run out of the box).
2. Make sure you are in the `base` conda environment: 
```
conda activate base
```
3. Create the `uwgda2023` conda environment on your local machine. Open a terminal on your machine, and run the following, substituting the appropriate path to your `environment.yml` file: 
```
mamba env create -f environment.yml
```
   * This may take a few minutes to solve for environment, download and unzip all of the packages.
   * If this fails, please post the error message to the `#it_help` Slack channel 
4. Activate the `uwgda2023` environment: 
```
conda activate uwgda2023
```
   * You should see a slightly different terminal prompt display with `(uwgda2023)`
   * Now when you type `python` it should run the python executable in the new conda environment, and all of the GDA packages will be available!
      * Try it! run `python`, then `import geopandas` (shouldn't see any errors), then `exit()`
5. Verify Jupyterlab extensions
```
jupyter labextension list
```
   * Should see "enabled OK" for at least 6 extensions

Note that once this setup is complete, you will need to `conda activate uwgda2023` when you start a new terminal (including after you restart your computer), but you don't need to recreate the environment.  You can consider adding `conda activate uwgda2023` to your `~/.bashrc` or `~/.bash_profile` files to make this permanent.

## Starting Jupyter lab

Once you've successfully created and activated the `uwgda2023` environment, open a terminal and `cd` to the local directory where you store your notebooks/code (`~` or lab/project repos that you previously cloned to a local directory, or location where you plan create new notebooks).  This could be something like `~/Documents/gda_course_2023/`.

Then from the terminal, start Jupyter lab with the command
```
jupyter lab
```

This should automatically open a new window/tab in your local browser and bring up the jupyter lab interface. Now, you can open and run the GDA course notebooks, or create your own notebooks with the GDA environment!

Note that the corresponding url will be printed in your terminal.  Something like `http://localhost:8888/?token=8c2ec9dc22517fac7323334fec7224e7eff07275c2f648e8`.  If you accidentally close the tab, you can just copy this url from the terminal and paste in a browser (no need to restart jupyter).

To end your jupyter lab session, you can close the tab in your browser, but the Jupyter lab server is still running.  To stop the server:
* From the open Jupyter lab tab, "File -> Shut Down".
* From the command line you can `Ctrl-C` in the same terminal where you ran `jupyter lab`, then select 'y' to shut down the server.  

## Updating environments, removing or starting over

See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Most of the time, you should be able to `conda update`, or manage environments to add/remove packages.

One of the best things about conda is the fact that it creates isolated environments, separate from your system Python. So if you no longer need it, or you have unresolvable issues, you can always just remove and recreate the environment. You can also start over with a fresh install of conda: https://docs.anaconda.com/anaconda/install/uninstall/

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

```
conda config --add channels conda-forge 
conda config --set channel_priority strict
```

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

`conda create -n my_favorite_env geopandas==0.7.0 matplotlib`

<b>Create an environment with a specific version of Python</b>

`conda create -n my_favorite_env python=3.9 geopandas matplotlib`

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
