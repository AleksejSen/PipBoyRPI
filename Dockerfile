FROM jozo/pyqt5

# Install npm
RUN apt-get update && apt-get install -y npm

# Install nodemon globally
RUN npm install -g nodemon
