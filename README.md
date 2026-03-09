# Distributed URL Shortener System

A backend system that converts long URLs into short links and redirects users to the original destination.

## Tech Stack

- Python
- FastAPI
- REST APIs
- Backend Service Architecture

## System Architecture

User → FastAPI API → URL Shortener Service → Storage

## Features

- Generate short URLs
- Redirect short URLs to original links
- REST API based backend
- Modular service architecture

## Example API

Create short URL

POST /shorten

{
 "url": "https://google.com"
}

Response

{
 "short_url": "http://localhost:8000/Ab23xY"
}

Redirect

GET /Ab23xY

Redirects to original URL.

## Project Structure

```
url-shortener-system
│
├── api
│   └── main.py
│
├── services
│   └── shortener.py
│
├── database
│   ├── db.py
│   └── models.py
│
├── cache
│   └── redis_client.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```
