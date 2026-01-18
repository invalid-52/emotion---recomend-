import React, { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Upload, Camera, Zap, Loader2, AlertCircle, Headphones, Music } from 'lucide-react'

const APIURL = 'http://localhost:8000'

export default function App() {
  const [activeTab, setActiveTab] = useState('image')
  const [inputData, setInputData] = useState('')
  const [imagePreview, setImagePreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [isDemoMode, setIsDemoMode] = useState(false)
  const [isCameraOpen, setIsCameraOpen] = useState(false)
  
  const fileInputRef = useRef(null)
  const videoRef = useRef(null)
  const canvasRef = useRef(null)

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true })
      if (videoRef.current) {
        videoRef.current.srcObject = stream
        setIsCameraOpen(true)
        setError(null)
      }
    } catch (err) {
      setError('Camera access denied')
    }
  }

  const stopCamera = () => {
    if (videoRef.current?.srcObject) {
      videoRef.current.srcObject.getTracks().forEach(track => track.stop())
      videoRef.current.srcObject = null
      setIsCameraOpen(false)
    }
  }

  const captureImage = () => {
    if (videoRef.current && canvasRef.current) {
      const context = canvasRef.current.getContext('2d')
      canvasRef.current.width = videoRef.current.videoWidth
      canvasRef.current.height = videoRef.current.videoHeight
      context.drawImage(videoRef.current, 0, 0)
      const dataUrl = canvasRef.current.toDataURL('image/jpeg')
      setImagePreview(dataUrl)
      setInputData(dataUrl.split(',')[1])
      stopCamera()
    }
  }

  const handleImageUpload = (e) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result)
        setInputData(reader.result.split(',')[1])
        setResult(null)
        setError(null)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = async () => {
    setLoading(true)
    setError(null)
    setResult(null)

    if (isDemoMode) {
      setTimeout(() => {
        setResult({
          emotion: 'happy',
          confidence: 0.92,
          recommendedmusic: ['Walking on Sunshine - Katrina', 'Good as Hell - Lizzo', 'Dont Stop Me Now - Queen']
        })
        setLoading(false)
      }, 1500)
      return
    }

    try {
      const endpoint = activeTab === 'image' ? 'predict/image' : 'predict/text'
      const body = { region: 'Global' }
      
      if (activeTab === 'image') {
        if (!inputData) throw new Error('Please upload an image')
        body.image = inputData
      } else {
        if (!inputData) throw new Error('Please enter text')
        body.text = inputData
      }

      const response = await fetch(`${APIURL}/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      })

      if (!response.ok) throw new Error('API Error')
      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const emoticons = {
    happy: '😊', sad: '😢', angry: '😠', fear: '😨', 
    surprise: '😲', neutral: '😐', disgust: '🤢'
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-12 pt-8">
          <div className="flex items-center gap-3">
            <Headphones className="text-purple-400" size={32} />
            <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              MoodMate
            </h1>
          </div>
          <button
            onClick={() => setIsDemoMode(!isDemoMode)}
            className={`px-4 py-2 rounded-full text-sm font-medium transition ${
              isDemoMode ? 'bg-green-500/20 text-green-400' : 'bg-gray-700 text-gray-200'
            }`}
          >
            {isDemoMode ? '🎬 Demo' : 'Live'}
          </button>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Input Section */}
          <div className="space-y-6">
            <div className="bg-white/10 backdrop-blur rounded-xl p-6 border border-white/20">
              <div className="flex gap-2 mb-4">
                <button
                  onClick={() => { setActiveTab('image'); setResult(null); stopCamera() }}
                  className={`flex-1 py-2 rounded-lg transition ${
                    activeTab === 'image' ? 'bg-purple-600' : 'bg-gray-700 hover:bg-gray-600'
                  }`}
                >
                  📷 Image
                </button>
                <button
                  onClick={() => { setActiveTab('text'); setResult(null); stopCamera() }}
                  className={`flex-1 py-2 rounded-lg transition ${
                    activeTab === 'text' ? 'bg-purple-600' : 'bg-gray-700 hover:bg-gray-600'
                  }`}
                >
                  ✍️ Text
                </button>
              </div>

              {activeTab === 'image' ? (
                <div className="space-y-4">
                  {isCameraOpen ? (
                    <div className="space-y-3">
                      <video ref={videoRef} autoPlay playsInline muted className="w-full rounded-lg" />
                      <div className="flex gap-2">
                        <button onClick={stopCamera} className="flex-1 bg-red-600 hover:bg-red-700 py-2 rounded-lg">
                          Stop
                        </button>
                        <button onClick={captureImage} className="flex-1 bg-green-600 hover:bg-green-700 py-2 rounded-lg">
                          Capture
                        </button>
                      </div>
                    </div>
                  ) : imagePreview ? (
                    <img src={imagePreview} alt="Preview" className="w-full rounded-lg" />
                  ) : (
                    <div className="aspect-video bg-gray-800 rounded-lg flex flex-col items-center justify-center gap-4">
                      <Upload size={32} />
                      <div className="flex gap-2">
                        <button onClick={() => fileInputRef.current?.click()} className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg">
                          Upload
                        </button>
                        <button onClick={startCamera} className="px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg">
                          Camera
                        </button>
                      </div>
                    </div>
                  )}
                  <input ref={fileInputRef} type="file" accept="image/*" onChange={handleImageUpload} className="hidden" />
                </div>
              ) : (
                <textarea
                  value={inputData}
                  onChange={(e) => setInputData(e.target.value)}
                  placeholder="Describe your mood or current situation..."
                  className="w-full h-40 bg-gray-800 text-white rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none"
                />
              )}
            </div>

            {error && (
              <div className="bg-red-500/20 border border-red-500 text-red-200 p-3 rounded-lg flex items-center gap-2">
                <AlertCircle size={20} />
                <span>{error}</span>
              </div>
            )}

            <button
              onClick={handleSubmit}
              disabled={loading || !inputData || isCameraOpen}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 disabled:opacity-50 disabled:cursor-not-allowed py-3 rounded-lg font-semibold flex items-center justify-center gap-2 transition"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin" size={20} />
                  Analyzing...
                </>
              ) : (
                <>
                  <Zap size={20} />
                  Analyze Mood
                </>
              )}
            </button>
          </div>

          {/* Result Section */}
          <div className="lg:block">
            <AnimatePresence>
              {result ? (
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="bg-white/10 backdrop-blur rounded-xl p-8 border border-white/20 space-y-6"
                >
                  <div className="text-center">
                    <div className="text-6xl mb-4">{emoticons[result.emotion?.toLowerCase()] || '😐'}</div>
                    <h2 className="text-3xl font-bold capitalize text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">
                      {result.emotion}
                    </h2>
                    <p className="text-gray-300 mt-2">
                      Confidence: {Math.round((result.confidence || 0.8) * 100)}%
                    </p>
                  </div>

                  {result.recommendedmusic && (
                    <div>
                      <h3 className="text-xl font-semibold flex items-center gap-2 mb-4">
                        <Music size={20} className="text-purple-400" />
                        Recommended Tracks
                      </h3>
                      <ul className="space-y-2">
                        {result.recommendedmusic.slice(0, 5).map((track, idx) => (
                          <li key={idx} className="bg-gray-800/50 hover:bg-gray-700/50 p-3 rounded-lg transition">
                            🎵 {track}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </motion.div>
              ) : (
                <div className="h-full flex items-center justify-center text-center text-gray-400">
                  <div>
                    <Music size={48} className="mx-auto mb-4 opacity-50" />
                    <p>Results will appear here</p>
                  </div>
                </div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
      <canvas ref={canvasRef} className="hidden" />
    </div>
  )
}
