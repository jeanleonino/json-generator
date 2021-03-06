import click

@click.command()
@click.option('--obj', '-o', default='', help="The JSON objects name")
@click.option('--element', '-e', default='', help="The element name")
@click.option('--key', '-k', multiple=True, default='', help="The keys for the element")
@click.option('--repeat', '-r', default=1, help = "The amount of elemtns within the JSON object")

def cli(obj, element, key, repeat):
    """This script generates blank JSON models"""
    print obj, element, key, repeat

    properties = []
    print key
    for i in key:
        properties.append(i)
    data = obj
    jsonData = "{\n\t\""+data+"\":[\n\t\t{\n"
    id_num = 0

    for i in range(repeat):
        id_num += 1
        jsonData += "\t\t\t\"id\": " + str(id_num) + ",\n"

        element_num = 0
        for i in properties:
            element_num += 1
            if element_num != len(properties):
                jsonData += "\t\t\t\""+i+"\":\"\",\n"
            else:
                jsonData += "\t\t\t\""+i+"\":\"\"\n"
        if id_num != repeat:
            jsonData += "\n\t\t},\n\n\t\t{\n"

    jsonData += "\n\t\t}\n\t]\n}"

    
    data = open("data.json", 'w')
    data.write(jsonData)
    data.close()
