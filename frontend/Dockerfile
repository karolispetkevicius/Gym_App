# Pull base image
FROM node:20.11.1

# Set working directory
WORKDIR /app

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Install application dependencies
COPY package.json /app/package.json
RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent

# Add app
COPY . /app

# Start app
CMD ["npm", "start"]