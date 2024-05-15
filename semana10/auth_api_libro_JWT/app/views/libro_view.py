def render_libro_list(libros):
    return [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "edicion": libro.edicion,
            "disponibilidad": libro.disponibilidad,
        }
        for libro in libros
    ]


def render_libro_detail(libro):
    return {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "edicion": libro.edicion,
        "disponibilidad": libro.disponibilidad,
    }