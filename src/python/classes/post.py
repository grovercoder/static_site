
import markdown
import frontmatter
from slugify import slugify
from classes.template import Template

class Post:
    def __init__(self, data):
        self.title = ""
        self.published = None
        self.tags = []
        self.summary = ""
        self.content = ""
        self.source_file = ""

        if isinstance(data, frontmatter.Post):
            keys = data.keys()
            for key in keys:
                keylower = key.lower()

                if keylower == 'title':
                    self.title = data[key]
                if keylower == 'published':
                    self.published = data[key]
                if keylower == "summary":
                    self.summary = data[key]
                if keylower == 'tags':
                    self.tags.append(data[key].split(','))

            self.content = data.content

    def slug(self):
        return slugify(self.title)

    def markdown(self):
        return self.content

    def html(self):
        return markdown.markdown(self.content)

    def page(self, template=None, template_file=None, placeholder="{main_content}"):
        currentTemplate = Template(name=template, file=template_file, placeholder=placeholder)
        return currentTemplate.page(self.html())

    def listItem(self):
        posturl = f"./posts/{self.slug()}.html"
        listitem = f'<section class="post"><div class="title"><h2><a href="{posturl}">{self.title}</a><h2></div><div class="meta">{self.published}</div><div class="summary">{self.summary}</div></section>'

        return listitem

        
