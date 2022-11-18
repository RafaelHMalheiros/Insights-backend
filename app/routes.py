from mvc_flask import Router

Router.get("/return/avaliacao_compras/<af>", "avaliacao_compras#getAvaliacaoCompra")
Router.post("/new/avaliacao_compras", "avaliacao_compras#postAvaliacaoCompra")
Router.get("/returnall/avaliacao_compras", "avaliacao_compras#getAllAvaliacaoCompras")
Router.delete("/delete/avaliacao_compras/<af>", "avaliacao_compras#deleteAvaliacaoCompra")

Router.get("/return/avaliacao/<fornecedor>", "avaliacao_geral#getAvaliacao")
Router.post("/new/avaliacao", "avaliacao_geral#postAvaliacao")
Router.get("/returnall/avaliacao", "avaliacao_geral#getAllAvaliacoes")
Router.delete("/delete/avaliacao/<fornecedor>", "avaliacao_geral#deleteAvaliacao")

Router.get("/return/compras/<af>", "compras#getCompra")
Router.post("/new/compras", "compras#postCompra")
Router.get("/returnall/compras", "compras#getAllCompras")

Router.get("/return/fornecedor/<id>", "fornecedor#getFornecedor")
Router.post("/new/fornecedor", "fornecedor#postFornecedor")
Router.get("/returnall/fornecedor", "fornecedor#getAllFornecedores")
Router.delete("/delete/fornecedor/<id>", "fornecedor#deleteFornecedor")

Router.get("/return/funcionarios/<id>", "funcionarios#getFuncionario")
Router.post("/new/funcionarios", "funcionarios#postFuncionario")
Router.get("/returnall/funcionarios", "funcionarios#getAllFuncionarios")
Router.delete("/delete/funcionarios/<id>", "funcionarios#deleteFuncionario")




