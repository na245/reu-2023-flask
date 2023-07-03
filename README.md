# reu-2023-graph-db
A repository to house the 2023 REU Graph DB project

## BRON
Our project builds on the existing graph database made by MIT. The database links Threat Tactics, Techniques, and Patterns with Defensive Weaknesses, Vulnerabilities and Affected Platform Configurations for Cyber Hunting. Threat data from MITRE ATT&CK, CAPEC, CWE, CVE, and so on are linked together in a graph called BRON.\
Research Paper can be found here: https://arxiv.org/pdf/2010.00533.pdf \
Project repository can be found here: https://github.com/ALFA-group/BRON#readme

## WORK IN PROGRESS - NO OFFICIAL DOCKER YET
## Docker
### Pre-requisites:
- Docker
- Docker Compose

To use this program ontop of BRON and ArangoDB, clone this repository and run:

    docker-compose up -d 

### The program starts in two containers:
- Driver: This container will grant access to the arango database and create/manipulate the database for use. Will close after completion.
- REU-2023: This container holds the program needed to run queries, display graphs, and prioritize the returned information

## Getting Started
Build the containers on localhost.\
Use this command after the containers have been built: 
    
    sudo docker exec –it REU-2023 /bin/bash
This will create a secure shell in the REU-2023 container.

### This container is equiped with test data:
- controls.json - a json file containing the implemented controls for a given system
- cve.json - a short json file containing reported cve's for a given system
- cves.json - a long json file containing many reported cve's for a given system
- cwe.json - a short json file containing reported cwe's for a given system

### To run the program

    usage: python3 cwe-cve_to_techniques.py [cve/cwe.json] [controls.json]
- [cve/cwe.json] - a json file containing cve's OR cwe's. File MUST be of only one type
- [controls.json] - a json file containing the controls implemented into the system

### To run the program with the given test data: 

    python3 cwe-cve_to_techniques.py cves.json controls.json

## Notes on the Program
The docker container has no internet browser installed.
To display the graph properly:
- on your local machine browse to localhost:8000 
- open graph.html
