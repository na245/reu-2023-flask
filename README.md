# 2023 MSU REU Graph DB

This project is a docker based web application to enhance analysis and mitigation, called Security System Plan Manager (SSPM).
A unique list of CVE/CWE's are generated with a static analysis tool, this project will produce a comprehensive list of attack paths and controls available in the system.

## Getting Started

These instructions will get you a copy of SSPM up and running on your local machine. 

### Prerequisites

Docker
- Docker
- Docker Compose

### Installing

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

It may take a few minutes for the driver to finish. It will open the additional data whithin its filesystem,
add to BRON, and complete all collections needed for the program. You can check its completion by monitoring
the `driver` container logs
```
docker logs -f driver
```
### Working With System Security Plan Manager

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
The files that are uploaded here must be a json file formatted as follows:
 ```
 [{
  "cve": "CVE-2022-22536"
},{
  "cve": "CVE-2021-36942"
}]
 ```
 ```
 [{
  "control": "CM-7"
},{
  "control": "SC-7"
}]
 ```

 The names of the files MUST be in the format
 - `cve.json`
 - `control.json`

 To start the program, click the `Test` button

 ### Reading the Results

The results are split into three sections:
- `View Connectivity Graph` - a graph showing the comprehensive connections of techniques and tactics available to the adversary in an attack
- `View Attack Paths Graph` - a network graph showing connected techniques that can be used in a sequence to achieve consecutive ATT&CK stages (tactics)
- `View Control Table` - a table of controls sorted by tactic and techniques that are shown top to bottom in order of recommended implementation

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

