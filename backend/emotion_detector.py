import numpy as np
from typing import Dict

EMOTION_CLASSES = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Preprocess image for emotion detection.
    Converts to grayscale, resizes to 48x48, and normalizes.
    """
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)
    
    # Resize to 48x48
    from scipy import ndimage
    if image.shape != (48, 48):
        image = ndimage.zoom(image, (48/image.shape[0], 48/image.shape[1]))
    
    # Normalize pixel values
    image = image / 255.0
    
    return image

def detect_facial_features(image: np.ndarray) -> Dict:
    """
    Detect facial features using edge detection and image analysis.
    This is a simplified feature extraction without ML models.
    """
    from scipy import ndimage
    
    # Edge detection
    edges = ndimage.sobel(image)
    edge_intensity = np.sum(edges)
    
    # Brightness analysis
    brightness = np.mean(image)
    brightness_variance = np.var(image)
    
    # Contrast
    contrast = np.std(image)
    
    # Horizontal and vertical gradients
    gx = ndimage.sobel(image, axis=0)
    gy = ndimage.sobel(image, axis=1)
    
    h_gradient = np.sum(np.abs(gx))
    v_gradient = np.sum(np.abs(gy))
    
    return {
        'edge_intensity': edge_intensity,
        'brightness': brightness,
        'brightness_variance': brightness_variance,
        'contrast': contrast,
        'h_gradient': h_gradient,
        'v_gradient': v_gradient
    }

def predict_emotion_image(image: np.ndarray) -> str:
    """
    Predict emotion from image using feature analysis.
    Returns one of the 7 emotion classes from FER2013.
    """
    try:
        # Preprocess
        processed = preprocess_image(image)
        
        # Extract features
        features = detect_facial_features(processed)
        
        # Simple heuristic-based classification
        # (In production, would use trained CNN model)
        edge_intensity = features['edge_intensity']
        brightness = features['brightness']
        contrast = features['contrast']
        h_grad = features['h_gradient']
        v_grad = features['v_gradient']
        
        # Scoring for each emotion based on features
        scores = {}
        
        # Happy: high brightness, less edges, good contrast
        scores['happy'] = (brightness * 0.3 + contrast * 0.3 + (1 - edge_intensity/1000) * 0.4)
        
        # Sad: lower brightness, more vertical gradients
        scores['sad'] = ((1 - brightness) * 0.3 + (v_grad / (h_grad + 1)) * 0.4 + (1 - contrast) * 0.3)
        
        # Angry: high edges, high contrast, dark areas
        scores['angry'] = ((edge_intensity / 1000) * 0.4 + contrast * 0.3 + (1 - brightness) * 0.3)
        
        # Disgust: moderate brightness, high h-gradient
        scores['disgust'] = ((h_grad / (v_grad + 1)) * 0.5 + (1 - brightness) * 0.3 + contrast * 0.2)
        
        # Fear: high variance, moderate edges
        scores['fear'] = ((features['brightness_variance'] * 0.4 + (edge_intensity/1000) * 0.3 + contrast * 0.3))
        
        # Surprise: high brightness, moderate edges
        scores['surprise'] = (brightness * 0.4 + (edge_intensity / 1500) * 0.3 + contrast * 0.3)
        
        # Neutral: balanced features
        scores['neutral'] = (0.5 - abs(brightness - 0.5)) * (1 - contrast/0.5)
        
        # Normalize scores
        total_score = sum(scores.values())
        if total_score > 0:
            scores = {k: v / total_score for k, v in scores.items()}
        else:
            scores = {emotion: 1/len(EMOTION_CLASSES) for emotion in EMOTION_CLASSES}
        
        # Return emotion with highest score
        predicted_emotion = max(scores, key=scores.get)
        return predicted_emotion
        
    except Exception as e:
        print(f"Error in emotion detection: {str(e)}")
        return 'neutral'
