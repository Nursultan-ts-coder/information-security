# Basic NGINX Server Setup (Compact)

## What NGINX Is Used For
- Web server (static/dynamic content)
- Reverse proxy & API gateway (proxy_pass)
- Load balancer
- SSL/TLS termination
- Caching, rate limiting

## Quick Setup (Ubuntu/Debian)

1) Install
```bash
sudo apt update
sudo apt install -y nginx
```

2) Create a site config
```bash
sudo tee /etc/nginx/sites-available/my_site >/dev/null <<'EOF'
server {
    listen 8000;
    server_name localhost;
    root /var/www/html;
    index my_site.html;

    location / {
        try_files $uri $uri/ =404;
        # proxy_pass http://127.0.0.1:5000;  # enable for API/backend
    }
}
EOF
```

3) Add content
```bash
echo '<div>My site on 8000</div>' | sudo tee /var/www/html/my_site.html
```

4) Enable the site
```bash
sudo ln -s /etc/nginx/sites-available/my_site /etc/nginx/sites-enabled/
```

5) Test and reload
```bash
sudo nginx -t
sudo systemctl reload nginx
```

6) Verify
- Browser: http://localhost:8000
- Logs (errors): `sudo tail -f /var/log/nginx/error.log`

## Reference Command Table

| Task | Command |
|------|---------|
| Install NGINX | `sudo apt install -y nginx` |
| Service status | `sudo systemctl status nginx` |
| Enable on boot | `sudo systemctl enable nginx` |
| Start / Stop / Reload | `sudo systemctl start nginx`<br>`sudo systemctl stop nginx`<br>`sudo systemctl reload nginx` |
| Test config | `sudo nginx -t` |
| Site config path | `/etc/nginx/sites-available/` |
| Enable site (symlink) | `sudo ln -s /etc/nginx/sites-available/<site> /etc/nginx/sites-enabled/` |
| Default web root | `/var/www/html` |
| Access log | `/var/log/nginx/access.log` |
| Error log | `/var/log/nginx/error.log` |

### proxy_pass (for APIs/backends)
Uncomment and adjust inside `location / { ... }`:
```nginx
proxy_pass http://127.0.0.1:5000;
```
Reload after changes: `sudo systemctl reload nginx`