from flask import request, jsonify
import mysql.connector

class AvaliacaoComprasService:

    def postOnDatabase(self):
        jsoninput = request.get_json(force=True)

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('INSERT INTO avaliacao_compra (af, id, fornecedor, preco, prazo, qualidade, condicao_de_pagamento, impacto_positivo, avaliacao_final, observacao) VALUES ('+ str(jsoninput['af']) +','+ str(jsoninput['id']) +',"'+ str(jsoninput['fornecedor']) +'",'+ str(jsoninput['preco']) +','+ str(jsoninput['prazo']) +','+ str(jsoninput['qualidade']) +','+ str(jsoninput['condicao_de_pagamento']) +','+ str(jsoninput['impacto_positivo']) +','+ str(jsoninput['avaliacao_final']) +', "'+ str(jsoninput['observacao']) +'")')

        mydb.commit()

        return jsonify(jsoninput)

    def getAllFromDatabase(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM avaliacao_compra")

        myresult = mycursor.fetchall()

        listOfDicts = []
        dict = {}

        for x in myresult:
            if x[7] == 1:
                impacto_positivo = "Sim"
            else:
                impacto_positivo = "Não"

            dict['af'] = x[0]
            dict['id'] = x[1]
            dict['Fornecedor'] = x[2]
            dict['Preco'] = x[3]
            dict['Prazo'] = x[4]
            dict['Qualidade'] = x[5]
            dict['Condicao de pagamento'] = x[6]
            dict['Impacto positivo'] = impacto_positivo
            dict['Avaliação final'] = x[8]
            dict['Observação'] = x[9]

            listOfDicts.append(dict)
            dict = {}

        return jsonify(listOfDicts)

    def getOneFromDatabase(self, af):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM avaliacao_compra WHERE af = ' + str(af) + ';')

        myresult = mycursor.fetchall()

        dict = {}

        if myresult[0][7] == 1:
            impacto_positivo = "Sim"
        else:
            impacto_positivo = "Não"

        dict['af'] = myresult[0][0]
        dict['id'] = myresult[0][1]
        dict['Fornecedor'] = myresult[0][2]
        dict['Preco'] = myresult[0][3]
        dict['Prazo'] = myresult[0][4]
        dict['Qualidade'] = myresult[0][5]
        dict['Condicao de pagamento'] = myresult[0][6]
        dict['Impacto positivo'] = impacto_positivo
        dict['Avaliação final'] = myresult[0][8]
        dict['Observação'] = myresult[0][9]

        return jsonify(dict)

    def deleteFromDatabase(self, fornecedor):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('DELETE FROM avaliacao_compra WHERE af = ' + str(fornecedor) + ';')

        mydb.commit()

        return "Avaliação foi deletada com sucessso"
