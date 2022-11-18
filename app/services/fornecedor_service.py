from flask import request, jsonify
import mysql.connector

class FornecedorService:

    def postOnDatabase(self):
        jsoninput = request.get_json(force=True)

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('INSERT INTO fornecedores (id, fornecedor, produto, email, contato_telefonico, cidade, fornecedor_local, link, categoria, status_atual, filial) VALUES ('+ str(jsoninput['id']) +',"'+ str(jsoninput['fornecedor']) +'","'+ str(jsoninput['produto']) +'","'+ str(jsoninput['email']) +'","'+ str(jsoninput['contato_telefonico']) +'","'+ str(jsoninput['cidade']) +'",'+ str(jsoninput['fornecedor_local']) +',"'+ str(jsoninput['link']) +'","'+ str(jsoninput['categoria']) +'","'+ str(jsoninput['status_atual']) +'","'+ str(jsoninput['filial']) +'")')

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

        mycursor.execute("SELECT * FROM fornecedores")

        myresult = mycursor.fetchall()

        listOfDicts = []
        dict = {}

        for x in myresult:
            if x[6] == 1:
                fornecedor_local = "Sim"
            else:
                fornecedor_local = "Não"

            dict['Id'] = x[0]
            dict['Fornecedor'] = x[1]
            dict['Produto'] = x[2]
            dict['Email'] = x[3]
            dict['Contato telefonico'] = x[4]
            dict['cidade'] = x[5]
            dict['Condicao de pagamento'] = fornecedor_local
            dict['Link'] = x[7]
            dict['Categoria'] = x[8]
            dict['Status Atual'] = x[9]
            dict['filial'] = x[10]

            listOfDicts.append(dict)
            dict = {}

        return jsonify(listOfDicts)

    def getOneFromDatabase(self, id):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM fornecedores WHERE id = ' + str(id) + ';')

        myresult = mycursor.fetchall()

        dict = {}

        if myresult[0][6] == 1:
            fornecedor_local = "Sim"
        else:
            fornecedor_local = "Não"

        dict['Id'] = myresult[0][0]
        dict['Fornecedor'] = myresult[0][1]
        dict['Produto'] = myresult[0][2]
        dict['Email'] = myresult[0][3]
        dict['Contato telefonico'] = myresult[0][4]
        dict['cidade'] = myresult[0][5]
        dict['Condicao de pagamento'] = fornecedor_local
        dict['Link'] = myresult[0][7]
        dict['Categoria'] = myresult[0][8]
        dict['Status Atual'] = myresult[0][9]
        dict['filial'] = myresult[0][10]

        return jsonify(dict)

    def deleteFromDatabase(self, id):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Insight",
            database="insight"
        )

        mycursor = mydb.cursor()

        mycursor.execute('DELETE FROM fornecedores WHERE id = ' + str(id) + ';')

        mydb.commit()

        return "Fornecedor foi deletada com sucessso"
