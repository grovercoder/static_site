# Static Site

This project generates a static web site based on markdown files and a template.

- The home page (`/index.html`) contains the template and a list of links to your posts
- Static web pages like `/about.html` are generated based on what markdown files are the `static` folder
- The `/posts` folder contains an HTML file for each of your posts

This site folder can then be copied to your webserver as needed.

Usage:

1. Clone this project
2. Edit the `src/template/basic` template to suit your needs, or create a new template folder. (see template notes below)
3. Create your articles/posts as Markdown files in the `posts` folder.  Ensure these have the `.md` extension.
4. Place any image files used by the site in the `static/img` folder.
5. Create any "normal" pages you would like in the `static` folder.  Any Markdown files here will be converted to an HTML file with the template.  For instance `static/about.md` would become `/about.html` in the website.
6. Run the build scripts:

```
    cd <project directory>
    python3 src/python/build.py -s ./static -p ./posts -t basic -o ./mysite
```

    The `mysite` folder will be created and populated as needed.

Posts / Static Pages

A "front matter" section can be defined in the Markdown files to provide some meta information.  For example:

```markdown
---
title: "My Post Title"
published: 2022-01-01
summary: "My Post's brief description"
---
# My Post

I have a post
```

## Templates

For now, templates are expected to be a folder in the `src/template` directory.  If you want to create a "red" template, you would then create the `src/template/red` directory.  Each template directory must have an `index.html` and a `style.css` file. 

The template's `index.html` file is expected to have a place holder contained in it.  Currently the place holder is the string "{main_content}".  This place holder is replaced with the generated HTML elements relevant to the page being created.

## Roadmap

- Add better directory/path handling so the template file can be edited locally, yet the generated file links to the correct location for the styles.css.  The "/css/styles.css" path does not work well when rendering the file in the browser and the file is not at the root of the drive.
- Add tags support, with a way to list posts by tag.
- Add better date support for the "published" front matter value - date and time should be allowed (Or I just need to learn the right incantation).
- Add site level meta data.  Allow the templates to be more generic and not have to hard code the site title and other generic things that occur in almost every page.
- Add SEO support.


## Comments

This works for my immediate needs.  The project was an exercise in both getting my own website up to date, and in diving into code again after a short break.  There are obviously other ways to just get my website updated, but I decided I wanted to do it this way.

I'd like to make this project more generic and useful for other people.  At the moment it seems too tightly coupled to just me.

