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
         
      - I didnot use Multi-stage build for backend app because it did not change the size of image too much. Instead I applied the best practice "rm -rf /var/lib/apt/lists/*" to its docker file to reduce the size of the image.

         
      - By using Multi-stage build, I decreased the size of frontend app 1.15Gb to 129Mb.
        
        To do that:
         1. I used nginx to serve the frontend app.
            
      - You can see from the screenshots below; The frontend app can talk to backend app to show data. 
         
         To do that: 
         
         1. I added "REACT_APP_BACKEND_URL" as env to the docker file of frontend app. So, React can call the backend app without getting "undefined" error.
         2. I also added "networks" for both application settings in docker compose file. So, I can make a reverse proxy on Nginx to send the UI request to Backend.
         
              [Frontend Docker File](https://github.com/ymuratsimsek/aws-bootcamp-cruddur-2023/blob/main/frontend-react-js/Dockerfile)
         
              [Frontend Nginx File](https://github.com/ymuratsimsek/aws-bootcamp-cruddur-2023/blob/main/frontend-react-js/nginx.conf)

              [Docker Compose File](https://github.com/ymuratsimsek/aws-bootcamp-cruddur-2023/blob/main/docker-compose.yml)

              **Image Size Before Multi-Stage Building**
              ![](assets/week-1-Murat-MultiStage1.png)
         
              **Image Size After Multi-Stage Building**         
              ![](assets/week-1-Murat-MultiStage2.png)
         
              **Reverse Proxy and Running Containers**
              ![](assets/week-1-Murat-MultiStage3.png)

              **Frontend Talks to Backend Successfully via Reverse Proxy**  
              ![](assets/week-1-Murat-MultiStage4.png)
         
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
         
         [BestPractices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
         
         I have checked the best practices and applied the "removing /var/lib/apt/lists" and multi-stage building to reduce the image size.

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

               ![](assets/week-1-Murat-LaunchEc2Docker3.png)

            3. I created "cli" folder at Github under "aws" folder and added all cli scripts.
            
               [CLI Scripts](https://github.com/ymuratsimsek/aws-bootcamp-cruddur-2023/tree/main/aws/cli)

               ![](assets/week-1-Murat-LaunchEc2Docker9.png)
            
            4. I installed Docker and started the backend application (pulling the tagged image from DockerHub) during launch of EC2 instance by executing the script.sh at userdata               
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

               ![](assets/week-1-Murat-LaunchEc2Docker4.png)
               
               ![](assets/week-1-Murat-LaunchEc2Docker5.png)

               ![](assets/week-1-Murat-LaunchEc2Docker6.png)
               
            5. In the end, I could reach the backend api from the browser seen in the screenshot
            
               ![](assets/week-1-Murat-LaunchEc2Docker7.png)
               
            6. To verify what I did, I also logged in the EC2 instance from "EC2 Connect" and checked Docker process, image and Docker version.

               ![](assets/week-1-Murat-LaunchEc2Docker8.png)

