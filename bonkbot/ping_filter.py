# def filter_message(message, botNumber):
#     newMessage = None
#     message = message.lower
#     ping = "@bonkbot" + botNumber
#     if ping in message:
#         messageArray = message.split(ping)
#         newMessage = "".join(messageArray)
#     return newMessage

def filter_message(message, botNumber):
    newMessage = "None"
    message = message.lower()
    ping = "@bonkbot" + botNumber
    if ping in message:
        messageArray = message.split(ping)
        newMessage = "".join(messageArray).strip()
    return newMessage

# Ensure script can be run as a standalone script and used as a module
if __name__ == "__main__":
    import sys
    message = sys.argv[1]
    botNumber = sys.argv[2]
    print(filter_message(message, botNumber))
