def render_producto_list(productos):
    return [
        {
            "id": producto.id,
            "name": producto.name,
            "description": producto.description,
            "price": producto.price,
            "stock": producto.stock,
        }
        for producto in productos
    ]


def render_producto_detail(producto):
    return {
        "id": producto.id,
        "name": producto.name,
        "description": producto.description,
        "price": producto.price,
        "stock": producto.stock,
    }