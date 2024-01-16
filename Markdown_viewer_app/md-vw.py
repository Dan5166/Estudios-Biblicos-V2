import markdown
with open("Mateo.md", "r") as f:
    text_md=f.read()
text_html=markdown.markdown(text_md, extensions=['markdown.extensions.tables'])
print(text_html)

# Le agregamos el encabezado y el pie de página
text_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Markdown viewer</title>
<link rel="stylesheet" href="studiesStyles.css">
</head>
<body>
""" + text_html + """
</body>
</html>
"""

# Lo guardamos en un archivo html
with open("Mateo.html", "w") as f:
    f.write(text_html)
