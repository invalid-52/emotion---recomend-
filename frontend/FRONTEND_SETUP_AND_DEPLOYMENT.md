# MoodMate Frontend - Complete Setup & Deployment Guide

## 📁 Project Structure

```
frontend/
├── index.html                 # HTML entry point
├── package.json              # Dependencies & scripts
├── vite.config.js            # Vite configuration with backend proxy
├── tailwind.config.js        # Tailwind CSS configuration
├── postcss.config.js         # PostCSS configuration
└── src/
    ├── main.jsx              # React DOM render
    ├── index.css             # Global Tailwind styles
    └── App.jsx               # Main application component
```

## 🚀 Quick Start (Local Development)

### Prerequisites
- Node.js 16+
- npm or yarn
- Backend running on `http://localhost:8000`

### Installation & Running

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will open at `http://localhost:3000`

## 🔗 Backend Connection

The frontend connects to backend via Vite proxy configuration:

**vite.config.js:**
- Frontend runs on: `http://localhost:3000`
- Backend proxy: `/api/*` → `http://localhost:8000/*`

**API Endpoints Used:**
- `POST /predict/image` - Emotion detection from image
- `POST /predict/text` - Emotion detection from text
- `GET /regions` - Available musical regions

**Important:** Backend must be running before starting frontend!

## 🏗️ Frontend Architecture

### Tech Stack
- **React 18** - UI framework
- **Vite** - Fast build tool & dev server
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Animations
- **Lucide Icons** - Beautiful icons

### Key Features

1. **Dual Input Methods**
   - Camera capture with real-time preview
   - File upload with drag-and-drop
   - Text input for emotion analysis

2. **Backend Integration**
   - Emotion detection (image/text)
   - Region-specific music recommendations
   - Confidence scoring

3. **Beautiful UI**
   - Dark theme with gradient accents
   - Smooth animations
   - Responsive design
   - Demo mode for testing without backend

## 📦 Build & Production

### Build for Production

```bash
npm run build
```

Outputs to `dist/` folder - ready for deployment!

### Preview Production Build

```bash
npm run preview
```

## 🚢 Deployment Options

### Option 1: Netlify (Recommended)

1. Push code to GitHub
2. Connect Netlify to repository
3. Build settings:
   - **Build command:** `npm run build`
   - **Publish directory:** `dist`
4. Set environment variables:
   ```
   VITE_API_URL=https://your-backend-url.com
   ```
5. Deploy!

### Option 2: Vercel

1. Push code to GitHub
2. Import project in Vercel
3. Build settings auto-detected
4. Deploy with one click

### Option 3: Manual Deployment

```bash
# Build
npm run build

# Copy dist folder to web server
cp -r dist/* /var/www/html/
```

## 🔧 Configuration

### Update Backend URL (for production)

Edit `src/App.jsx` if backend URL differs:

```javascript
const APIURL = 'https://your-backend-url.com';
```

Or use Vite proxy in `vite.config.js`:

```javascript
proxy: {
  '/api': {
    target: 'https://your-backend-url.com',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, '')
  }
}
```

## 📝 src/App.jsx - Main Component

The App component includes:

- Camera integration with canvas capture
- File upload with drag-and-drop
- Text input
- Real-time backend API calls
- Error handling & loading states
- Beautiful result displays
- Demo mode for testing

Key functions:
- `startCamera()` - Initialize webcam
- `captureImage()` - Capture from camera
- `handleSubmit()` - Send to backend API
- `getEmoji()` - Emotion-based emojis
- `getGradient()` - Emotion-based colors

## 🎨 Styling

Uses Tailwind CSS with dark theme:
- Color scheme: `#09090b` (dark) to gradients
- Animations: Framer Motion
- Icons: Lucide React

## 🐛 Troubleshooting

**Backend not connecting?**
- Ensure backend is running on port 8000
- Check CORS headers in backend
- Test API with Postman

**Styles not loading?**
- Run `npm install` again
- Clear browser cache
- Check Tailwind config

**Camera not working?**
- Allow camera permissions
- Use HTTPS for production
- Check browser console for errors

## 📱 Responsive Design

Works seamlessly on:
- Desktop (1024px+)
- Tablet (768px+)
- Mobile (320px+)

## 🚀 Production Checklist

- [ ] Build runs without errors
- [ ] Backend URL configured
- [ ] CORS headers set correctly
- [ ] Environment variables set
- [ ] Camera/file permissions in docs
- [ ] Error handling tested
- [ ] Mobile responsiveness verified
- [ ] Performance optimized

## 📞 Support

For issues or questions about the frontend, check:
1. Browser console for errors
2. Network tab for API calls
3. Backend logs for issues
4. GitHub issues for known problems

---

**Ready to deploy? Follow the steps above and enjoy MoodMate! 🎵**
