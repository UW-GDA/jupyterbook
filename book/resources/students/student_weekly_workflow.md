# Student weekly workflow

## Accepting Assignments
1. Join the new Slack channel for the lab
1. Click on the link to the Github Classroom assignment
1. Accept the assignment invitation
1. Wait for progress bars to complete (should take a few seconds, refresh)
    * It is possible this may hang for a few minutes.  If it is taking longer, post on Slack so we can figure out if it is isolated or others are also experiencing issues.
1. Click on the resulting link to go to your assignment repository (now has your github username appeneded)
1. Click the big green Code button and copy the default https URL (something like `https://github.com/UW-GDA/03_numpy_pandas_matplotlib-dshean.git`)
1. On the course Jupyterhub, open a new terminal
1. If you haven't already, I recommend you create a directory called labs (`mkdir labs`) and `cd labs`
1. Clone your assignment repo: `git clone [paste url]`

## Do the Assignment
1. Read the instructions and introduction/background
   * I recommend you skim through entire notebook to gauge effort required, and plan accordingly (don’t wait until an hour before the deadline on Friday to start)
1. Write code to answer questions
1. Discuss questions and issues with others during lab and on Slack
1. Rember to `git add` and `git commit` your modified files as you make progress to record "checkpoints" in your work

### Important Notes on Assignments
#### Completing the lab exercises is not a race!
   * Take your time as you work through these in groups and for homework. 
   * Read the background information and instructions, follow links to documentation, read or at least skim some of the external resources. 
   * Try to work toward improving your understanding rather than rushing to find an answer to all questions as quickly as possible. 
* Following instructions vs. thinking and coming up with your own solution
   * I’ve spent a fair amount of time attempting to prepare instructions that are clear and at the right level (offering hints, but not telling you exactly what to do).
   * I update, correct and improve the instructions every year based on student questions and common sticking points.
   * I really appreciate it when people ask for clarification, offer suggestions, fixes for typos, etc.
#### Sanity checks
   * As you work, remember to include periodic sanity checks.
   * It’s relatively easy to produce a plot or calculate a number, but try to stop and ask yourself if it actually makes sense based on what you expect and general knowledge.  
   * For example, several students had latitude and longitude backwards on initial plots in Lab 03 (a common mistake, one that I still occasionally make).  When you make a plot, check axes, and ask yourself, is it possible to have points at a latitude of -125°? (ah, no, as this exceeds -90° latitude at the south pole)
#### Sample code and output
   * When preparing the exercises notebooks, I remove most of the code, but I preserve a subset of plots and other output.
   * These are intended to serve as a guide, help you check your own output, and keep you on the right track - not a substitute for doing your own sanity checks.
   * These are not the “correct” answer or a plot that you must reproduce! Many are quick plots that I generated using personal preferences/habits, and they can contain mistakes or other issues that should be fixed.  
   * Rather than reproduce sample output, try to create plots/output that you think offers the best answer or visualization for the task/question. Better yet, make a plot that improves upon what I included! 
   * And if your answer differs from mine, but you are confident, back it up with some justification. You’re probably right! You’re all smart and collectively will notice things that I missed, and I will gladly update the solutions notebook to avoid confusion in future years. Thanks!
#### Getting help
   * If you’re confused or uncertain about something, please ask! 
   * Post questions or comments on the relevant Slack channel for the lab (e.g., #lab03)
   * I really appreciate it when people follow up because they genuinely want to understand something, rather than just producing some output and quickly moving on to the next question (though I understand there’s only so much time, and lots of content).

## Submitting Completed Assignments
### 1. Prepare Jupyter notebook for submission
* Include your name and date at top of notebook, please don't submit your homework as David Shean :)
* Replace `%matplotlib widget` with `%matplotlib inline`
* From the top menu, click Kernel -> Restart Kernel and Run all Cells…
* Your figures are now statically rendered jpg and will be embedded in the notebook for review/grading
    * If you are unhappy with figure size, you can change default figure size by adding `plt.rcParams['figure.figsize'] = [10, 8]` or increasing the dpi, after the  `import matplotlib.pyplot as plt` line, or tweaking each figure size in inches. Note that this will increase the filesize of your notebook!
    * When you’re satisfied, Run All Cells again.  
* Save the notebook by clicking the little floppy disk icon.  

### 2. Git workflow
* In a Jupyterlab terminal, `cd` to your assignment repo
* Use standard git add/commit/push workflow
    * `git add completed_notebook.ipynb`
    * `git commit -m 'Meaningful commit message'`
    * `git push`
* Go to your Github repo, click on the notebook file to render in the browser (might fail the first time if filesize is large, click reload), and verify that everything looks good!

### 3. Canvas submission
* Go to the Canvas assignment page, and submit the url to your Github repo

### 4. Instructor/TA will review
1. Instructor/TA will review the changes you made (summarized in the "Feedback Pull Request") and add inline comments/discussion.
1. If your submission is a Jupyter notebook, cell-level comments will be added using ReviewNB
1. Final grade assigned via Canvas
1. Instructor/TA will post solutions to the solutions repo on UW-GDA Organization
   * These are meant to be used as a "read-only" reference for you to review after turning in your assignment
   * They represent one set of solutions, and they are not necessarily the most elegant, efficient or best solutions. 
   * There are always going to be several ways to solve these problems, and rarely a “right” answer.

### 5. Reviewing instructor feedback
1. Open your assignment repo on Github
1. Click the Pull Request tab near the top of the page
1. Click the Pull Request named Feedback
1. Review any general comments or other comments visible on Github (more relevant for text files and/or shell)
1. To review comments on your notebook submisison, click the purple ReviewNB button
1. Review the cell-level and general comments from instructor
    * Respond to questions/comments as needed
    * Follow up on anything that is unclear
    * If instructor/TA made a mistake during grading, let them know!

### 6. Merge the Pull Request on Github
* This won't change anything for your submission, but it indicates to the TA/instructor that you reviewed the feedback, and interactive discussion is complete.
