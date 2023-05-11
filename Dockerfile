# Base Image
FROM node:14-alpine

# Work directory set to /app inside container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install envrinment dependencies
RUN npm install --production

# Copy the application code to the docker container
COPY . .

# Setting up the environment variables
ENV PORT=5000
ENV NODE_ENV=production

# Expose port 3000 for the Node JS application
EXPOSE 5000

# Run/Start the application inside the container
CMD [ "npm", "start" ]
