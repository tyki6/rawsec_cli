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
