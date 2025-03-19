Version control in professional software development

Version Control plays a crucial part in software development. As a developer, you’ll work with other developers on projects to deliver software to customers. Depending on the role, you could be working with a small team of 2 or 3 developers in a single project or a large team spanning multiple projects. In either scenario, Version Control will be a crucial tool to help your team succeed.

However, Version Control must be complemented by other tools and procedures to ensure quality and efficiency throughout the software development process. In this lesson, we’ll explore some of the common tools and strategies developers use in conjunction with Version Control.

Workflow
Using Version Control without a proper workflow is like building a city without traffic lights; without appropriate management, everything will turn into chaos.

For example, let’s say you’re working on a big project and editing a file. Another developer also starts editing a file. Both of you submit the file to the VCS at the same time. Now there’s a conflict! How should the conflict be resolved? A good workflow will have a process for resolving conflicts.

Another example is when a new junior developer is joining your team. If the project code is used for a critical system, it is risky to allow them to submit code changes directly. To solve this, many developers use a peer review system where another developer must review code before it can be merged in.

Workflows are essential to ensure code is managed correctly and reduce mistakes from happening. Different projects will have different workflows. In this course, you’ll learn some common workflows using the Git Version Control System.

Continuous Integration
Continuous Integration, or CI, is used to automate the integration of code changes from multiple developers into a single main stream. Using a workflow whereby small changes are merged frequently, often many times per day, will reduce the number of merge conflicts.

This process is widespread in test-driven software development strategies. CI is often used to automatically compile the project and run tests on every code change to ensure that the build remains stable and prevent regressions in functionality.

Continuous Delivery
Continuous Delivery is an advanced practice built on top of Continuous Integration. In this approach, once changes are merged into the main codebase, a Continuous Delivery pipeline automates the process of preparing the application for deployment. This process includes tasks like building the application, running tests, and packaging it for deployment to a production-like environment.

The main goal of Continuous Delivery is to ensure that the application is always in a deployable state, even after multiple changes by different developers. By automating these steps, Continuous Delivery eliminates the risk of human errors during the packaging process and reduces delays in getting the application ready for deployment. However, Continuous Delivery requires manual approval to release the application to the production environment. Although this gives teams greater control over when and how changes are deployed to live systems, Continuous Delivery is slower than Continuous Deployment because of this manual step.

Continuous Deployment
Continuous Deployment takes Continuous Delivery a step further by automating the actual deployment of the application to production. With this practice, every change that passes through automated tests and validations in the pipeline is automatically deployed to production without the need for manual intervention.

The strategy involves deploying to a staging environment first, where additional checks or validations might occur, and then promoting the changes to the live production environment. Unlike Continuous Delivery, Continuous Deployment eliminates the manual approval step, making it faster and more efficient. This approach ensures that updates, features, and fixes are delivered to customers as soon as they are ready, fostering rapid and iterative delivery. Continuous Deployment is ideal for teams that prioritize speed and frequent releases over manual control.

Automation is the key difference that sets Continuous Deployment apart from Continuous Delivery. These two deployment types can be used together in a pipeline or adopted independently, depending on the organization’s processes and requirements. When used together, the Continuous Delivery steps ensure the code is production-ready after passing all tests and reviews. The Continuous Deployment then automates the final step of deploying production-ready code without manual intervention. Using them together in a production environment provides an additional safety layer but also increases the time required.

Conclusion
With these tools and procedures, it is possible to understand how software starts from a developer writing code to being deployed live for customers to use. Of course, there is much more to running a live software service, but that is a lesson for another day.

---

Development Environments

Every development team prior to releasing their new features or changes needs to verify that the code they do release is not going to cause any issues or bugs. In order to achieve this, they normally set up multiple environments for different ways to test and verify.  A common practice is for teams to have a developer environment, a UAT or QA environment, and a staging environment. The main purpose of this flow is to find any potential issues that may arise due to changes or new features being added to the codebase. The more ways to test the changes the less likely bugs will be introduced.

