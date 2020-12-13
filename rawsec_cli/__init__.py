"""Version"""
from git import Repo

repo_path = ""
repo = Repo(repo_path)
__version__ = "1.0.0"
__commit__ = str(repo.commit())
