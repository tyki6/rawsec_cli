# Usage
## Search
Search command can be used for searching Tools, Resources, Ctf Platforms, OS. All projects will be displayed on a tab .
If your research containing only 1 Result, rawsec will open a new brower tab redirect to source project or website if exist.
### Examples:
You can search by key word, you will see all projects with jwt in their description or name:
```
rawsec search jwt
```

You can search a project, if the Search containing 1 result you will see result in console, and a tab is opened on your browser with redirect to website if informed or source:
```
rawsec search myjwt
```
## List
You can list all projects by category.
### Category List
```
rawsec list
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
        binary_exploitation
        bug_bounty
        code_analysis
        collaboration_report
        configuration_audit
        cracking
        cryptography
        digital_forensics
        honeypot_decoy
        incident_response
        intentionally_vulnerable_applications
        networking
        osint
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
```
rawsec list tools 
```

List all [binary exploitation tools](#toolss-category):
 ```
rawsec list tools binary_exploitation
```
### Resources
You can list all tools by Resources's category.

#### Resources's Category
```
Category available:
        bug_bounty_and_disclosure_platforms
        challenges_platforms
        cve
        events
        information
        knowledge_and_tools
        national_security_agencies_and_services
        non_english
        trainings_and_courses
        tutorials
        writeups_collections_and_challenges_source
```
#### Examples:
List all resources:
```
rawsec list resources  
```

List all [events resources](#resourcess-category):
 ```
rawsec list resources events
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
```
rawsec list ctf  
```

List all [attack_defense ctf](#ctfs-category):
 ```
rawsec list ctf attack_defense
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
```
rawsec list os  
```

List all [maintained os](#oss-category):
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