Staging
The staging environment should mimic your production environment. The reason for this is because you want to test the code in an environment that matches what you have in production. This allows teams to spot or find any potential issues prior to them getting to production. The closer the staging environment is to your production, the more accurate your testing is going to be. Staging environments can also be used for testing and verifying new features and allow other teams including QA or stakeholders to see and use those features as a pre-trial. Staging should also cover all areas of the architecture of the application including the database and any other services that may be required. Areas that benefit from staging environments include:

New Features
Developers submitting new features along with feature flags for turning them on and off should always do a testing round in a staging environment. They allow teams to verify that the feature works, it can be turned on and off via configuration flags and also that it does not break or interfere with existing functionality.

Testing
As the staging environment mimics your production environment, it's also a great place to run tests. QA teams will normally use it to verify new features, configuration changes or software updates/patching. The types of testing covered will be Unit testing, Integration testing and performance testing. All except performance testing can also be carried out in production. Performance can also be completed in production but only at specific times - usually out of hours as it will have a drastic effect on the user experience.

Sometimes it is not always feasible to have an exact replication either due to costs or time. Certain areas can be cut back - for example, if your service is load balanced on 10 virtual machines in production, you could still have 4 virtual machines in staging. The underlying architecture is the same but the overall performance may be different.

Migrations
Staging is a perfect place to test and verify data migrations. Snapshots can be taken from production and used to test your migration scripts to confirm your changes will not break anything. If in the case it does cause an issue, you simply rollback and try again. Doing something like a migration in production is extremely risky and error-prone.

Configuration Changes
Configuration can also cause headaches for teams, especially in a large cloud-based architecture. Having a staging environment will allow you to spot any potential issues or bottlenecks.

Production
Production is live. It's out there for people to see and/or interact with. Any issues or problems you may have had should have been caught and fixed in the staging environment. The staging area gives the team a safety net to catch these possible issues. Any code that is deployed to production should have been tested and verified before the deployment itself. 

Downtime
Downtime for any service especially customer facing will most likely be revenue impacting. If customers can not access or use your website or app to its full capabilities, it will most likely have a cost involved. Take for example an e-commerce company that allows users to buy goods and services online. If they release a new feature to their shopping cart which actually breaks the payment process, this will have an impact on customers not being able to buy goods online.

Vulnerabilities
Cyber-security should also play a big role in what gets released in production. Any updates to software such as patching or moving to the latest version should be checked and verified. This is also the same rule for not upgrading software when critical updates are released.

Reputation
Downtime or issues in production is damaging for a company as it does not instill confidence in end users. If something is down or broken it can cause the company to lose potential customers.

---


---

remote and local

In the pre-internet era, saving project files to different machines for backup and transfer was a tedious process. It required manually copying files between machines, one at a time. Making things slow for teams. Nowadays the cloud has enabled a more efficient way to do this. And in this video I'll explain the differences between remote and local on Git hub. You have previously learned about the flows modified, staged and committed in a Git workflow. Now you will learn about pushing your changes from your local to a remote repository. Remote refers to any other remote repository to which developers can push changes. This can be a centralized repository, such as one provided by Git hub or repositories on other developer devices. In this lesson, you will be hearing some new terms such as clone, push, pull and repo. Don't worry. These will all be explained soon. The remote code is accessed through a URI which is unique and only accessible to those who have permission local. On the other hand refers to your machine which can be a laptop, desktop or even a mobile device and is only accessible to you to demonstrate both of these in action. Let's say we have a project called coding project one which is located on Git hub with a unique URL. In other words, this project is stored on a remote server. When a user wants to copy this project to their local device, they need to either perform a clone if it's the first time or pull it to get the latest changes. To clone a project a user must first choose a folder on their local machine. Coding project one is then cloned from the server and copied into the chosen folder. The user can then make changes to the project and push those changes back to the server. Other users working on the code base won't see those changes on their local machines unless they pull the latest changes from the server. One of the advantages of it is that you can work offline and then commit your changes when you are ready. Now let's go through an example of how exactly you would do this and Git hub. In this video I'm going to explain what local and remote mean in Git hub and help you to understand the differences between the two. First off, I'm going to create a new local repository using the Git in IT command. I'll start by inputting M K D I R to create A new directory and then I'll set the name as my second repo. Next I'll use the change directory command which is CD followed by the name that I just said. Finally, I'll perform the Git in IT command to create my new repository. This will return a line telling me that an empty repository has been initialized under route projects my second repo. If I execute another command called git remote, it comes back as blank. The reason for that is that I've only initialized a local repository which has no connection to a central repository that sits either on Git hub or another server. Right now it's only available locally on my machine. Now I'll step back out from this directory and go into my first repo with a CD command. Again, this is a repository that I created earlier and does have a connection to Git hub. Using the remote URI I'll then check it by using the get remote minus V command. Git tells me that it's set to git tutorials 101 my first repo.Git. Next I'm going to set this against her second repository.

