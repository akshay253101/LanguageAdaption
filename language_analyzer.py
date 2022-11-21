import git
from typing import Dict, List, Set, Tuple
from pathlib import Path
import time
from linguist_wrapper import linguist

# Creates a repo object of given git and clones if not exist. 
def git_repo(url: str, branch: str, repo_path: str):
    if not (repo_path / ".git").is_dir(): repo = git.Repo.clone_from(url, repo_path)
    else: repo = git.Repo(repo_path)
    # Checkout to required branch
    repo.git.checkout(branch)
    return repo

# Provide list of dict containing language graph for each tags on given repo
def repo_languages() -> Tuple[Set[str], List[Dict[str,str]], str]:
    repo_url = input('Enter a valid git url:')
    branch_name = input('Enter the branch name:')
    repo_name = repo_url.split('.git')[0].split('/')[-1]
    repo_path = Path("./clone/" + repo_name)

    repo = git_repo(repo_url, branch_name, repo_path)
    # Sorts tag by version_code in ascending order
    tags = sorted(repo.tags, key= lambda t: list(map(str, t.name.split('v')[1].split('.'))))
    # Maintaining set of headers, we don't know what all languages are used in repo thought out the git-history 
    # so by looping over tags we update all language detected at that checkout. 
    headers: Set[str] = set()
    langs: List[Dict[str,str]] = [] 

    for tag in tags :
        repo.git.checkout(tag)
        # Tags might be created on a single day, that is why relying on commit date
        commit  = repo.head.commit
        date = time.strftime("%d %b %Y", time.gmtime(commit.committed_date))
        detected_langs = sorted(linguist(repo_path), key= lambda l: list(map(str, l[0])))
        metaDict = { "Tag": tag.name, "Date": date }
        lang_dict = dict(detected_langs)
        row_dict = metaDict | lang_dict
        langs.append(row_dict)
        headers.update(row_dict.keys())
        print(row_dict)
    
    return (headers, langs, repo_name)
