from infra.configs.connection import DBConnectionHandle
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes


class AtoresRepository:
    def select(self):
        with DBConnectionHandle() as db:
            data = (
                db.session.query(Atores)
                .join(Filmes, Filmes.titulo == Atores.titulo_filme)
                .with_entities(Atores.nome, Filmes.genero, Filmes.titulo)
                .all()
            )
            return data