I'll step into the new directory once more using the CD command.

In this case we're going to add this URL to the remote settings by using the command. Git remote add specifying a name and then passing in URI, the name that is typically used here is origin. So I'll stick with that. So again the full command with the URL should read Git remote at origin. Git at Github.com: Git tutorials 101/ My first repo.Git. This time when I execute the Git remote minus V command. I have this set up against the get tutorials 101 which sits up on Git hub. What I'm going to do next is use the Git pull command which will connect with the GIT hub server, and pull down all the changes from the repository. So on my local I now have all the changes, but when I check the directory it's blank. The reason for this is that I haven't set up a branch that matches with what I have on the server repository. Fortunately I can change that by performing the command. Git check out main. Which will set up a branch main on my local that tracks the branch main from the remote. And now when I check my folder using the LS command, it confirms that I have the read me test and test two files available on my local.

In this video, you learned about the differences between local and remote and Git hub. This will help set you up to exchange data more efficiently within your development team. See you next time.

---

pull and push

By now, you should know how to use git add, and git commit to add new changes to your local repository. Put them into the staging area, and get them ready for a commit. Now, let me guide you through the next step in uploading these changes to the remote repository using git push. I'll also demonstrate how to retrieve changes from the remote servers and apply them to your local repository with git pull. Before we begin, let's go over the command line and perform the command git status. Git tells me that I'm on the branch, main, but also the my branch is ahead of the origin main branch by one commit. What this means is that all the changes that I have on my local repository are currently ahead of what is stored in the remote repository on GitHub that ties into Git's distributed workflow in which you can work in an offline state and then only ever communicate with a remote repository when you use the commands of git push or git pull. Now I'll guide you on pushing your changes to the remote repository, and then I'll demonstrate how to use the pull command to get the latest changes. It's always good practice to check which branch you're currently on. You can use git status or git branch to do this. This is important because if you do make changes in a different branch, you need to specify where you're pushing up to. Let's push up the changes using the git push command. I'll specify the origin branch to be the main branch. As in, I'm pushing my changes to the origin as the remote repository, and then I want to push it to this branch as the main. I'll be prompted for my login information as I am pushing using HTTPS. Once I enter my login information, you'll notice that the commit is pushed from the local main to the remote main, on the remote repository. Let's refresh the page on the GitHub website. You can see that my test.txt file now appears there. That's taken the commit snapshots that I have in my local repository and pushed it up to the remote repository. Git has then compared those files with what's on the remote repository to find any conflicts or problems. If none are found, it'll just merge them straight through, which is classed as an auto merge. If there are any conflicts, my push will fail. Before doing a push, it's also good practice to perform a git pull in order to get the latest changes from the remote repository and reduce the odds of encountering a conflict. Because I only have a single file and this will be a new repository, I'm not going to run into any conflict or any issues. Now let's move on and I will guide you through how you can use git pull. Normally when you're working on a project, you could have several developers all submitting with different branches, different code, and different features. In order for you to get those changes, you need to use the git pull command. To demonstrate this, I will add a single line to the test.txt file, using the GitHub UI and then add the climate change, updated the test.txt file. I'll then commit it directly to the main branch, by clicking on Commit Changes. The changes now appear on the UI. But because I haven't used the git pull command on my local machine yet, I should have no content of the test.txt file. Let's verify by using the cut command on test.txt. Sure enough, the file is empty, which is what you'd expect. As I mentioned before, I need to run the command git pull. This will get the latest changes from the remote repository. If any new changes were added, it'll be reflected in the shell output. I run the command, and in this case, Git tells me that one file has changed with one insertion. If I run the cut command on test.txt once more, it shows that the line "this is my change" is now available in my local directory. With git pull, you're taking all that data from the remote server. Git then merges the snapshot from the remote with the snapshot that's on your local. It will auto merge them if there is no conflicts. Once that's complete, I'll have the latest changes on my local machine. You have now learned how to push to and pull from your GitHub repository.

