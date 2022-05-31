song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal',
                                     'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano',
                               'synth']}

user_recent_songs = {
    'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
    'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
tags_int = set(user_recent_songs['Retro Words']).intersection(
    set(user_recent_songs['Lowkey Space']))
print(tags_int)

recommended_songs = {}
for k, v in song_data.items():
    for i in v:
        if i in tags_int:
            if k not in user_recent_songs:
                recommended_songs.update({k: i})

print(recommended_songs)
