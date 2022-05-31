# def outer_function():
#     enclosing_value = 'Enclosing Value'
#     def nested_function():
#         nested_value = 'Nested Value'
#         def second_nested():
#             print(enclosing_value)
#             print(nested_value)
#         second_nested()
#     nested_function()
# outer_function()


# option ONE!
# def enclosing_function():
#     var = [1, 2]
#     def nested_function():
#         var = [2, 4]
#     nested_function()
#     print(var)
# enclosing_function()

# option two!
# def enclosing_function():
#     var = [1, 2]
#     def nested_function():
#         nonlocal var
#         var = [2, 4]
#     nested_function()
#     print(var)
# enclosing_function()
