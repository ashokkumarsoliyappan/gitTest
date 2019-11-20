from git import Repo
import git

repoPath = R"C:\Users\z028605\AppData\Local\Programs\Python\Python37-32"
remoteCloneRepository = "https://github.com/ashokkumarsoliyappan/demo.git"
nameoftheRepo = "demo"
# repository = Repo.init(repoPath)
print("local repository initiated")
# git.Git(repoPath).clone(remoteCloneRepository)
repo = git.Repo("demo")
origin = repo.remote(name='origin')
# origin.pull()
repo.git.add(".")
# repo.git.commit('-m', 'two files')
repo.git.push()
exit()
origin.push()
exit()
exit()

# repo.git.checkout('master')
repo.git.add("automationPuml")
print(repoDirct)

repoDirct.remote().fetch()

