import shlex,subprocess
from subprocess import call

def gitAdd(fileName, repoDir):
    cmd = 'git add ' + fileName
    pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir)
    pipe.wait()
    return
gitAdd('example.txt', '/usr/local/example_git')
