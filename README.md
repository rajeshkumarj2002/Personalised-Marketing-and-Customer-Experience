# Personalised-Marketing-and-Customer-Experience

This project is a **Flask-based web application** that demonstrates how **data-driven personalization** can improve customer engagement through tailored messaging and insights. It utilizes **customer segmentation**, **purchase behavior**, and **device analytics** to enhance the user journey.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Code Explanation](#code-explanation)
- [Running the Project](#running-the-project)
- [Key Points](#key-points)
- [Screenshot Preview](#screenshot-preview)
- [License](#license)

---

## Overview

The project simulates a marketing portal that identifies customer status based on:
- Purchase history
- Engagement (email opens)
- Recency (last purchase date)
- Device info logging

The UI is responsive and informative, giving users personalized feedback and analyzing the devices they use to visit the platform.

---

## Features

- **Customer Classification**:
  - *New Customer*
  - *Low Engagement*
  - *Churn Risk*
  - *Healthy Customer*
- **Personalized Messaging** for each customer type.
- **Device Detection**:
  - Type (Phone, Tablet, Desktop)
  - Screen Size
  - Device Memory
- **Logs Device Info** into a CSV file for backend analytics.
- **Bootstrap 5 UI** for a modern look and mobile responsiveness.

---

## How It Works

1. User opens the site.
2. JS script detects device specs and logs them to the backend.
3. User fills out the form with their name and email.
4. Backend matches the email with a sample customer database and determines:
   - Engagement score
   - Purchase frequency
   - Time since last purchase
5. Returns a customized message and status.

---

## Tech Stack

- **Frontend**:
  - HTML5, Bootstrap 5
  - JavaScript for device detection
- **Backend**:
  - Python 3
  - Flask (Web framework)
  - Pandas (Customer database & logging)

---

## Code Explanation

### 1. **Customer Database (`customer_db`)**

Stores mock data of existing customers including:
- Email
- Name
- Last Purchase Date
- Frequency
- Total Spend
- Email Opens

### 2. **Customer Status Function**

Checks:
- Whether the email exists
- Email opens < 3 and frequency < 2 → **Low Engagement**
- Recent activity > 30 days and high spend → **Churn Risk**
- Default → **Healthy**

Returns a status and a personalized message.

### 3. **Device Logging API**

Logs:
- Screen size
- Device type
- Memory
- Timestamp

Saved into `device_logs.csv` for future analytics.

### 4. **Frontend Home Page**

- Responsive layout using Bootstrap
- Displays the project purpose
- Detects device info using `navigator` APIs in JavaScript
- Sends a POST request to `/log-device` endpoint

### 5. **Form Submission**

- Gets user name, email, and message
- Uses the `get_customer_status()` function
- Displays results in a clean, styled HTML page

---

## Running the Project

### 1. **Install Dependencies**
```bash
pip install flask pandas
```

### 2. **Run the Flask App**
```bash
python app.py
```

### 3. **Open in Browser**
```
http://127.0.0.1:5000/
```

---

## Key Points

- Simulates real-world marketing intelligence with personalization.
- Demonstrates customer segmentation logic using Python.
- Highlights how device info can be used for optimizing UX.
- Easily extendable to a full CRM or marketing dashboard.
- Ideal for academic projects focused on digital marketing + AI.

---

## Screenshot Preview

*You can add a screenshot of the web page or form submission output here.*

---

## License

This project is for educational and demonstration purposes. You can freely modify and expand it for learning, portfolio, or academic use.
