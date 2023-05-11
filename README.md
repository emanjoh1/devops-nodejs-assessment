# node-js-getting-started

Here is the complete step by step documentation which will describe how the solution for the given problem has been implemented.


## Prerequisite configuration and setup for the assessment

```sh
$ Installation of the Docker-compose and docker tools on public cloud like AWS.
$ git clone https://github.com/heroku/node-js-getting-started.git #  clone your own fork. add code into this local repo

1. Set up a virtual machine on AWS cloud  and install Docker and Docker Compose utility.

2. Create a Dockerfile for the NodeJS application that will be deployed on Heroku.

3. Use the Docker build command to create a Docker image with the application: "docker build -t demo:latest ."

4. Run the Docker container using the following command: "docker run -it -d -p 5000:5000 demo:latest"

5. Check the browser to confirm that the NodeJS application has been successfully deployed using the Dockerfile.

6. Once the application is up and running, create a Docker Compose file to spin up all the necessary containers for the task, including Loki, Grafana, and Promtail.

7. Run the Docker Compose command "docker-compose up -d" and verify that all containers have been created using the command "docker ps".

After executing the "docker-compose up -d" command, all the created containers should be displayed by running the "docker ps" command.

8. Verify in the GUI if the application is up and running or not.

```

NodeJS app running on Heroku platform -  http://$IP:5000/

Your app should now be running on - 


Deployed Node JS application logs are available on - http://$IP:3000/



##### Documentation for the Dockerfile #####

The initial line of the Dockerfile mentions the source image that we're utilizing, which is the official Node.js runtime image based on Alpine Linux.

Next, we specify the working directory as /app and transfer the package.json and package-lock.json files to the container.

We then initiate the installation of production dependencies with npm install.

Following that, we copy the remaining code of the application into the container.

Subsequently, we configure the environmental variables for the application, such as the port that will be utilized for listening and the environment (production).

Finally, we expose port 5000 (the default application port) and start the application by executing the npm start command.

##### Documentation for the Docker-Compose #####

The docker-compose file includes four services: nodejs, promtail, loki, and grafana. The nodejs service is built using the Dockerfile from earlier and is configured to run in the production environment on port 5000. The logging for the application is set up to send logs to Loki.

The promtail service uses the official Grafana Promtail image and mounts a local directory with Promtail configuration. The loki service uses the official Grafana Loki image and exposes port 3100 for external access. The grafana service uses the official Grafana image and exposes port 3000 for external access. Environment variables are set for the initial admin user and password.

All services are connected to the monitoring network for communication between each other. The docker-compose file sets up a complete monitoring stack with Loki, Grafana, Promtail, and the NodeJS application. Promtail collects logs from the application and sends them to Loki for storage and querying, while Grafana provides a dashboard for visualizing and analyzing the logs.

The docker-compose file has the following sections:

version: This specifies the version of Docker Compose being used.

services: This top-level section defines the services in the application.

nodejs-app: This service builds a Docker image from the current directory (.) and exposes port 5000 on the host machine. Labels are added to the container for log collection using Promtail. The logging section specifies that logs should be sent to Loki using the gelf driver.

grafana: This service uses an official Grafana image and exposes port 3000 on the host machine. It mounts a configuration file for data sources and sets environment variables for anonymous authentication. It is also attached to the app network.

loki: This service uses an official Loki image and exposes port 3100 on the host machine. It sets the command to use a local configuration file.

promtail: This service uses an official Promtail image and attaches to the loki service. It mounts configuration files for Promtail and Docker, as well as the Docker socket, to read container logs. It also sets the command to use a local configuration file.

networks: This top-level section defines the networks used by the application. The app network is used by all services and is created with the specified name.



###Python Coding Problem for wordy Numbers ###

Number Conversion Script
This Python script prints numbers from 0 to 100 and converts every tenth number to its wordy version.

Function
convert_to_word(num) function is defined to convert the tenth numbers to its wordy version.

Main Code
In the main code block, a for loop is used to iterate over the numbers from 0 to 100. If the current number is a multiple of 10, the convert_to_word(num) function is called to convert the number into its wordy version and print it. Otherwise, the number is simply printed.


## Output of the task:- 

![image](https://github.com/emanjoh1/devops-nodejs-assessment/assets/112668324/46cdae45-dc0b-48fe-a408-62ae7ecd4acf)


## Reference Documentation

- [Best Practices for writing dockerfile](https://devcenter.heroku.com/articles/node-websocketshttps://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Best Practices for DOCKER Compose](https://docs.docker.com/develop/dev-best-practices/)
