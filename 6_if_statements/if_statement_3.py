# 6. Conditionals - if statements


# Use these to test the if statement block
message = "short message"
# message = "medium message"
# message = "this is long message"
# message = "this is a really long message"

# To find the length of a string, use len("hello") or len(message)
message_length = len(message)
print(message_length)

# if statement block
if message_length > 21:
    print('long message')
elif message_length > 28:
    print("really long message")
elif message_length < 12:
    print("medium message")
else:
    print("short message")


# TODO fix this code to detect all four messages
# Hint: the numbers next to message length are all correct

