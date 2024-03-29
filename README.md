<h1 align="center">Rogalowski's Project <img src="https://komarev.com/ghpvc/?username=rogalowski&label=Profile%20views&color=0e75b6&style=flat" alt="rogalowski" /></h1>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/jacek-rogowski" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="jacek-rogowski" height="30" width="40" /></a>
<a href="https://instagram.com/jack_jrogow" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="jack_jrogow" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://babeljs.io/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/babeljs/babeljs-icon.svg" alt="babel" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://webpack.js.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/d00d0969292a6569d45b06d3f350f463a0107b0d/icons/webpack/webpack-original-wordmark.svg" alt="webpack" width="40" height="40"/> </a> </p>

![](http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=rogalowski&theme=solarized)

<p>  <img align="center" src="https://github-readme-stats.vercel.app/api?username=rogalowski&show_icons=true&locale=en" alt="rogalowski" /> &nbsp; <img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=rogalowski&show_icons=true&locale=en&layout=compact" alt="rogalowski" /> </p>

<h1 align="center">Ticketing System Project</h1>

Database design: https://sqldbd.com/pub/p48x91cfe82b422664b/ticket-system-db.html
Trello Kanban Project Manager: https://trello.com/b/xIr9IQb3 https://trello.com/b/xIr9IQb3/ticketing-system
Visual Design: https://app.moqups.com/cL6fXRN3Sn/edit/page/aafa9bb4b

# Basic Overview

Please check published aplication: https://ticketing.rogalowski.uk/
Placed on mikr.us VPS, Ubuntu 20.04, nginx, gunicorn: https://mikr.us/

System for managing reports on technical problems of users (Trouble Ticket). The system contains
Four sections, login system, adding new tickets depending on the type of problem and department which refers to
Views of users, tickets and its editing.

# Features:

-   Login panel
-   Company Information Ticket System
-   statistics on the amount of TT on each of the departments (after clicking on the department passes to the TT queue)
-   Detailed User's logged in
-   Integrated test by pytest library

TT content:

-   ID TT
-   Title
-   Description
-   status
-   Priority (Low, Medium, High, ASAP)
-   the date of creation
-   Date of the end (after adding the resolved status, also add a comment)
-   Correspondence for employees with the date of issue, by whom
-   the department to which TT is issued
-   Category of problem
-   assignment
-   Who staged TT and from which department
-   Possibility to add files / photos (optional)
-   Ticket's change history (optional)

STATUS = (
('Not Acknowledged', 'Not Acknowledged'),
('Pending ', 'Pending'),
('Pending Requestor Information', 'Pending Requestor Information'),
('Work in Progress', 'Work in Progress'),
('Blocked', 'Blocked'),
('Dropped', 'Dropped'),
('Resolved Successfull', 'Resolved Successfull'),
)

PRIORITY = (
('Low', 'Low'),
('Medium', 'Medium'),
('High', 'High'),
('ASAP', 'ASAP'),
)

DEPARTMENTS = (
('Test', 'Test'),
('IT', 'IT'),
('HR', 'HR'),
('PM', 'PM'),
('F&B', 'F&B'),
)

CATEGORY_PROBLEM = (
('Desktops/Software', 'Desktops/Software'),
('Pherieral devices', 'Pherieral devices'),
('Mobile Devices', 'Mobile Devices'),
('Network/Infrastructure', 'Network/Infrastructure'),
('Work Schedule', 'Work Schedule'),
('Hiring Process', 'Hiring Process'),
('Employee', 'Employee'),
('Documents', 'Documents'),
('Project realization', 'Project realization'),
('Improvement', 'Improvement'),
('Inspection', 'Inspection'),
('Invoices', 'Invoices'),
('Payment', 'Payment'),
('Delegation payment', 'Delegation payment'),
('Orders', 'Orders'),
('Other', 'Other'),
)

# Tech Stack:

    Python 3.8
    Django 3.0.6
    Postgres 13.7
    Docker 20.10.17
    Jinja

# Configuration:

Clone repo & create a virtual environment and activate

    1 pip install virtalenv
    2 python -m virtualenv venv  --python=/usr/bin/python3.8
    3 cd envname\scripts\activate
    4 cd into project folder
    5 pip install -r requirements.txt
    6 install & run postgres database service (docker: sudo docker run --rm --name databasepostgres  -p 5433:5432 -e POSTGRES_PASSWORD=coderslab postgres:13.7)
    7 create ticketing_db database && import last dump from folder project or python manage.py migrate
    9 python manage.py runserver

    TEST PASSES FROM DATABASE:
    login: it_jacek password: admin
    login: admin password: admin

# DOCKERIZED APP USE:

sudo USER_ID=1000 GROUP_ID=1000 docker-compose up --build
and update database by:
sudo docker exec -i postgres_db psql -U postgres -d postgres < dump_11-09-2021_19_03_34.sql
