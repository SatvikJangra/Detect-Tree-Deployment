# Deployment Guide for Flask Application

This guide provides detailed steps to deploy your Flask application using Docker, Kubernetes, and Jenkins.

## Prerequisites

- Docker installed on your local machine.
- Kubernetes cluster set up and configured.
- Jenkins installed and configured.
- Access to your GitHub repository and Docker Hub account.

## Steps to Deploy

### Step 1: Prepare Your Flask Application

1. **Ensure Your Flask App Is Ready:** Ensure that your Flask application (`app.py`) and any dependencies are prepared. Make sure the application is running as expected locally.
   
2. **Organize Your Project Files:** Ensure your project files are well-organized, including the Flask application, the `requirements.txt` file, and any other supporting files such as HTML, CSS, and JavaScript files.

### Step 2: Set Up a Dockerfile

1. **Create a Dockerfile:** In the root directory of your project, create a file named `Dockerfile` to specify how your application should be containerized.

2. **Define the Base Image:** Use the `python:3.10-slim` base image in your Dockerfile.

3. **Set the Working Directory:** Use the `WORKDIR /app` command to set the working directory inside the container.

4. **Copy the Requirements:** Use the `COPY requirements.txt .` command to copy the `requirements.txt` file into the container and install dependencies with the `RUN pip install --no-cache-dir -r requirements.txt` command.

5. **Copy the Application Code:** Use the `COPY . .` command to copy all project files into the container.

6. **Expose the Flask App Port:** Use the `EXPOSE 5926` command to expose the Flask app port.

7. **Set the Entry Point:** Use `CMD ["python", "app.py"]` as the entry point to run the Flask application when the container starts.

### Step 3: Build and Push the Docker Image

1. **Build the Docker Image:** Use the command `docker build -t satvikjangra/dockertry:latest .` to build the Docker image.

2. **Push the Docker Image:** Use the command `docker push satvikjangra/dockertry:latest` to push the image to Docker Hub.

### Step 4: Set Up Kubernetes Configuration Files

1. **Create `Deployment.yaml`:** In your project directory, create a file named `Deployment.yaml` to specify the deployment configuration.

2. **Create `Service.yaml`:** Create a file named `Service.yaml` to specify how the application should be exposed.

### Step 5: Deploy the Application Using Kubernetes

1. **Apply the Deployment Configuration:** Use the command `kubectl apply -f Deployment.yaml` to deploy the application using Kubernetes.

2. **Apply the Service Configuration:** Use the command `kubectl apply -f Service.yaml` to set up the service.

### Step 6: Set Up Jenkins Pipeline

1. **Create a Jenkinsfile:** In the root directory of your project, create a file named `Jenkinsfile` to define your CI/CD pipeline.

2. **Define Pipeline Stages:** Specify the stages for cloning the repository, building the Docker image, pushing the image to Docker Hub, and deploying the application using Kubernetes.

3. **Configure Jenkins:** Ensure Jenkins is set up and connected to your repository.

4. **Trigger the Pipeline:** Run the Jenkins pipeline to build, push, and deploy your application.

By following these steps, you can successfully deploy your Flask application using Docker, Kubernetes, and Jenkins. Adjust the configurations and files as needed for your specific deployment scenario.
