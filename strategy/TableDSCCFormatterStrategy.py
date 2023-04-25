from interface.IFormatterStrategy import IForamtterStrategy
from collections import namedtuple
import json
import pandas as pd

class TableDSCCFormatterStrategy(IForamtterStrategy):
    def format(content):
        content = json.loads(content)
        table = namedtuple('table', 'Document Description URL')
        order_table = []

        for column in content:
            document = column["Document"]
            description = column["Description"]
            url = column["URL"]
            order_table.append(table(document, description, url))
        return order_table