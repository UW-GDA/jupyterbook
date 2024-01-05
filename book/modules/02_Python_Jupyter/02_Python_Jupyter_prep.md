# 02: Python and iPython/Jupyter

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

Please quickly read through this entire document once, then go back and start tackling the various tasks.

Thanks to those of you who submitted responses to the week 1 form. These responses are essential for me to properly adjust the level and content moving forward.

## Overview
This week is another “flip the classroom” situation. Before class, you will be responsible for reviewing material from external resources. Consider this your homework (in addition to completing the lab exercises from last week). During lecture/lab, I will briefly review some of this material, do some interactive demos, we will discuss questions and clarify concepts as a class, and then collaboratively work on some problems/exercises to help solidify the concepts (which will inevitably lead to more questions and discussion). I think this is the best use of our limited time together.

## Reading and Tutorials
This week we are reviewing Python, and iPython/Jupyter notebooks, which are essential for the rest of the course (and future data science endeavors). This review will ensure that we have a common baseline and set of references moving forward. **If you are relatively new to Python, it is critical that you spend extra time with self-study this week.**

Again, this is intended to be an individual review. Tailor to your needs, and adjust emphasis so you are best using your time outside of class. Even if you’ve been using these tools for many years, it can still be valuable to review the basics, as you will inevitably learn (or re-learn) some new tricks and develop a better grasp of more complex concepts.

As with the week 1 assignment, don’t wait until Friday morning to start.  This material will be much more useful if broken up over several sessions throughout the week - try an hour a day.

### 1. A Whirlwind Tour of Python (~2-4 hours)
* Work your way through Jake VanderPlas’ excellent “Whirlwind Tour of Python”: https://jakevdp.github.io/WhirlwindTourOfPython/
* In a terminal on the Jupyterhub:
    * Create a new directory with `mkdir` to store external resources and `cd` into that directory
    * `git clone https://github.com/jakevdp/WhirlwindTourOfPython`
* Work through the notebooks, taking some time to experiment along the way (don’t just shift-Enter without reading text or absorbing concepts)
    * Can skip sections on Python installation and conda - we’ve taken care of this with the class Jupyterhub setup, and we will revisit conda later in the quarter
    * Note that we are exclusively using Python3 in this class (but good to know about potential issues with Python2 compatibility)
    * If you’re short on time (or feeling overwhelmed), you can skip sections 09 (Errors and Exceptions), 12 (Generators and Generator Expressions) and 14 (Strings and Regular Expressions)
      * Note: chapter numbers in the book vs. the interactive notebooks are slightly different
* Note that you can also view rendered versions of the notebooks on the original github page, but please take advantage of the interactive notebooks - try changing some things and rerunning

### 2. iPython and Jupyter Notebooks (~1-2 hours)
* Start working through Jake Vanderplas’ slightly more dense, but also excellent “Python Data Science Handbook”: https://jakevdp.github.io/PythonDataScienceHandbook/
    * `git clone https://github.com/jakevdp/PythonDataScienceHandbook`
* Read the **Preface**
* Interactively work through **Chapter 1. iPython: Beyond Normal Python**
    * Don’t worry about instructions for installing or launching, as we've already done this for you in the Jupyterhub environment
    * As discussed during week 1, you can use the Jupterlab Launcher (“+” icon in upper left corner) to create a new Jupyter notebook.
    * You can also double-click on the ipynb files in the file browser (left hand window).
* *Note:* We will review Chapters 2-4 (Numpy, Pandas, and Matplotlib) next week, but if you have extra time this week, feel free to continue ahead
* Peruse the documentation on Jupyterlab, which is more sophisticated than the standard Jupyter notebook interface
https://jupyterlab.readthedocs.io/en/latest/user/interface.html

### 3. (Optional) Sections 4 and 7 of the *Intro to Earth Data Science* textbook
* https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/
* https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/

### Extra Credit
If all of this is too basic (or you’re curious), try one or more of the following:
* Learn new iPython/Jupyter keystrokes and magic functions
* Read the official Python documentation: https://docs.python.org/3/index.html.
* Review documentation and source code for the Python standard library:
    * This is the definition of pure Python, and a great reference of how to write clean, efficient, well-documented Python code.
    * https://docs.python.org/3/library/
    * https://github.com/python/cpython/tree/master/Lib
    * For example, when you `import os`, here's what you're running: https://github.com/python/cpython/blob/master/Lib/os.py
* Review the Python style guide: https://www.python.org/dev/peps/pep-0008/

## Assignment: due next Friday before lab
* Complete the above reading
* Fill out this form: https://forms.gle/CFK8twgfDH5SY26m7
* Finish and turn in the lab exercises from last week

## Additional resources
Learn Python in Y minutes: https://learnxinyminutes.com/docs/python/

Google's Python Class: https://developers.google.com/edu/python/

Additional resources if you’re still learning Python:
http://swcarpentry.github.io/python-novice-inflammation/

More information about iPython:
https://ipython.readthedocs.io/en/stable/interactive/tutorial.html

More information about the JupyterLab interface we are using for the class:
https://jupyterlab.readthedocs.io/en/latest/
