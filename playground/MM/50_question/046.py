from colorama import init, Fore, Back, Style

init()
print(Fore.RED + "Tekst na czerwono")
print(Back.YELLOW + "... na żółtym tle")
print(Style.RESET_ALL + "... i znowu normalnie")