import os
import shutil
import re
from markdown_blocks import markdown_to_html_node


PUBLIC_DIR_NAME = 'public'
STATIC_DIR_NAME = 'static'
CONTENT_DIR_NAME = 'content'

def extract_title(markdown: str) -> str:
    match = re.search(r'^# (.*)$', markdown, re.MULTILINE)

    if match:
        return match.group(1)

    raise ValueError('No title found in markdown')

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    # Print a message like "Generating page from from_path to dest_path using template_path".
    print(f"Generating page from `{from_path}` to `{dest_path}` using `{template_path}`")

    markdown: str | None = None
    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path, 'r') as file:
        # Read the template file at template_path and store the contents in a variable.
        markdown = file.read()

    template: str | None = None
    with open(template_path, 'r') as file:
        template = file.read()

    html_string = markdown_to_html_node(markdown).to_html()
    extracted_title = extract_title(markdown)

    # Replace the string "{{ title }}" in the template with the extracted title.
    template = template.replace('{{ Title }}', extracted_title)
    # Replace the string "{{ content }}" in the template with the markdown content.
    template = template.replace('{{ Content }}', html_string)

    print("\n\n\n", "dest_path: ", dest_path, "\n\n\n")
    # Write the modified template to dest_path.
    with open(dest_path, 'w') as file:
        file.write(template)


    # Read the template file at template_path and store the contents in a variable.


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str)  -> None:
    # base_path_from = os.path.join(os.getcwd(), PUBLIC_DIR_NAME)
    # base_path_to = os.path.join(os.getcwd(), STATIC_DIR_NAME)
    items = os.listdir(path=dir_path_content)
    for item in items:
        from_path = f"{dir_path_content}/{item}"
        to_path = f"{dest_dir_path}/{item}"
        if os.path.isdir(from_path):
            if (not os.path.isdir(to_path)):
                os.mkdir(to_path)
            generate_pages_recursive(from_path, template_path, to_path)
        else:
            # shutil.copy(src=f'{base_path_to}/{item}', dst=f'{base_path_from}/{item}')
            formatted_to_path = to_path;

            if (to_path.endswith(".md") ):
                base_name, _ = os.path.splitext(to_path)
                formatted_to_path = base_name + "." + "html"

            generate_page(
                from_path,
                template_path,
                formatted_to_path
            )

def build():
    if (os.path.exists(path=f'./{PUBLIC_DIR_NAME}')):
        shutil.rmtree(path=f'./{PUBLIC_DIR_NAME}')

    os.makedirs(name=f'./{PUBLIC_DIR_NAME}')

    items = os.listdir(path=f'./{STATIC_DIR_NAME}')

    base_path_from = os.path.join(os.getcwd(), PUBLIC_DIR_NAME)
    base_path_to = os.path.join(os.getcwd(), STATIC_DIR_NAME)
    for item in items:
        if os.path.isdir(f'{base_path_to}/{item}'):
            shutil.copytree(src=f'{base_path_to}/{item}', dst=f'{base_path_from}/{item}')
        else:
            shutil.copy(src=f'{base_path_to}/{item}', dst=f'{base_path_from}/{item}')

    # Generate a page from content/index.md using template.html and write it to public/index.html.
    # generate_page(from_path=('./content/index.md'), template_path=('./template.html'), dest_path=(f'./{PUBLIC_DIR_NAME}/index.html'))
    generate_pages_recursive('./content', './template.html', PUBLIC_DIR_NAME)

def main():
    build()

if __name__ == "__main__":
    main()
