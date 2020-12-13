"""Version"""
__version__ = "1.0.0"
try:
    from git import Repo

    repo_path = ""
    repo = Repo(repo_path)
    __commit__ = str(repo.commit())
except:
    pass
