# 🚀 MoodMate - Quick Deployment Guide (5 Minutes)

## ONE-CLICK NETLIFY DEPLOYMENT

### Step 1: Deploy Frontend to Netlify

1. Go to **https://netlify.com**
2. Click **"New site from Git"**
3. Connect your GitHub account if not already connected
4. Select this repository: `emotion-detection-music-recommendation`
5. Select branch: `main`
6. Netlify will auto-detect settings from `netlify.toml`
   - Build command: `cd frontend && npm install && npm run build`
   - Publish directory: `frontend/dist`
7. Click **"Deploy site"**

✅ **Your frontend will be live in 2-5 minutes!**

**Your Frontend URL:** `https://your-site-name.netlify.app`

---

### Step 2: Deploy Backend to Render

1. Go to **https://render.com**
2. Click **"New" → "Web Service"**
3. Connect your GitHub account
4. Select this repository
5. Configure settings:
   - **Name:** moodmate-backend
   - **Runtime:** Python 3.10
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
6. Click **"Create Web Service"**

✅ **Your backend will be live in 5-10 minutes!**

**Your Backend URL:** `https://moodmate-backend.onrender.com`

---

### Step 3: Connect Backend URL to Frontend

1. In Netlify Dashboard, go to your site
2. Click **"Site settings" → "Build & deploy" → "Environment"**
3. Add environment variable:
   - **Key:** `VITE_API_URL`
   - **Value:** `https://your-backend-url.onrender.com`
4. Click **"Trigger deploy"** to rebuild with new API URL

✅ **Your frontend is now connected to backend!**

---

## TESTING CHECKLIST

### Frontend Tests
- [ ] Website loads at your Netlify URL
- [ ] Page displays MoodMate title and interface
- [ ] Can toggle between "Live" and "Demo" modes
- [ ] Demo mode works without backend
- [ ] Upload button works
- [ ] Camera permission dialog appears

### Backend Tests  
- [ ] Backend URL is accessible
- [ ] API endpoints respond
- [ ] No 502/504 errors

### Integration Tests
- [ ] Upload an image → "Analyze Mood" button
- [ ] Wait for response (may be slow on free tier)
- [ ] Should see emotion + confidence + music recommendations
- [ ] Try text input
- [ ] Results display correctly

---

## TROUBLESHOOTING

### "API is not working"
- Backend may be sleeping on free Render tier
- Wait 30 seconds and try again
- Or upgrade Render to paid tier

### "Cannot connect to backend"
- Check your backend URL in Netlify environment variables
- Make sure backend URL is correct (ends with .onrender.com)
- Restart backend on Render dashboard

### "Styles not loading"
- Clear browser cache (Ctrl+Shift+R)
- Wait for Netlify build to complete (check build logs)

### "Camera not working"
- Camera only works on HTTPS (Netlify provides this)
- Check browser permissions for camera access
- Use Firefox or Chrome

---

## QUICK REFERENCE LINKS

- **Netlify:** https://netlify.com
- **Render:** https://render.com  
- **Your Repo:** https://github.com/invalid-mate/emotion-detection-music-recommendation

---

## ENVIRONMENT VARIABLES

**Frontend (Netlify):**
```
VITE_API_URL=https://your-backend-url.onrender.com
```

**Backend (Render):**
- No additional variables needed
- Make sure Python version is 3.10+

---

## PERFORMANCE TIPS

⚡ **Free tier speed:**
- First request after inactivity: ~10-15 seconds (free tier spins up)
- Subsequent requests: 1-5 seconds
- Upgrade Render to paid for instant responses

---

## SUCCESS INDICATORS

✅ **Deployment complete when:**
1. Frontend URL loads without errors
2. "Demo" mode works (no backend needed)
3. Backend API responds
4. Frontend can send requests to backend
5. Results display with music recommendations

---

**Congratulations! Your MoodMate app is now LIVE! 🎉**

Share your deployment URLs:
- Frontend: `https://your-site.netlify.app`
- Backend: `https://your-backend.onrender.com`
