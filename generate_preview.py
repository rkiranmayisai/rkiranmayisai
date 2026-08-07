import json
import base64
import os

with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# Replace image paths with base64 data URIs for local preview
for media_name in ["header_banner.jpg", "developer_illustration.gif"]:
    if os.path.exists(media_name):
        with open(media_name, "rb") as media_f:
            ext = "jpeg" if media_name.endswith(".jpg") else "gif"
            media_b64 = base64.b64encode(media_f.read()).decode('utf-8')
            data_uri = f"data:image/{ext};base64,{media_b64}"
            readme_content = readme_content.replace(f"./{media_name}", data_uri)
            readme_content = readme_content.replace(f"{media_name}", data_uri)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README Preview - Reddy Kiranmayi</title>
    <!-- GitHub Dark Markdown Theme -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <style>
        body {{
            background-color: #0d1117;
            color: #c9d1d9;
            margin: 0;
            padding: 40px 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
        }}
        .markdown-body {{
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
            background-color: #0d1117;
            border: 1px solid #30363d;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .markdown-body img {{
            max-width: 100%;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        }}
    </style>
</head>
<body>
    <article class="markdown-body" id="content"></article>

    <script>
        const rawMarkdown = {json.dumps(readme_content)};
        document.getElementById('content').innerHTML = marked.parse(rawMarkdown);
        hljs.highlightAll();
    </script>
</body>
</html>
"""

with open("preview.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("preview.html created successfully with video animation!")
