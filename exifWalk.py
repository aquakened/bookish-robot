import exifread

# Read in image from disk in binary format
o = open("file1.jpg",'r+b') 
tags = exifread.process_file(o)
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
	     print("%s @ %s" % (tag, tags[tag]))

print("-----------------------BREAK---------------------")
o = open("file2.jpg",'r+b') 
tags = exifread.process_file(o, stop_tag='UNDEF')
print("EXIF ExifImageWidth @ %s" % ( tags['EXIF ExifImageWidth']))
print("EXIF ExifImageLenght @ %s" % ( tags['EXIF ExifImageLength']))
if tags['Image Make'] :
#	print("Image Make @ %s" % ( tags['Image Make']))
	print("TRUE")
else :
	print("FALSE")
#           print("Image Make @ NULL")

# for tag in tags.keys():
#    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
#       print("%s @ %s" % (tag, tags[tag]))
#       print("EXIF ExifImageWidth @ %s" % ( tags['EXIF ExifImageWidth']))
        

print("-----------------------BREAK---------------------")
o = open("file3.jpg",'r+b') 
tags = exifread.process_file(o)
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
	     print("%s @ %s" % (tag, tags[tag]))

# Return Exif tags

# tags = exifread.process_file(o)

# for tag in tags.keys():
#    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#	     print("Key: %s, value \'%s\'" % (tag, tags[tag]))

#for tag in tags.keys():
#    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
#	     print("%s @ %s" % (tag, tags[tag]))

# And now in CSV format
#for tag in tags.keys():
#   if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'EXIF MakerNote'):
#      print(tags[tag])
#      print(" ,")
