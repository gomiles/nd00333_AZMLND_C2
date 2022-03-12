 # Project Overview
 
In this Udacity project the goal was to learn how to operationalize machine learning in the Azure cloud.
Steps completed:
 - Train a Model (AutoML)
 - Deploy a Model (Rest endpoint)
 - Use the Model (Consume rest endpoints via HTTPS)
 - Automate the Process (Create pipeline + publish)
 - Use Automation (Trigger pipeline via HTTPS)

 # Architectual Diagram
 ![image](https://user-images.githubusercontent.com/56161454/157675813-decd84bc-4867-4813-81a7-c6b283c92795.png)

 # Improvements
  - Pipeline Parameter
    - A new run of the pipeline makes only sense if something new needs to be processed. This could be the trainingdata used to train the model. Or different pipeline parameters.
  - Automatic Model Deployment
    - The next step in automation would be to automatically deploy the best model of a pipeline run.

 # Key Steps
 ## Deploy Model
 ### Register Dataset
 The first step for any machine learning project is to make the data accessible. In the case of Azure this is done via datasets:
 ![image](https://user-images.githubusercontent.com/56161454/157677786-de087cd6-1273-49de-a8a7-4a72ab70c751.png)
 ### Train Model
 A lot of work can go into training a ML model and various options are available. For this project the training of the model is not the relevent part. The easiest way to train a model in Azure ML is to use the AutoML feature. You should end up with a trained model:
 ![image](https://user-images.githubusercontent.com/56161454/157678023-7dae682d-bcc0-40b3-a32c-92be4d37d934.png)
 ### Deploy Model
 To use the model in production it needs to be deployed. There are multiple ways to archive the same result including UI in ML Studio, AzureML SDK and Azure CLI. The deployed model is accessible via a scoring URI via HTTPS:
 ![image](https://user-images.githubusercontent.com/56161454/157678404-3bcd0aac-0bcc-4a87-95dd-f6a15ec8a111.png)
 ### Log via Application Insights
 It is usefull to know what is going on under the hood. Application Insights is the easiest way to get a better understanding how the model is performing (via the UI) or view the logs:
 ![image](https://user-images.githubusercontent.com/56161454/157704196-ec525065-2bd8-474d-82a7-f943549c96f5.png)
 ### Explore Swagger of endpoint
 Swagger is a usefull way to understand the input format that is expected by the API:
 ![image](https://user-images.githubusercontent.com/56161454/157704665-29cce543-fe80-4ecf-881f-cc3931f25a3a.png)
  ### Use Model
  Sending a HTTPS request with data in a JSON format to the scoring URI returns the prediciton of the model in a valid HTTPS responde:
  ![image](https://user-images.githubusercontent.com/56161454/157709477-88cf8d10-508a-41be-837b-3a3f068422b8.png)
  ### Benchmark using Apache Benchmark
  Apache Benchmark can be used to measure performance of the deployed model:
  ![image](https://user-images.githubusercontent.com/56161454/157704966-579a261e-a387-44d9-bd77-3f1ed8d58d26.png)
## Publish Pipeline
  ### Create Pipeline
  In order to automate machine learning in azure pipelines are the tool of choice. Pipelines can be created in multiple ways, here the AzureML SDK was used:
  ![image](https://user-images.githubusercontent.com/56161454/157679227-3a5840aa-b652-42ac-9b98-454bfde2bdbf.png)
  ### Configure with SDK
  The SDK is a powerfull way to do everithing that needs to be done with pipeline. For example you can easily monitor the status of a running pipeline:
  ![image](https://user-images.githubusercontent.com/56161454/157710277-a6468460-b654-427f-a180-c45ad013c045.png)
  ### Deploy Pipeline
  To make the automation of the ML process accessable a pipeline can be deployed which creates an pipeline endpoint:
  ![image](https://user-images.githubusercontent.com/56161454/157680286-0466ee1b-7298-4eca-a468-d1d0d9d41041.png)
  ### Details of Deployed Pipeline
  A new run of a deployed pipeline can be triggered by sending a request to the REST endpoint:
  ![image](https://user-images.githubusercontent.com/56161454/158007734-6f48589b-7df8-4af2-ac6f-6098a8299ead.png)
  ### Trigger Pipeline
  The response of such a request contains all the relevant information to further track the newly created run:
  ![image](https://user-images.githubusercontent.com/56161454/157743696-b03eb9ff-cfc8-4962-a76b-ad429c2f0a89.png)
  ### Pipeline Rerun
  The newly created run is also available in the Azure ML Studio:
  ![image](https://user-images.githubusercontent.com/56161454/157711475-ee61553a-58f4-40a4-b018-ad999bd16512.png)

 # Screencast
 https://youtu.be/FSHurKVr68E
 
