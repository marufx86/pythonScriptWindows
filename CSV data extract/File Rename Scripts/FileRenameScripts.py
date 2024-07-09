##remove every string which is on filename.split(" - 8-Bit Action II - Lufus.wav")
# import os

# directory = r"C:\Users\Mifunee\Desktop\musicPacks\4th milestone\8-Bit Action I & II\8-Bit Action II - Soundtrack Pack\Loop Versions" 

# for filename in os.listdir(directory):
#     if filename.endswith(".wav"):  # Correct extension check
#         new_filename = filename.split(" - 8-Bit Action II - Lufus.wav")[0] + ".wav"
#         old_filepath = os.path.join(directory, filename)
#         new_filepath = os.path.join(directory, new_filename)
#         os.rename(old_filepath, new_filepath)



# ##remove every string which is on filename.split(" - 8-Bit Action II - Lufus.wav") and replace space with a underscore
# import os

# directory = r"C:\Users\Mifunee\Desktop\musicPacks\4th milestone\8-Bit Casual I & II\8-Bit Casual - Soundtrack Pack - Copy" 

# for filename in os.listdir(directory):
#     if filename.endswith(".wav"):
#         new_filename = filename.split(" (8-Bit Version) - Full Version - 8-Bit Casual - Lufus")[0] + ".wav" 
#         new_filename = new_filename.replace(" ", "_") # Replace spaces with underscores
#         old_filepath = os.path.join(directory, filename)
#         new_filepath = os.path.join(directory, new_filename)
#         os.rename(old_filepath, new_filepath)


####remove every string which is on filename.split(" - 8-Bit Action II - Lufus.wav") and replace space with a underscore also add WAV_ prefix
# import os

# directory = r"C:\Users\Mifunee\Desktop\musicPacks\4th milestone\8-Bit Casual I & II\8-Bit Casual - Soundtrack Pack - Copy" 

# for filename in os.listdir(directory):
#     if filename.endswith(".wav"):
#         new_filename = filename.split(" (8-Bit Version) - Full Version - 8-Bit Casual - Lufus")[0] + ".wav" 
#         new_filename = new_filename.replace(" ", "_") 
#         new_filename = "WAV_" + new_filename # Add the prefix

#         old_filepath = os.path.join(directory, filename)
#         new_filepath = os.path.join(directory, new_filename)
#         os.rename(old_filepath, new_filepath)


###remove every string which is on filename.split(" - 8-Bit Action II - Lufus.wav") and replace space with a underscore also add WAV_ prefix
import os

directory = r"C:\Users\Mifunee\Desktop\musicPacks\4th milestone\Cyberpunk III & IV\Cyberpunk III - Soundtrack Pack\Loops" 

for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        new_filename = filename.split(" - Epic Fantasy - Lufus")[0] + ".wav" 
        new_filename = new_filename.replace(" ", "_") 
        new_filename = "WAV_" + new_filename # Add the prefix

        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)


