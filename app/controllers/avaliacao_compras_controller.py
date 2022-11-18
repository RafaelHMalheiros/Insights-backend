from app.services.avaliacao_compras_service import *


class Avaliacao_ComprasController:
    def getAvaliacaoCompra(self, af):
        avaliacaoCompras = AvaliacaoComprasService()
        return avaliacaoCompras.getOneFromDatabase(af)
    def postAvaliacaoCompra(self):
        avaliacaoCompras = AvaliacaoComprasService()
        return avaliacaoCompras.postOnDatabase()
    def getAllAvaliacaoCompras(self):
        avaliacaoCompras = AvaliacaoComprasService()
        return avaliacaoCompras.getAllFromDatabase()
    def deleteAvaliacaoCompra(self, af):
        avaliacaoCompras = AvaliacaoComprasService()
        return avaliacaoCompras.deleteFromDatabase(af)