from pprint import pprint

"""
-  Unions
-  Intersections (and Intersection Updates)
-  Differences (and Difference Updates)
-  Symmetric Differences (and Symmetric Difference Updates)
"""

#Union
# can be implemented wit '|' and method union()
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'],
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}

for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set

pprint(new_song_data)
