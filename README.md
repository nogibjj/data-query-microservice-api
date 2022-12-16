[![Docker Image Sent to ECR and Built Via Code Build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoicmVFYndqOStzMVZ2VFB4cnFKMDg0SG5Xa3lPSjVGbXBoYTFWYUJJU2ZoekdFbHBIYlFGcXp5YkVNWjI4amVjOGRRZTBOWXBmdWZ0Q05reGg1MVN0eWY0PSIsIml2UGFyYW1ldGVyU3BlYyI6Ikd1ZFFVbHFyc0s2M1c1cm0iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# IDS706 Group Project

This is a repository for continuous delivery of containerized microservice which performs a query using SQL and returns useful information to the user.

<img width="784" alt="image" src="https://user-images.githubusercontent.com/112578065/207986486-372d8d2d-92ea-46f9-ad75-f0ca8d5c4623.png">

## Project Description

This group project was done as part of IDS706 Data Engineering class at Duke University. 

## Contents

### 1. Creation of Database
(1) Kaggle API
![image](https://user-images.githubusercontent.com/112578065/207997214-98d54398-2417-4fe6-9452-9a253ec4960a.png)

(2) AWS RDS
![image](https://user-images.githubusercontent.com/112578065/207997090-e6c0e5f4-7f98-44eb-a8dd-8b6733bd6925.png)

### 2. EDA Implementation
- Exploring useful information
- Drawing plots

### 3. Continuous Integration
A makefile, a requirements file, and the test files were created. They were all run by github actions as a measure of continuous integration. 

### 4. Generating FastAPI
- Wrapping all the functions
- Swagger documentation

### 5. Continuous Delivery
A docker image was built to containerize the app. Then it was sent to an AWS ECR repository. From there, it gets built through AWS Code Build. It is important to also flag that the AWS account's owner must add the AmazonEC2ContainerRegistryFullAccess to the permissions under the policy that manipulates or oversees that repository. Otherwise, the build won't complete. Once built, the app is deployed through AWS AppRunner, and it becomes immediately available to anyone. Something else that affects the permissions is creating a codebuild with elevated build privileges, a good way to avoid the "are the docker daemons running" error.

### 6. Streamlit
- Hosting APIs
- Showing users end result

## Expected Output

## Dataset

The global temperature data used in this project was sourced from Kaggle, but it was originally provided by the Berkeley Earth, which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature Study combines 1.6 billion temperature reports from 16 pre-existing archives. It is nicely packaged and allows for slicing into interesting subsets (for example by country). They publish the source data and the code for the transformations they applied.

(Reference: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCountry.csv)


