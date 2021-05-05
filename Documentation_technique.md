## Docker-compose :

* Déploiement:

Lancez le terminal, place-vous à la racine du dossier du projet et saisir la comande suivante:

```bash
docker-compose up
```

Une fois les deux containers lancés. Pour lancer l'api, il suffit de saisir cette adresse dans le navigateur : http://127.0.0.1:8081/

Pour lancer la page web contenant le chatbot il faudrait saisir cette adresse dans le navigateur: http://127.0.0.1:8080/

* Le fichier Docker-compose:

```bash
version: "3.3"

services:
    api:
        image: api:1.0
        build:
            context: ./backend/app
            dockerfile: Dockerfile
        restart: unless-stopped
        container_name: api
        ports:
            - 8081:8081

    vue:
        image: vue:1.0
        build:
            context: ./frontend
            dockerfile: Dockerfile
        restart: unless-stopped
        container_name: vue
        ports:
            - 8080:8080
```
Le docker-compose créé deux images sur Docker.
La première, api, contien l'API du Back-end, et la deuxième,Vue, cotient le front-end.

* Dépendances:
Le fichier Requirements.txt contient les librairies et modules utils.
```bash
    fastapi
    uvicorn
    motor
    dnspython
    numpy
    nltk
    aiofiles
```