# ==============================================================================
# OpenCV Studio - Frontend Dockerfile (Multi-stage Build: Vite + Nginx)
# ==============================================================================

# Stage 1: Build the React SPA bundle
FROM node:22-alpine AS builder

WORKDIR /app

# Copy dependency definitions
COPY package*.json ./

# Install npm dependencies
RUN npm ci

# Copy application source code
COPY . .

# Build production bundle using Vite
RUN npm run build

# Stage 2: Serve the production assets with Nginx
FROM nginx:alpine

# Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy built artifacts from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration with reverse proxy for /api/
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
