from test_api_request import fetch_animals_data


def load_file_content(file_path):
    """loads the content of a text file and returns it as a string.

    Args: file_path (str): path to text file

    Returns: content of file as str"""

    with open(file_path, "r") as file:
        return file.read()


def save_text_to_file(output_path, content):
    """saves text content to a specified file path.

    Args:
    - output_path (str): path to file where content will be saved
    - content (str): text content to save

    Returns: None"""

    with open(output_path, "w") as file:
        file.write(content)


def serialize_animal(animal):
    """generates html string for a single animal entry

    Args: animal (dict): dictionary with animal data

    Returns: html string for the animal entry"""

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
    """loads html template, serializes each animal to html and saves result in new html file.

    Args: data (list): list of dictionaries, each representing an animal's data

    Returns: None"""

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
    """Main function to load data, generate html, and save output.
    Returns: None"""

    # specify animal name for API request
    animal_name = input("Please enter animal name: ")

    # fetch data from API
    animal_data = fetch_animals_data(animal_name)

    # check if data is available/existing before creating html
    if animal_data:
        generate_animal_html(animal_data)
        print("Website was successfully generated to the file animals.html")

    else:
        print(f"No data found for specified animal {animal_name}.")


if __name__ == "__main__":
    main()
