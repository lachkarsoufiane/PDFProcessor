from interface.IGenerator import IGenerator
import re

class NameGenerator(IGenerator):
    def generate(path):
        file_name = re.split('\/', path)[-1]
        name = file_name.split(".")[0]
        return name