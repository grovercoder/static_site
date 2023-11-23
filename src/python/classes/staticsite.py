import string
import random
import pathlib
import shutil
import os
import markdown

from classes.posts import Posts
from classes.template import Template
from classes.content import Content

# BUILD_DIR = "../build"
# TEMPLATE_DIR = "../template"
# STATIC_DIR = "../static"
# TEMPLATE_PLACEHOLDER = "{main_content}"

class StaticSite:
    def __init__(self, template="basic", static="", posts="", output=""):
        self.template = Template(template)
        self.static = static
        self.posts = Posts(source=posts)
        self.output = output

    def _hash_generator(self, size=6, chars=string.ascii_uppercase + string.digits) :
        return ''.join(random.choice(chars) for _ in range(size))

    def resetBuildDir(self):
        # remove build directory if it exists
        print(": Removing previous build directory")
        shutil.rmtree(self.output, ignore_errors=True)

        # create the css, img, and posts directories
        print(": Creating directories")
        cssdir = f"{self.output}/css"
        imgdir = f"{self.output}/img"
        postsdir = f"{self.output}/posts"

        os.makedirs(cssdir)
        os.makedirs(imgdir)
        os.makedirs(postsdir)

        # copy the template style
        print(": Copying template style")
        shutil.copy(f"{self.template.dir}/style.css", f"{cssdir}")
        shutil.copy(f"{self.template.dir}/style.css.map", f"{cssdir}")

        # copy static images
        print(": Copying static images")
        shutil.copytree(f"{self.static}/img", f"{imgdir}", dirs_exist_ok=True)

    # create the home page, with a listing of current posts
    def buildHomePage(self):
        print(": Creating the home page")
        postblocks = []
        for post in self.posts.current():
            postblocks.append(post.listItem())

        listhtml = f'<div id="postList">{"".join(postblocks)}</div>'
        homehtml = self.template.page(listhtml)
        with open(f"{self.output}/index.html", 'w') as fh:
            fh.write(homehtml)

    # Any *.md file in the static directory will become a HTML file in the root of the site.
    def createStandardPages(self):
        print(": Creating other pages")
        staticdir = pathlib.Path(self.static)
        standardFiles = staticdir.rglob("*.md")

        for md in standardFiles:
            content = Content(md)
            target_file = f"{self.output}/{md.stem}.html"
            with open(target_file, 'w') as tf:
                tf.write(content.page())

    # create a page for each of the posts
    def createPostPages(self):
        print(": Creating post pages")
        for post in self.posts.all():
            target_file = f"{self.output}/posts/{post.slug()}.html"
            with open(target_file, 'w') as tf:
                tf.write(post.page())

    # re-generate the static site from scratch
    def generate(self, template=None):
        self.template = Template(name=template)
        self.resetBuildDir()
        self.buildHomePage()
        self.createPostPages()
        self.createStandardPages()
        print("Done")

        