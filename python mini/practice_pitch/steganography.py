from stegano import lsbset
from stegano.lsbset import generators

# Hide the message in the image
flag = "This is a sample text message!"
# Hide the message in the image and save it as 'steg.png'
steg_image = lsbset.hide("./test.png", flag, generators.eratosthenes())
steg_image.save("steg.png")

# Show the message from the image
revealed_message = lsbset.reveal("steg.png", generators.eratosthenes())
print("Revealed message:", revealed_message)
