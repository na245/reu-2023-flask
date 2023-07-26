# 2023 MSU REU Graph DB

This project is a docker based web application to enhance analysis and mitigation called Security System Plan Manager (SSPM).
A unique list of CVE/CWE's are generated with a static analysis tool, this project will produce a comprehensive list of attack paths and controls available in the system.

## Getting Started

These instructions will get you a copy of SSPM up and running on your local machine. 
See deployment for notes on how to deploy SSPM on a live system.

### Prerequisites

Docker
- Docker
- Docker Compose

### Installing

To deploy BRON on top of ArangoDB, clone the BRON repository and run:
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

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

