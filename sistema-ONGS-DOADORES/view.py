import re
from flask import Flask, jsonify, request
from main import app, con
from flask_bcrypt import generate_password_hash, check_password_hash

# DOADOR - CADASTRO

@app.route('/cadastro_doador', methods=['GET'])
def cadastro_doador():
    cur = con.cursor()
    cur.execute("SELECT id_usuario, nome, e_mail, senha FROM usuario")
    doador = cur.fetchall()
    doador_dic = []
    for doadores in doador:
        doador_dic.append({
            'id_usuario': doadores[0],
            'nome': doadores[1],
            'e_mail': doadores[2],
            'senha': doadores[3]
        })
    return jsonify(mensagem='Registro de Cadastro de Doadores', doadores=doador_dic)

def validar_senha_doador(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%¨&*])(?=.*\d).{8,}$'

    if re.fullmatch(padrao, senha):
        return True
    else:
        return False

@app.route('/cadastro_doador', methods=['POST'])
def doador_post():
    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    if not validar_senha_doador(senha):
        return jsonify('A sua senha precisa ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')

    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE E_MAIL = ?", (e_mail,))

    if cursor.fetchone():
        return jsonify({"error": "E-mail já cadastrado!"}), 400

    senha = generate_password_hash(senha).decode('utf-8')

    cursor.execute("INSERT INTO USUARIO(NOME, E_MAIL, SENHA) VALUES (?, ?, ?)",
                   (nome, e_mail, senha))

    con.commit()
    cursor.close()

    return jsonify({
        'message': "Doador registrado com sucesso!",
        'usuario': {
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha
        }
    })


@app.route('/cadastro_doador/<int:id>', methods=['PUT'])
def doador_put(id):
    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha from usuario WHERE id_usuario = ?", (id,))
    doador_data = cursor.fetchone()

    if not doador_data:
        cursor.close()
        return jsonify({"Registro do Doador não encontrado."})

    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor.execute("UPDATE usuario SET NOME = ?, E_MAIL = ?, SENHA = ? WHERE ID_USUARIO = ?",
                   (nome, e_mail, senha, id))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Cadastro do Doador atualizado com sucesso!",
        'usuario': {
            'id_usuario': id,
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha
        }
    })

@app.route('/cadastro_doador/<int:id>', methods=['DELETE'])
def deletar_cadastro_doador(id):
    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE ID_USUARIO = ?", (id,))
    if not cursor.fetchone():
        cursor.close()
        return jsonify({"error": "Registro do Doador não encontrado."}), 404

    cursor.execute("DELETE FROM usuario WHERE ID_USUARIO = ?", (id,))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Cadastro do Doador excluído com sucesso!",
        'id_usuario': id
    })



# DOADOR - LOGIN

@app.route('/login_doador', methods=['POST'])
def login_doador():
    data = request.get_json()
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha, tipo from usuario WHERE e_mail = ?", (e_mail,))
    login_data = cursor.fetchone()

    if not login_data:
        cursor.close()
        return jsonify({'erro': "Credenciais não encontradas"}), 400

    senha_hash = login_data[3]

    if check_password_hash(senha_hash, senha):
        if login_data[4] == 3:
            return jsonify({
                'message': "Login do doador feito com sucesso!"
            })
    else:
        return jsonify({
            'message': "Erro no login do doador!"
        })



# ONG - CADASTRO

@app.route('/cadastro_ong', methods=['GET'])
def cadastro_ong():
    cur = con.cursor()
    cur.execute("SELECT id_usuario, nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco FROM usuario")
    ong = cur.fetchall()
    ong_dic = []
    for ongs in ong:
        ong_dic.append({
            'id_usuario': ongs[0],
            'nome': ongs[1],
            'e_mail': ongs[2],
            'senha': ongs[3],
            'cnpj': ongs[4],
            'categoria': ongs[5],
            'descricao_da_causa': ongs[6],
            'cep': ongs[7],
            'chave_pix': ongs[8],
            'num_agencia': ongs[9],
            'num_conta': ongs[10],
            'nome_banco': ongs[11]
        })
    return jsonify(mensagem='Registro de Cadastro de ONGs', ongs=ong_dic)

