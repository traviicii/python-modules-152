import custom # from a local module I created myself
from colorama import Fore, Back, Style # we had to pip install the colorama package to use it
# https://pypi.org/project/colorama/
# pip install colorama


from ascii_magic import AsciiArt # had to be installed with pip
# https://pypi.org/project/ascii-magic/
# pip install ascii_magic

# to see currently installed packages globally available you can run the command 'pip list'


custom.hello()

print(Fore.RED + 'some red text')
print('and with a green background')
print(Fore.GREEN + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


my_art = AsciiArt.from_image('./pokeapi_256.png')
my_art.to_terminal()

other_image = AsciiArt.from_url('https://i.pinimg.com/736x/00/68/d5/0068d58c89dbba9b71325a553d8c9480.jpg')
other_image.to_terminal()



# random link to some article with 11 cool python packages:
# https://dev.to/taipy/11-fun-python-libraries-to-make-your-day-better-4gpc

# Google search- "fun python packages"
# https://www.google.com/search?q=fun+python+packages&oq=fun+python+packages&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyCggHEAAYgAQYogQyCggIEAAYgAQYogTSAQgzNjI0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8