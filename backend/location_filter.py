REGION_SETTINGS = {
      'India': {'language': 'Hindi', 'genre': 'Bollywood', 'popular': 'AR Rahman'},
      'USA': {'language': 'English', 'genre': 'Hip-Hop', 'popular': 'Drake'},
      'UK': {'language': 'English', 'genre': 'Pop', 'popular': 'Ed Sheeran'},
      'Japan': {'language': 'Japanese', 'genre': 'J-Pop', 'popular': 'AKB48'},
      'Korea': {'language': 'Korean', 'genre': 'K-Pop', 'popular': 'BTS'},
      'Germany': {'language': 'German', 'genre': 'Techno', 'popular': 'Kraftwerk'},
      'Brazil': {'language': 'Portuguese', 'genre': 'Samba', 'popular': 'Tom Jobim'},
      'Global': {'language': 'English', 'genre': 'Pop', 'popular': 'Universal'}
  }

def filter_by_location(region: str):
      return REGION_SETTINGS.get(region, REGION_SETTINGS['Global'])
