# set up file for executable application
from cx_Freeze import setup, Executable

includefiles = ['templates/', 'static/']

base = None

main_executable = Executable("app.py", base=base)

setup(name="WebReports",
      version="0.1",
      description="ECO Web Reports",
      options={
          'build_exe': {
              'packages': ['jinja2',
                           'jinja2.ext',
                           'os'],
              'include_files': includefiles,
             }},
      executables=[main_executable], requires=['flask', 'reportlab', 'pyodbc'])
