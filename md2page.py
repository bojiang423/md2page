"""
This script converts markdown files into html files, and include the urls to index.html 
The name of the markdown file should be "yyyy-mm-dd-title.md"
"""
import os
import markdown

markdown_dir = "markdown/"
pages_dir = "pages/"
index_filename = "index.html"
page_header = "<h1>Markdown to Pages</h1><hr>"

# convert markdown to html 
def brew_md_2_html(markdown_filename):

    markdown_fullname = markdown_dir + markdown_filename
    html_filename= os.path.splitext(markdown_filename)[0] + ".html"
    html_fullname = pages_dir + html_filename
    page_date = html_filename[:10]
    page_title = os.path.splitext(markdown_filename)[0][11:]
    page_title = page_title.replace("-", " ")

    with open(markdown_fullname, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    html = page_header + html

    with open(html_fullname, 'w') as f:
        f.write(html)

    return html_fullname, page_date, page_title
        
if __name__ == "__main__":

    # delete all existing pages 
    pages = os.listdir(pages_dir)
    no_of_pages = len(pages)
    for page in pages:
        os.remove(pages_dir + page)
    #print(str(no_of_pages) + " pages are deleted")

    # get all markdown files 
    files = os.listdir(markdown_dir)
    # sort by name 
    files.sort()

    # convert markdown files to html pages
    index_page_content = page_header
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext.upper() in (".MD", ".MARKDOWN"):
            html_fullname, page_date, page_title = brew_md_2_html(file)
            index_page_content = index_page_content + \
                    "<p><a href='" + html_fullname + "'>" + \
                    "[" + page_date + "] " + \
                    page_title + "</a></p>"

    # update index.html page  
    with open(index_filename, "w") as f:
        f.write(index_page_content) 
    
