## Aplicação Web na Nuvem com Docker Compose

Esta é uma aplicação web simples desenvolvida com Flask e conectada a um banco de dados PostgreSQL. A aplicação e o banco de dados são orquestrados utilizando Docker Compose e executados em uma instância EC2 na AWS.

## Descrição

A aplicação Flask realiza consultas a um banco de dados PostgreSQL e exibe os resultados na página inicial. 
O projeto utiliza Docker Compose para gerenciar dois serviços:
* **web:** Serviço que executa a aplicação Flask.
* **db:** Serviço que executa o banco de dados PostgreSQL.


## Estrutura do Projeto

├── app.py               

├── Dockerfile    

├── docker-compose.yml     

├── requirements.txt       

└── README.md              


## Tecnologias Utilizadas

**Flask** - Microframework para a aplicação web.

**PostgreSQL** - Banco de dados relacional utilizado pela aplicação.

**Docker** - Ferramenta de contêinerização usada para empacotar a aplicação.

**Docker** Compose - Orquestrador para gerenciar múltiplos containers Docker.

**AWS EC2** - Instância de máquina virtual onde a aplicação é executada na nuvem.
