from typing import Dict

EMOTION_KEYWORDS = {
      'happy': ['happy', 'joy', 'excited', 'wonderful', 'great', 'awesome'],
      'sad': ['sad', 'unhappy', 'depressed', 'crying', 'lonely'],
      'angry': ['angry', 'furious', 'mad', 'rage', 'hate', 'frustrated'],
      'disgust': ['disgusted', 'gross', 'yuck', 'revolting'],
      'fear': ['scared', 'afraid', 'terrified', 'anxiety', 'worried'],
      'surprise': ['surprised', 'amazed', 'shocked', 'astonished'],
      'neutral': ['ok', 'fine', 'normal', 'regular']
  }

def detect_text_emotion(text: str) -> Dict:
      text_lower = text.lower()
      emotion_scores = {e: 0 for e in EMOTION_KEYWORDS.keys()}
      for emotion, keywords in EMOTION_KEYWORDS.items():
                for kw in keywords:
                              if kw in text_lower: emotion_scores[emotion] += 1
                            dominant = max(emotion_scores, key=emotion_scores.get) if sum(emotion_scores.values()) > 0 else 'neutral'
              conf = emotion_scores[dominant] / max(sum(emotion_scores.values()), 1)
            return {'emotion': dominant, 'confidence': min(conf, 1.0), 'scores': emotion_scores}
