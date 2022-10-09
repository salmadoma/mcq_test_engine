# MCQ Test Engine #

## System Description ##

Our system can support the following scenario

● Student can enroll in exam by entering his basic info and choose the topic
he wants to take the exam for, and he should receive all question in this
topic

● The question and their choices should be shuffled every time I enroll into
an exam, which means every time I enroll I get the questions in different
order and the choices of each question in a different order.

● When a student sends the answers to the MCQ service which marks whether it is correct or not and sends it to the scoring service
without calculating the score and scoring service should calculate the
score.

## Technologies ##
* Python (3.9)
* Django (4.1)
* Docker (20.10.14)
* Docker Compose (1.29.2)
* MongoDB
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
1. Clone the repository: `git clone https://github.com/salmadoma/mcq_test_engine.git`.
1. change directory to `cd mcq_test_engine/`.
1. Generate .env file with: `make generate_env [development/production]` (defaults to development).
1. Fill the needed values in .env file (if you're in production environment).
1. Launch the system: `make run` (to start all services).
1. Go to browser (default: <http://127.0.0.1:8000/v1/core/>). 
`just defines needed steps to integrate with Django framework`
1. You can use Swagger by using (default: <http://127.0.0.1:8000/v1/core/doc/>). 
1. To shut down: `make down`  (to remove volumes as well).

## Make Commands ##
[Makefile](Makefile) is available on the root directory to help running common CLI commands.

