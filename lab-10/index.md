# Lab 10: Configuring NGINX - Complete Guide

## What is NGINX?

NGINX is a high-performance, open-source web server, reverse proxy, and load balancer designed for handling high concurrency with low memory usage.

### Use Cases:

| Use Case            | Description                                         |
| ------------------- | --------------------------------------------------- |
| **Web Server**      | Serves static and dynamic content efficiently       |
| **Reverse Proxy**   | Forwards client requests to backend servers         |
| **Load Balancer**   | Distributes traffic across multiple servers         |
| **API Gateway**     | Manages API requests and authentication             |
| **SSL Termination** | Handles HTTPS encryption to offload backend servers |
| **Caching**         | Stores responses to improve performance             |
| **Rate Limiting**   | Controls request rates to prevent abuse             |

---

## 1. Installation

```bash
# Update package list
sudo apt update

# Install NGINX
sudo apt install -y nginx

# Start NGINX service
sudo systemctl start nginx

# Enable NGINX to start on boot
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
```

---

## 2. Configuration File Structure

### Important Paths:

| Path                          | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| `/etc/nginx/nginx.conf`       | Main configuration file                    |
| `/etc/nginx/sites-available/` | Site configurations (available)            |
| `/etc/nginx/sites-enabled/`   | Site configurations (enabled via symlinks) |
| `/var/www/html/`              | Default web root directory                 |
| `/var/log/nginx/access.log`   | Access logs                                |
| `/var/log/nginx/error.log`    | Error logs                                 |

---

## 3. Creating a Basic Static Site

### Step 1: Create configuration file

```bash
sudo nano /etc/nginx/sites-available/my_site
```

### Step 2: Add server block configuration

```nginx
server {
    listen 8000;
    server_name localhost;
    root /var/www/html;
    index my_site.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Step 3: Create HTML content

```bash
sudo nano /var/www/html/my_site.html
```

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My NGINX Site</title>
  </head>
  <body>
    <h1>Welcome to My Site on Port 8000</h1>
    <p>NGINX is serving this page!</p>
  </body>
</html>
```

### Step 4: Enable the site (create symbolic link)

```bash
sudo ln -s /etc/nginx/sites-available/my_site /etc/nginx/sites-enabled/
```

### Step 5: Test and reload

```bash
# Test configuration for syntax errors
sudo nginx -t

# Reload NGINX to apply changes
sudo systemctl reload nginx
```

### Step 6: Verify

Open browser: `http://localhost:8000`

---

## 4. Reverse Proxy with proxy_pass

### Use Case: Forward requests to a backend API (e.g., Flask/Node.js running on port 5000)

### Configuration:

```bash
sudo nano /etc/nginx/sites-available/api_proxy
```

```nginx
server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Enable and reload:

```bash
sudo ln -s /etc/nginx/sites-available/api_proxy /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### proxy_pass Parameters Explained:

| Directive                            | Purpose                                          |
| ------------------------------------ | ------------------------------------------------ |
| `proxy_pass`                         | URL of the backend server to forward requests to |
| `proxy_set_header Host`              | Passes original host header to backend           |
| `proxy_set_header X-Real-IP`         | Passes client's real IP address                  |
| `proxy_set_header X-Forwarded-For`   | Chain of proxy IPs                               |
| `proxy_set_header X-Forwarded-Proto` | Original protocol (http/https)                   |

---

## 5. Load Balancing

### Configuration for distributing traffic across multiple backend servers:

```nginx
upstream backend_servers {
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
    server 127.0.0.1:5003;
}

server {
    listen 80;
    server_name loadbalancer.example.com;

    location / {
        proxy_pass http://backend_servers;
    }
}
```

### Load Balancing Methods:

| Method            | Directive                         | Description                             |
| ----------------- | --------------------------------- | --------------------------------------- |
| Round Robin       | (default)                         | Distributes requests evenly             |
| Least Connections | `least_conn;`                     | Sends to server with fewest connections |
| IP Hash           | `ip_hash;`                        | Same client always goes to same server  |
| Weighted          | `server 127.0.0.1:5001 weight=3;` | Higher weight = more requests           |

