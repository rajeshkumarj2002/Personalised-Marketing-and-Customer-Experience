from flask import Flask, request, render_template_string, jsonify
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Dummy Customer Database
customer_db = pd.DataFrame({
    'Email': ['john@example.com', 'jane@example.com', 'alex@example.com'],
    'Name': ['John', 'Jane', 'Alex'],
    'LastPurchaseDate': [datetime(2024, 12, 1), datetime(2025, 4, 1), datetime(2025, 5, 1)],
    'PurchaseFrequency': [5, 1, 3],
    'MonetaryValue': [500, 50, 200],
    'EmailOpens': [10, 1, 3]
})

# Response Template for Form
response_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Thank You</title>
</head>
<body>
  <h1>Thank You, {{ name }}!</h1>
  <p>Status: {{ status }}</p>
  <p>Message: {{ message }}</p>
  <a href="/">Go back</a>
</body>
</html>
"""

# Customer Status Function
def get_customer_status(email):
    row = customer_db[customer_db['Email'].str.lower() == email.lower()]
    if row.empty:
        return "New Customer", "Welcome! Enjoy a 10% discount on your first order."
    customer = row.iloc[0]
    recency = (datetime.today() - customer['LastPurchaseDate']).days
    if customer['EmailOpens'] < 3 and customer['PurchaseFrequency'] < 2:
        return "Low Engagement", "We miss you! Here's a 20% re-engagement discount."
    elif recency > 30 and customer['MonetaryValue'] > 100:
        return "Churn Risk", "Come back and enjoy exclusive loyalty perks!"
    else:
        return "Healthy", "Thanks for staying with us! Here's what's new this week."

# Log Device Info API
@app.route('/log-device', methods=['POST'])
def log_device():
    data = request.get_json()
    print("📱 Device Info Received:", data)
    df = pd.DataFrame([data])
    df.to_csv("device_logs.csv", mode='a', header=False, index=False)
    return jsonify({"status": "success", "message": "Device info logged"})

# Home Page
@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Personalised Marketing and Customer Experience</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    .info-box {
      background-color: #e8f0fe;
      border-left: 5px solid #0d6efd;
      padding: 20px;
      margin-top: 30px;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <header class="bg-dark text-white text-center py-4">
    <div class="container">
      <h1 class="display-5">Personalised Marketing and Customer Experience</h1>
      <p class="lead">Using Data to Deliver Customized Customer Journeys</p>
    </div>
  </header>

  <main class="container my-5">
    <div class="row mb-4">
      <div class="col">
        <div class="p-4 bg-light rounded shadow-sm">
          <h2>Project Overview</h2>
          <p>This project explores how personalized marketing can enhance the customer journey by tailoring content and offers based on user behavior, preferences, and history.</p>
        </div>
      </div>
    </div>

    <div class="row mb-4">
      <div class="col-md-6">
        <div class="p-4 bg-white rounded shadow-sm border">
          <h3>Data-Driven Insights</h3>
          <p>Leverage customer purchase history, engagement levels, and behavior patterns to dynamically adjust marketing strategies.</p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="p-4 bg-white rounded shadow-sm border">
          <h3>Segmentation & Targeting</h3>
          <p>Automatically segment users into categories like loyal, new, or at-risk, and send personalized campaigns that drive conversions.</p>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="p-4 bg-light rounded shadow-sm">
          <h2>Why Personalization Matters</h2>
          <ul>
            <li>Boosts customer retention and loyalty</li>
            <li>Increases engagement and conversion rates</li>
            <li>Delivers relevant content and offers</li>
            <li>Strengthens brand relationships</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="info-box">
          <h4>Your Device Info</h4>
          <p><strong>Device Type:</strong> <span id="deviceType">Detecting...</span></p>
          <p><strong>Screen Size:</strong> <span id="screenSize">Detecting...</span></p>
          <p><strong>Memory:</strong> <span id="memory">Detecting...</span></p>
        </div>
      </div>
    </div>
  </main>

  <footer class="bg-dark text-white text-center py-3">
    <small>&copy; 2025 Your Name or College | CSE Project</small>
  </footer>

  <script>
    function getDeviceType() {
      const width = window.innerWidth;
      if (width <= 767) return "Phone";
      else if (width <= 1024) return "Tablet";
      else return "Desktop / PC";
    }

    function updateDeviceInfo() {
      const deviceType = getDeviceType();
      const screenSize = window.innerWidth + " x " + window.innerHeight;
      const memory = navigator.deviceMemory ? navigator.deviceMemory + " GB" : "Not available";

      document.getElementById('deviceType').textContent = deviceType;
      document.getElementById('screenSize').textContent = screenSize;
      document.getElementById('memory').textContent = memory;

      fetch("/log-device", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          device_type: deviceType,
          screen_size: screenSize,
          memory: memory,
          user_agent: navigator.userAgent,
          timestamp: new Date().toISOString()
        })
      }).then(res => res.json())
        .then(data => console.log("✅ Device info logged"))
        .catch(err => console.error("Logging error:", err));
    }

    window.onload = updateDeviceInfo;
    window.onresize = updateDeviceInfo;
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route('/submit-form', methods=['POST'])
def handle_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    status, personalized_msg = get_customer_status(email)
    return render_template_string(response_template, name=name, status=status, message=personalized_msg)

if __name__ == '__main__':
    app.run(debug=True)