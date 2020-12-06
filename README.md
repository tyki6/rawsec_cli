# rawsec_cli

# Introduction
[Rawsec's Cybersecurity](https://inventory.raw.pm/overview.html) Inventory is an inventory with 4 category(Tools, Resources, Ctf Platforms, OS).
This cli can search a project, submit a project, list all projects by category, you can filter your research with option --help for more information.
# Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Download](#download)
- [Contribute](#contribute)

# Features
- search a project
- list Tools, Resources, Ctf Platforms, OS
- submit a project
- filter by lang, price(Free or not), online or not, present on blackarch
# Installation
To install rawsec, simply use setup.py:
```
python setup.py install
```
To install rawsec, on git:
```
git clone https://github.com/mBouamama/rawsec_cli.git
cd ./rawsec_cli
pip install -r requirements.txt
python rawsec_cli/cli/cli.py --help
```
# Usage
## Search
You can search by key word:
```
rawsec search jwt
```
You can see all project with jwt in their description or name

You can search a project:
```
rawsec search myjwt
```
If just 1 result you see result in console, and a tab is open on your browser with url = website if informed else url = source
## List
You can list all projects.
### Tools
```
rawsec list tools 
```
 You can filter by category like:
 ```
rawsec list tools binary_exploitation
```
### Resources
```
rawsec list resources  
```
 You can filter by category like:
 ```
rawsec list resources events
```
### CTF
```
rawsec list ctf  
```
 You can filter by category like:
 ```
rawsec list ctf attack_defense
```
### OS
```
rawsec list os  
```
 You can filter by category like:
 ```
rawsec list os maintained
```

## Option
```
rawsec search --help
rawsec list ctf --help
rawsec list os --help
rawsec list resources --help
rawsec list tools --help
```
# Download
Check github releases. Latest is available at https://github.com/mBouamama/rawsec_cli/releases/latest
# Contribute
- Fork this repository or clone it
- Create a new branch (feature, hotfix, etc...)
- Make necessary changes and commit those changes
- Check lint with `make lint`
- Check unit_test with `make test`
- Send Pull Request
I will check as Soon as Possible.

# Change log

The log's become rather long. It moved to its own file.

See [CHANGES](https://github.com/mBouamama/rawsec_cli/blob/master/CHANGELOG.md).
