
# Flask & Redis Visitor Counter

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview
This project is a simple Flask web application that uses Redis to count and store the number of times a website has been visited. Each visit updates the count, which is displayed on the homepage.

## Project Structure
```
./
├── app/                    # Flask application folder
│   ├── app.py              # Main Flask application code
│   ├── requirements.txt    # List of Python dependencies
│   └── Dockerfile          # Docker configuration for the Flask app
├── redis/                  # Redis configuration folder
│   └── docker-compose.yml         #  Docker Compose configuration file
└── README.md               # Project documentation
```

## Prerequisites
To run this project locally, ensure you have the following installed:

- Docker (version 20.10+)
- Docker Compose (version 1.29+)
- Python 3.x

## Setup and Installation
Follow these steps to set up and run the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Muhammadatef/flask_with_redis_using_docker.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd <repository_folder>
   ```

3. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```

4. **Verify that the app is running**:
   Open your browser and go to `http://localhost:5000`. You should see a message displaying the current visit count.

## Usage
1. **Start the application**:
   ```bash
   docker-compose up
   ```

2. **Visit the homepage**:
   Open your browser and go to `http://localhost:5000`.

3. **Stop the application**:
   Press `Ctrl + C` to stop the Docker containers or use:
   ```bash
   docker-compose down
   ```

## Endpoints
- **GET `/`**: Displays the number of visits to the website in an incremented sentence.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **Redis**: An in-memory key-value store used for counting visits.
- **Docker**: Used to containerize the application.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

## Troubleshooting
If you encounter any issues, try the following:

1. **Check if Docker is running**:
   ```bash
   docker ps
   ```

2. **Restart the containers**:
   ```bash
   docker-compose down && docker-compose up --build
   ```

3. **Inspect logs**:
   ```bash
   docker-compose logs
   ```

## License
This project is licensed under the MIT License.
