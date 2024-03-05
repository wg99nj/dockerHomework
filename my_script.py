from pystrich.datamatrix import DataMatrixEncoder
encoder = DataMatrixEncoder("Matrix")
encoder.save('./output.png')
print(encoder.get_ascii())