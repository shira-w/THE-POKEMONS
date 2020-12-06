from mako.template import Template

def write_list_html_t(docs):
    template = """
    <!DOCTYPE html>
    <html>
    <head><title>Pokemon</title><link rel="stylesheet" type="text/css" href="style.css" />
</head>
    <body>
      <img id="image" src="image.png" onload="resizeToMax(this.id)"> </img>

    % for doc in docs:
    <footer><a href="/select_pokemons?trainer=${doc}"  style="font-size: 20px; text-decoration: none"> ${doc} </a></div></footer>
    % endfor
    </body>
    </html>
    """
    res= Template(template).render(docs=docs)
    Html_file= open("templates/trainers.html","w")
    Html_file.write(res)
    Html_file.close()
