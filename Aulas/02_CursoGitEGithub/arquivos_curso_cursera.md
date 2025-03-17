Version Control
In this course, you will learn about how modern software developers collaborate across the world without messing up each other's code. You will look at the different version control systems and how to create an effective software development workflow. You will be introduced to some of the most commonly used Linux commands that you can use to work with files on your hard drive and create powerful workflows that will automate your work, saving you time and effort. Finally, you will see how Git can be used in software development projects to manage team files, you will create a repository that can manage code revisions.

After completing this course, you will be able to:

Implement Version Control systems.

Navigate and configure using the command line.

Manage code revisions.

Create and use a GitHub repository.

The modules and resources that you will work through and explore in this course will help you to prepare for the Exam: 

Below is an outline of the modules that will be covered in this course:

Module 1: Software Collaboration

In this module, you will learn about using version control or subversion to bring order to the chaos of massive software projects that have the potential for mistakes and bugs. You will look at the different version control systems and how to create an effective software development workflow.

After completing this module, you will be able to: 

Describe how modern software teams collaborate and work on the same codebase.

List different version control systems and methodologies. 

Illustrate a standard software development workflow.

Module 2: Command Line

In this module, you will learn how to use the command line to execute commands in Linux. You will be introduced to some of the most commonly used commands that traverse, create, rename, and delete files on your hard drive. You will learn how easy it is to use piping and redirection to create powerful workflows that will automate your work, saving you time and effort.

After completing this module, you will be able to: 

Describe how the command line is and how it is used.

Practice traversing your hard drive via the command line.

Create, rename and delete files and folders on your hard drive using Unix commands.

Use pipes and redirection.

Module 3: Git

This module will help you to develop a strong conceptual understanding of the Git technology and how it is used in software development projects to manage team files. You will install Git, create a local repository, create a commit, create a remote repository and push commits to a remote repository. 

After completing this module, you will be able to: 

Outline the Git principles.

Use a GitHub repository.

Describe the steps in a standard GitHub workflow.

Create branches and merge different branches and sources.

Describe how code goes from local development to version control and then to live production.

Module 4: Graded Assessment

In the final module, you'll learn about the graded assessment. After you complete the individual units in this module, you'll synthesize the skills you gained from the course to manage a project on GitHub.

You'll also have the opportunity to reflect on the course content and the learning path that lies ahead.   

After completing this module, you will be able to: 

Recap on all of the topics covered throughout the course.

Apply all the skills you have learned in a graded project.

Practical Exercises 

We encourage you to complete the practical exercises in this course. By completing these exercises you will have a more practical understanding of how to explore Version Control.

---

A history of version control
As you know by now, version control is a system that records changes to a file or set of files over time so that you can access specific versions later. In software development, Version Control Systems (VCS) allows developers to manage changes to their code and track who made each change. But how did this software come about?

Version Control has a long history going back to the 1980s. In fact, version control systems were created before the Internet!

One of the first significant Version Control Systems was the Concurrent Versions System (CVS). It was first developed in 1986 by Walter F. Tichy at Purdue University and released publicly in 1990.

CVS stores information about every file in a folder structure, including the name of the file, its location in the folder structure, who last modified it, and when it was last modified. The CVS also stores information about folders, including their names and who created them.

It was popular for many years; however, it has some significant flaws in its design. CVS does not include integrity checks which means your data can become corrupted. When you update or submit changes to the system, if an error occurs, the system accepts the partial or corrupted files. Additionally, the system was designed mainly for text files, not binary files such as images or videos.

The main successor to CVS was Subversion (SVN).

CollabNet developed Subversion in 2000 and solved many of the issues present in CVS. To ensure data integrity, it included integrity checks in its design. It also supported the versioning of binary files better than CVS. Thanks to these improvements, SVN became popular in the open-source community with free hosting being offered for open-source projects by Google and SourceForge.

However, Subversion used a centralized VCS model. This means that all operations have to be done using a centralized server. If the server were down or slow, this would impede development.

In 2005, two new projects were started to develop distributed version control systems; Mercurial and Git. Both projects were created in response to an event involving the Linux kernel development.

Previously, the Linux kernel was using a proprietary VCS known as BitKeeper. BitKeeper was one of the first distributed version control systems initially released in 2000. BitKeeper had originally provided a free license to Linus Torvalds to support Linux’s development. However, in 2005, the license was revoked. This controversy led to the creation of the Mercurial and Git projects.

Mercurial was developed by Olivia Mackall. It is developed as a high-performance distributed VCS. Many platforms offering Subversion hosting began to offer Mercurial hosting too. It became popular as Subversion users found it easy to transition to a Mercurial repository, thanks to the hosting providers and its small learning curve.

Git was developed by Linus Torvalds to host the Linux kernel’s source code. Like Mercurial, it is a distributed VCS. Its first public release came in 2007.

Git became popular in the open-source community due to its distributed VCS design and Github offering free Git hosting for open-source projects. Git has since become the selected version control system for many open-source and proprietary software projects.

---

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