from flask import request, jsonify
import mysql.connector

class AvaliacaoGeralService:
    def postOnDatabase(self):
        jsoninput = request.get_json(force=True)

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('INSERT INTO avaliacao_geral (fornecedor, preco, prazo, qualidade, condicao_de_pagamento, impacto_positivo, avaliacao_final, observacao) VALUES ("'+ str(jsoninput['fornecedor']) +'",'+ str(jsoninput['preco']) +','+ str(jsoninput['prazo']) +','+ str(jsoninput['qualidade']) +','+ str(jsoninput['condicao_de_pagamento']) +','+ str(jsoninput['impacto_positivo']) +','+ str(jsoninput['avaliacao_final']) +', "'+ str(jsoninput['observacao']) +'")')

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

        mycursor.execute("SELECT * FROM avaliacao_geral")

        myresult = mycursor.fetchall()

        listOfDicts = []
        dict = {}

        for x in myresult:
            if x[5] == 1:
                impacto_positivo = "Sim"
            else:
                impacto_positivo = "Não"

            dict['Fornecedor'] = x[0]
            dict['Preco'] = x[1]
            dict['Prazo'] = x[2]
            dict['Qualidade'] = x[3]
            dict['Condicao de pagamento'] = x[4]
            dict['Impacto positivo'] = impacto_positivo
            dict['Avaliação final'] = x[6]
            dict['Observação'] = x[7]

            listOfDicts.append(dict)
            dict = {}

        return jsonify(listOfDicts)

    def getOneFromDatabase(self, fornecedor):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM avaliacao_geral WHERE fornecedor = "' + str(fornecedor) + '";')

        myresult = mycursor.fetchall()

        dict = {}

        if myresult[0][5] == 1:
            impacto_positivo = "Sim"
        else:
            impacto_positivo = "Não"

        dict['Fornecedor'] = myresult[0][0]
        dict['Preco'] = myresult[0][1]
        dict['Prazo'] = myresult[0][2]
        dict['Qualidade'] = myresult[0][3]
        dict['Condicao de pagamento'] = myresult[0][4]
        dict['Impacto positivo'] = impacto_positivo
        dict['Avaliação final'] = myresult[0][6]
        dict['Observação'] = myresult[0][7]

        return jsonify(dict)
    def deleteFromDatabase(self, fornecedor):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('DELETE FROM avaliacao_geral WHERE fornecedor = "' + str(fornecedor) + '";')

        mydb.commit()

        return "Avaliação foi deletada com sucessso"
