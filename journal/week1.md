# Week 1 — App Containerization

##  Homework Challenges
   1. **Run the dockerfile CMD as an external script:**
         
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/)

   2. **Push and tag a image to DockerHub (they have a free tier):**
        
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/)

   3. **Use multi-stage building for a Dockerfile build:**
         
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/)

   4. **Implement a healthcheck in the V3 Docker compose file:**
         
         We can check the health of the containers for example:
            - if the container has endpoints like nginx, we can check if the url/api works. 
              **I added a new simple healthcheck api into the backend-flask and checked it with docker compose health check**
            - if the container is a database, we can check the specific table that we determined. **I checked if the db is up&running**
         I have updated the docker-compose.yml with heatlhcheck settings.
         
         

         ```
         
         ```


          docker inspect --format='{{json .State.Health}}' docker-flask
          docker ps

         ![HealtChecker](assets/.png)
         
         [Docker Documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/)
   5. **Research best practices of Dockerfiles and attempt to implement it in your Dockerfile:**
         
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/)

   6. **Learn how to install Docker on your localmachine and get the same containers running outside of Gitpod / Codespaces:**
         
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/)
   
   7. **Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes:**
         
         [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
   
         ![EventBridge](assets/)
