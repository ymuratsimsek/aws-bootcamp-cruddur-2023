# Week 2 — Distributed Tracing

##  Homework Challenges
   1. **Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend[HARD]:**
         
         I followed the [Honeycomb Doc](https://docs.honeycomb.io/getting-data-in/opentelemetry/browser-js/) to complete this task.

         - **HeatMap Durations by Url and Root Name:**         
            ![Instrumentation of Frontend](assets/week-2-Murat-HeatMap.png)

            ![Instrumentation of Frontend](assets/week-2-Murat-HeatMap2.png)         

         - **UI/Messages:**         
         ![Instrumentation of Frontend](assets/week-2-Murat-Latency-UI-messages.png)

         - **UI/Notifications:**         
         ![Instrumentation of Frontend](assets/week-2-Murat-Latency-UI-notifications.png)

         - **API/Messages:**         
         ![Instrumentation of Frontend](assets/week-2-Murat-Latency-Api-messages.png)

         - **API/Activities:**         
         ![Instrumentation of Frontend](assets/week-2-Murat-Latency-Api-activities.png)

   2. **Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span:**
   
         - I have added instrumentations to all services except my custom health check api.               
         
         - I have fixed the class name of data_show_activity to test the instrumentation I added.
        
            ```python
              data = ShowActivities.run(activity_uuid=activity_uuid)
            ```
         - **Honecomb Search Graph:**
         ![Honecomb Search Graph](assets/week-2-Murat-Span-Graph.png)
         
         - **CreateActivitiy Spans:**
         ![CreateActivitiy](assets/week-2-Murat-Span-CreateActivitiy.png)
         
         - **MessageGroups Spans:**
         ![MessageGroups](assets/week-2-Murat-Span-MessageGroups.png)
         
         - **Message Spans:**
          ![Message](assets/week-2-Murat-Span-Messages.png) 

         - **Notifications Spans:**
          ![Notifications](assets/week-2-Murat-Span-Notifications.png) 
         
         - **ShowActivities Spans:**
          ![ShowActivities](assets/week-2-Murat-Span-ShowActivities.png) 

         - **UserActivities Spans:**
          ![UserActivities](assets/week-2-Murat-Span-UserActivities.png) 
         
         
   3. **Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces:**

         - **Total Call Count of Frontend by Pages:**         
            ![Instrumentation of Frontend](assets/week-2-Murat-QueryFrontend1.png)

            ![Instrumentation of Frontend](assets/week-2-Murat-QueryFrontend2.png)
         
         - **Total Call Count of APIs by Api Url, Method and Http Status Code:**         
            ![Instrumentation of Backend](assets/week-2-Murat-QueryBackend1.png)

            ![Instrumentation of Backend](assets/week-2-Murat-QueryBackend2.png)
         
         - **Performance(%) of API Calls by API:**         
            ![Instrumentation of Backend](assets/week-2-Murat-QueryBackendPerformance1.png)

            ![Instrumentation of Backend](assets/week-2-Murat-QueryBackendPerformance2.png)
         
         - **HTTP Calls Longer Than 100ms:**         
            ![Instrumentation of All](assets/week-2-Murat-QueryPerfAll1.png)

            ![Instrumentation of All](assets/week-2-Murat-QueryPerfAll2.png)
         
   4. Cloud Career Homework Details
         - When I check the 5 job descriptions, I saw that all of them have common requeirements for this job such as:
         
             1. Relevant IT infrastructure & platform knowledge
             2. Deep understanding and problem solving ability
             3. Verbal & written communication skills
             4. Analytical and problem solving skills
             5. Understanding of CI/CD and associated tools (Jenkins, etc.)
             6. Knowledge of Cloud Platform
             7. Knowledge of Infrastructure as Code (IaC)
             8. Knowledge of monitoring & alerting systems
             9. Hands on development experience with scripting languages
             
             ![Instrumentation of All](assets/JourneyToThe-Cloud.png)


