def model_add(model_name, fields):
    model_string = "class {}(models.Model():\n".format(model_name.title())
    for field in fields:
        model_string += "\t{} = models.{}\n".format(field[0],field[1])
    return model_string

def detail_view_add(model_name):
    detail_string = "\nclass {}DetailView(DetailView)\n\tmodel = {}".format(model_name.title(), model_name)
    return detail_string

def list_view_add(model_name):
    list_string = "\nclass {}ListView(ListView) \n\tmodel = {}".format(model_name.title(), model_name)
    return list_string

def create_view_add(model_name, fields):
    create_string = "\nclass {}CreateView(CreateView) \n\t".format(model_name.title())
    create_string += "model = {}\n".format(model_name)
    create_string += "\tfields = ({})\n".format([str(x[0]) for x in fields])
    create_string += "\tdef form_valid(self,form):\n"
    create_string += "\t\tinstance = form.save(commit=False)\n"
    create_string += "\t\treturn super().form_valid(form)\n"
    create_string += "\tdef get_success_url(self):\n\treturn '/'"
    return create_string

def update_view_add(model_name, fields):
    update_string = "\nclass {}UpdateView(UpdateView):\n".format(model_name.title())
    update_string += "\tmodel = {}\n".format(model_name)
    update_string += "\tfields = ({})\n".format([str(x[0]) for x in fields])
    update_string += "\tsuccess_url = '/'"
    return update_string

def url_add(model_name):
    url_string = "\turl(r'^{}/(?P<pk>\d+)/$', {}DetailView.as_view(), name='{}_index_view'),\n".format(model_name, model_name.title(), model_name)
    url_string += "\turl(r'^{}s/$', {}ListView.as_view(), name='{}_list_view'),\n".format(model_name, model_name.title(), model_name)
    url_string += "\turl(r'^{}/new/$', {}CreateView.as_view(), name='{}_create_view'),\n".format(model_name, model_name.title(), model_name)
    url_string += "\turl(r'^{}/(?P<pk>\d+)/update/$', {}UpdateView.as_view(), name='{}_update_view',\n".format(model_name, model_name.title(), model_name)
    return url_string

def detail_template_add(model_name):
    html_string = "<h2>{} Detail View</h2>\nThis page refers to a specific {}".format(model_name.title(), model_name)
    return html_string

def list_template_add(model_name):
    html_string = "<h2>{} List View</h2>\nThis page lists all {}s".format(model_name.title(), model_name)
    html_string += "\n{% for item in object_list %}\n\t{{ item }}\n{% endfor %}"
    return html_string

def create_template_add(model_name):
    html_string = "<h2>Add a new {}</h2>".format(model_name)
    html_string += "\n<form class='' method='post'>\n{% csrf_token %}\n{{ form }}"
    html_string += "\n<input type='submit' value='submit>'\n</form>"
    return html_string

# print(model_add('post',[['first', 'string'],['second', 'string']]))
