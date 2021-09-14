import astropy.table as table
import pkg_resources


def get_table(n: int):
    stream = pkg_resources.resource_stream(__name__, f'data/table_{n}.csv')
    return table.Table.read(stream, format="ascii.csv")
