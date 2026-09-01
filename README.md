# Freelance Project Collaboration Platform

## 1. Project Description

The Freelance Project Collaboration Platform is a web-based application designed to connect clients and freelancers and support project collaboration.

Clients can register, log in, create projects, view freelancer proposals, review proposals, and accept a suitable freelancer.

Freelancers can register, log in, manage their profile, browse available projects, view project details, submit proposals, and track their proposal status.

The project is developed using a collaborative Git and GitHub workflow with feature branches, meaningful commits, Pull Requests, code reviews, and merging into the main branch.

---

## 2. Project Objectives

The main objectives of the project are:

- Connect clients and freelancers through a single platform.
- Allow clients to create and manage project requirements.
- Allow freelancers to browse available projects.
- Allow freelancers to submit proposals for projects.
- Allow clients to view and review submitted proposals.
- Allow clients to accept a suitable freelancer proposal.
- Assign the project to the selected freelancer.
- Provide separate workflows for clients and freelancers.
- Provide role-based dashboards.
- Follow a structured Git and GitHub collaboration workflow.
- Deploy the application on an AWS EC2 Linux server as part of Sprint 5.

---

## 3. Current Features

### User Registration

The platform provides separate registration options for clients and freelancers.

#### Client Registration

Clients can register by providing:

- Full Name
- Email Address
- Password
- Confirm Password

#### Freelancer Registration

Freelancers can register by providing:

- Full Name
- Email Address
- Password
- Primary Skill

### User Login

Registered users can log in using their email address and password.

The platform supports two user roles:

- Client
- Freelancer

After login, users can access the dashboard associated with their role.

### Client Features

Clients can:

- Register an account.
- Log in to the platform.
- Access the Client Dashboard.
- Manage their profile.
- Post new projects.
- View posted projects.
- View project details.
- View freelancer proposals.
- Review proposals.
- Accept a freelancer proposal.

### Freelancer Features

Freelancers can:

- Register an account.
- Log in to the platform.
- Access the Freelancer Dashboard.
- Manage their profile.
- Browse available projects.
- View project details.
- Submit proposals.
- View submitted proposals.
- Check proposal status.
- View accepted project activity.

### Project Features

Clients can create projects containing information such as:

- Project Title
- Project Description
- Budget
- Deadline
- Project Type
- Required Skills

Freelancers can browse available projects and view project details.

### Proposal Features

Freelancers can submit proposals for available projects.

The proposal workflow allows:

- Freelancer to select a project.
- Freelancer to submit a proposal.
- Client to view received proposals.
- Client to review freelancer proposals.
- Client to accept a suitable proposal.
- Accepted proposal to be associated with the project.

---

## 4. Application Workflow

### Complete Client and Freelancer Workflow

```text
Client Registration
        ↓
Client Login
        ↓
Client Dashboard
        ↓
Post Project
        ↓
Project Available
        ↓
Freelancer Login
        ↓
Freelancer Dashboard
        ↓
Browse Projects
        ↓
View Project Details
        ↓
Submit Proposal
        ↓
Client Reviews Proposals
        ↓
Accept Proposal
        ↓
Project Assigned
        ↓
Freelancer Sees Accepted Project

Client Flow

Client Registration
        ↓
Client Login
        ↓
Client Dashboard
        ↓
Post Project
        ↓
View My Projects
        ↓
View Proposals
        ↓
Review Freelancer Proposal
        ↓
Accept Proposal


Freelancer Flow

Freelancer Registration
        ↓
Freelancer Login
        ↓
Freelancer Dashboard
        ↓
Browse Projects
        ↓
View Project Details
        ↓
Submit Proposal
        ↓
My Proposals
        ↓
Check Proposal Status
        ↓
View Accepted Project


Proposal Acceptance Flow
Freelancer Submits Proposal
            ↓
Client Receives Proposal
            ↓
Client Opens Proposals
            ↓
Client Reviews Proposal
            ↓
Client Accepts Proposal
            ↓
Proposal Status = Accepted
            ↓
Project Assigned
            ↓
Freelancer Can See Accepted Project


5. Project Structure
freelance-project-collaboration-platform/
│
├── backend/
│   ├── app.py
│   └── README.md
│
├── frontend/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── client-dashboard.html
│   ├── freelancer-dashboard.html
│   ├── profile.html
│   ├── projects.html
│   ├── project-details.html
│   ├── post-project.html
│   ├── proposals.html
│   ├── submit-proposal.html
│   ├── my-proposals.html
│   ├── script.js
│   └── style.css
│
├── docs/
│
├── testcases/
│
├── .gitignore
│
└── README.md
Frontend

The frontend/ folder contains the user interface of the Freelance Project Collaboration Platform.

It contains pages for:

Home
Registration
Login
Client Dashboard
Freelancer Dashboard
Profile
Projects
Project Details
Post Project
Proposals
Submit Proposal
My Proposals
Backend

The backend/ folder contains the server-side application and backend logic.

Documentation

The docs/ folder contains project-related documentation.

Test Cases

The testcases/ folder contains test cases used to verify the implemented features.

6. Technologies Used
Frontend Technologies
HTML5
CSS3
JavaScript
Backend Technologies
Python
Flask
Version Control
Git
GitHub
Development Tools
Visual Studio Code
Git Bash
Web Browser
Deployment
Amazon Web Services (AWS)
Amazon EC2
Linux Server
7. Project Setup
Prerequisites

The following software is required:

Git
Python
Visual Studio Code
Git Bash
A modern web browser