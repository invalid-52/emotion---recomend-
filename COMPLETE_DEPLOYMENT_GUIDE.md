# Complete Deployment Guide - MoodMate

## Overview
This guide covers deploying the MoodMate emotion detection and music recommendation application with both frontend (React + Vite) and backend (FastAPI) components.

## Prerequisites
- Node.js 18+ and npm (for frontend)
- Python 3.8+ and pip (for backend)
- Git and GitHub account
- Vercel or Netlify account (for frontend)
- Render, Railway, or Heroku account (for backend)

## Project Structure
```
emotion---recomend-/
├── frontend/              # React + Vite app
│   ├── src/
│   │   ├── App.jsx       # Main app component (UPDATED: uses VITE_API_URL)
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── index.html
│   └── .env.example      # Environment variables template
└── backend/              # FastAPI server
    ├── main.py
    ├── requirements.txt
    └── .env              # Backend env vars (not in git)
```

## Phase 1: Frontend Updates ✅ COMPLETED

### Changes Made:
1. **Updated App.jsx** - Changed API URL from hardcoded `http://localhost:8000` to use environment variable:
   ```javascript
   const APIURL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
   ```

2. **Created .env.example** - Template for environment configuration in `frontend/.env.example`

## Phase 2: Backend Deployment

### Option A: Deploy to Render

1. **Push code to GitHub** (already done)
2. **Go to [render.com](https://render.com)**
3. **Create New → Web Service**
4. **Connect GitHub repository:**
   - Select `invalid-52/emotion---recomend-`
   - Branch: `main`

5. **Configure Build Settings:**
   ```
   Build Command:    pip install -r requirements.txt
   Start Command:    uvicorn main:app --host 0.0.0.0 --port 8000
   Root Directory:   backend
   ```

6. **Set Environment Variables:**
   - Add any necessary env vars from your `.env` file

7. **Deploy**
   - Copy the deployed URL (e.g., `https://your-backend.onrender.com`)

### Option B: Deploy to Railway

1. **Go to [railway.app](https://railway.app)**
2. **Create New Project → GitHub Repo**
3. **Select `invalid-52/emotion---recomend-`**
4. **Configure Variables → Root Directory: `backend`**
5. **Add Environment Variables**
6. **Deploy and copy the URL**

## Phase 3: Frontend Deployment

### Option A: Deploy to Vercel (Recommended)

1. **Go to [vercel.com](https://vercel.com)**
2. **Import Project from Git**
3. **Select `invalid-52/emotion---recomend-`**
4. **Configure Project:**
   - Framework Preset: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

5. **Set Environment Variables:**
   - Add `VITE_API_URL` with your backend URL
   - Example: `https://your-backend.onrender.com`

6. **Deploy**
   - Vercel will automatically deploy on every push
   - Your frontend will be live at `https://your-project.vercel.app`

### Option B: Deploy to Netlify

1. **Go to [netlify.com](https://netlify.com)**
2. **New site from Git**
3. **Select `invalid-52/emotion---recomend-`**
4. **Configure Settings:**
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/dist`

5. **Set Environment Variables (Netlify UI):**
   - Go to Site settings → Environment variables
   - Add `VITE_API_URL` = `https://your-backend-url.com`

6. **Deploy**

## Phase 4: Testing & Verification

### 1. Test Backend API
```bash
curl https://your-backend-url/docs  # FastAPI Swagger docs
curl https://your-backend-url/predict/text -X POST -H "Content-Type: application/json" -d '{"text": "I am happy", "region": "Global"}'
```

### 2. Test Frontend
- Visit your deployed frontend URL
- Test with demo mode first (green "Demo" button)
- Switch to live mode and test with real API
- Test image upload and text input features
- Verify music recommendations are displayed

### 3. Check API Connection
- Open browser DevTools (F12)
- Go to Network tab
- Try a prediction
- Verify requests go to your backend URL

## Environment Variables Reference

### Frontend (.env)
```
VITE_API_URL=https://your-backend-url.com
```

### Backend (.env)
Add any backend-specific variables needed for your FastAPI app

## Troubleshooting

### "Cannot find module" errors
```bash
cd frontend
npm install
```

### CORS errors
- Ensure backend has CORS enabled for your frontend URL
- Check backend `main.py` has proper CORS configuration

### API requests failing
- Verify `VITE_API_URL` is set correctly in deployment
- Check backend logs: `Render/Railway dashboard → Logs`
- Ensure backend is running and responding

### Image upload not working
- Check file size limits on backend
- Verify multipart form data handling

## Quick Reference - Deployment URLs

Once deployed, update this section:

- **Frontend:** `https://your-frontend-url`
- **Backend API:** `https://your-backend-url`
- **API Documentation:** `https://your-backend-url/docs`

## Post-Deployment Checklist

- [ ] Backend deployed and responding
- [ ] Frontend deployed successfully  
- [ ] Environment variables set correctly
- [ ] API calls working (check Network tab)
- [ ] Image upload feature working
- [ ] Text input feature working
- [ ] Music recommendations displaying
- [ ] Demo mode working
- [ ] Live mode working
- [ ] Error handling working

## Additional Resources

- [Vite Documentation](https://vitejs.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Render Deployment Guide](https://render.com/docs)
- [Vercel Deployment Guide](https://vercel.com/docs)
- [Netlify Deployment Guide](https://docs.netlify.com)

## Support

For issues or questions, check the other deployment guides in this repository:
- `GO_LIVE_NOW.md`
- `QUICK_DEPLOYMENT_STEPS.md`
- `DEPLOYMENT_AND_TESTING_GUIDE.md`
