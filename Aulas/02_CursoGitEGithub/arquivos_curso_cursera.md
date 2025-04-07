
Resolving conflicts

Conflicts will normally occur when you try to merge a branch that may have competing changes. Git will normally try to automatically merge (auto-merge), but in the case of a conflict, it will need some confirmation.  In such scenarios, user intervention is required to review and resolve the competing changes. This process is called merging or rebasing. 

To resolve, the the developer must look at the changes on the server and their local repository and validate which changes should be resolved.

A merge conflict example is when two developers work on their dependent branches. We will be demonstrating this with the help of an example in this reading. Imagine that both developers are working on the same file called Feature.js. Consider a scenario where two developers are working on dependent branches. Each of their tasks is to add a new feature to an existing method. Developer 1 is working on a branch named feature1, and Developer 2 is working on a branch named feature2.

Developer 1 completes their changes and pushes them to the remote repository. Later, Developer 2 also attempts to push their changes. Since both have modified Feature.js, Git detects a conflict that requires resolution before the merge can proceed.

Demonstration of the push pull methodDemonstration of the push pull method
Let's walk through how this would happen in Git. Both Developer 1 and Developer 2 check out the main repository on Monday morning. At this point, they both have an identical copy of the code. Each developer then creates their own branch: feature1 and feature2.

**ver exemplos do código no site do coursera**

--- 
