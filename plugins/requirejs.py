import os

def preDeploy(site):
    build_path = site.paths['build']
    os.system("r.js -o %s/app.build.js" % site.path)
    os.system("rm -rf %s/static" % build_path)
    os.system("mv %s/static-build %s/static" % (site.path, build_path))