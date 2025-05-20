# Customer Support Chatbot

## Overview

This project is a full-stack chatbot solution. The aim is to optimize sales processes for companies in construction and home materials. The chatbot interacts with a product catalog dataset and improves the customer experience by providing relevant, context-driven responses.

Two integration approaches were explored for the chatbot:
1. **Embedding Database**: Used to fetch relevant context from the CSV but had limitations in performance and flexibility.
2. **LangChain**: Chosen as the primary framework for connecting the Language Learning Model (LLM) to the product catalog dataset, enabling dynamic context retrieval, chat history integration, and prompt refinement.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Provided Resources](#provided-resources)
- [Task Implementation](#task-implementation)
- [Environment Variables](#environment-variables)
- [Functionality Overview](#functionality-overview)
- [Contributing](#contributing)

## Installation

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/amirzarandi/internship-case-study
   cd internship-case-study
   ```

### 2. **Install Python and Pipenv**
   - Ensure Python is installed on your system.
   - Install Pipenv for virtual environment management:
     ```bash
     pip install pipenv
     ```

### 3. **Install Dependencies**
   - Create and activate the virtual environment using Pipenv:
     ```bash
     pipenv install
     pipenv shell
     ```
   - This will install all the required dependencies for the backend.

## Setup

### 1. **Backend Setup**
   - The backend uses Flask to create an LLM-powered chat endpoint connected to the product catalog dataset.
   - To set up the backend, run:
     ```bash
     flask run
     ```
   - Make sure to set up the environment variable `OPENAI_API_KEY` for LLM integration (see [Environment Variables](#environment-variables) below).

### 2. **Database Setup**
   - The provided Python scripts initialize a database storing product catalog data from the CSV file.
   - To set up the database, run:
     ```bash
     python add_csv_knowledge_langchain.py
     python add_csv_knowledge_embed.py
     ```

### 3. **Frontend Setup**
   - The frontend is based on a React boilerplate template provided by Instalily.
   - You can run it using npm (Node Package Manager):
     ```bash
     npm install
     npm run
     ```
   - The frontend has been modified to enhance user experience and visuals, providing better interaction with the chatbot.

## Running the Project

### 1. **Start the Backend**
   - Ensure the virtual environment is active, and the `OPENAI_API_KEY` is set:
     ```bash
     flask run
     ```

### 2. **Start the Frontend**
   - From the frontend directory, start the React application:
     ```bash
     npm run
     ```

## Provided Resources

This case study includes:
1. **Product Catalog Dataset**: A CSV file containing product details that the chatbot uses for context.
2. **Frontend Boilerplate Template**: A React-based template for the chat interface, which has been modified to enhance user experience.

## Task Implementation

The task was to build a full-stack chatbot solution with the following criteria:
1. **Backend Chat Endpoint**:
   - Developed using Flask and LangChain to connect the product catalog CSV data to the LLM.
   - LangChain dynamically retrieves context from the CSV, incorporates chat history, and refines prompts based on user input.
2. **Integrated Frontend**:
   - The frontend was customized from the provided boilerplate to improve the user interface, interaction flow, and visual design.
   - User-friendly elements were added to make the chat experience more intuitive.

## Environment Variables

- **OPENAI_API_KEY**: Required for interacting with the OpenAI LLM.
  - Set this variable in your terminal or environment file before running the backend:
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```

## Functionality Overview

### 1. **LangChain-based Contextual Interaction**
   - The chatbot retrieves context from the CSV using LangChain, allowing it to process user inputs effectively.
   - The process includes:
     1. **Context Retrieval**: Fetches up to 10 relevant rows related to the user’s query.
     2. **History Integration**: Adds chat history to maintain continuity over multiple interactions.
     3. **User Input**: Combines the input with context to refine the final prompt.
     4. **LLM Querying**: Queries the LLM for a refined response.

### 2. **Embedding Database (Initial Approach)**
   - Initially, embeddings were used for context retrieval from the CSV, but this approach was slower and less flexible than LangChain.

## Contributing

Feel free to open issues or submit pull requests for improvements, bug fixes, or new features.
