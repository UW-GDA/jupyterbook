# Week 1: Intro, Shell and Github

UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

Please quickly read through this entire document once, then go back and start tackling the various tasks.

## Overview
We are going to “flip the classroom” for the first two weeks. Before class, you will be responsible for reviewing material from external resources. Consider this your week 1 homework. During our Friday meetings, I will briefly review some of this material and do an interactive demo, we will discuss questions and clarify concepts as a class, and then collaboratively work on some problems/exercises to help solidify the concepts (which will inevitably lead to more questions and discussion). I think this is the best use of our limited time together.

## Logistics before first lecture
* Review the syllabus (restricted to UW accounts): https://docs.google.com/document/d/1uaEMqANMU9NlvH2ELkGtALQ3MlGY1U9-uCqNKz5JOqk/edit?usp=sharing
   * I’ve enabled comments on the Google Doc, so if you find any mistakes or have questions, please add comments inline, and/or come to class ready to ask questions.
* Fill out the background questionnaire (restricted to UW accounts): https://forms.gle/g6od17HJ1L8wB2sq5
   * Don't overthink this, it shouldn't take more than 5-10 minutes to fill out!
* Complete all of the items outlined in the [Student Initial Setup](../../resources/students/student_initial_setup.md) document.
   * Reminder: send me a Slack message with your github username!
* Review the course [Code of Conduct](../../code_of_conduct.md) document. 
* Attempt to log on to the course Jupyterhub: https://rttl.axdd.s.uw.edu/2021-winter-cee-498-d
    * This is the computing environment we will use for the quarter
    * We will review this interface as a group during lab, but feel free to start exploring
    * If you have trouble logging in, send a message to the #it_help channel on Slack
    * To bring up a terminal to use for the shell and git exercises:
        1. Click the "+" icon in the upper left corner to bring up the Launcher
        2. Under "Other" click on the Terminal icon.
        3. This will launch a new tab with default bash shell

## Reading and Tutorials before first lab
I recommend that you break these lessons up into a few sessions, so you have some time to digest what you’re learning (don’t attempt to get through everything an hour before lab starts). Even if you are already an expert on these topics, please take some time to work through the lessons. I guarantee that you will learn something new or will gain a better understanding of something that you’ve seen before (I certainly did). 

Please attempt to work your way through the following lessons (make sure you attempt some of the relevant examples!):

### 1. Background
* Chapter 1 of Introduction to Earth Data Science Textbook: https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/ (~30 min)
    * This is a fantastic set of resources prepared by the Earth Lab at CU Boulder. Feel free to explore this textbook and other resources on the site. We will cover many of these concepts throughout the quarter.
    * While the sections on Jupyter contain some great background, several of the sections on local setup and the jupyter notebook interface are irrelevant, as we're using a shared Jupyterhub environment with everything ready to go (you're welcome!) and the more powerful/flexible Jupyter lab interface.

### 2. Unix shell
* Software Carpentry: http://swcarpentry.github.io/shell-novice/ (~2-4 hours). 
    * You don’t need to master all of this material, but you need to know the basics (navigating the filesystem, previewing/editing text files, basic for loops and conditionals). Please try to read through most of the lessons and do some interactive exploration on your own.
    * If you already feel very comfortable with the shell, and the beginner material is too basic, spend some time working through the intermediate lesson: https://carpentries-incubator.github.io/shell-extras/.  
* Chapter 2 of Introduction to Earth Data Science Textbook: https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/

### 3. Git and Github
* You will need to be comfortable with basic git functionality (`clone`, `add`, `commit`, `push`), and will need more advanced functionality later in the quarter. 
* If you’ve never worked with git and github, it’s going to be confusing at first. Please do your best to understand the basics. Review and work through these introductory guides (or search the web for other introductory material):
    * https://guides.github.com/introduction/git-handbook/
    * https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6
* If those were easy/fast, review the table of contents for the Software Carpentry lessons, and decide for yourself which components will be most valuable based on your experience:
    * http://swcarpentry.github.io/git-novice/ (~2-3 hours)
    * https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/

If all of this is new, don’t sweat it, but you will need to put in the extra time during the first few weeks of class to practice and get up to speed. This means actually typing the commands from the tutorial on your computer and reviewing the output (don’t just skim or selectively copy/paste). 

If you’re stuck or confused, please send a message to the #lab01_shell_git Slack channel, and David, the TA, and/or or others in the class can help you work through issues.

## Assignment: Due Friday
* Send me a direct Slack message with your github username (do this as soon as possible)
* Complete the above reading assignment
* Fill out this form about the reading assignment: https://forms.gle/rnHSJHozvuoveP8o7

## Outlook
During week 2, we will review Python, iPython/Juptyer, and continue exploring the shell and git/github. There will be opportunities to continue learning all of this material throughout the course, but I want to reiterate that this is not an intro Python or intro programming class. By week 3, I’m hoping that everyone will be comfortable with the basics, and we can jump into some actual geospatial applications. With that said, I’ve intentionally kept the schedule flexible, so we can adjust as we go along - I need to calibrate after I get a better sense of everyone’s experience level.
