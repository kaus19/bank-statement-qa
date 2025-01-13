# Use the official Jupyter base image
FROM jupyter/base-notebook:python-3.11.6

# Set environment variables for Jupyter
ENV JUPYTER_ENABLE_LAB=yes

# Install dependencies first
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt || cat /tmp/requirements.txt

# Expose the default Jupyter port
EXPOSE 8888

# Set the default working directory
WORKDIR /workspace

# Copy project files into the container
COPY . /workspace