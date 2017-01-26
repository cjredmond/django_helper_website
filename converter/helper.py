def model_add(model_name, fields):
    model_string = "class {}(models.Model():\n".format(model_name.title())
    for field in fields:
        model_string += "\t{} = models.{}\n".format(field[0],field[1])
    return model_string



# print(model_add('post',[['first', 'string'],['second', 'string']]))
