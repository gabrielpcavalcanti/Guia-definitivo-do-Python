# Workflow

Usar o controle de versão sem um fluxo de trabalho adequado é como construir uma cidade sem semáforos; sem o gerenciamento adequado, tudo se tornará um caos.

Por exemplo, digamos que você esteja trabalhando em um grande projeto e editando um arquivo. Outro desenvolvedor também começa a editar um arquivo. Ambos enviam o arquivo para o VCS ao mesmo tempo. Agora há um conflito! Como o conflito deve ser resolvido? Um bom fluxo de trabalho terá um processo para resolver conflitos.

Outro exemplo é quando um novo desenvolvedor júnior se junta à sua equipe. Se o código do projeto for usado em um sistema crítico, é arriscado permitir que ele envie alterações de código diretamente. Para resolver isso, muitos desenvolvedores usam um sistema de revisão por pares em que outro desenvolvedor deve revisar o código antes que ele possa ser incorporado.

Os fluxos de trabalho são essenciais para garantir que o código seja gerenciado corretamente e reduzir a ocorrência de erros. Projetos diferentes terão fluxos de trabalho diferentes. Neste curso, você aprenderá alguns fluxos de trabalho comuns usando o sistema de controle de versão Git.

Existem diversos Workflows utilizados (você pode criar o seu). Nesse aquivo eu mostro alguns deles. Nenhum dos conceitos vistos abaixo foram explicados ainda, não se preocupe, eles serão explicados nas próximas aulas.

O intuito aqui é mostrar alguns Workflows prontos para que depois que você entenda os conceitos, apenas pegue o "tamplate" e aplique ao seu projeto.

I'm still in the feature lesson branch. I can check out my main branch by typing git checkout main. Then I run the git pull command. I'll then receive the latest changes that were merged in from the feature branch that I just created. Notice that the test2.txt file is now available. I can also verify that by doing a simple check within the directory by using the ls command. This returns a read-me file test.txt and the test2.txt, which is from my branch. You have now learned the branching workflow, which will use regularly when collaborating with other developers.

Choosing a workflow needs careful consideration. It can depend on the size of the team, the culture of your workplace and also the type of product you intend to build or update. With that in mind.

---

## Workflow N° 1

Criando um repositório

Preparação para o commit (Staging)

Fazendo um commit 

## Workflow N° 2 modelo GitHub

clona 

push

pull

By now, you should know how to use git add, and git commit to add new changes to your local repository. Put them into the staging area, and get them ready for a commit. Now, let me guide you through the next step in uploading these changes to the remote repository using git push.

## Workflow N° 3

This is a common workflow when working with Git on a team of developers:

Create a branch for a new change
Make the change
Merge the branch back into main (or whatever branch your team dubs the "default" branch)
Remove the branch
Repeat

## Workflow N° 4

update repositório - pull or/and fech
create a new branch
commit in the new branch
merge or rebase to main branch 
push
pull request

## Workflow N° 5

While on the topic of pull requests, I want to share a note on my simple workflow. 90% of the time, you're only using a handful of git commands to get your coding work done.

Keep Stuff on GitHub
I keep all my serious projects on GitHub. That way if my computer explodes, I have a backup, and if I'm ever on another computer, I can just clone the repo and get back to work.

Rebase vs. Merge
I've configured Git to rebase by default on pull, rather than merge so I keep a linear history. If you want to do the same, you can add this to your global Git config:

git config --global pull.rebase true

My Solo Workflow
When I'm working by myself, I usually stick to a single branch, main. I mostly use Git on solo projects to keep a backup remotely and to keep a history of my changes. I only rarely use separate branches.

Make changes to files
git add . (or git add \<files> if I only want to add specific files)
git commit -m "a message describing the changes"
git push origin main
It really is that simple for most solo work. git log, git reset, and some others are, of course, useful from time to time, but the above is the core of what I do day-to-day.

My Team Workflow
When you're working with a team, Git gets a bit more involved (and we'll cover more of this in part 2 of this course). Here's what I do:

