# Week 0 — Billing and Architecture

## Required Homework

   1. **Conceptual Diagram:**

         I'm sorry I couldn't find a pen and draw on a napkin.
         [Lucid Shared Link](https://lucid.app/lucidchart/caf757ed-d7ec-4e83-aee7-c3b569b8f615/edit?viewport_loc=-13%2C9%2C1579%2C833%2C0_0&invitationId=inv_2659dc32-9e1e-429d-a0e0-54c406de6f68)

         ![Conceptual Diagram](assets/week-0-Murat-Conceptual_Diagram.png)

   2. **Logical Architectual Diagram:**
         I wanted to create High Available architecture but Free Lucid has limitations, I got this limitation error while adding more details. 
         
         ![Lucid Error](assets/week-0-Murat-Limitation_Lucid.png)         
         
         That's why I could not connect the each component for the second availability zone.
         
         [Lucid Shared Link](https://lucid.app/lucidchart/8296b0fe-7dd7-48f4-9077-c5b8b75e8c3c/edit?viewport_loc=-1339%2C790%2C3790%2C2001%2C0_0&invitationId=inv_09e2f46c-56a6-49b2-a07e-badf17890c8a)
         
         ![Logical Diagram](assets/week-0-Murat-Lucid_Logical_Diagram.jpeg)

   3. **Create an Admin User:**

         ![Admin User](assets/week-0-Murat-Admin_User.png)
   
   4. **Use CloudShell**

         ![Use CloudShell](assets/week-0-Murat-Cloudshell.png)
   
   5. **Generate AWS Credentials:**
   
         ![AWS CLI Credentials](assets/week-0-Murat-Generate_AWS_Credentials.png)
   
   6. **Installed AWS CLI:**
   
         ![Installed AWS CLI](assets/week-0-Murat-Installed_AWS_CLI.png)
            
   7. **Create a Billing Alarm:**
  
         ![Billing Alarm](assets/week-0-Murat-Billing_Alarm.png)

         ![Cloudwatch Alarm](assets/week-0-Murat-CloudWatch_Alarm.png)
         
   8. **Create a Budget:**

         ![Create a Budget](assets/week-0-Murat-Create_Budget0.png)
         
         ![Create a Budget](assets/week-0-Murat-Create_Budget1.png)
         
         ![Create a Budget](assets/week-0-Murat-CloudWatch_Alarm.png)

##  Homework Challenges
   1. **Destroy your root account credentials, Set MFA, IAM role:**
   
         ![Root Account MFA](assets/week-0-Murat-Root_Account_Mfa.png)

   
   2. **Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue:**
      
      [AWS Documentation](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)

         ![EventBridge](assets/week-0-Murat-Eventbridge_SNS_Alarm0.png)

         ![EventBridge](assets/week-0-Murat-Eventbridge_SNS_Alarm1.png)

         ![EventBridge](assets/week-0-Murat-Eventbridge_SNS_Alarm3.png)
   
   3. **Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts**
     
      [AWS Documentation](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/)

      [Lucid Shared Link](https://lucid.app/lucidchart/a4e64e1e-dc13-4ef1-aa9c-b40493e18b7e/edit?viewport_loc=676%2C-68%2C2438%2C1287%2C0_0&invitationId=inv_4db324de-7cc1-4080-83b7-b0bb2ab36c75)
      
      ![EventBridge](assets/week-0-Murat-CI_CD_Logical_Pipeline.jpeg)
      
   4. **Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility**

      For example AWS WAF, we need to use a specific port to listen and protect the system, WAF has some limitations like ports and filters. To do that, we have to pick another solution like F5.
      
      [AWS Documentation](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

   5. **Open a support ticket and request a service limit**
      
         ![Service Limit](assets/week-0-Murat-ServiceLimit0.png)

         ![Service Limit](assets/week-0-Murat-ServiceLimit1.png)
      
