# Appointment Scheduling System (AWS Cloud-Native)

A cloud-native Appointment Scheduling System developed using Amazon Web Services (AWS), implementing a scalable serverless architecture. The system is currently deployed on AWS but is designed to support future hybrid multi-cloud integration with platforms such as Microsoft Azure or Google Cloud.

---

## 🌐 Live Application
http://healthconnect-frontend-luana.s3-website-us-east-1.amazonaws.com

---

## 🏗️ System Architecture

The system follows a **serverless cloud-native architecture**, separating frontend, backend, and data layers:

- **Frontend Layer**: Hosted on Amazon S3 (static website)
- **API Layer**: Amazon API Gateway (RESTful API)
- **Application Layer**: AWS Lambda (business logic)
- **Data Layer**: Amazon DynamoDB (NoSQL database)
- **Monitoring**: Amazon CloudWatch
- **Security**: AWS Identity and Access Management (IAM)

This architecture enables high scalability, flexibility, and reduced operational overhead.

---

## ⚙️ Technologies Used

- **Amazon S3** – Static website hosting (frontend)
- **AWS Lambda** – Serverless backend processing
- **Amazon API Gateway** – RESTful API communication
- **DynamoDB** – NoSQL database for storing appointment data
- **CloudWatch** – Monitoring and logging
- **IAM** – Access control and security management

---

## 🔗 API Endpoints

The system exposes RESTful endpoints via API Gateway:

| Method | Endpoint        | Description                     |
|--------|----------------|---------------------------------|
| POST   | /appointments  | Create a new appointment        |
| GET    | /appointments  | Retrieve all appointments       |
| PUT    | /appointments  | Update appointment status       |
| DELETE | /appointments  | Delete an appointment           |

These endpoints enable secure communication between the frontend and backend components.

---

## 🧠 Features

- Create appointments  
- View stored appointments  
- Confirm appointment status  
- Delete appointments  
- Real-time data updates via API integration  

---

## 🔐 Security Implementation

- IAM roles enforce secure access between AWS services  
- HTTPS ensures secure data transmission  
- DynamoDB encryption protects stored data  
- API Gateway manages request validation and routing  

---

## 📊 Monitoring and Logging

- AWS CloudWatch monitors system activity  
- Logs track API requests and Lambda execution  
- Supports real-time error detection and debugging  

---

## 🚀 Deployment

The system is fully deployed using AWS cloud services:

- Frontend deployed via Amazon S3 static website hosting  
- Backend implemented using AWS Lambda  
- API Gateway connects frontend and backend services  
- DynamoDB stores appointment data  

The application is publicly accessible via the live URL above, demonstrating a fully operational cloud-native system.

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
- Frontend files (HTML)  
- Documentation of the system architecture  

---

## 📌 Author

Developed as part of a Cloud Computing coursework project.
