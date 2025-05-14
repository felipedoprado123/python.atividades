from flask import Flask, render_template, request
import os 

#Define a pasta onde estão os aquivos HTML (neste caso, a raíz do projeto)
template_dir = os.path.abspath(os.path.dirname(_file_))