# MCQ Test Engine #
REST API Template and endpoints follows this [schema](https://jira-dowhile.atlassian.net/wiki/spaces/TGPT/pages/734134291/Relational+Database+Sample).
## Technologies ##
* Python (3.9)
* Django (4.1)
* Docker (20.10.14)
* Docker Compose (1.29.2)
* PostgreSQL (12.0)
* Makefile 

## Requirements ##
* For getting the application up and running
    * Makefile (<https://www.gnu.org/software/make/>).
    * Docker ([Installation](https://docs.docker.com/engine/installation/)).
    * Docker Compose ([Installation](https://docs.docker.com/compose/install/)).

* Notes for Windows users: Please install Git/Make for Windows.
    * Follow this [page](https://jira-dowhile.atlassian.net/wiki/spaces/TGPT/pages/389480487/Bash+Make+for+Windows#Option-3%3A-Use-Git-bash) for instructions.

* For development
    * Install `requirements.txt` file
## Quick Start ##
1. Clone the repository: `git clone git@bitbucket.org:dowhile-csab/templates-python.git`.
1. change directory to `cd `cd rest-api-template/`.
1. Generate .env file with: `make generate_env [development/production]` (defaults to development).
1. Fill the needed values in .env file (if you're in production environment).
1. Build docker image (services): `make build`.
1. Launch the system: `make up` (to start all services).
1. Go to browser (default: <http://127.0.0.1:8000/v1/core/>). 
`just defines needed steps to integrate with Django framework`
1. You can use Swagger by using (default: <http://127.0.0.1:8000/v1/core/doc/>). 
1. To shutdown: `make down` or `make down-v` (to remove volumes as well).

## Make Commands ##
[Makefile](Makefile) is available on the root directory to help running common CLI commands.
