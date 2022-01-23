def generic_model_mutation_process(model, data, id=None, commit=True):
    """
    Crea y actualiza objetos en base de datos a un model y un id;
    Esta funcion se debe utilizar momento de actualizar o añadir director, pelicula(film), persona(people)
    paneta(planet) productor(producer), si en el query se especifica el id, se debe actualizar el objeto, de lo contrario
    se añade un nuevo objeto.

    Para añadir a la base de datos:
    Cuando se llama la función de añadir mediante el query, esta no ingresa un parámetro id del usuario y por tal razón
    no ingresa a la condición de la línea 19 ya que id es null por defecto; pero si entra a la condición de la línea 31
    verifica que sus campos estén correctos y por consiguiente lo guarda en la base de datos cuando ingresa a la condición
    de la línea 35.

    Para actualizar a la base de datos
    Cuando se llama la función de añadir mediante el query, esta ingresa como parámetro el id del usuario y por tal razón
    ingresa a la condición de la línea 19 ya que existe id como parámetro, luego busca en la base de datos según el id
    trae el objeto, luego en la line 32 de data borra el objeto llamado id del diccionario, después procede a remplazar
    campo por campo del data ingresado por el query al diccionario de la variable item; por consiguiente lo guarda en 
    la base de datos cuando ingresa a la condición de la línea 35.

    :param model: Model de Django:.
    :param data: Dict con los fields para el objeto a creat/actualizar.
    :param id: Int para buscar el objeto a actualizar
    :param commit: Indica si se debe guardar el objeto.
    :return: model instance.
    """
    print(id)
    if id:
        print("entra")
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            # Sacar el id por si envían el data tal cual llega.
            pass

        for field, value in data.items():
            setattr(item, field, value)

    else:
        item = model(**data)
        # TODO: Verificaciones, auto_ids, hashing, asserts, etc.

    if commit:
        item.save()

    return item
