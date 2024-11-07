import json


def load_json_data(file_path):
    """loads JSON-data from specified file path"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_file_content(file_path):
    """loads the content of a text file and returns it as a string."""
    with open(file_path, "r") as file:
        return file.read()


def save_text_to_file(output_path, content):
    """saves text content to a specified file path."""
    with open(output_path, "w") as file:
        file.write(content)


def serialize_animal(animal):
    """generates html string for a single animal entry"""

    output = '<li class="cards__item">\n'

    # add name as title
    name = animal.get("name")
    if name:
        output += f'<div class="card__title"> {name}</div>\n'

    # add other characteristics as text
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations")
    animal_type = characteristics.get("type")

    output += '<p class="card__text">\n'

    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br/>\n'
    if animal_type:
        output += f'<strong>Type: </strong>{animal_type}<br/>\n'
    output += '  </p>\n'

    # close the list item for this animal
    output += '</li>\n'

    return output


def generate_animal_html(data):
    """loads html template, serializes each animal to html and saves result in new HTML file."""

    # load html template using load_file_content function
    html_template = load_file_content('animals_template.html')

    # generate html code for each animal and add it to list
    output = ""
    for animal in data:
        output += serialize_animal(animal)

    # replace placeholder in html template with generated html
    html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

    # save generated HTML content to the specified output file
    save_text_to_file('animals.html', html_content)


def main():
    """Main function to load data, generate HTML, and save output."""
    # load animal data from JSON file
    animals_data = load_json_data('animals_data.json')

    # generate html and save it to a file
    generate_animal_html(animals_data)


if __name__ == "__main__":
    main()
