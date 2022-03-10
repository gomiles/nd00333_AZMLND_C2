 # Project Overview
 
In this Udacity project the goal was to learn how to operationalize machine learning in the Azure cloud.
Steps completed:
 - Deploy a model
 - Use the model (consume endpoints)
 - Automate the process (pipeline automation)

 # Architectual Diagram
 ![image](https://user-images.githubusercontent.com/56161454/157675813-decd84bc-4867-4813-81a7-c6b283c92795.png)

 # Key Steps
 ## Deploy Model
  - Register Dataset: ![image](https://user-images.githubusercontent.com/56161454/157677786-de087cd6-1273-49de-a8a7-4a72ab70c751.png)
  - Train Model: ![image](https://user-images.githubusercontent.com/56161454/157678023-7dae682d-bcc0-40b3-a32c-92be4d37d934.png)
  - Deploy Model: ![image](https://user-images.githubusercontent.com/56161454/157678404-3bcd0aac-0bcc-4a87-95dd-f6a15ec8a111.png)
  - Log via Application Insights: ![image](https://user-images.githubusercontent.com/56161454/157704196-ec525065-2bd8-474d-82a7-f943549c96f5.png)
  - Explore Swagger of endpoint: ![image](https://user-images.githubusercontent.com/56161454/157704665-29cce543-fe80-4ecf-881f-cc3931f25a3a.png)
  - Use Model: ![image](https://user-images.githubusercontent.com/56161454/157709477-88cf8d10-508a-41be-837b-3a3f068422b8.png)
  - Benchmark using Apache Benchmark: ![image](https://user-images.githubusercontent.com/56161454/157704966-579a261e-a387-44d9-bd77-3f1ed8d58d26.png)
## Publish Pipeline
  - Create Pipeline: ![image](https://user-images.githubusercontent.com/56161454/157679227-3a5840aa-b652-42ac-9b98-454bfde2bdbf.png)
  - Configure with SDK: ![image](https://user-images.githubusercontent.com/56161454/157710277-a6468460-b654-427f-a180-c45ad013c045.png)
  - Deploy Pipeline: ![image](https://user-images.githubusercontent.com/56161454/157680286-0466ee1b-7298-4eca-a468-d1d0d9d41041.png)
  - Trigger Pipeline: ![image](https://user-images.githubusercontent.com/56161454/157743696-b03eb9ff-cfc8-4962-a76b-ad429c2f0a89.png)
  - Pipeline Rerun: ![image](https://user-images.githubusercontent.com/56161454/157711475-ee61553a-58f4-40a4-b018-ad999bd16512.png)

 # Improvements
  - Pipeline Parameter
    - A new run of the pipeline makes only sense if something new needs to be processed. This could be the trainingdata used to train the model. Or different pipeline parameters.
  - Automatic Model Deployment
    - The next step in automation would be to automatically deploy the best model of a pipeline run.
 
 # Screencast
 https://youtu.be/FSHurKVr68E
 
