# 2023 MSU REU Graph DB

This project is a docker-based web application to enhance analysis and mitigation, called Security System Plan Manager (SSPM).
A unique list of CVE/CWE's is generated with a static analysis tool, this project will produce a comprehensive list of attack paths present and security controls recommended for the system. SSPM can be used to know which NIST 800-53 Security Controls should be prioritized to efficiently protect the system.

## Getting Started

These instructions will get you a copy of SSPM up and running on your local machine. 

### Prerequisites

Docker
- Docker
- Docker Compose

### Installing

BRON is a graph database made by a research team at MIT that combines threat data from [MITRE ATT&CK](https://attack.mitre.org/), [CAPEC](https://capec.mitre.org/), [CWE](https://cwe.mitre.org/), [CVE](https://nvd.nist.gov), and a few others. The data types are linked with bi-directional edges. This graph was created to link and evaluate public threat and mitigation data for cyber hunting.

To deploy BRON on top of ArangoDB, clone the [BRON repository](https://github.com/ALFA-group/BRON) and run:
```
docker-compose up -d
```
The deployment starts in two containers:
- `brondb`: an ArangoDB server hosting the BRON graph and collections
- `bootstrap`: a container that build BRON and loads it into the graph database

It may take a few minutes for the bootstrap to finish. It will download and analyze the required datasets,
build BRON, and import it into the database. You can check its completion by monitoring the `bootstrap` container logs
```
docker logs -f bootstrap
```

To deploy SSPM on top of BRON, clone this repository and run:
```
docker-compose up -d
```
The deployment is in another two containers:
- `driver`: a container that collects the extra information and adds it into BRON
- `flask-frontend`: the front-end container to interface with the SSPM user interface

It may take a few minutes for the driver to finish. It will open the additional data within its filesystem,
add to BRON, and complete all collections needed for the program. You can check its completion by monitoring
the `driver` container logs
```
docker logs -f driver
```
## Working With System Security Plan Manager

These instructions will run through the use of SSPM and the produced results

### Prerequisites

Getting Started Completion
- All four containers must have been successfully ran
- `brondb` and `flask-frontend` must be currently running

### Beginning the Program

To access the SSPM start page, open a webbrowser and go to [localhost:5000](http://localhost:5000/)
```
http://localhost:5000/
```

The start page holds the upload function for the program.
The files that are uploaded here **MUST** be a json file formatted as follows:
 ```
[{
  "cve": "CVE-2022-22536"
},{
  "cve": "CVE-2021-36942"
}]
 ```
 ```
[{
  "cwe": "119"
},{
  "cwe": "787"
}]
 ```
 ```
[{
  "control": "CM-7"
},{
  "control": "SC-7"
}]
 ```

 The names of the files **MUST** be in the format
 - `vulnerabilities.json` - this file **MUST** be in the CVE **OR** CWE format
 - `controls.json` - this file **MUST** be in the Control format

 To start the program, click the `Test` button

 ### Reading the Results

The results are split into three sections:
- `View Connectivity Graph` - a graph showing the comprehensive connections of techniques and tactics available to the adversary in an attack
- `View Attack Paths Graph` - a network graph showing connected techniques that can be used in a sequence to achieve consecutive ATT&CK stages (tactics)
- `View Control Table` - a table of controls sorted by tactic and techniques that are shown top to bottom in order of recommended implementation

## Explaining the Project

This section will walk through the program, explaining the process from start to end

### Completing BRON

The program starts with the BRON database. As is, the database is missing information that must be added. The missing information includes:
- Controls
- Technique to Controls
- Tactic to Tactic
- Remove duplicate data in Tactic to Technique

### Querying the Database

The information needed to find all CVE/CWE's to Techniques, Tactics, and Controls is gathered from queries sent into the BRON database.

### The Connectivity Graph

This graph shows the comprehensive connections of techniques and tactics available to the adversary in an attack.
A tactic with many techniques shows that an adversary can use multiple strategies to complete that stage of an attack.

In the graph you will notice a red tactic, this is the tactic chosen by the algorithm explained in the next section.

### Using the Algorithm 

The algorithm implemented into the SSPM prioritizes tactics in order of easiest mitigation.
Mitigating this tactic breaks the attack path an attacker could use against your system.

The algorithm is a process of two sorts, Tactic and Technique
#### Tactic 
Tactic is sorted by the sumber of connections to other tactics.
As a tactic path is linear, the max number of connections a tactic can have is two.
- Low: No tactic connections
- Mid: One tactic connection
- High: Two tactic connections
#### Technique
Techniques are sorted by the number of connections to a single tactic.
If a tactic has one connection to a technique, the sort is value 1.
If a tactic has four connections to four different techniques, the sort value is 4.
A value of 1 is sorted higher than a value of 4

This is a fully sorted table for example
| Tactic     |  Technique    |
|------------|---------------|
| High       |  1, 4, 5, 7   |
| Mid        |    2, 3, 4    |
| Low        |  1, 3, 6, 7   |

### The Network Graph

This graph shows the different attack paths that are present in the system.
The techniques shown and connected can be used in sequence to achieve consecutive ATT&CK stages.
The edges within the graph represent the sequencial 'flow' an adversary could use to facilitate an attack on the system.

Disconnected tactics in the Connectivity Graph are ignored and will not be represented in the Network Graph.

## Built With

* [Arango DB](https://www.arangodb.com/) - The underlying database structure
* [BRON](https://github.com/ALFA-group/BRON) - The starting database
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - Web App Interface

## Authors

* **Aurora Duskin**
* **Noah Hassett**

See also the list of [contributors](https://github.com/na245/reu-2023-flask/contributors) who participated in this project.

## Acknowledgments

* National Science Foundation Award # 1947750

