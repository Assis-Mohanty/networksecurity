
---

Phishing involves cybercriminals tricking users into revealing sensitive data like passwords, credit card details, and bank information. This project aims to build a comprehensive network security solution that automatically detects phishing data through an automated and scalable MLOps pipeline.

## Project Overview

The core objective is to classify incoming phishing data as either malicious or benign using machine learning models within a robust MLOps framework. Emphasis is placed on automation, scalability, and reproducibility to ensure consistent and reliable threat detection.

## Architecture and Workflow

* **Data Engineering:**
  Designed ETL pipelines to extract, transform, and load phishing datasets into a MongoDB database. Data ingestion splits the dataset into training and testing partitions, saved as artifacts for traceability. Validation routines monitor data quality and drift, ensuring model input consistency. Preprocessing scripts generate reusable transformer objects (preprocessor.pkl) for downstream use.

* **Modeling:**
  Trained various classification algorithms—Logistic Regression, KNN, AdaBoost, Decision Tree, and Random Forest. Models were rigorously evaluated to identify the top performer, culminating in a final serialized model (model.pkl). Separate pipelines handle both model training and batch inference for operational flexibility.

* **Experiment and Artifact Management:**
  Leveraged DagsHub integrated with MLflow to maintain detailed experiment logs, metric tracking, and version control. Critical artifacts, including models and preprocessors, are securely stored and versioned in AWS S3 buckets.

* **Real-Time Serving:**
  Built a FastAPI web service to provide real-time phishing detection predictions, ensuring fast and scalable model accessibility.

* **Deployment and Automation:**
  Containerized the application using Docker and pushed images to AWS Elastic Container Registry (ECR). CI/CD workflows implemented with GitHub Actions automate testing and deployment, with the final system deployed on AWS EC2 instances for robust production readiness.

## Technologies Utilized

* Databases & Storage: MongoDB, AWS S3
* MLOps & Experimentation: DagsHub, MLflow
* Machine Learning Frameworks: Scikit-learn (Logistic Regression, KNN, AdaBoost, Decision Tree, Random Forest)
* Web Framework: FastAPI
* Cloud Infrastructure: AWS EC2, AWS ECR, AWS S3
* Automation Tools: GitHub Actions
* Containerization: Docker

## Outcome

This project delivers an end-to-end automated pipeline for phishing detection, combining data engineering, model training, evaluation, and deployment. The use of state-of-the-art MLOps tools and cloud technologies guarantees reproducibility, scalability, and efficient management of models and data artifacts. The deployed system is production-ready and capable of handling real-world phishing detection tasks.

---