---

Resolving conflicts
Conflicts will normally occur when you try to merge a branch that may have competing changes. Git will normally try to automatically merge (auto-merge), but in the case of a conflict, it will need some confirmation.  In such scenarios, user intervention is required to review and resolve the competing changes. This process is called merging or rebasing. 

To resolve, the the developer must look at the changes on the server and their local repository and validate which changes should be resolved.

A merge conflict example is when two developers work on their dependent branches. We will be demonstrating this with the help of an example in this reading. Imagine that both developers are working on the same file called Feature.js. Consider a scenario where two developers are working on dependent branches. Each of their tasks is to add a new feature to an existing method. Developer 1 is working on a branch named feature1, and Developer 2 is working on a branch named feature2.

Developer 1 completes their changes and pushes them to the remote repository. Later, Developer 2 also attempts to push their changes. Since both have modified Feature.js, Git detects a conflict that requires resolution before the merge can proceed.

Demonstration of the push pull methodDemonstration of the push pull method
Let's walk through how this would happen in Git. Both Developer 1 and Developer 2 check out the main repository on Monday morning. At this point, they both have an identical copy of the code. Each developer then creates their own branch: feature1 and feature2.

12
    git pull
    git checkout -b feature1
12
    git pull
    git checkout -b feature2
Developer 1 makes their changes to a file called Feature.js and then commits the changes to the repository for approval via a PR (pull request)

1234
    git add Feature.js
    git commit -m 'chore: added feature 1!!'
    git pull origin main
    git push -u origin feature1
The Pull Request (PR) is reviewed and then merged into the main branch. Meanwhile, Developer 2 is working on their feature. They follow a similar process to Developer 1.

Note:  If you look at the code, any reference for HEAD in Git refers to the current branch or commit you're working on.

12345678910
    git add Feature.js
    git commit -m 'chore: added feature 2!!!'
    git pull origin main

From github.com:demo/demo-repo
 * branch            main       -> FETCH_HEAD
   9012934..d3b3cc0  main       -> origin/main
Auto-merging Feature.js
CONFLICT (content): Merge conflict in Feature.js
Automatic merge failed; fix conflicts and then commit the result.
At this point, Developer 2 encounters a merge conflict. Git notifies that a merge conflict has occurred and requires resolution before changes can be pushed to the remote repository. Running git status provides additional details about the conflict:

1234567891011
    git status
    On branch feature2
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   Feature.js


To resolve the issue, Developer 2 must review and compare the changes made by Developer 1. It’s a good practice to first identify the conflicting branch by using the following command:

123456789101112131415
 git log --merge