def validar_senha_ong(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%¨&*])(?=.*\d).{8,}$'

    if re.fullmatch(padrao, senha):
        return True
    else:
        return False

@app.route('/cadastro_ong', methods=['POST'])
def ong_post():
    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')
    cnpj = data.get('cnpj')
    categoria = data.get('categoria')
    descricao_da_causa = data.get('descricao_da_causa')
    cep = data.get('cep')
    chave_pix = data.get('chave_pix')
    num_agencia = data.get('num_agencia')
    num_conta = data.get('num_conta')
    nome_banco = data.get('nome_banco')

    if not validar_senha_ong(senha):
        return jsonify('A sua senha precisa ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.')

    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE E_MAIL = ?", (e_mail,))

    if cursor.fetchone():
        return jsonify({"error": "E-mail já cadastrado!"}), 400

    senha = generate_password_hash(senha).decode('utf-8')

    cursor.execute("INSERT INTO USUARIO(NOME, E_MAIL, SENHA, CNPJ, CATEGORIA, DESCRICAO_DA_CAUSA, CEP, CHAVE_PIX, NUM_AGENCIA, NUM_CONTA, NOME_BANCO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco))

    con.commit()
    cursor.close()

    return jsonify({
        'message': "ONG registrada com sucesso!",
        'usuario': {
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha,
            'cnpj': cnpj,
            'categoria': categoria,
            'descricao_da_causa': descricao_da_causa,
            'cep': cep,
            'chave_pix': chave_pix,
            'num_agencia': num_agencia,
            'num_conta': num_conta,
            'nome_banco': nome_banco
        }
    })


@app.route('/cadastro_ong/<int:id>', methods=['PUT'])
def ong_put(id):
    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco from usuario WHERE id_usuario = ?", (id,))
    ong_data = cursor.fetchone()

    if not ong_data:
        cursor.close()
        return jsonify({"Registro da ONG não encontrado."})

    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')
    cnpj = data.get('cnpj')
    categoria = data.get('categoria')
    descricao_da_causa = data.get('descricao_da_causa')
    cep = data.get('cep')
    chave_pix = data.get('chave_pix')
    num_agencia = data.get('num_agencia')
    num_conta = data.get('num_conta')
    nome_banco = data.get('nome_banco')

    cursor.execute("UPDATE usuario SET NOME = ?, E_MAIL = ?, SENHA = ?, CNPJ = ?, CATEGORIA = ?, DESCRICAO_DA_CAUSA = ?, CEP = ?, CHAVE_PIX = ?, NUM_AGENCIA = ?, NUM_CONTA = ?, NOME_BANCO = ? WHERE ID_USUARIO = ?",
                   (nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco, id))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Cadastro da ONG atualizado com sucesso!",
        'usuario': {
            'id_usuario': id,
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha,
            'cnpj': cnpj,
            'categoria': categoria,
            'descricao_da_causa': descricao_da_causa,
            'cep': cep,
            'chave_pix': chave_pix,
            'num_agencia': num_agencia,
            'num_conta': num_conta,
            'nome_banco': nome_banco
        }
    })

@app.route('/cadastro_ong/<int:id>', methods=['DELETE'])
def deletar_cadastro_ong(id):
    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE ID_USUARIO = ?", (id,))
    if not cursor.fetchone():
        cursor.close()
        return jsonify({"error": "Registro da ONG não encontrado."}), 404

    cursor.execute("DELETE FROM usuario WHERE ID_USUARIO = ?", (id,))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Cadastro da ONG excluído com sucesso!",
        'id_usuario': id
    })


# ONG - LOGIN

@app.route('/login_ong', methods=['POST'])
def login_ong():

    data = request.get_json()
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha, tipo from usuario WHERE e_mail = ?", (e_mail,))
    login_data = cursor.fetchone()

    if not login_data:
        cursor.close()
        return jsonify({'erro': "Credenciais não encontradas"}), 400

    senha_hash = login_data[3]

    if check_password_hash(senha_hash, senha):
        if login_data[4] == 2:
            return jsonify({
                'message': "Login da ONG feito com sucesso!"
            })
        if login_data[4] == 3:
            return jsonify({
                'message': "Login do doador feito com sucesso!"
            })
    else:
        return jsonify({
            'message': "Erro no login da ONG!"
        })

