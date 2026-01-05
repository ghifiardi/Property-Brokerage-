# Deployment Guide

## AI-Powered Property Brokerage System - Deployment Instructions

This guide provides step-by-step instructions for deploying the AI-Powered Property Brokerage System in various environments.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Development Setup](#local-development-setup)
3. [Production Deployment](#production-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Cloud Deployment](#cloud-deployment)
6. [Configuration](#configuration)
7. [Monitoring & Maintenance](#monitoring--maintenance)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

**Minimum Requirements:**
- CPU: 2 cores
- RAM: 4 GB
- Storage: 10 GB
- OS: Linux, macOS, or Windows

**Recommended Requirements:**
- CPU: 4+ cores
- RAM: 8+ GB
- Storage: 20+ GB
- OS: Linux (Ubuntu 20.04+ or CentOS 8+)

### Software Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Git
- OpenAI API key (for AI features)
- (Optional) Docker for containerized deployment
- (Optional) Redis for Celery task queue

---

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ghifiardi/Property-Brokerage-.git
cd Property-Brokerage-
```

### 2. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` file with your configuration:

```env
OPENAI_API_KEY=your_actual_api_key_here
DATABASE_URL=sqlite:///property_brokerage.db
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### 5. Run the Application

```bash
python app.py
```

The system should now be running and display the initialization screen.

---

## Production Deployment

### 1. Server Setup

**Update system packages:**
```bash
sudo apt update
sudo apt upgrade -y
```

**Install Python and required packages:**
```bash
sudo apt install python3.8 python3-pip python3-venv git -y
```

### 2. Create Application User

```bash
sudo useradd -m -s /bin/bash propertybroker
sudo su - propertybroker
```

### 3. Deploy Application

```bash
cd /home/propertybroker
git clone https://github.com/ghifiardi/Property-Brokerage-.git
cd Property-Brokerage-

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Production Environment

```bash
cp .env.example .env
nano .env
```

Set production values:
```env
FLASK_ENV=production
DATABASE_URL=postgresql://user:password@localhost/propertydb
OPENAI_API_KEY=your_production_api_key
SECRET_KEY=generate_strong_random_key_here
```

### 5. Setup Systemd Service

Create service file:
```bash
sudo nano /etc/systemd/system/propertybroker.service
```

Add the following content:
```ini
[Unit]
Description=Property Brokerage AI System
After=network.target

[Service]
User=propertybroker
Group=propertybroker
WorkingDirectory=/home/propertybroker/Property-Brokerage-
Environment="PATH=/home/propertybroker/Property-Brokerage-/venv/bin"
ExecStart=/home/propertybroker/Property-Brokerage-/venv/bin/python app.py

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable propertybroker
sudo systemctl start propertybroker
sudo systemctl status propertybroker
```

### 6. Setup Nginx Reverse Proxy (Optional)

Install Nginx:
```bash
sudo apt install nginx -y
```

Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/propertybroker
```

Add configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/propertybroker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 7. Setup SSL with Let's Encrypt (Recommended)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## Docker Deployment

### 1. Create Dockerfile

Create `Dockerfile` in the project root:

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production

EXPOSE 5000

CMD ["python", "app.py"]
```

### 2. Create docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped

  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"
    restart: unless-stopped
```

### 3. Build and Run

```bash
docker-compose build
docker-compose up -d
```

### 4. View Logs

```bash
docker-compose logs -f app
```

### 5. Stop Services

```bash
docker-compose down
```

---

## Cloud Deployment

### AWS EC2 Deployment

1. **Launch EC2 Instance:**
   - Choose Ubuntu 20.04 LTS
   - Instance type: t2.medium or higher
   - Configure security group (ports 22, 80, 443)

2. **Connect to Instance:**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Follow Production Deployment steps** from above

### Google Cloud Platform (GCP)

1. **Create Compute Engine Instance:**
```bash
gcloud compute instances create propertybroker \
    --image-family=ubuntu-2004-lts \
    --image-project=ubuntu-os-cloud \
    --machine-type=n1-standard-2 \
    --zone=us-central1-a
```

2. **SSH to instance:**
```bash
gcloud compute ssh propertybroker --zone=us-central1-a
```

3. **Follow Production Deployment steps**

### Heroku Deployment

1. **Create Procfile:**
```
web: python app.py
```

2. **Create runtime.txt:**
```
python-3.8.12
```

3. **Deploy to Heroku:**
```bash
heroku create propertybroker-ai
heroku config:set OPENAI_API_KEY=your_key
heroku config:set SECRET_KEY=your_secret
git push heroku main
```

---

## Configuration

### Database Configuration

**SQLite (Development):**
```env
DATABASE_URL=sqlite:///property_brokerage.db
```

**PostgreSQL (Production):**
```env
DATABASE_URL=postgresql://username:password@host:5432/database
```

### OpenAI API Configuration

Get your API key from: https://platform.openai.com/api-keys

```env
OPENAI_API_KEY=sk-...your-key-here...
```

### Email Configuration (SMTP)

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### Redis Configuration (for Celery)

```env
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

## Monitoring & Maintenance

### Log Management

**View system logs:**
```bash
sudo journalctl -u propertybroker -f
```

**Application logs location:**
```
/home/propertybroker/Property-Brokerage-/logs/
```

### Performance Monitoring

Install monitoring tools:
```bash
pip install prometheus-flask-exporter
```

### Database Backup

**Automated backup script:**
```bash
#!/bin/bash
BACKUP_DIR="/home/propertybroker/backups"
DATE=$(date +%Y%m%d_%H%M%S)
sqlite3 property_brokerage.db ".backup '$BACKUP_DIR/backup_$DATE.db'"
```

Add to crontab:
```bash
0 2 * * * /home/propertybroker/backup.sh
```

### Updates and Upgrades

```bash
cd /home/propertybroker/Property-Brokerage-
git pull origin main
source venv/bin/activate
pip install -r requirements.txt --upgrade
sudo systemctl restart propertybroker
```

---

## Troubleshooting

### Common Issues

**1. Module Import Errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**2. Database Connection Issues**
```bash
# Check database URL
echo $DATABASE_URL

# Test database connection
python -c "from sqlalchemy import create_engine; engine = create_engine('$DATABASE_URL'); print('Connected!')"
```

**3. OpenAI API Errors**
```bash
# Verify API key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**4. Permission Issues**
```bash
# Fix file permissions
sudo chown -R propertybroker:propertybroker /home/propertybroker/Property-Brokerage-
chmod +x app.py
```

**5. Service Won't Start**
```bash
# Check service status
sudo systemctl status propertybroker

# View detailed logs
sudo journalctl -u propertybroker -n 100 --no-pager
```

### Debug Mode

Enable debug mode for detailed error messages:
```env
FLASK_ENV=development
FLASK_DEBUG=1
```

**Note:** Never use debug mode in production!

### Getting Help

1. Check logs first: `journalctl -u propertybroker`
2. Review error messages carefully
3. Check GitHub issues: https://github.com/ghifiardi/Property-Brokerage-/issues
4. Contact support with:
   - Error messages
   - System information
   - Steps to reproduce

---

## Security Best Practices

1. **Always use HTTPS in production**
2. **Keep SECRET_KEY secure and random**
3. **Never commit .env file to Git**
4. **Regularly update dependencies**
5. **Use strong database passwords**
6. **Implement rate limiting**
7. **Enable firewall (ufw/iptables)**
8. **Regular security audits**

### Enable Firewall

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

---

## Performance Optimization

### 1. Enable Caching

Install Redis:
```bash
sudo apt install redis-server -y
```

### 2. Database Optimization

- Use connection pooling
- Add appropriate indexes
- Regular VACUUM (PostgreSQL)

### 3. Gunicorn for Production

Install Gunicorn:
```bash
pip install gunicorn
```

Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Backup and Recovery

### Regular Backups

1. **Database backups** (daily)
2. **Application code** (version control)
3. **Configuration files** (encrypted storage)
4. **Logs** (rotate and archive)

### Recovery Procedure

1. Restore database from backup
2. Pull latest code from Git
3. Restore configuration files
4. Restart services
5. Verify functionality

---

## Scaling

### Horizontal Scaling

1. Setup load balancer (Nginx/HAProxy)
2. Deploy multiple application instances
3. Use shared database
4. Implement session storage (Redis)

### Vertical Scaling

1. Increase server resources (CPU/RAM)
2. Optimize database queries
3. Enable caching layers
4. Use CDN for static assets

---

## Maintenance Schedule

- **Daily:** Check logs, monitor performance
- **Weekly:** Review error reports, update dependencies
- **Monthly:** Security patches, database optimization
- **Quarterly:** Full system audit, disaster recovery test

---

## Support

For deployment assistance:
- Email: support@propertybroker.ai
- GitHub Issues: https://github.com/ghifiardi/Property-Brokerage-/issues
- Documentation: https://github.com/ghifiardi/Property-Brokerage-/wiki

---

**Last Updated:** 2026-01-05
