# Use the official Nginx image
FROM nginx:alpine

# Copy frontend files from the src directory
COPY ./src/templates/ /usr/share/nginx/html/
COPY ./src/static/ /usr/share/nginx/html/static/

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]