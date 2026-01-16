from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from emotion_detector import predict_emotion_image, EMOTION_CLASSES
from text_emotion import detect_text_emotion
from music_recommender import recommend_music
from location_filter import filter_by_location, REGION_SETTINGS
import base64
from io import BytesIO
from PIL import Image

app = FastAPI(title="MoodMate API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ImageRequest(BaseModel):
    image: str
    region: str = "Global"

class TextRequest(BaseModel):
    text: str
    region: str = "Global"

class EmotionResponse(BaseModel):
    emotion: str
    recommended_music: list
    mood: str
    region_settings: dict
    confidence: float = None
    emotion_scores: dict = None

@app.post("/predict/image", response_model=EmotionResponse)
async def predict_image(req: ImageRequest):
    try:
        img_bytes = base64.b64decode(req.image)
        img = Image.open(BytesIO(img_bytes))
        img_array = np.array(img)
        emotion = predict_emotion_image(img_array)
        music = recommend_music(emotion, req.region)
        region = filter_by_location(req.region)
        return EmotionResponse(emotion=emotion, recommended_music=music['recommended_songs'], mood=music['emotion'], region_settings=region)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/text", response_model=EmotionResponse)
async def predict_text(req: TextRequest):
    try:
        result = detect_text_emotion(req.text)
        emotion = result['emotion']
        music = recommend_music(emotion, req.region)
        region = filter_by_location(req.region)
        return EmotionResponse(emotion=emotion, confidence=result['confidence'], emotion_scores=result['scores'], recommended_music=music['recommended_songs'], mood=music['emotion'], region_settings=region)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/regions")
async def get_regions():
    return {"regions": list(REGION_SETTINGS.keys())}

@app.get("/emotions")
async def get_emotions():
    return {"emotions": EMOTION_CLASSES}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "MoodMate"}

@app.get("/")
async def root():
    return {"name": "MoodMate API", "docs": "/docs", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
