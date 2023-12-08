# 🎮 NerdvanaAPI 🎮

This is the repository for NerdvanaAPI, designed for those who love video games!

## Introduction

Welcome to the Video Game API, your one-stop solution for accessing a comprehensive database of video games, fetching prices from various stores, receiving personalized game recommendations through machine learning, and setting up alerts for price drops. The game database is sourced from the TwitchAPI, ensuring up-to-date and accurate information.

### Key Features

- **Game Database:** Built from the TwitchAPI, providing detailed information about a wide range of video games.

- **Price Comparison:** Search for the cheapest prices for games in popular online stores.

- **Recommendation System:** Utilizes machine learning to offer personalized game recommendations based on user preferences.

- **Alert System:** Set up email alerts to be notified when a game reaches a specified lower price.

## Stack

### Backend

- Django REST framework for a powerful API
- Django ORM for interacting with the database
- RabbitMQ and Celery for async tasks
- Celery Beat for scheduled tasks
- PostgreSQL

## Running the API

### Prerequisites

Make sure you have the following installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python (3.10 or higher)
- pip (Python package installer)

### Installation

To run the Nerdvana API locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Marcostbo/NerdvanaAPI.git
   cd NerdvanaAPI
   ```
2. Set Up Docker Compose
   ```bash
   docker-compose up -d
   ```
   This command will start the following Docker containers in the background:
   - API Container: Hosting the Django application for the Video Game API.
   - RabbitMQ Container: A message broker facilitating communication between components.
   - Celery Worker for E-mail Container: Handling asynchronous tasks to send emails.
   - Celery Worker for Game Price Alert Cron Container: Managing periodic tasks for game price alerts.
3. Migrate Database
   ```bash
   docker-compose exec api python manage.py migrate
   ```
4. Create Superuser (Optional, but recommended to use Django Admin)
   ```bash
   docker-compose exec api python manage.py createsuperuser
   ```
   Follow the prompts to create a superuser account.
5. Access the API
   Open your web browser and navigate to http://localhost:8000 to access the API.

6. Stop the Containers
   ```bash
   docker-compose down
   ```
This will stop and remove the Docker containers.

Feel free to explore the various features and functionalities of NerdvanaAPI!
