# Temp  First fetch an image from the internet
import urllib
import exifread

myImage = urllib.urlretrive('https://farm9.staticflickr.com/8367/8588252956_49d28ddb1a_z.jpg')
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print "Key: %s, value %s" % (tag, tags[tag])
