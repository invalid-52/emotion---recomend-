# MoodMate - Complete Deployment & Testing Guide

## 🎯 Step-by-Step Setup & Deployment

### **PART 1: LOCAL TESTING (Development Environment)**

---

## Step 1: Clone/Pull Latest Repository

```bash
# Clone the repository (if not already cloned)
git clone https://github.com/invalid-mate/emotion-detection-music-recommendation.git
cd emotion-detection-music-recommendation

# OR Pull latest changes if already cloned
git pull origin main
```

---

## Step 2: Set Up Backend Server

```bash
# Navigate to backend folder
cd backend

# Create Python virtual environment (Recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
python main.py
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

✅ **Backend is now running on `http://localhost:8000`**

---

## Step 3: Set Up Frontend (New Terminal/Tab)

```bash
# In new terminal, navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Expected Output:**
```
  Local:        http://localhost:3000
```

✅ **Frontend is now running on `http://localhost:3000`**

---

## Step 4: Test Local Integration

### **Test 1: Check Backend API Endpoints**

Use Postman or curl to test backend:

```bash
# Test image emotion detection
curl -X POST http://localhost:8000/predict/image \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_image_string", "region": "Global"}'

# Test text emotion detection
curl -X POST http://localhost:8000/predict/text \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling happy", "region": "Global"}'

# Test regions endpoint
curl -X GET http://localhost:8000/regions
```

### **Test 2: Check Frontend in Browser**

1. Open `http://localhost:3000` in browser
2. You should see MoodMate interface with:
   - 📷 Image upload option
   - 🎥 Camera capture option
   - ✍️ Text input option
   - Toggle for "Live" / "Demo" mode

### **Test 3: Test Frontend-Backend Communication**

#### **Demo Mode (No Backend Required):**
1. Click "Live" button in top-right to toggle to "Demo" mode
2. Take a photo or upload image
3. Click "Analyze Mood"
4. ✅ Should show happy emoji with recommended tracks

#### **Live Mode (Requires Backend):**
1. Click "Demo" button to toggle back to "Live" mode
2. Upload an image or use camera
3. Click "Analyze Mood"
4. Wait for API response
5. ✅ Should show emotion with music recommendations

### **Test 4: Feature Testing Checklist**

#### Frontend Features:
- [ ] **Camera Capture**: Click camera → Allow permissions → Take photo → Capture works
- [ ] **Image Upload**: Click upload → Select image → Preview shows image
- [ ] **Drag & Drop**: Drag image to area → Image previews
- [ ] **Text Input**: Switch to "Text" tab → Type mood → Text appears
- [ ] **Demo Mode**: Works without backend
- [ ] **Live Mode**: Connects to backend API
- [ ] **Results Display**: Shows emotion, confidence, and tracks
- [ ] **Error Handling**: Shows error messages on failures
- [ ] **Responsive**: Works on mobile/tablet/desktop
- [ ] **Animations**: Smooth transitions visible

#### Backend Features:
- [ ] **Emotion Detection**: Correctly identifies emotions
- [ ] **Music Recommendations**: Appropriate tracks for mood
- [ ] **Region Filtering**: Regional playlists work
- [ ] **Error Responses**: Proper error messages
- [ ] **Performance**: Fast response times (<2 seconds)

---

## PART 2: PRODUCTION BUILD & DEPLOYMENT

---

## Step 5: Build Frontend for Production

```bash
# In frontend folder
npm run build
```

**This creates `dist/` folder with optimized production build:**
- HTML, CSS, JS bundled and minified
- Ready for deployment
- File size: ~500KB-1MB

### **Verify Build Success:**
```bash
# Preview production build locally
npm run preview
# Open http://localhost:4173
```

---

## Step 6: Deploy Frontend to Netlify

### **Option A: Deploy via GitHub (Recommended)**

1. **Push code to GitHub:**
```bash
cd ../
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Connect Netlify:**
   - Go to https://netlify.com
   - Click "New site from Git"
   - Select GitHub repository
   - Select branch: `main`
   - Build settings:
     - Base directory: `frontend`
     - Build command: `npm run build`
     - Publish directory: `dist`
   - Click "Deploy site"

3. **Configure Environment Variables:**
   - In Netlify dashboard → Site settings → Build & deploy → Environment
   - Add variables:
     ```
     VITE_API_URL=https://your-backend-url.com
     ```

4. **Wait for deployment** (2-5 minutes)
   - Netlify will show your live URL
   - Example: `https://moodmate-xxxxx.netlify.app`