commit 79bca730b68e5045b38b96bec35ad374f44fe4e3 (HEAD -> feature2)
Author: Developer 2 
<developer2@demo.com>
Date:   Sat Jan 29 16:55:40 2022 +0000

    chore: add feature 2

commit 678b0648107b7c53e90682f2eb8103c59f3cb0c0

From the log, we can see that conflicting changes occurred in feature1 and feature2. Developer 2 now examines the specific differences causing the conflict:

123456789101112131415
git diff

diff --cc Feature.js
index 1b1136f,c3be92f..0000000
--- a/Feature.js
+++ b/Feature.js
@@@ -1,4 -1,4 +1,8 @@@
  let add = (a, b) => {
++<<<<<<< HEAD
 +  if(a + b > 10) { return 'way too much'}

The only difference is in the wording of the return statement. Developer 1 used 'too much', while Developer 2 used 'way too much'. Git uses markers (<<<<<<<, =======, and >>>>>>>) to indicate the conflict. Developer 2 resolves the conflict by editing the file and removing the markers:

1234
let add = (a, b) => {
  if(a + b > 10) { return 'way too much'}
  return a + b;
}
Developer 2 then stages and commits the resolved changes:

123
 git add Feature.js
 git commit -m 'fix merge conflicts'
 git push -u origin feature2
Developer 2 has now resolved the merge conflict and can create a PR to merge their changes into the main branch.

This may seem bit complicated at the beginning, but merge conflicts are a normal occurrence in collaborative coding, and each developer gets better at handling them with practice. It will begin to feel more natural as you follow along and practice these methods yourself.

--- 

Example workflow

Have you ever applied for a job? You know the process, prepare your resume, look for jobs, submit an application, prepare for interviews. That is an example of a workflow, in computer programming workflows are really important. By the end of this video, you will be able to describe what a workflow is, and you will also be able to identify different workflows available. Now, let's start with an example to illustrate why workflows are important. As a developer working on a project, you first need to pull the project down from a remote repository to your local machine. This is commonly called checking out a project or pulling a project. Once on your local machine, you can build and run the project and make changes. When you're done, you have to push the changes you made back to the remote repository so other developers can see them. From this example, you can understand that the purpose of a workflow is to guide you and other members of your team. It should not disrupt or cause blockers for deployment or testing or for any other developer who contributes to the project itself. Choosing a workflow needs careful consideration. It can depend on the size of the team, the culture of your workplace and also the type of product you intend to build or update. With that in mind, let me explain feature branching, a common workflow used by many developers. Feature branching means you create a new branch from the main line and work on this dedicated branch until the task is completed. Rules and conditions need to be made in order for this branch of code to be kept in a good state. Every code base has a main repository which is essentially the source of truth for the application. All changes such as add, edit or delete are submitted directly to the feature branch, the main branch stays as is. When you are ready and happy with the code you have added, you have to commit the changes and then push to the server repository. To commit, you push the changes and as it's a feature branch, a pull request follows. The pull request is compared to the main branch, so developers who peer reviewed the code can see exactly what was changed. Once it's reviewed and approved, it can then be merged into the mainline.

Now let me guide you through how this works using Git and Git hub. Before creating a new branch, always ensure you have the latest code. You can do this by running the git pull command to pull the latest code from the remote repository. Next you need to create your new branch. You can do this by passing the -b flag with the check out action. Next, let's add new content to this branch. Let's create a README.md file, to do this type git add. or git add README.md and press Enter. Next, we need to commit the new file and provide a meaningful message so other developers can see what you added. To do that Run the git commit command with a -m option to include a message with a short description of the changes being committed. The file has now been added to the local branch, this means that the file is only visible locally to you. To allow other developers to see the changes, you need to push the file to the remote repository. You can do that by running the git push command and referencing the new file. The changes are now pushed to the remote repository on git hub. Your next action is to get a review as part of a pull request, but more about that later. And that brings us to the end of this video. Now, you know what a workflow is and how a feature workflow works, well done.

   