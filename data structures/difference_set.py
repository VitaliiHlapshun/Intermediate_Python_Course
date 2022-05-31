song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal',
                                     'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano',
                               'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {
    'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
tag_diff = set(user_liked_song['Back To Art']).difference(
    set(user_disliked_song['Retro Words']))

print(tag_diff)
recommended_songs = {}
for k, v in song_data.items():
    for el in v:
        if el in tag_diff:
            if k not in user_disliked_song.keys() and k not in user_liked_song.keys():
                recommended_songs[k] = v
print(recommended_songs)
