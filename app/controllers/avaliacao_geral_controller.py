from app.services.avaliacao_geral_service import *

class Avaliacao_GeralController:
    def getAvaliacao(self, fornecedor):
        avaliacaoGeral = AvaliacaoGeralService()
        return avaliacaoGeral.getOneFromDatabase(fornecedor)
    def postAvaliacao(self):
        avaliacaoGeral = AvaliacaoGeralService()
        return avaliacaoGeral.postOnDatabase()
    def getAllAvaliacoes(self):
        avaliacaoGeral = AvaliacaoGeralService()
        return avaliacaoGeral.getAllFromDatabase()
    def deleteAvaliacao(self, fornecedor):
        avaliacaoGeral = AvaliacaoGeralService()
        return avaliacaoGeral.deleteFromDatabase(fornecedor)
