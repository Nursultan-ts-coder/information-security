# Basic Nginx Server Setup

This guide covers installing, configuring, and verifying a basic Nginx server on Debian/Ubuntu, plus notes for macOS (Homebrew).

## Install and Start (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install -y nginx

# Service status / enable / start
sudo systemctl status nginx --no-pager
sudo systemctl enable nginx
sudo systemctl start nginx
```

## Key Paths

- Config: `/etc/nginx/nginx.conf`
- Sites available: `/etc/nginx/sites-available/`
- Sites enabled: `/etc/nginx/sites-enabled/`
- Web root (default): `/var/www/html`
- Logs: `/var/log/nginx/access.log`, `/var/log/nginx/error.log`

## Create a Simple Server Block

```bash
sudo mkdir -p /var/www/example
echo '<h1>Hello from Nginx</h1>' | sudo tee /var/www/example/index.html

cat << 'EOF' | sudo tee /etc/nginx/sites-available/example
server {
    listen 80;
    server_name _;
    root /var/www/example;
    index index.html;
    access_log /var/log/nginx/example.access.log;
    error_log  /var/log/nginx/example.error.log;
    location / {
        try_files $uri $uri/ =404;
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/example /etc/nginx/sites-enabled/example
sudo rm -f /etc/nginx/sites-enabled/default

# Test config and reload
sudo nginx -t
sudo systemctl reload nginx
```
