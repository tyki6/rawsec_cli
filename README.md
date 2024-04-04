# rawsec_cli

[![tyki6](https://github.com/tyki6/rawsec_cli/workflows/Unit%20Test/badge.svg)](https://github.com/tyki6/rawsec_cli)
[![PyPI](https://img.shields.io/pypi/v/rawsec-cli)](https://pypi.org/project/rawsec-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rawsec-cli)](https://pypi.org/project/rawsec-cli/)
[![PyPI - Download](https://pepy.tech/badge/rawsec-cli)](https://pepy.tech/project/rawsec-cli)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/tyki6/rawsec_cli)](https://github.com/tyki6/rawsec_cli/releases)
[![Documentation Status](https://readthedocs.org/projects/rawsec_cli/badge/?version=latest)](https://rawsec_cli.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/tyki6/rawsec_cli)
[![docstr_coverage](./img/docstr_coverage_badge.svg)](https://github.com/HunterMcGushion/docstr_coverage.git)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/tyki6/rawsec_cli/main.svg)](https://results.pre-commit.ci/latest/github/tyki6/rawsec_cli/main)
[![codecov](https://codecov.io/gh/tyki6/rawsec_cli/branch/main/graph/badge.svg?token=YKclZIzF6Z)](https://codecov.io/gh/tyki6/rawsec_cli)
[![Updates](https://pyup.io/repos/github/tyki6/rawsec_cli/shield.svg)](https://pyup.io/repos/github/tyki6/rawsec_cli/)
[![Known Vulnerabilities](https://snyk.io/test/github/tyki6/rawsec_cli/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/tyki6/rawsec_cli?targetFile=requirements.txt)
[![Rawsec's CyberSecurity Inventory](https://inventory.raw.pm/img/badges/Rawsec-inventoried-FF5050_flat.svg)](https://inventory.raw.pm/tools.html#rawsec_cli)

# Introduction

[Rawsec's Cybersecurity](https://inventory.raw.pm/overview.html) Inventory is an inventory with 4 category(Tools, Resources, Ctf Platforms, OS).
This cli can search a project,list all projects by category, you can filter your research with option --help for more information.

# Table of Contents

- [Features](#features)
- [RoadMap](#roadmap)
- [Installation](#installation)
- [Usage](#usage)
- [Download](#download)
- [Contribute](#contribute)

# Features

- search a project
- list Tools, Resources, Ctf Platforms, OS
- filter by lang, price(Free or not), online or not, present on blackarch

# RoadMap

- [ ] submit command
- [X] Ci/CD
- [X] pypi package
- [X] github issue template
- [X] github action
- [X] better test for unit_test
- [X] docker
- [X] a better documentation

# Installation

To install rawsec-cli, simply use pip:

```bash
pip install rawsec-cli
```

To run rawsec-cli from a docker image, run:

```bash
docker run -it docker.pkg.github.com/tyki6/rawsec_cli/rawsec-cli:latest rawsec-cli --help
```

To install rawsec-cli, on git:

```bash
git clone https://github.com/tyki6/rawsec_cli.git
cd ./rawsec_cli
pip install -r requirements.txt
python setup.py install
```

To install rawsec-cli on BlackArch:

```bash
pacman -S rawsec-cli
```

[![Packaging status](https://repology.org/badge/vertical-allrepos/rawsec-cli.svg)](https://repology.org/project/rawsec-cli/versions)

# Usage

## Search

Search command can be used for searching Tools, Resources, Ctf Platforms, OS. All projects will be displayed on a tab .
If your research containing only 1 Result, rawsec will open a new brower tab redirect to source project or website if exist.

### Examples:

You can search by key word, you will see all projects with jwt in their description or name:

```bash
rawsec-cli search jwt
```

You can search a project, if the Search containing 1 result you will see result in console, and a tab is opened on your browser with redirect to website if informed or source:

```bash
rawsec-cli search myjwt
```

## List

You can list all projects by category.

### Category List

```
rawsec-cli list
output: 
    ctf
    os
    resources
    tools
```

### Tools

You can list all tools by tool's category.

#### Tools's Category

```
Category available:
        adversary_simulation
        binary_exploitation
        bug_bounty
        cloud
        code_analysis
        collaboration_and_report
        configuration_audit
        cracking
        crisis_management
        cryptography
        defensive
        digital_forensics
        hardware
        honeypot_and_decoy
        incident_response
        intentionally_vulnerable_applications
        networking
        osint_and_reconnaissance
        other
        plugins
        red_teaming
        reverse_engineering
        steganography
        system_exploitation
        threat_intelligence
        vulnerability_assessment
        web_application_exploitation
        wireless
```

#### Examples:

List all tools:

```bash
rawsec-cli list tools 
```

List all [binary exploitation tools](#toolss-category):

```bash
rawsec-cli list tools binary_exploitation
```

### Resources

You can list all tools by Resources's category.

#### Resources's Category

```
Category available:
        bug_bounty_pentest_and_disclosure_platforms
        challenges_platforms
        cve
        events
        information_news_blog
        knowledge_and_tools
        national_security_agencies_and_services
        non_english
        trainings_and_courses
        tutorials
        writeups_collections_and_challenges_source
```

#### Examples:

List all resources:

```bash
rawsec-cli list resources  
```

List all [events resources](#resourcess-category):

```bash
rawsec-cli list resources events
```

### CTF

You can list all ctf by ctf's category.

#### CTF's Category

```
Category available:
        attack_defense
        hybrid
        jeopardy
```

#### Examples:

List all ctf:

```bash
rawsec-cli list ctf  
```

List all [attack_defense ctf](#ctfs-category):

```bash
rawsec-cli list ctf attack_defense
```

### OS

You can list all tools by OS's category.

#### OS's Category

```
Category available:
        maintained
        no_more_maintained
        project_transferred
```

#### Examples:

List all os:

```bash
rawsec-cli list os  
```

List all [maintained os](#oss-category):

```bash
rawsec-cli list os maintained
```

## Options

## rawsec-cli

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -V, --version      | None           | show version.                                            |
| -h, --help         | None           | Show  help message and exit.                             |

## search

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -l, --lang         | language       | Filter by Language                                       |
| -p, --paid         | None           | Filter by Price, when price is equal to paid             |
| -f, --free         | None           | Filter by Price, when price is equal to free             |
| -on, --online      | None           | Filter by Online, when online is equal to true           |
| -off, --offline    | None           | Filter by Online, when online is equal to false          |
| -b, --blackarch    | None           | Filter by Blackarch when package is present on Blackarch |
| -o, --output       | list, json,csv,table | Output format                                            |
| -of, --output-file | file path      | Output file name if you want.                            |
| -h, --help         | None           | Show search help message and exit.                       |

## list

### tools

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -l, --lang         | language       | Filter by Language                                       |
| -p, --paid         | None           | Filter by Price, when price is equal to paid             |
| -f, --free         | None           | Filter by Price, when price is equal to free             |
| -on, --online      | None           | Filter by Online, when online is equal to true           |
| -off, --offline    | None           | Filter by Online, when online is equal to false          |
| -b, --blackarch    | None           | Filter by Blackarch when package is present on Blackarch |
| -o, --output       | list, json,csv,table | Output format                                            |
| -of, --output-file | file path      | Output file name if you want.                            |
| -h, --help         | None           | Show list tools help message and exit.                   |

### resources

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -p, --paid         | None           | Filter by Price, when price is equal to paid             |
| -f, --free         | None           | Filter by Price, when price is equal to free             |
| -o, --output       | list, json,csv,table | Output format                                            |
| -of, --output-file | file path      | Output file name if you want.                            |
| -h, --help         | None           | Show list resources help message and exit.               |

### ctf

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -l, --lang         | language       | Filter by Language                                       |
| -p, --paid         | None           | Filter by Price, when price is equal to paid             |
| -f, --free         | None           | Filter by Price, when price is equal to free             |
| -o, --output       | list, json,csv,table | Output format                                            |
| -of, --output-file | file path      | Output file name if you want.                            |
| -h, --help         | None           | Show list ctf help message and exit.                     |

### os

| command            | type           | description                                              |
| ------------------ | -------------- | ---------------------------------------------------------|
| -b, --base         | Text           | Filter by base(ex: Linux)                                |
| -o, --output       | list, json,csv,table | Output format                                            |
| -of, --output-file | file path      | Output file name if you want.                            |
| -h, --help         | None           | Show list ctf help message and exit.                     |

# Download

Check github releases. Latest is available at https://github.com/tyki6/rawsec_cli/releases/latest

# Thanks 

See [THANKS.md](https://github.com/tyki6/rawsec_cli/blob/master/THANKS.md).

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

See [CHANGES](https://github.com/tyki6/rawsec_cli/blob/master/CHANGELOG.md).
