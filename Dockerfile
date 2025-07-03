#FROM node:18-alpine
#
## Install Allure CLI
#RUN npm install -g allure-commandline --save-dev
#
#WORKDIR /app
#
#COPY package*.json ./
#RUN npm ci
#
#COPY . .
#
## Run tests and generate Allure results
#CMD ["sh", "-c", "npm test && allure generate --clean allure-results -o allure-report"]