### **Option B: Deploy via Vercel**

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd frontend
vercel
```

Follow prompts to complete deployment.

---

## Step 7: Deploy Backend to Render (Free Tier)

### **Option A: Deploy to Render**

1. **Push backend to GitHub**
2. **Go to https://render.com**
3. **Create New → Web Service**
4. **Connect GitHub repository**
5. **Configure:**
   - Runtime: Python 3.10
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
6. **Deploy**

**Your backend URL:** `https://your-service.onrender.com`

### **Option B: Deploy to Railway**

1. Go to https://railway.app
2. Connect GitHub repository
3. Railway auto-detects Python app
4. Deploy (free tier available)

---

## Step 8: Update Frontend with Production Backend URL

After backend is deployed:

1. **Edit `src/App.jsx`:**
```javascript
const APIURL = 'https://your-backend-url.onrender.com'
```

2. **Or update Netlify environment variable:**
   - Netlify Dashboard → Environment → Edit
   - Set `VITE_API_URL=https://your-backend-url.onrender.com`
   - Redeploy

---

## PART 3: FINAL TESTING & VALIDATION

---

## Step 9: Test Live Production Website

### **Test Checklist:**

1. **Open Production URL:**
   - Navigate to your deployed frontend URL
   - Should load MoodMate interface

2. **Test Image Upload:**
   - Upload a clear photo of a face
   - Click "Analyze Mood"
   - Wait for response
   - Verify: Emotion detected + music recommendations shown

3. **Test Camera:**
   - Click camera icon (if on HTTPS)
   - Allow permissions
   - Take photo
   - Verify: Works and detects emotion

4. **Test Text Input:**
   - Switch to "Text" tab
   - Type: "I am feeling very happy"
   - Click "Analyze Mood"
   - Verify: Emotion detected + tracks shown

5. **Test Demo Mode:**
   - Click "Live" to toggle demo
   - Test without backend
   - Verify: Works offline

6. **Performance Tests:**
   - Load time: Should be <3 seconds
   - Analysis time: Should be <5 seconds
   - No console errors

7. **Mobile Test:**
   - Open on phone
   - Test upload/camera
   - Verify: Responsive design works

---

## Step 10: Common Issues & Troubleshooting

### **Issue: "Cannot GET /api/predict/image"**
**Solution:**
- Backend not running
- Wrong backend URL in frontend
- CORS not enabled on backend

### **Issue: Camera not working**
**Solution:**
- Use HTTPS (Netlify provides this)
- Allow camera permissions
- Try different browser

### **Issue: Slow response times**
**Solution:**
- Backend might be on free tier (slow to start)
- Upgrade to paid tier for better performance
- Check network latency

### **Issue: "502 Bad Gateway"**
**Solution:**
- Backend service crashed
- Restart backend on Render/Railway
- Check backend logs

### **Issue: Styles not loading**
**Solution:**
- Clear browser cache
- Hard refresh (Ctrl+Shift+R)
- Check Tailwind config

---

## Useful Commands Reference

```bash
# Development
npm run dev              # Start frontend dev server
python main.py           # Start backend dev server

# Production
npm run build            # Build frontend
npm run preview          # Preview production build

# Testing
curl -X POST http://localhost:8000/predict/image  # Test backend

# Git
git add .               # Stage changes
git commit -m "message" # Commit changes
git push origin main    # Push to GitHub

# Debugging
# Browser: F12 → Console tab
# Backend: Check terminal output
```

---

## 🎉 Success Indicators

✅ **Local testing:**
- Frontend loads at http://localhost:3000
- Backend running at http://localhost:8000
- Emotion detection works
- Music recommendations appear

✅ **Production deployed:**
- Website live at custom URL
- Image/text analysis works
- No 404 or 500 errors
- Mobile responsive
- Fast loading times

✅ **Full integration:**
- Frontend ↔ Backend communication working
- All features functional
- Error handling in place
- Demo mode available

---

## Need Help?

- Check frontend logs: Browser DevTools (F12)
- Check backend logs: Terminal/Console output
- GitHub Issues: Report problems on repository
- Test endpoints: Use Postman or curl

---

**Congratulations! Your MoodMate application is deployed and ready to use! 🎵**
