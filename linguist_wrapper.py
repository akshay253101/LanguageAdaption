import subprocess
import shutil
import ghlinguist as ghl
from typing import  List, Tuple, Union
from pathlib import Path

EXE = shutil.which("github-linguist")
GIT = shutil.which("git")

# Copy pasted from ghlinguist to make function return lang name instead of loc
def linguist(path: Path, rtype: bool = False) -> Union[str, List[Tuple[str, str]]]:
    """runs Github Linguist Ruby script"""

    if not EXE:
        raise ImportError("GitHub Linguist not found, did you install it per README?")

    path = Path(path).expanduser()

    if not ghl.checkrepo(path):
        return None

    ret = subprocess.check_output([EXE, str(path)], universal_newlines=True).split("\n")

    # %% parse percentage
    lpct = []

    for line in ret:
        L = line.split()
        if not L:  # EOF
            break
        lpct.append((L[2], L[0][:-1])) # The only change made in api is to return lang name

    if rtype:
        return lpct[0][0]

    return lpct