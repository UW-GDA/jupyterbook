# Jupyter Notes
UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for Jupyter resources (Jupyterhub, Jupyter lab and Jupyter notebooks) used during the course.  Additional notes on initial setup and weekly workflow can be found in the [GDA instructor resources](instructors/README.md).

Additional UW eScience Hackweek resources on initial Jupyterhub setup and navigation:
https://snowex-hackweek.github.io/website/preliminary/jupyterhub.html

## Jupyterhub

### Logging out
Please try to remember to shut down your server and log out of the Jupyterhub when you're done for the day. This will help save money (we'd like to avoid paying for cloud computing resources while you're sleeping), and provides a clean start the next time you log in, which can help avoid various issues listed below.

### Troubleshooting
If you are experiencing strange behavior with the course Jupyterhub, please try the following:

#### 1. Reload the tab in your browser
* Can resolve issues with notebook cells that appear strange or "cut off"
* If you have unsaved changes, save the notebook, then reload

#### 2. Log out and reauthenticate
* File -> Log out
* Click "Sign in" button and reauthenticate with UW netid Canvas credentials

#### 3. Restart Jupyterhub Server
* All students have the ability to stop and restart their own server on the Jupyterhub (don’t need to ask instructor or IT).
* **File --> Hub Control Panel --> Stop My Server (wait a ~30 seconds, then start again)**
* After image is updated (e.g., new packages added to default conda environment), all users will need to restart their server to see changes.

#### 4. Review the list of common errors and solutions below

#### 5. Post a message to `#it_help` channel on the class Slack workspace
* Important to post to public channel, as other students can chime in to help, and if this is a larger issue, confirm similar experiences
* Provide detailed report - copy/paste error messages, include screenshots, etc. so we can help diagnose
* Course instructor and IT help will provide assistance

### Common Jupyterhub Errors
#### `Kernel Restarting`
 * Likely ran out of memory. 
 * Can "Restart Kernel and Run up to selected cell" to restore state
 * Remember, closing a notebook tab in JupyterLab interface doesn't actually shut down the kernel! If you have opened/run many notebooks during a session, you may start to experience performance issues. 
 * To remedy, click the "Running Terminals and Kernels" button (square inside a circle) on the left panel. It will show you all of the kernels  that are running. Shut down any that you no longer need.

#### `Dask Server Error`
 * If you see this, it is likely that your server was shut down due to inactivity. Reload the page in your browser, and log back onto the Hub.

#### `File Save Error for *.ipynb` or `Failed to write *.ipynb`
 * Temporary network interruption, dismiss and try manually saving
 * Check to make sure you haven't filled the your allocated home directory storage (see below) 

#### `Spawn failed: Server at .... didn't respond in 30 seconds`
 * This occurs when attempting to log into the hub, and the server fails to start (don't panic)
 * Likely an issue with a full disk.
 * Reach out on `#it_help` Slack channel with a screenshot, and we will follow up with UW-IT (should be resolved quickly)
 * See section on managing storage below to avoid this problem.

### Managing data storage and disk space
 * The default storage allocation for each student is 5 or 10 GB, which should be sufficient for the assignments. For project work, we can increase the storage allocation.
 * Please make sure you are not storing multiple copies of large data directories.
 * Always use relative paths to load data from existing data directories elsewhere on the filesystem (like the `LS8_sample` directory), rather than copying them to your assignment repo. 
    * In the real world, you (or your employer) have to pay for every GB per month, so good to learn best practices now.
 * You can also safely delete large data directories from previous demo/labs, as you can rerun the data download notebooks to download in the future.

#### Checking current storage and available disk space
 * Open a Terminal on the hub and run:
    * `du -s -h ~/*` - shows you total data volume in each directory, can `cd` and rerun to identifiy large subdirectories/files
    * `df -h ~` - shows total available storage and amount/percent used

#### Freeing up storage
* If your `df` percentage is >80%, please do the following:
    * Delete large data files/directories that are no longer necessary or can be easily downloaded again in the future.
    * Reach out on the `#it_help` Slack channel or send a direct message, and we can request more storage. Please don't hesitate to do this if you will need more temporary storage for projects. 

### Initial Instructor Setup

#### Work with UW-IT template 
See sample for 2020 here: https://github.com/UW-GDA/uwgda-image
Most of the user-level customization is found in the `binder` subdirectory.
We used a `dev` branch to submit Pull Requests with modifications (e.g., adding a new package) and then merged into `master` after tests completed. 

#### Add any core utilities to `apt.txt`
This includes common command line tools like `wget` or text editors like `vim`. Sample:    
https://github.com/UW-GDA/uwgda-image/blob/master/binder/apt.txt

#### Create a shared conda environment 
Include all packages that will be needed for the course, with version numbers if desired.
Sample: https://github.com/UW-GDA/uwgda-image/blob/master/binder/environment.yml
Can update this list throughout the course, and continuous integration will automatically rebuild and deploy the updated image.  

#### Add any custom Jupyter lab extensions
Add useful interactive visualization tools (pyviz, leaflet), Dask integration, etc.  
Sample: https://github.com/UW-GDA/uwgda-image/blob/master/binder/postBuild
See available extensions: https://github.com/topics/jupyterlab-extension 

## Jupyter notebooks

### Use keyboard shortcuts
https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/jupyter-notebook-shortcuts/

### Best practices for memory management
* Avoid duplicating large arrays ( as in “dynamically process original and plot in one command” instead of “process original, store as new array, then plot new array”)
* Avoid unnecessarily increasing bit depth (e.g., loading a `UInt16` array as `float64` quadruples memory footprint)
* Release memory from arrays that are no longer needed with `myarray = None` (see https://stackoverflow.com/a/35316944)
* Use Dask!

### Disable Jupyter Notebook Warnings
```
import warnings
warnings.filterwarnings('ignore')
```

