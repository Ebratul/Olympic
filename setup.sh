#!/bin/bash

# Streamlit App Deployment Setup Script

# Install pip packages from requirements.txt
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set Streamlit configuration (optional)
echo "[server]" > ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "port = \$PORT" >> ~/.streamlit/config.toml
echo "address = \"0.0.0.0\"" >> ~/.streamlit/config.toml

echo "Setup completed."
