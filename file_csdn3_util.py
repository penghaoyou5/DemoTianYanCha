# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

def write_error(error_obj):
    error_file = open("error.file","a+")
    error_file.writelines(str(error_obj))
    error_file.close()