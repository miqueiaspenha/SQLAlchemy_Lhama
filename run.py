# from infra.repository.filmes_repository import FilmesRepository

# repo = FilmesRepository()

# repo.insert("qualquer filme", "comedia", 2010)

# repo.delete("Batman")

# data = repo.select()

# print(data)

#############################################################

from infra.repository.atores_repository import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository


repo = AtoresRepository()
response = repo.select()
# print(response)

repo2 = FilmesRepository()
response2 = repo2.select()
response2_1 = repo2.select_drama_filmes()

# filme = response2[0]
# print(filme.atores)
# print(filme.titulo)

print(response2_1)
