import frontmatter
import pathlib
import datetime

from classes.post import Post

class Posts:
    def __init__(self, source=""): 
        self.source = source
        self.posts = []
        self.refresh()

    def refresh(self):
        posts = []

        postdir = pathlib.Path(self.source)
        mdfiles = postdir.rglob("*.md")

        for item in mdfiles:
            data = frontmatter.load(item)
            post = Post(data)
            post.source_file = item
            posts.append(post)

        self.posts = sorted(posts, key=lambda x: x.published, reverse=True)

    def all(self):
        return self.posts

    # list posts within the past year
    def current(self):
        filtered = []
        limit = datetime.datetime.now()
        limit = limit.replace(year=limit.year - 1)
        
        for p in self.posts:
            pubdate = datetime.datetime(p.published.year, p.published.month, p.published.day)
            
            if pubdate > limit:
                filtered.append(p)

        return filtered