Update my local main branch with git pull origin main
Checkout a new branch for the changes I want to make with git switch -c \<branchname>
Make changes to files
git add .
git commit -m "a message describing the changes"
git push origin \<branchname> (I push to the new branch name, not main)
Open a pull request on GitHub to merge my changes into main
Ask a team member to review my pull request
Once approved, click the "Merge" button on GitHub to merge my changes into main
Delete my feature branch, and repeat with a new branch for the next set of changes

Merge Pull Request
In a typical team workflow, you would ask a team mate to review your pull request. If they approve of the changes, they would approve the pull request, and you'd be clear to merge.

We're the dictators of our own repo however, so no need to wait for approval!


## Workflow N° 6

As a developer working on a project, you first need to pull the project down from a remote repository to your local machine. This is commonly called checking out a project or pulling a project. 

Once on your local machine, you can build and run the project and make changes. When you're done, you have to push the changes you made back to the remote repository so other developers can see them. 

let me explain feature branching, a common workflow used by many developers. Feature branching means you create a new branch from the main line and work on this dedicated branch until the task is completed. Rules and conditions need to be made in order for this branch of code to be kept in a good state. 

Every code base has a main repository which is essentially the source of truth for the application. All changes such as add, edit or delete are submitted directly to the feature branch, the main branch stays as is.

When you are ready and happy with the code you have added, you have to commit the changes and then push to the server repository. To commit, you push the changes and as it's a feature branch, a pull request follows. 

The pull request is compared to the main branch, so developers who peer reviewed the code can see exactly what was changed. Once it's reviewed and approved, it can then be merged into the mainline.

Now let me guide you through how this works using Git and Git hub. 

Before creating a new branch, always ensure you have the latest code. You can do this by running the git pull command to pull the latest code from the remote repository. 

Next you need to create your new branch. You can do this by passing the -b flag with the check out action. 

Next, let's add new content to this branch. Let's create a README.md file, to do this type git add. or git add README.md and press Enter. 

Next, we need to commit the new file and provide a meaningful message so other developers can see what you added. To do that Run the git commit command with a -m option to include a message with a short description of the changes being committed. The file has now been added to the local branch, this means that the file is only visible locally to you. 

To allow other developers to see the changes, you need to push the file to the remote repository. You can do that by running the git push command and referencing the new file. 
The changes are now pushed to the remote repository on git hub. 

Your next action is to get a review as part of a pull request, but more about that later. 

And that brings us to the end of this video. Now, you know what a workflow is and how a feature workflow works, well done.

## Workflow N°7

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

## Worflow N° 8

First off, I'm going to create a new local repository using the Git in IT command. I'll start by inputting M K D I R to create A new directory and then I'll set the name as my second repo. 

Next I'll use the change directory command which is CD followed by the name that I just said. 

Finally, I'll perform the Git in IT command to create my new repository. This will return a line telling me that an empty repository has been initialized under route projects my second repo. 

If I execute another command called git remote, it comes back as blank. The reason for that is that I've only initialized a local repository which has no connection to a central repository that sits either on Git hub or another server. 

Right now it's only available locally on my machine.

Now I'll step back out from this directory and go into my first repo with a CD command. Again, this is a repository that I created earlier and does have a connection to Git hub. Using the remote URI I'll then check it by using the get remote minus V command. Git tells me that it's set to git tutorials 101 my first repo.Git. Next I'm going to set this against her second repository.

I'll step into the new directory once more using the CD command.

In this case we're going to add this URL to the remote settings by using the command. Git remote add specifying a name and then passing in URI, the name that is typically used here is origin. So I'll stick with that. So again the full command with the URL should read Git remote at origin. Git at Github.com: Git tutorials 101/ My first repo.Git. This time when I execute the Git remote minus V command. I have this set up against the get tutorials 101 which sits up on Git hub. 

What I'm going to do next is use the Git pull command which will connect with the GIT hub server, and pull down all the changes from the repository. So on my local I now have all the changes, but when I check the directory it's blank. The reason for this is that I haven't set up a branch that matches with what I have on the server repository. 

Fortunately I can change that by performing the command. Git check out main. Which will set up a branch main on my local that tracks the branch main from the remote. And now when I check my folder using the LS command, it confirms that I have the read me test and test two files available on my local

---
