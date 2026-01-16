MOOD_MUSIC = {
      'happy': ['Don\'t Stop Me Now - Queen', 'Walking on Sunshine', 'Good as Hell - Lizzo'],
      'sad': ['Someone Like You - Adele', 'Tears in Heaven - Clapton', 'The Scientist - Coldplay'],
      'angry': ['Blinding Lights - The Weeknd', 'We Will Rock You - Queen', 'Monster - Eminem'],
      'fear': ['Midnight City - M83', 'Haunted - Evanescence', 'In the Dark - Billy Talent'],
      'surprise': ['Wake Me Up - Avicii', 'Dancing Queen - ABBA', 'All of the Stars'],
      'neutral': ['Weightless - Marconi Union', 'Clair de Lune', 'Bach - Air on G String'],
      'disgust': ['Heavy - Kiiara', 'Break My Soul - Beyonce', 'Stronger - Kanye West']
  }

def recommend_music(emotion: str, region: str = 'Global'):
      emotion = emotion.lower()
      songs = MOOD_MUSIC.get(emotion, MOOD_MUSIC['neutral'])
      return {'emotion': emotion, 'recommended_songs': songs, 'region': region}
