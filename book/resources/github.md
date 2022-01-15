# Github and Github Classroom Notes
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

These are a set of loosely organized notes, tips, tricks and gotchas for git and Github resources used during the course.  Additional notes on initial setup and weekly workflow for students and instructors can be found in the Resources.

There are many good resources on git and Github on the web.  See the [01_Shell_Github](../modeules/01_Shell_Github) reading assignment and demo.  

Additional UW eScience Hackweek resources on initial Github setup and navigation: 
* https://snowex-hackweek.github.io/website/preliminary/github.html
* https://snowex-hackweek.github.io/website/preliminary/git.html

## First time login
*Replace the following with your name and the email you used to create your Github account*  
`git config --global user.name "Matt Damon"`  
`git config --global user.email "email@example.com"`

## Authentication
As of August 2021, Github disabled using passwords for remote command line access. We will use the more secure Personal Access Token (PAT) authentication option. 

### Create Personal Access Token (PAT)
* Follow the basic instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token 
    * Step 6: Name the token "GDA Jupyterhub"
    * Step 7: Set expiration to "Never"
    * Step 8: Check permission boxes for `repo`, `workflow` and `delete_repo`
    * Copy the code and store in a safe location (e.g., password manager, keychain)
* When using git on the course Jupyterhub, enter your code when prompted to enter a Github password (e.g., when pushing to a remote repo)
    * *NOTE: when you paste the code, it will be hidden and remain blank! Hit enter to accept after pasting* 

### Store credentials
*So you don't have to enter github username and PAT each time you pull or push to a remote repo*  

#### Permanently
1. Run this once:  
`git config --global credential.helper store`
1. You may receive a warning about loose permissions the first time you `git pull`.  To prevent this:  
`chmod 0700 /home/jovyan/.cache/git/credential`
1. Enter credentials one additional time:  
`git pull` (Should prompt for username)
1. [Enter username and PAT]
1. The next time you run a git command requiring remote origin, no username/password required!  
`git pull` (Should say "Already up to date.")

#### Store credentials for 15 minutes (900 seconds) without reauthenticating
`git config --global credential.helper 'cache --timeout=900'`

### Two-factor authentication (2FA)
In past years, enabling 2FA led to issues with authentication using the terminal on the course Jupyterhub. This may be resolved with updated PAT authentication requirements.
* Should be disabled by default (for new accounts)
* If you're using an existing Github account and previously enabled two-factor authentication, you may need to disable 

## Git workflows
### Clone remote repository
1. Open repository webpage
1. Click big green "Code" button
1. Select HTTPS and copy link
1. On course Jupyterhub, open a terminal
1. Navigate to the directory containing assignments (`cd labs`)
```
git clone [paste https link]
cd [repo name]
```
### Basic with remote 
```
git pull
git add myfile.py
git commit -m 'Added myfile.py'
git push
```
### Basic branching (local)
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
```
git checkout -b newbranch
git add updated_file.py
git commit -m 'Fixed typo in updated_file.py'
git checkout main
git merge newbranch
git checkout -d newbranch
```

## FAQ, Notes

### Improved git log formatting
`git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit`  
*Note: Can add as alias to ~/.gitconfig file*

### Should I git clone via https or ssh?
* Default is https, requires authentication with Github username and password
* Can also set up ssh keys on Jupyterhub, if that doesn't sound intimidating

### Why are a bunch of random files added to my repo?
* You probably ran `git add .` or `git add -A` rather than adding individual files `git add newscript.py notebook.ipynb`
* https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add
* You may not have a `.gitignore` for the repo
    * https://git-scm.com/docs/gitignore
    * Python template: https://github.com/github/gitignore/blob/main/Python.gitignore

### Should I store data in the git repo?
* A few small files or test data are great, even better if they are text data or some other non-binary format
* Large data files do not belong in the repo, store them externally and fetch dynamically
    * Zenodo, UW Library, Amazon S3 or Google Cloud Storage bucket, some other public data archive
* Do you need to track changes to the data files?
* https://docs.github.com/en/repositories/working-with-files/managing-large-files

### Issues with large notebooks (>5-10 MB) rendering on Github
*May no longer be relevant*
Github can fail to render notebooks. Sometimes reloading works.

If notebook is in a public Github repo, go to https://nbviewer.jupyter.org/ and paste the url to the notebook.

## Github Organization Notes

### To make your repo visible to students/instructors in the organization
Settings -> Manage Access - > Invite Teams (Green Button) -> gda_w2020_students, and grant read access to desired teams

### To make your project repo public for the world
Settings -> Options (left menu) -> Danger Zone -> Make public

To check public visibility, you can always sign out of Github and navigate the GDA org https://github.com/UW-GDA/ to see the public repos.

## Github Classroom Notes
See the instructor resources on the weekly Github Classroom workflow for assignment distribution.

### Issues accepting assignments
In both 2019 and 2020, during one week, the students went to accept their assignment, and the progress bar froze. Worked for a few students, then majority of class can't get the assignment. Panic ensues.
Can make starter code visible to the student team, then show them how to Fork
In dire circumstances, just post the notebook on Slack channel
A good teaching moment.
The issue resolves itself within ~24 hours, students can use their fork or clone the assignment repo, then copy working notebook
