# Micro servicio para miniaturas: Serverless Framework Template

## Descripción:
Micro servicio para generar las miniaturas del proyecto [Game Library](https://github.com/atomWeb/game-library), el cual es una librería personal de videojuegos que está desarrollado en Angular y con propósitos únicamente didácticos.

## Web:
[Game Library](https://nabugames.duckdns.org/)

## Tecnologías:
* El backend se vale del paradigma de la Infraestructura como código (IaC) utilizando para ello el framework [serverless framework](https://www.serverless.com/).

* Es un backend totalmente serverless utilizando las herramientas Cloud (S3, API Gateway y DynamoDB) de [AWS](https://aws.amazon.com/es/).

* Las funciones están escritas en Python 3.8.

## Importante:
install the following plugin:
https://github.com/UnitedIncome/serverless-python-requirements

Además en el equipo que hagas el deploy debe estar instalado docker.