"""The .remove() method searches for an element within the set and removes
it if it exists, otherwise, a KeyError is thrown. The .discard() method
works the same way but does not throw an exception if an element is not
present. """

song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
print(tag_set)
tag_set.discard('onion')
tag_set.discard('spam')
tag_set.discard('helloworld')
song_data_users.update({'Retro Words': list(tag_set)})
print(tag_set)
print(song_data_users)
