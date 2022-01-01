# Final Project

UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

## Overview
The final project is an essential component of this course. It provides an opportunity for you to independently scope and explore a topic of interest, and hopefully apply some of the concepts and approaches that we've covered during the course, solidifying your understanding of the material. The hope is that you can share what you learned with your classmates, and then proudly post your final project repository on your Github page to share with the world (and future employers).

## Expectations, Deliverables, and Milestones
### Weeks 1-3: Defining a project
If you already have an idea for a project, great! If not, also great!

There is intentionally a lot of flexibility here. This can be an individual or group project, though I encourage you to consider a group project, as you can do more collectively, and it will provide real-world experience with collaborative development on Github. 

You have multiple options:
1. Propose a research question or a new tool/package, develop a plan (hopefully applying the concepts we’ve covered in class) and do the development, analysis, and interpretation
    * If you’re already engaged in independent research, try to define a project that will help you move that work forward
    * Explore a side project unrelated to your current research - you never know, it could become a viable research project in the future
    * If independent research is new to you, I encourage you to talk to me, and talk to other professors and grad students in your discipline to define a suitable final project
2. Join forces with others in the class who have already done #1.
3. Something that doesn’t fit into the above categories - pitch it!

### Week 3-4: Project Idea Pitches
* Develop a short, 1-minute pitch/summary of project idea(s)
* Come to class ready to share your idea(s) in small groups and provide feedback to others
* If you see potential opportunities to work with other students, follow up with them on Slack!

### Week 5: Submit Short Summary
* Submit a short summary of your project. This could be a few sentences or a short paragraph, and will be part of your repo. Two options:
   * If you feel like you're ready (you probably are!), please post directly to the #project channel on Slack
      * Others can provide feedback, or potentially join forces
      * Remember that this is non-binding and your project will inevitably change as you continue refining and start the work
   * Send a direct message to the instructor and TA on Slack
      * Instructor/TA will attempt to provide feedback and answer lingering questions
      * When ready, please post updated/refined idea to #project channel

### Week 6: Review Summaries, Continue Refining, Additional Group Formation
* Review the lists of project summaries on the #project channel
   * Offer feedback, ask questions, suggestions for datasets
* If you see potential opportunities to work with others, follow up with them on Slack! Or continue with an individual project!
   * For group projects, start discussing next steps with your team, defining roles, dividing tasks
* Start preparing more detailed project outline (see below)

### Week 7: Repo and Project Outline 
#### Create a Github repository
Create a new private repo for your project *within the GDA organization* (can transfer to personal accounts later if desired). Go to https://github.com/UW-GDA and click the big green "New" button.

Try to think of a descriptive repo name, bonus points if it is clever - try to avoid repo names like “finalproject”, which doesn’t help your classmates distinguish between projects.

When you initialize, select to include a README.md and include a .gitignore file for Python.

Don’t stress too much about the specifics of the repo - these are not permanent, and you can always change repo names, or start over entirely (just copy and add existing files as a first commit). One of the goals here is to gain more experience using git (potentially for collaborative work), and you’re inevitably going to make some mistakes along the way. Best to do it here, where stakes are pretty low.

#### Group project initialization
If you’ve decided to do a group project, pick a project lead to initiate and manage the repo, add others as collaborators (individuals or using a new Github Team within the UW-GDA organization), and make sure all can access and commit to the repo. 

Some of the resources from our recent ICESat-2 Hackweek event may be useful here (swapping `UW-GDA` for `ICESAT-2HackWeek` in the urls): https://icesat-2hackweek.github.io/learning-resources/projects/project_initialization/.  If you encounter issues, send me a direct message on Slack (including everyone on the group project), so I can help you navigate. 

I would like to see **at least one commit from each group member** at this phase of the project, even if it is as simple as everyone using the Github interface to edit the README.md file and add their name. There are many approaches to collaborative group/team development using git/Github and no "right" way. 

#### Group project collaboration
Collaboration can be a bit more complicated with Jupyter notebooks (vs. standalone Python scripts/libraries), since running cells in the notebook will change execution count and output, even if the code and content appear identical. Best practice is to avoid situations where two people are independently working on the same notebook. When trying to push/pull changes to/from same origin branch, there will inevitably be merge conflicts that can be messy to untangle (though ReviewNB is useful for reviewing notebook diff).

General recommendation - split up the project into multiple smaller notebooks, and have each person work on different components. Avoid the long mega-notebook (like most of our labs), and instead structure your repo with a series of notebooks. For example, you could have one notebook that ingests files, reduces/manipulates the data (e.g., reprojection), then writes new files out to disk in "analysis-ready" format. Then a second notebook reads in those data and does some analysis, creates some plots, etc. If you can pass things back and forth between group members like this, you'll avoid conflicts.

Alternatively, each team member can create separate notebooks with different filenames that both live in the shared repo. When another team member does some work and commits their notebook to the shared repo, you can can pull changes, open their notebook, select relevant cells, copy and paste into your notebook. One simple option with this model is for each group member to create and maintain a subdirectory within the repo where they will stage and modify their own notebooks for their component of the project. 

If you feel comfortable with git/github, you can also use a more standard git branching workflow: https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow/. Reach out to the instructor and TA for additional recommendations.

