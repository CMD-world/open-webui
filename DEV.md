# Development Guide

## Frontend

```
cp .env.example .env
npm install
npm run dev
```

## Backend

```
cd backend
conda create --name open-webui python=3.11
conda activate open-webui
pip install -r requirements.txt -U
ENV=dev WEBUI_AUTH=False ./dev.sh
```
