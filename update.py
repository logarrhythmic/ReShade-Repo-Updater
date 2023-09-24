import os, re, shutil;

github_url = re.compile(r"https://(?:www\.)?github\.com/(.*?)/(.*?)(?:\.git)")
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
clones = 0
pulls = 0
errors = 0
checked_repos = 0
listfile = open("repolist.txt", "r")
for line in listfile.readlines():
    match = github_url.match(line)
    link = match.group(0)
    if match:
        checked_repos += 1
        author = match.group(1)
        repository = match.group(2)
        target_dir = f"{author}_{repository}"
        repo_dir = f"repos\\{target_dir}"
        print(f"{author}/{repository} => {repo_dir}")
        if os.path.exists(repo_dir):
            print("Updating repository with git pull...")
            pull_res = os.system(f"git -C {repo_dir} pull")
            if pull_res == 0:
                pulls += 1
            else:
                errors += 1
        else:
            print("Getting copy of new repository with git clone...")
            clone_res = os.system(f"git clone --depth=1 {link} {repo_dir}")
            if clone_res == 0:
                clones += 1
            else:
                errors += 1
        for (dirpath, dirnames, filenames) in os.walk(repo_dir):
            if "Shaders" in dirnames:
                shutil.copytree(f"{dirpath}\\Shaders", f"{dname}\\Shaders\\{target_dir}", dirs_exist_ok=True)
            if "ComputeShaders" in dirnames:
                shutil.copytree(f"{dirpath}\\ComputeShaders", f"{dname}\\Shaders\\{target_dir}", dirs_exist_ok=True)
            if "Textures" in dirnames:
                shutil.copytree(f"{dirpath}\\Textures", f"{dname}\\Textures\\{target_dir}", dirs_exist_ok=True)
    else:
        print(f"{link} is not a valid github url")
    print("")
    
listfile.close()
print(f"Checked {checked_repos} repositories.\nAdded {clones} new repos and checked updates for {pulls}.\n{errors} operations failed.")
input("Press Enter to close this window.")