# reu-2023-graph-db
A repository to house the 2023 REU Graph DB project

# Contained In The Project 
## BRON
<p>Our project builds on the existing graph database made by MIT. The database links Threat Tactics, Techniques, and Patterns with Defensive Weaknesses, Vulnerabilities and Affected Platform Configurations for Cyber Hunting. Threat data from MITRE ATT&CK, CAPEC, CWE, CVE, and so on are linked together in a graph called BRON.</p>
<p>Research Paper can be found here: https://arxiv.org/pdf/2010.00533.pdf</p>
<p>Project repository can be found here: https://github.com/ALFA-group/BRON#readme</p>

## Driver Container
### Contents
- driver.py
- get_json_from_db.py
- insert_control_data.py
- insert_tactic_path.py
- insert_tech_ctrl_edge.py
- nist800-53-r5-mappings2.json
- rm_dup_tac_tech.py
### Integration
<p>The files listed above all run in the driver container that will update the BRON database with new information, create new edges between existing information, and clean the database of any duplicate data that will hinder the speed of the queries.</p>

## Query Container
### Contents
- controls.json
- cve.json
- cwe-cve_to_techniques.py
- cwe.json
- tech_tac_graph.py
### Integration
<p>The above files consist of the program (cwe-cve_to_techniques.py, tech_tac_graph.py) and test data that can be used to run the program.</p>

# How The Project Works
## Database Completion
<p>In the driver container, we connect to the BRON database that has been already set up and mostly filled by following the steps from the BRON project repository (link above). Here we can add and modify collections within the database using python-arango. The information added into the database can be found in nist800-53-r5-mappings2.json.</p>

## Querying the Database
<p>In the query container, we use the complete information from the BRON database to find a comprehensive list of Techniques and Tactics from a given list of CVE/CWE's. This list of CVE/CWE's is a json file that will be provided to the program upon calling. Sample CVE/CWE json files have been provided.</p>
<p>A list of implemented controls will also be given at call time, test data provided. This list of implemented controls will be used to filter the tactics and techniques to eliminate mitigated tactics and techniques and remove them from the graph.</p>
<p>From this filtered list, we have made an interactive graph that will show all connected techniques and tactics that are vulnerable through a given system.</p>

## Reading the Graph
<p>The graph shown will include vulnerable tactics and techniques. Among them is a red node (Tactic), this is the default highest priority tactic. This node has been chosen by the algorithm as the most infuential node that would be the best to mitigate first.</p>

## Understanding the Algorithm
<p>The default algorithm implemented to prioritize influencial nodes is based upon two factors. Tactic to Tactic connectivity, and Tactic to Technique connectivity.</p>

### ***Tactic to Tactic***
<p>From the graph, we can find attack tactics that connect to other tactics to form an attack path. The amount of connections is directly influenced by the amount of CVE/CWE's detected in a system, and the amount of controls implemented in the system. The first sort of the algorithm is split into three categories, High, Medium, and Low. Depending on the amount of edges a tactic has to other tactics determines it's category. Due to the linear path of an attack, the maximum amount of tactic to tactic connections is two.</p>

- High (2 Tactic to Tactic edges)
- Medium (1 Tactic to Tactic edge)
- Low (No Tactic to Tactic edges)

### ***Tactic to Technique***
<p>After the Tactics have been categorized into High, Medium, and Low priority, the categories are individually sorted based on the amount of Tactic to Technique edges. The smaller the amount of these edges a Tactic has, the more prioritized that Tactic will be.</p>
<p>For example, a tactic of high priority that has 5 technique edges will be *less* important than a tactic of high priority that has 1 technique edge, by default. This is due to the amount of controls that would have to be implemented to mitigate that specific tactic. A single control mitigation would be prioritized over a several controls mitigation.</p>

# To Use The Program
## WORK IN PROGRESS - NO OFFICIAL DOCKER YET
## Docker
### Pre-requisites:
- Docker
- Docker Compose
- Running BRON Container (Instructions found at https://github.com/ALFA-group/BRON#readme)

To use this program ontop of BRON and ArangoDB, clone this repository and run:

    docker-compose up -d 

### The program starts in two containers:
- driver: This container will grant access to the arango database and create/manipulate the database for use. Will close after completion.
- reu-2023: This container holds the program needed to run queries, display graphs, and prioritize the returned information

## Getting Started
<p>Build the containers on localhost.</p>
Use this command after the containers have been built: 
    
    sudo docker exec –it reu-2023 /bin/bash
This will create a secure shell in the reu-2023 container.

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
<p>The docker container has no internet browser installed.</p>
To display the graph properly:

- on your local machine browse to localhost:8000 
- open graph.html