---

## 6. SSL/TLS Configuration (HTTPS)

```nginx
server {
    listen 443 ssl;
    server_name secure.example.com;

    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name secure.example.com;
    return 301 https://$server_name$request_uri;
}
```

---

## 7. Error Handling and Debugging

### Test configuration before reload:

```bash
sudo nginx -t
```

**Success output:**

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**Error output example:**

```
nginx: [emerg] unknown directive "servr" in /etc/nginx/sites-enabled/my_site:2
nginx: configuration file /etc/nginx/nginx.conf test failed
```

### View logs:

```bash
# Real-time error log
sudo tail -f /var/log/nginx/error.log

# Real-time access log
sudo tail -f /var/log/nginx/access.log

# Last 50 lines of error log
sudo tail -n 50 /var/log/nginx/error.log
```

### Common errors and fixes:

| Error                    | Cause                           | Fix                                            |
| ------------------------ | ------------------------------- | ---------------------------------------------- |
| `Address already in use` | Port conflict                   | Change listen port or stop conflicting service |
| `Permission denied`      | File/directory permissions      | `sudo chmod 755 /var/www/html`                 |
| `404 Not Found`          | Wrong root path or missing file | Check `root` directive and file existence      |
| `502 Bad Gateway`        | Backend server not running      | Start your backend application                 |

---

## 8. URL Rewriting and Redirects

```nginx
server {
    listen 80;
    server_name example.com;

    # Redirect /old-page to /new-page
    location /old-page {
        return 301 /new-page;
    }

    # Rewrite URLs (internal)
    location /api/v1 {
        rewrite ^/api/v1/(.*)$ /api/v2/$1 last;
    }

    # Redirect www to non-www
    if ($host = www.example.com) {
        return 301 https://example.com$request_uri;
    }
}
```

---

## 9. Rate Limiting

```nginx
# Define rate limit zone (in http block of nginx.conf)
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;

server {
    listen 80;
    server_name example.com;

    location /api/ {
        limit_req zone=mylimit burst=20 nodelay;
        proxy_pass http://127.0.0.1:5000;
    }
}
```

| Parameter          | Description                      |
| ------------------ | -------------------------------- |
| `zone=mylimit:10m` | 10MB shared memory for tracking  |
| `rate=10r/s`       | 10 requests per second limit     |
| `burst=20`         | Allow burst of 20 extra requests |
| `nodelay`          | Don't delay burst requests       |

---

## 10. Command Reference

| Task                        | Command                                    |
| --------------------------- | ------------------------------------------ |
| Install NGINX               | `sudo apt install -y nginx`                |
| Start service               | `sudo systemctl start nginx`               |
| Stop service                | `sudo systemctl stop nginx`                |
| Restart service             | `sudo systemctl restart nginx`             |
| Reload config (no downtime) | `sudo systemctl reload nginx`              |
| Check status                | `sudo systemctl status nginx`              |
| Enable on boot              | `sudo systemctl enable nginx`              |
| Test configuration          | `sudo nginx -t`                            |
| View error log              | `sudo tail -f /var/log/nginx/error.log`    |
| View access log             | `sudo tail -f /var/log/nginx/access.log`   |
| List enabled sites          | `ls -la /etc/nginx/sites-enabled/`         |
| Disable site                | `sudo rm /etc/nginx/sites-enabled/my_site` |

---

## 11. Complete Example: API Proxy with Static Files

```nginx
server {
    listen 80;
    server_name myapp.example.com;

    # Serve static files
    root /var/www/myapp;
    index index.html;

    # Static content
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API proxy to backend
    location /api/ {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket support
    location /ws/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## 12. Practical Demo Project

This lab includes a complete working demo with FastAPI backend and multiple NGINX configurations.

### Project Structure:

```
lab-10/
├── api/
│   └── main.py              # FastAPI server
├── html/
│   ├── static-index.html    # Static site HTML
│   └── webapp-index.html    # Web app with API calls
├── nginx-configs/
│   ├── 01-static-site.conf         # Port 8001 - Static files
│   ├── 02-reverse-proxy.conf       # Port 8002 - Simple reverse proxy
│   ├── 03-api-with-frontend.conf   # Port 8003 - Frontend + API proxy
│   ├── 04-load-balancer.conf       # Port 8004 - Load balancing
│   └── 05-rate-limiting.conf       # Port 8005 - Rate limited API
├── setup.sh                  # Automated setup script
└── nginx-config.md           # This documentation
```

### Quick Start:

```bash
# 1. Install dependencies
pip install fastapi uvicorn

