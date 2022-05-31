allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin',
                'indie', 'alternative rock', 'classical', 'k-pop', 'country',
                'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat',
                'party', 'synth', 'rhythmic', 'emotional', 'relationship',
                'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb',
                                   'warm', 'due', 'writer', 'happy',
                                   'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
bad_tags = [i for i in tag_set if i not in allowed_tags]
print(bad_tags)
