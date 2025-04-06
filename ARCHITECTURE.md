# System Architecture

This document outlines the architecture of the Restaurant-Scraper-Rag-Bot application.

## Overview

<<<<<<< HEAD
The unbasa-eats Restaurant RAG Chatbot is designed to provide users with information about restaurants, their menus, and features using a Retrieval-Augmented Generation (RAG) approach. The architecture consists of several components that work together to scrape restaurant data, process it into a knowledge base, and serve it through a FastAPI backend.
=======
The application follows a microservices-oriented approach, separating concerns between data collection, backend processing, and frontend presentation. It leverages Retrieval-Augmented Generation (RAG) to provide intelligent responses based on scraped restaurant data.
>>>>>>> 23119e6 (refactor: update architecture documentation and enhance README overview and features)

![Daigram](https://www.mermaidchart.com/raw/2da8c3bd-a959-4bb3-8992-199bc7b2c6de?theme=light&version=v0.1&format=svg)

## Components

1.  **Web Scraper(s) (Python):**
    *   Responsible for fetching raw data (restaurant details, menus, reviews, etc.) from specified external sources (websites, APIs).
    *   May consist of multiple scripts or modules tailored to different sources.
    *   Outputs raw or semi-structured data.

2.  **Data Processing Script (Python):**
    *   Takes raw data from the scraper(s).
    *   Cleans, transforms, and structures the data into a usable format (e.g., JSON objects, database records).
    *   Populates the Data Storage components.
    *   Generates embeddings for relevant text data (e.g., menu descriptions, reviews) and populates the RAG Knowledge Base.

3.  **Data Storage:**
    *   **Primary Database (e.g., PostgreSQL, SQLite):** Stores structured restaurant information, menus, user data (if applicable).
    *   **Vector Database (e.g., ChromaDB, FAISS, Pinecone):** Stores text embeddings and metadata for efficient similarity search required by the RAG engine. This forms the core of the Knowledge Base.

4.  **FastAPI Backend (Python):**
    *   Provides a RESTful API and WebSocket endpoints for the frontend.
    *   Handles user requests (e.g., searching restaurants, asking questions, chatting).
    *   Interacts with the Data Storage to retrieve/store information.
    *   Interfaces with the RAG Engine to answer natural language queries.
    *   Manages chat sessions and context via WebSockets.
    *   Handles authentication and authorization if implemented.

5.  **RAG Engine / Knowledge Base (Python Libraries):**
    *   Integrated within the FastAPI backend or as a separate service.
    *   Receives user queries (natural language questions).
    *   Converts the query into an embedding.
    *   Searches the Vector Database for relevant document chunks (context).
    *   Combines the original query and the retrieved context.
    *   Uses a Large Language Model (LLM) (e.g., via OpenAI API, local model) to generate a final answer based on the query and context.

6.  **React Frontend (JavaScript/TypeScript):**
    *   Provides the user interface (UI) for interacting with the application.
    *   Communicates with the FastAPI backend via HTTP requests and WebSockets.
    *   Displays restaurant information, menus, and chat interfaces.
    *   Manages client-side state.

7.  **Docker:**
    *   Containerizes the different components (Frontend, Backend, Scraper, etc.) for consistent development, testing, and deployment environments.
    *   `docker-compose.yml` defines the services and their interactions.

8.  **Deployment Platform (Render):**
    *   The cloud platform where the containerized application components (Frontend, Backend, Databases) are hosted and made publicly accessible via `https://restaurant-scraper-rag-bot.onrender.com/`.

## Data Flow Example (User Query)

<<<<<<< HEAD
- **/ARCHITECTURE.md**: This file, providing an overview of the architecture.

- **config.py**: Configuration settings for the application.

- **docker-compose.yml**: Docker Compose file for orchestrating multi-container applications.

- **Dockerfile**: Dockerfile for containerizing the application.

- **main.py**: Entry point for the application, orchestrating the scraping and knowledge base building.

- **/pyproject.toml**: Configuration file for the project.

- **README.md**: Overview and instructions for the project.

- **requirements.txt**: Lists the dependencies required for the project.

- **SETUP.md**: Instructions for setting up the development environment.

## Architecture Diagram
![Architecture Diagram](assets/architecture.png)

## Components Description

### API

- **backend.py**: Sets up the FastAPI server, handles incoming requests, and serves static files. It defines endpoints for chatting with the bot and retrieving restaurant information.

### Chatbot

- **chatbot.py**: Implements the main chatbot logic, integrating the retriever and generator components.
- **conversation.py**: Manages the conversation history for each user session.
- **generator.py**: Uses AI to generate responses based on retrieved information.
- **retriever.py**: Retrieves relevant documents from the knowledge base based on user queries.

### Knowledge Base

- **indexer.py**: Creates an index for quick lookups of restaurant data.
- **processor.py**: Processes raw data into a structured format suitable for the knowledge base.

### Scraper

- **scraper.py**: Contains the logic for scraping restaurant data from specified URLs.
- **helper.py**: Provides utility functions for cleaning and processing scraped data.

### Utilities

- **exceptions.py**: Defines custom exceptions for error handling.
- **logger.py**: Configures logging for the application.

## Conclusion

The unbasa-eats Restaurant RAG Chatbot is a modular and extensible application that leverages web scraping, AI, and a structured knowledge base to provide users with accurate and relevant restaurant information. The architecture is designed to be user-friendly and maintainable, allowing for easy updates and enhancements in the future.
=======
1.  User types a question (e.g., "Which restaurants have gluten-free pasta?") into the React Frontend.
2.  Frontend sends the question via an API call (HTTP or WebSocket) to the FastAPI Backend.
3.  Backend receives the request and passes the query to the RAG Engine.
4.  RAG Engine generates an embedding for the query.
5.  RAG Engine queries the Vector Database using the embedding to find relevant text chunks (e.g., menu items mentioning "gluten-free pasta", restaurant descriptions mentioning dietary options).
6.  RAG Engine retrieves the relevant chunks (context).
7.  RAG Engine sends the original query and the retrieved context to an LLM.
8.  LLM generates a response based on the provided information.
9.  RAG Engine returns the generated response to the FastAPI Backend.
10. Backend sends the response back to the React Frontend.
11. Frontend displays the answer to the user.
>>>>>>> 23119e6 (refactor: update architecture documentation and enhance README overview and features)