#### Prepare your README
The README.md file in your new repo will serve as the landing page for your project. You can continue to update as your project evolves, but for now, please prepare a basic project outline. I recommend that you review the markdown cheat sheet and use some basic headings, bulleted/numbered lists, and other formatting to organize your outline.

Please include the following (can combine and reorganize as necessary):
- Project Title
- Name(s) of individual or team members
   - See requirement above for at least one contribution/commit from each team member on the project README.md. Adding names is a good way to practice collaboratively editing a file on Github.
- Short 1-2 sentence summary
- Some introductory background information
- Problem statement, question(s) and/or objective(s)
- Datasets you will use (with links, if available)
- Tools/packages you’ll use (with links)
- Planned methodology/approach
- Expected outcomes
- Any other relevant information, images/tables, references, etc.
- References

That may sound like a lot, but some of these items should only be 1-2 sentences, others can be short lists. Consider this the start of your final report.

### Weeks 7-10: Do the project!
* Start early!
* Create subdirectories in your repo to store:
   * notebooks
   * data (if applicable) - make sure filesize (<20 MB) and total number of files (<20) is limitied.
   * doc (if applicable) for any additional documentation, static images you want to include in notebooks or markdown files, etc.
* Start adding and developing notebooks, code, markdown files, etc.
* Start with limited test case(s) for initial development and exploration:
   * Extract a small region of a large raster
   * If you need the entire raster, start with a downsampled version, then when you're happy with methods, run for native resolution
   * Start with a single timestep or subset of timesteps for time series analysis
* Data storage
    * Ideally, develop reproducible workflows that dynamically fetch and process data stored on centralized public data centers (e.g., AWS S3, NSIDC, CUAHSI)
    * If necessary, you can store files on the Jupyterhub, or even better, host externally and fetch dynamically for analysis
    * Don’t add unnecessary files to your repo (careful with `git add .`)
    * We'll discuss some options during labs later in the quarter
* Commit early, commit often

### Final Exam Week: Presentations
* Each individual/group will prepare and deliver a ~5-10 minute presentation/demo during a group session at the eScience Institute
    * If you only need 5 minutes, that’s perfectly acceptable
    * Larger groups will have up to 10 minutes if necessary
    * Format is flexible: can be slides, scrolling through notebook(s), scrolling through markdown files
      * If using slides, please include a copy of your presentation in your final project repo (ideally a pdf, which will render on Github)
* There will be short Q&A/discussion after each presentation
    * Let's try to type all questions/comments in the #project Slack channel, so presenters can follow up later
    * Hoping we can do one short question/response live during the transition to the next speaker
    * I expect active engagement from the entire class. Part of your final project grade is based on participation during the group session
* Before our project presentation session, please enable read access on your repo, so others in the class can see your great work, and learn from what you've done!
   * Open the "Settings" tab near the top of your repo
   * Select "Manage Access" on left side
   * Click the green "Invite teams or people"
   * Type `gda_w2021_students` in the search bar and select
   * Use the default Read access and click the green button to proceed
   * Check the UW-GDA organization to see other project repos!
   * I recognize that this may feel a little uncomfortable, especially if you didn’t have as much time as expected or don’t feel your repo is “finished.” It’s OK! We’re all in the same boat and projects like this are never truly finished. See below for some additional thoughts, and please reach out if you would like to discuss.

#### Some Perspective
Please remember that nobody is asking for or expecting perfection on your final projects. The reality is that you probably only had time to attempt 10-30% of the things you outlined during Week 6. And that’s OK. If some things worked out, fantastic! Tell us a little about them so we can share your success and learn from what you’ve done. If nothing worked out, that’s also OK! Share a bit of why you chose this project, what you attempted, some of the challenges you encountered, and plans/recommendations for future work.

This was meant to be an exercise to get you independently scoping your own projects and starting to explore new data/techniques, while also solidifying and building on some of the material we covered this quarter. Nobody is expecting a research project that is ready for publication or a presentation ready for a major international conference.

If after this week, you never revisit this work, I hope that it was a useful learning experience. However, I think several of you will continue to pursue some of the things you started, maybe for your MS/PhD research, which is always really rewarding for me to see. I'm happy to continue offering input as you continue.

You all know each other by now, and you know that this is a friendly, open, supportive group. Nobody is judging you or your presentation/repo. We all have a lot going on right now. Let’s support each other, offer constructive feedback, and celebrate our collective accomplishments.

### Final Exam Week: Repo Submission
* Finalize your repository with notebooks, scripts and documentation
    * Can use README, notebooks, or separate markdown files to summarize methods, results, conclusions, lessons learned and future work
    * Clean up old or unused files (can remove or create an `old` subdirectory and move files there)
    * Update the README with information about the notebooks used during processing and provide a clear indication of which notebooks contain the final results
      * Help someone who is unfamiliar with your project quickly find the good stuff! 
* Submit the Github url for your final project repo on Canvas before midnight on Friday of final exam week
* Optional: make your repo visible to the world! Just need to switch from private to public visibililty:
   * From the "Settings" tab, scroll down to the Danger Zone and click "Change Visibility"
   * Select "Make Public" and type the repo name in the prompt
   * Share the url with others!

## Sample project ideas
Please review examples from previous years in the UW GDA Github organization.

## Sample data
See separate document: [Data Sources](./project_data_sources.md)
