# LanguageAdaption
Linguist based language detector, shows language graph for each git tag to detect the overall project growth in terms of language adaption

## Install

Ruby is required for Linguist:

* Windows: Windows Subsystem for Linux is recommended.
* Linux: see Notes section at bottom of this README
* MacOS / Linux Homebrew: `brew install ruby`

1. Install Linguist as usual:

   ```sh
   gem install github-linguist
   ```
2. Install this Python wrapper:

   ```sh
   pip install ghlinguist
   ```
   
## Example
 
1. Execute language-detector.py
2. Enter git url and branch name in terminal
3. Each tag data will be printed on terminal. 
4. After successful attempt repo_name.png and repon_name.svg can be found at reports dir.

![alt text](https://github.com/akshay253101/LanguageAdaption/blob/main/reports/android-language.png)

## Uses
[Scivision Linguist Python](https://github.com/scivision/linguist-python) - Pure Python command-line wrapper of Ruby-based Github Linguist. 
