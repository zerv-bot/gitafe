# GITAFE - Time is money.
# Author : Harvey Wu

import os
import sys
import yaml

VERSION = '0.1'
CONFIG_VERSION = '0.0'
CONFIG_PATH = 'config.yaml'
GIT_BRANCH = 'main'

def main():
    try:
        with open(CONFIG_PATH, 'r') as f:
            data = yaml.safe_load(f)
            CONFIG_VERSION = str(data.get('version'))
            GIT_BRANCH = str(data.get('branch'))
    except:
        print("config.yaml NOT FOUND")

    if sys.argv[1] == '-v' or sys.argv[1] == 'version':
        print("GITAFE - Time is money. [GITHUB VERSION]")
        print("version "+VERSION)
        print("config version "+CONFIG_VERSION)
        os.system('git --version')
    elif sys.argv[1] == '-h' or sys.argv[1] == 'help':
        print("GITAFE - Time is money.")
        print("usage: gitafe <argument>")
        print("             -h, help      : print help message")
        print("             -v, version   : print the GITAFE version")
        print("       gitafe <-d, down> <repo owner/repo name>")
        print("       gitafe <-u, up> <file or directory> <commit title> <commit description>")
    elif sys.argv[1] == '-d' or sys.argv[1] == 'down':
        os.system('git clone https://' + str(data.get('git_platform'))+'/'+sys.argv[2]+'.git')
    elif sys.argv[1] == '-u' or sys.argv[1] == 'up':
        try:
            os.system('git add '+sys.argv[2])
            os.system('git commit -m '+sys.argv[3]+' -m '+sys.argv[4])
            os.system('git push origin '+GIT_BRANCH)
        except:
            os.system('git push origin '+GIT_BRANCH)
    else:
        print("unknown command '"+sys.argv[1]+"'")


if __name__ == '__main__':
    main()
