#NAAN MUDHALVAN - IBM

COLLEGE CODE : 1125
COLLEGE NAME : Sri Venkateswara Institute of Science and Technology, Tiruvallur
DEPARTMENT : CSE,CSE(Cyber Security),CSE,CSE,AI&DS

STUDENT NM-ID : e47d7c744a82b52bea74fa4549ec05e5
                e465596f0af825e99f44d6ca155c83d3 
                b6e95e95d19b8ce8c4740d2f4f5f249b 
                8a6e787d3fa24d0897a48d36100ff7d3 
                86e0117af78c5a7bb3f44e887f0bfadf

ROLL NO :

              112523104003
              112523149002
              112523104011
              112523104301
              112523243302

SUBMITTED BY,

           ASWIN R

           MUKESH VARMA N

           RAJESH KUMAR J

           SARATHY B

          PARVEEN KUMAR G

DATE : 15/05/2025

AI - PERSONALISED MARKETING AND CUSTOMER EXPERIENCE

1. Project Demonstration

Overview

The AI-Powered Personalized Marketing and Customer Experience system will be demonstrated to stakeholders, showcasing its features, performance improvements, and functionality. This demonstration highlights the system’s targeted marketing capabilities, real-time data analysis, security measures, and performance scalability.

Demonstration Details

System Walkthrough: A live walkthrough of the platform, from user interaction to the output, showcasing how the AI analyzes customer data to deliver personalized marketing content. AI Speed: The demonstration will show how the AI model provides fast responses and actions based on user interactions and marketing data.

Data Integration: Real-time analysis of customer interactions will be demonstrated, highlighting how marketing strategies are adapted based on user behavior.
Performance Metrics: Response time, system scalability, and load handling under multiple user interactions will be highlighted to show improved system capacity.
Security & Privacy: Encryption protocols and privacy measures will be explained and demonstrated as the system handles user data.

Outcome

By the end of the demonstration, the system’s ability to handle real-world scenarios, ensure data security, and deliver targeted marketing content will be showcased to the stakeholders.

Project Documentation Overview

Comprehensive documentation for the AI-Powered Personalized Marketing and Customer Experience system is provided to detail every aspect of the project. This includes system architecture, AI model details, code explanations, and usage guidelines for both users and administrators.

Documentation Sections

System Architecture :Diagrams illustrating the complete system, including AI algorithms, data processing workflows, and customer interaction modules.
Code Documentation: Source code and explanations for all code modules, including AI training scripts, API integrations, and marketing content delivery mechanisms.
User Guide: A manual for marketing managers and users, explaining how to interact with the system, analyze customer data, and generate targeted marketing campaigns. Administrator Guide: Instructions for system maintenance, monitoring, and performance testing procedures.
Testing Reports: Detailed reports on performance metrics, load testing, and data security evaluations.

Outcome

All critical components of the system will be well-documented, providing a clear guide for future development, deployment, or system scaling.

Personalized Marketing & Customer Service

This project demonstrates how to enhance the customer experience using personalized marketing and customer service strategies. It consists of a Python Flask backend and a modern HTML frontend. The system adapts responses and insights based on customer engagement data and behavior.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
- [Python Backend Explanation](#python-backend-explanation)
- [HTML Frontend Explanation](#html-frontend-explanation)
- [How to Run the Project](#how-to-run-the-project)

## Project Overview

This system enables personalized user experiences using basic customer data like purchase history, email engagement, and device info. It tailors responses to the user and logs device-related data to help improve marketing strategies.

---

## Technologies Used

- Python 3
- Flask (Web Framework)
- Pandas (Data Handling)
- HTML5 & CSS3
- Bootstrap (via CDN)

---

## Key Features

### Backend
- Customer segmentation based on behavior
- Email and purchase frequency analysis
- Device info logging to CSV
- Dynamic message generation

### Frontend
- Informative, responsive webpage
- Simple form to capture user details
- Device information auto-detection via JavaScript

---

## Python Backend Explanation

### 1. `get_customer_status(email)`
- Identifies user type:
  - New Customer
  - Low Engagement
  - Churn Risk
  - Healthy
- Returns a message based on segmentation logic using customer database.

### 2. `/submit-form`
- Accepts `POST` request from the HTML form.
- Returns a personalized thank you page with status and message.
  
### 3. `/log-device`
- Receives device info (screen size, memory, user agent) via JS.
- Appends it to `device_logs.csv` for analysis.

### 4. `/`
- Renders the homepage (HTML UI) using `return` string.

---

## HTML Frontend Explanation

### Sections:
- **Header**: Title and navigation links
- **Marketing Section**: Describes data-driven marketing
- **Customer Service Section**: Highlights personalization in support
- **Contact Section**: Contains a form to collect user name, email, and message

### Styles:
- Uses simple CSS for layout, responsive design, and color theming.
- Clean and modern look with rounded sections and interactive form.

---

## How to Run the Project

1. **Install Dependencies**
   ```bash
   pip install flask pandas
   ```

2. **Run the App**
   ```bash
   python app.py
   ```

3. **Open in Browser**
   Visit: `http://localhost:5000`
