# Signature Comparison App

Welcome to the Signature Comparison App! This application is designed to work with handwritten signatures by analyzing their characteristics to determine similarity, storing them securely, and potentially using them for authentication (and possibly authorization) purposes.

---

## **Project Overview**

This project demonstrates key functionalities of a signature analysis system using demo pages and a robust backend service. Below is a breakdown of the components:

### **Demo Scripts**
The application provides interactive JavaScript demos located in the `static` folder:

1. **`demo-script.js`**: 
   - Illustrates specific features of the signature analysis process.

2. **`drawer.js`**:  
   - Implements an algorithm that interprets a signature as a set of ordered points.
   - Captures key signature metrics, including pen speed and stroke sequence.

   > User-specific demo functionalities are stored within their respective demo folders, allowing you to test the application holistically using pre-built pages and scripts.

### **Backend Components (Python)**

1. **`server.py`**:
   - The core backend service that handles client requests.
   - Manages libraries and services responsible for data processing.

2. **`abstractions.py`**:
   - Defines data structures and models for database operations.

3. **`authorization_service.py`**:
   - Implements working authorization and token-based authentication logic.

4. **`lib/`**:
   - Contains signature analysis algorithms used to compare and evaluate matching signatures.

5. **`mongo_orm.py`**:
   - A specialized library that interacts with MongoDB, managing database entities efficiently.

6. **`posts_service.py` and `sign_service.py`**:
   - Handle interactions with the database through structured data models and specialized services.

### **Security Considerations**

Files like `settings.py` and `migration.py` contain sensitive information and should be secured appropriately to prevent unauthorized access.

---

## **Current Features**
- **Signature Matching Algorithm**: Analyzes handwritten signatures as sequences of points, factoring in pen speed and stroke order.
- **Modular JavaScript Demos**: Visualize and interact with the core functionality.
- **Token-based Authentication**: Implements basic user authorization for secure access.
- **MongoDB Integration**: Uses an ORM layer to manage data storage and retrieval.

---

## **Planned Enhancements**
- Deployment to a cloud environment (e.g., Heroku) for wider accessibility.
- Expanded security features to handle encryption and enhanced user privacy.
- More robust analytics for signature verification accuracy.

---

## **Getting Started**
To run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Groxikm/ReferenseForSignApp/tree/main
   cd ReferenseForSignApp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python server.py
   ```

4. Access the demo pages in your browser to explore the functionality.
