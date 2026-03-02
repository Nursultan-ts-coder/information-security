#!/bin/bash
# =============================================================================
# NGINX Demo Setup Script
# =============================================================================
# This script sets up all NGINX configurations for the demo
# Run with: sudo ./setup.sh
# =============================================================================

set -e

echo "=========================================="
echo "NGINX Demo Setup"
echo "=========================================="

# Create directories
echo "[1/5] Creating directories..."
mkdir -p /var/www/html/static-demo
mkdir -p /var/www/html/webapp

# Copy HTML files
echo "[2/5] Copying HTML files..."
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cp "$SCRIPT_DIR/html/static-index.html" /var/www/html/static-demo/index.html
cp "$SCRIPT_DIR/html/webapp-index.html" /var/www/html/webapp/index.html

# Set permissions
echo "[3/5] Setting permissions..."
chmod -R 755 /var/www/html/static-demo
chmod -R 755 /var/www/html/webapp

# Copy NGINX configs
echo "[4/5] Copying NGINX configurations..."
cp "$SCRIPT_DIR/nginx-configs/01-static-site.conf" /etc/nginx/sites-available/static-demo
cp "$SCRIPT_DIR/nginx-configs/02-reverse-proxy.conf" /etc/nginx/sites-available/api-proxy
cp "$SCRIPT_DIR/nginx-configs/03-api-with-frontend.conf" /etc/nginx/sites-available/webapp
cp "$SCRIPT_DIR/nginx-configs/04-load-balancer.conf" /etc/nginx/sites-available/loadbalancer
cp "$SCRIPT_DIR/nginx-configs/05-rate-limiting.conf" /etc/nginx/sites-available/ratelimit

# Create symlinks
echo "[5/5] Enabling sites..."
ln -sf /etc/nginx/sites-available/static-demo /etc/nginx/sites-enabled/
ln -sf /etc/nginx/sites-available/api-proxy /etc/nginx/sites-enabled/
ln -sf /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/
ln -sf /etc/nginx/sites-available/loadbalancer /etc/nginx/sites-enabled/
ln -sf /etc/nginx/sites-available/ratelimit /etc/nginx/sites-enabled/

# Test and reload NGINX
echo "=========================================="
echo "Testing NGINX configuration..."
nginx -t

echo "Reloading NGINX..."
systemctl reload nginx

echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Available endpoints:"
echo "  - Static Site:      http://localhost:8001"
echo "  - Reverse Proxy:    http://localhost:8002"
echo "  - Webapp + API:     http://localhost:8003"
echo "  - Load Balancer:    http://localhost:8004"
echo "  - Rate Limited:     http://localhost:8005"
echo ""
echo "Don't forget to start the FastAPI server:"
echo "  cd api && uvicorn main:app --host 127.0.0.1 --port 5000"
echo "=========================================="
