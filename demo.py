class OlaMundo:
    def __enter__(self):
        print("Entrando")
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('saindo')

with OlaMundo() as ola:
    print('no meio')