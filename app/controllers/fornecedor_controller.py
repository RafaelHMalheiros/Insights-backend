from app.services.fornecedor_service import FornecedorService


class FornecedorController:
    def getFornecedor(self, id):
        fornecedorCompras = FornecedorService()
        return fornecedorCompras.getOneFromDatabase(id)
    def postFornecedor(self):
        fornecedorCompras = FornecedorService()
        return fornecedorCompras.postOnDatabase()
    def getAllFornecedores(self):
        fornecedorCompras = FornecedorService()
        return fornecedorCompras.getAllFromDatabase()
    def deleteFornecedor(self, id):
        fornecedorCompras = FornecedorService()
        return fornecedorCompras.deleteFromDatabase(id)