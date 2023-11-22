from jinja2 import Template, FileSystemLoader, Environment
from user import information_to_list

file_name = 'txt_files/information_about_all_users.txt'
users_information = information_to_list(file_name)


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('content.html')
msg = tm.render(users=users_information)


def safe_text_to_html(n_html_file, mess):
    """Сохраняет информацию в файл, а если файл уже существует, то удаляет его и создаёт новый"""
    with open(n_html_file, 'w') as f:
        f.write(mess)


name_html_file = 'users_htmlcode.html'
safe_text_to_html(name_html_file, msg)
