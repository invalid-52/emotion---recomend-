from flask import Flask, request, jsonify
import numpy as np
from emotion_detector import predict_emotion_image
from text_emotion import detect_text_emotion
from music_recommender import recommend_music
from location_filter import filter_by_location
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/predict/image', methods=['POST'])
def predict_image():
    try:
        data = request.json
        image_data = data.get('image')
        region = data.get('region', 'Global')
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        image_array = np.array(image)
        
        # Predict emotion
        emotion = predict_emotion_image(image_array)
        
        # Get music recommendation
        music_data = recommend_music(emotion, region)
        filtered_music = filter_by_location(region)
        
        return jsonify({
            'emotion': emotion,
            'recommended_music': music_data['recommended_songs'],
            'mood': music_data['emotion'],
            'region_settings': filtered_music,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

@app.route('/predict/text', methods=['POST'])
def predict_text():
    try:
        data = request.json
        text = data.get('text', '')
        region = data.get('region', 'Global')
        
        # Predict emotion from text
        emotion_result = detect_text_emotion(text)
        emotion = emotion_result['emotion']
        
        # Get music recommendation
        music_data = recommend_music(emotion, region)
        filtered_music = filter_by_location(region)
        
        return jsonify({
            'emotion': emotion,
            'confidence': emotion_result['confidence'],
            'emotion_scores': emotion_result['scores'],
            'recommended_music': music_data['recommended_songs'],
            'mood': music_data['emotion'],
            'region_settings': filtered_music,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

@app.route('/regions', methods=['GET'])
def get_regions():
    try:
        from location_filter import REGION_SETTINGS
        regions = list(REGION_SETTINGS.keys())
        return jsonify({'regions': regions, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'MoodMate Backend'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
