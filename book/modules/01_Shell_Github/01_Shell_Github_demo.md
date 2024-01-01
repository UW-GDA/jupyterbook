# Demo
UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

## Preparation and discussion
- Make sure all students are on Jupyterhub (add UW netid from Hub Control Panel if necessary)
- Distribute link to course Jupyterhub, have students start server
- Basic interface overview - start a shell, start a notebook (next week)
- Ask about OS? Anybody using Linux? All of you!
- Discuss virtual machine and cloud computing
   - underlying infrastructure, computer somewhere in Google data center in CA or OR
   - `uname -a`, `lscpu`, `free`, `top`, `df -h .`
- Close tab in Jupyterlab - demonstrate persistence
- Storage will persist throughout quarter, server will shut down after ~1 hour of inactivity

## Shell overview
- Discussion of prompt (jovyan)
- Disucssion of file system navigation (all the way to /)
- Commands and arguments
- Tab completion
- `ls -l` - modificaiton timestamps

## Set up git on Jupyterhub
- https://uwgda-jupyterbook.readthedocs.io/en/latest/resources/github.html#first-time-login
- Set up token

## Basic git/Github workflow
1. Distribute Week 01 Github classroom assignment link through Slack channel 
1. Clone assignment locally:  
   ```
   git clone https://github.com/UW-GDA/01-shell-github-dshean.git
   cd gda_test  
   ls -l
   ```
1. git vs. github, local vs remote 
1. Discuss repo contents - markdown files, csv
1. Pick a text editor
    * Demonstration of Jupyterlab text editor
    * Discuss text editors, pick one for command line
    * https://web.stanford.edu/class/cs107/resources/editors
1. Edit `README.md` and add your name
1. Commit the change
```
git status
git add README.md
git status
git commit -m "Added my name to README.md"
git status
```

### Discussion of local vs origin
* Open web browser to view origin repo on Github
* `git push`
* Refresh page, verify README.md was updated

### Edit README.md on Github, commit directly
* Add today's date below your name

### Pull changes to local repo
* `git pull`
* `git log`

## Add a new file to the repo

### Create a new text file
* `nano git_reflections.txt`
* Add some text "Git is ..."
* Follow above add, commit, push
   * For now, always specify each file to commit
   * For now, modify single file, add and commit
   * Try without `-m` and demonstrate nano (how to get out)

### Create a new text file
* Discuss extensions (.sh vs. .txt or .py)
* `vim myawesomescript.py`
* Add some lines:
    ```
    #! /usr/bin/env python
    print("Pancakes rule!")
    ```

### Commit the change
```
git status
git add myawesomescript.py
git status
git commit -m "Added myawesomescript.py"
```

### Try to execute script, doesn't work
`./myawesomescript.py`

### Check permissions
`ls -l ./myawesomescript.py`

### Change permissions
```
chmod +x myawesomescript.py
ls -l myawesomescript.py
./myawesomescript.py
```

### Commit permission change
```
git status
git diff myawesomescript.py
git add myawesomescript.py
git status
git commit -m "Change permissions on myawesomescript.py"
```

### Review log, main is ahead of origin
```
git log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

### Push to origin
```
git push
git status
```

### Review log, both origin and main are same
```
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

# Other topics to discuss
* You will make mistakes, it's OK, can always start over with git
* Post to #01_shell_github channel for help
* Best practices with git
    * https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add
    * https://uwgda-jupyterbook.readthedocs.io/en/latest/resources/github.html#why-are-a-bunch-of-random-files-added-to-my-repo
* Tab completion
* Command `history` (use up arrow)
* du and df
* top and ps
* ssh and scp
* tmux and screen
* Discuss filesystem
    * Output from `which ls`
    * Go to /
    * Explore /bin
* Discuss executables
* `$PATH`
* bits, bytes
* for loop
    ```
    for i in solutions.txt words README.md
    do
        ls $i
    done
    #One line:
    for i in solutions.txt words README.md; do ls $i; done
    ```

# Introduce assignment
* create `labs` folder!
* Walk through first few questions of assignment together
