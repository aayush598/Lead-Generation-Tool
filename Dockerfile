FROM python:3.12-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    tor \
    curl \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Setup working dir
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Copy Tor config
COPY torrc /etc/tor/torrc

# Expose Streamlit port
EXPOSE 8501

# Start Tor and Streamlit together
CMD tor & streamlit run app.py --server.port 8501 --server.enableCORS false
