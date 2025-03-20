# GitHub

As I am using https, I will be prompted for my login information. Once this action has been completed, GitHub will recognize that a new branch has been added. It will then prompt me to create a poll requests that can be compared against another branch, in this case, the main branch.

## Criando um repositório local

```
git remote add origin <URL>
```

## Git push

O comando git push empurra (envia) alterações locais para qualquer “remoto” - no nosso caso, o GitHub. Por exemplo, para enviar os commits do nosso ramo principal local para o ramo principal da origem remota, executaríamos:

```
git push origin main
```

Outras formas

```
git push origin <localbranch>:<remotebranch>
```

You can also delete a remote branch by pushing an empty branch to it:

```
git push origin :<remotebranch>
```

## Git pull

Fetching is nice, but most of the time we want the actual file changes from a remote repo, not just the metadata.

```
git pull [<remote>/<branch>]
```

he [...] syntax means that the bracketed remote and branch are optional. If you execute git pull without anything specified it will pull your current branch from the remote repo.

## Pull request

On GitHub, a pull request is a way to propose changes, typically to the rest of your team, or to the maintainer of a project you're contributing to.

Pull requests allow team members to see what changes are being proposed and to discuss them before they are merged into the main codebase.

The purpose of a pull request is to obtain a peer review of changes made to the branch. In other words, to validate that the changes are correct when coding, many teams will have conditions around the unit tests and integration tests. These conditions will usually include validating that the standards have been met for merging back into the main line, a team will also check for any issues that might have been missed.

My next step is to open the GitHub UI. GitHub will show my new branch with a prompt. Click on the compare and pull request button. A pull request lets the team know that I've made new changes that I want them to review and that I also want to approve or request changes to the actual poll request itself. Another thing to note on the GitHub UI is that I'm comparing this with the main branch. I've essentially cut a branch from the main called feature lesson. I've then added a new file called test2.txt. It's this file which is the main difference between the two branches. Next, I check the pull request. I can see that there has been one commit. In other words, just one file has been changed and it's been added as test2.txt. I then click create pull request. The team will then review the changes and either approve or decline them. Once approved, you can then merge your changes to the main branch. This is much cleaner than everyone working off the main branch.

## Git clone

Let's say we have a project called coding project one which is located on Git hub with a unique URL. In other words, this project is stored on a remote server. When a user wants to copy this project to their local device, they need to either perform a clone if it's the first time or pull it to get the latest changes. 

To clone a project a user must first choose a folder on their local machine. Coding project one is then cloned from the server and copied into the chosen folder. The user can then make changes to the project and push those changes back to the server.

Other users working on the code base won't see those changes on their local machines unless they pull the latest changes from the server. One of the advantages of it is that you can work offline and then commit your changes when you are ready. 


