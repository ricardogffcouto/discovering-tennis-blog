
import markdown
import os

POSTS_DIR = "posts"
PUBLIC_DIR = "public"

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            posts.append(filename)
    return sorted(posts, reverse=True)

def main():
    if not os.path.exists(PUBLIC_DIR):
        os.makedirs(PUBLIC_DIR)

    posts = get_posts()
    index_content = ""

    for post_filename in posts:
        with open(os.path.join(POSTS_DIR, post_filename), "r") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)
        post_basename = os.path.splitext(post_filename)[0]
        post_html_filename = f"{post_basename}.html"

        with open(os.path.join(PUBLIC_DIR, post_html_filename), "w") as f:
            f.write(html_content)

        index_content += html_content
        index_content += "\n<hr>\n"

    with open(os.path.join(PUBLIC_DIR, "index.html"), "w") as f:
        f.write(index_content)

if __name__ == "__main__":
    main()
