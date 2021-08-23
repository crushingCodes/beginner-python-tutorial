# 6. Conditionals - if statements


message = "short message"
# message = "medium message"
# message = "this is long message"
# message = "this is a really long message"

message_length = len(message)

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

