import glob
import os
import Image

MAX_WIDTH = 540
MAX_HEIGHT = 800

def preDeploy(site):
    build_path = site.paths['build']
    images_path = "%s/static/images/" % build_path
    print images_path
    print "="*100
    for image_path in glob.glob("%s*" % images_path):
        path = image_path.split('/')
        filename = path[-1]
        (name, ext) = filename.split('.')
        if not name.endswith('-full'):
            full_path = "%s/%s-full.%s" % (images_path, name, ext)
            if not os.path.exists(full_path):
                im = Image.open(image_path)
                os.rename(image_path, full_path)
                im.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.ANTIALIAS)
                im.save(image_path)
        
    print "="*100
    