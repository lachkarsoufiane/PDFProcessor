from interface.IFormatterStrategy import IForamtterStrategy
from collections import namedtuple

class TableDSCCFormatterStrategy(IForamtterStrategy):
    def format(content):
        table = namedtuple('table', 'Document Description URL')
        order_table = []

        for column in content:
            document = column["Document"]
            document = column["Document"]
            order_table.append(table(document))
        
        return order_table