# 2. Run setup (copies configs, creates directories)
cd lab-10
sudo ./setup.sh

# 3. Start FastAPI server
cd api
uvicorn main:app --host 127.0.0.1 --port 5000
```

### Demo Configurations:

| Port | Config File                 | Use Case                           |
| ---- | --------------------------- | ---------------------------------- |
| 8001 | `01-static-site.conf`       | Serve static HTML directly         |
| 8002 | `02-reverse-proxy.conf`     | Proxy all requests to FastAPI      |
| 8003 | `03-api-with-frontend.conf` | Static frontend + API proxy        |
| 8004 | `04-load-balancer.conf`     | Balance across 3 backend instances |
| 8005 | `05-rate-limiting.conf`     | API with rate limiting (5 req/sec) |

---

### Demo 1: Static Site (Port 8001)

```bash
# Test static site
curl http://localhost:8001/
```

No backend needed - NGINX serves files directly from `/var/www/html/static-demo`.

---

### Demo 2: Reverse Proxy (Port 8002)

```bash
# Start FastAPI
uvicorn main:app --host 127.0.0.1 --port 5000

# Test through proxy
curl http://localhost:8002/
curl http://localhost:8002/api/users
curl http://localhost:8002/api/health
```

Request flow: Browser → NGINX:8002 → FastAPI:5000

---

### Demo 3: Frontend + API (Port 8003)

```bash
# Open in browser
http://localhost:8003

# API calls work seamlessly
curl http://localhost:8003/api/users
```

Frontend served by NGINX, API calls proxied to backend. No CORS issues!

---

### Demo 4: Load Balancer (Port 8004)

```bash
# Start 3 backend instances
PORT=5001 uvicorn main:app --host 127.0.0.1 --port 5001 &
PORT=5002 uvicorn main:app --host 127.0.0.1 --port 5002 &
PORT=5003 uvicorn main:app --host 127.0.0.1 --port 5003 &

# Test load balancing - watch server_port change
for i in {1..6}; do
  curl -s http://localhost:8004/ | grep server_port
done
```

Expected output shows requests distributed across ports 5001, 5002, 5003.

---

### Demo 5: Rate Limiting (Port 8005)

```bash
# Rapid requests - some will be rejected (429)
for i in {1..20}; do
  echo -n "Request $i: "
  curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8005/api/users
done
```

Expected: First ~15 requests return 200, then 429 (Too Many Requests).

---

## Summary

NGINX competencies demonstrated:

1. **Installation** - apt package manager
2. **Configuration structure** - sites-available/sites-enabled pattern
3. **Static content serving** - root, index, try_files directives
4. **Reverse proxy** - proxy_pass to backend APIs
5. **Load balancing** - upstream blocks with multiple servers
6. **SSL/TLS** - HTTPS configuration
7. **Error handling** - nginx -t, log analysis
8. **URL rewriting** - redirects and rewrites
9. **Rate limiting** - request throttling
10. **Symbolic links** - enabling/disabling sites

---

## FastAPI Server Endpoints

The included FastAPI server (`api/main.py`) provides:

| Endpoint          | Method | Description                |
| ----------------- | ------ | -------------------------- |
| `/`               | GET    | Root - returns server info |
| `/api/health`     | GET    | Health check               |
| `/api/users`      | GET    | List all users             |
| `/api/users/{id}` | GET    | Get user by ID             |
| `/api/echo`       | POST   | Echo back JSON data        |

Each response includes `server_port` to identify which backend served the request (useful for load balancing demo).
