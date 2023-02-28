# Week 1 — App Containerization

##  Homework Challenges
   1. **Run the dockerfile CMD as an external script:**
       
         ![RunCMDasScript](assets/week-1-Murat-RunCMDasScript.png)

   2. **Push and tag a image to DockerHub (they have a free tier):**
   
         - **Build with Tag:**
         ![DockerHub1](assets/week-1-Murat-Push1.png)
         
         - **List Images:**
         ![DockerHub2](assets/week-1-Murat-Push2.png)
         
         - **Push Images to Dockerhub:**
         ![DockerHub3](assets/week-1-Murat-Push3.png)
         
         - [Docker Hub Url](https://hub.docker.com/repository/docker/ymsimsek/backend_flask/general)
         
            ![DockerHub4](assets/week-1-Murat-Push4.png) 
         
   3. **Use multi-stage building for a Dockerfile build:**
         
         To keep the size of docker images small as:
             1. Smaller images are pulled/pushed faster
             2. Smaller images take up less disk space
             The simplest case is a compiler image and a runtime image: the compiler image compiles the code, and the runtime image copies the resulting artifact over. The runtime image never includes the compiler layer, and can therefore be smaller in size.      
         
         
         []()

         ![](assets/)

   4. **Implement a healthcheck in the V3 Docker compose file:**
                  
         - I have implemented the healthchecks by using docker compose file. Such as:
         
            [Docker Documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/)
            ```shell
             healthcheck:
             test: ["CMD", "curl", "-f", "http://localhost:4567/api/health"]
             interval: 5s
             timeout: 10s
             retries: 3
             start_period: 40s
            ```
         - To make a `curl` request, I had to update the backed-end docker file to install the curl. 
             ```shell
             apt-get install -y curl
             ```
         - I developed a new simple healthcheck api for the backend-flask and used it with docker compose health check settings
              ```python
              @app.route("/api/health", methods=['GET'])
              ```
              ![HealtChecker](assets/week-1-Murat-NewHealthCheckApi.png)

         - As seen in the screenshot, I can monitor the statuses of the backend, frontend and PostgreSQL containers.
             
              - I tried to make the health checker of Dynamodb healthy but I could not. I spent too much time thats why I did not create custom docker image for dynamodb to make a custom health check.
              
              ![HealtChecker](assets/week-1-Murat-DockerHealthCheckResult.png)
                 
         - How can we check if the containers are healtly?
            ```
            docker ps
            ```
         - How can we check the logs of health checker?
           ```
            docker inspect --format='{{json .State.Health}}' <container id>
            ```
         
   5. **Research best practices of Dockerfiles and attempt to implement it in your Dockerfile:**
         
         [BestPractices](Best practices for writing Dockerfiles)

         ![](assets/)

   6. **Learn how to install Docker on your localmachine and get the same containers running outside of Gitpod / Codespaces:**
         
         - I have installed Grafana, Prometheus, Node Exporter, Grok Exporter and Push gateway for my local Observability&Monitoring.

           ![Local Docker Running](assets/week-1-Murat-LocalDocker.png)
           
           ![Local Docker Running](assets/week-1-Murat-LocalDocker4.png)
         
           ![Local Docker Output](assets/week-1-Murat-LocalDocker3.png)
         
           ![Local Docker Output](assets/week-1-Murat-LocalDocker2.png)
   
   7. **Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes:**
         
         - I installed and configure EC2 and docker via AWS CLI
            1. I created security group via AWS CLI
   
               ![](assets/week-1-Murat-LaunchEc2Docker1.png)
               ![](assets/week-1-Murat-LaunchEc2Docker2.png)

            2. I authorized security group ingress via AWS CLI

               ![](assets/week-1-Murat-LaunchEc2Docker2.png)

            3. I created "cli" folder at Github under "aws" folder and added all cli scripts.
            
               [CLI Scripts](https://github.com/ymuratsimsek/aws-bootcamp-cruddur-2023/tree/main/aws/cli)

               ![](assets/week-1-Murat-LaunchEc2Docker9.png)
            
            4. I installed Docker and started the backend application (pulling the image from DockerHub) during launch of EC2 instance by executing the script at userdata               
                ```bash
                   #!/bin/sh
                   export PATH=/usr/local/bin:$PATH;
                   yum update
                   yum install docker -y
                   sudo usermod -a -G docker ec2-user
                   sudo systemctl enable docker.service
                   sudo systemctl start docker.service
                   sudo docker pull ymsimsek/backend_flask:v1
                   sudo docker run --rm -p 4567:4567 -e FRONTEND_URL='*' -e BACKEND_URL='*' -d ymsimsek/backend_flask:v1
                ```

            3. I created EC2 security group ingress via AWS CLI
            3. I created EC2 security group ingress via AWS CLI
            3. I created EC2 security group ingress via AWS CLI


