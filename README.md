# Student Management System

A web-based Student Management System developed using Python and Flask. This project allows users to add and manage student academic records through a simple and interactive browser interface. The application is based on my original  Python project and later converted into a Flask web application for localhost hosting and future deployment.

---

## Live Website Preview

![Render Website Preview](images/render-preview.png)

> **For the best viewing experience, open the website on a desktop or laptop screen.**

---

## Localhost Preview

![Localhost Preview](images/homepage.png)

---

## Features

- Add Student Records
- Store Student Academic Details
- Display Student Data in Tabular Format
- Web-based User Interface
- Flask Localhost Server Integration
- Simple and Beginner-Friendly Design

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- VS Code

---

## Required Project Files

The following files and folders should be present in the project directory for proper execution:

student-management-system/
│
├── app.py
├── Studentmanagementreportcard.py
├── requirements.txt
├── README.md
│
└── images/
    ├── homepage.png
    └── render-preview.png

---

## requirements.txt

The following dependency should be included inside the `requirements.txt` file:

```text
flask
```

---

## How to Run the Project

### Step 1 — Download or Clone the Project

Download the project ZIP file and extract it  
OR clone the repository using Git:

```bash
git clone https://github.com/your-username/student-management-system.git
```

---

### Step 2 — Open Project Folder in VS Code

1. Open VS Code
2. Click on:

```text
File → Open Folder
```

3. Select the project folder

---

### Step 3 — Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

A terminal will open at the bottom of VS Code.

---

### Step 4 — Install Flask

In terminal type:

```bash
pip install flask
```

This installs Flask, which is required to run the web server.

---

### Step 5 — Run the Flask Application

In terminal type:

```bash
python app.py
```

Press Enter.

---

### Step 6 — Open Localhost Server

After running the command, you will see:

```text
Running on http://127.0.0.1:5000
```

Open this link in your browser:

```text
http://127.0.0.1:5000
```

---

### Step 7 — Use the Application

You can now:

- Enter Student Details
- Add Records
- View Student Data in Table Format

The project is now running successfully on your local server.

---

## Deployment

After successfully running the project on the local Flask server, the application can be deployed online using platforms like Render for public access and hosting.

### Render Deployment Steps

1. Upload the project to GitHub
2. Create a new Web Service on Render
3. Connect the GitHub repository
4. Add the following build command:

```bash
pip install -r requirements.txt
```

5. Add the following start command:

```bash
python app.py
```

6. Deploy the project

After deployment, Render provides a public website link that can be used in resumes, portfolios, and LinkedIn profiles.

---

## Future Improvements

- Search Student Records
- Modify Student Data
- Delete Records
- Database Integration
- Authentication System
- Responsive UI Design
- Cloud Deployment

---

## Developer

Dhruv Sharma

BCA 2nd-Year Student specializing in Cybersecurity and Cloud Security.