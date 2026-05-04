# Appointment Scheduling System (AWS Cloud-Native)

A cloud-native Appointment Scheduling System developed using Amazon Web Services (AWS), implementing a scalable serverless architecture. The system allows users to create, view, confirm, and delete appointments through a web-based interface, with full backend processing handled via AWS services.

---

## 🌐 Live Application
http://healthconnect-frontend-luana.s3-website-us-east-1.amazonaws.com

---

## 🏗️ System Architecture

The system follows a **serverless cloud-native architecture**, separating frontend, backend, and data layers:

- **Frontend Layer**: Hosted on Amazon S3 (static website)
- **API Layer**: Amazon API Gateway (REST API)
- **Application Layer**: AWS Lambda (business logic)
- **Data Layer**: Amazon DynamoDB (NoSQL database)
- **Monitoring**: Amazon CloudWatch
- **Security**: AWS IAM roles and policies

---

## ⚙️ Technologies Used

- **Amazon S3** – Static website hosting (frontend)
- **AWS Lambda** – Serverless backend processing
- **Amazon API Gateway** – RESTful API management
- **DynamoDB** – NoSQL database for storing appointments
- **CloudWatch** – Monitoring and logging
- **IAM** – Access control and security management

---

## 🔗 API Endpoints

The system exposes RESTful endpoints via API Gateway:

| Method | Endpoint           | Description                  |
|--------|------------------|------------------------------|
| POST   | /appointments     | Create a new appointment     |
| GET    | /appointments     | Retrieve all appointments    |
| PUT    | /appointments     | Update appointment status    |
| DELETE | /appointments     | Delete an appointment        |

---

## 🧠 Features

- Create appointments
- View stored appointments
- Confirm appointment status
- Delete appointments
- Real-time data updates via API integration

---

## 🔐 Security Implementation

- IAM roles control access between services
- HTTPS ensures secure data transmission
- DynamoDB encryption protects stored data
- API Gateway handles request validation and routing

---

## 📊 Monitoring and Logging

- AWS CloudWatch is used to monitor system activity
- Logs track API requests and Lambda execution
- Helps identify and debug errors in real time

---

## 🚀 Deployment

The system is fully deployed using AWS cloud services:

- Frontend deployed via Amazon S3 static hosting
- Backend deployed using AWS Lambda
- API Gateway connects frontend and backend
- DynamoDB stores appointment data

---

## 💡 Future Improvements

- Implement CI/CD pipelines for automated deployment
- Add authentication (e.g., AWS Cognito)
- Enhance UI/UX design
- Extend system to hybrid multi-cloud architecture

---

## 📁 Source Code

This repository contains:
- Backend (AWS Lambda function)
- Frontend files (HTML, CSS, JavaScript)
- Documentation of the system architecture

---

## 📌 Author

Developed as part of a Cloud Computing coursework project.
