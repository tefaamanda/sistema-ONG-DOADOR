from flask import Flask, jsonify, request
from main import app, con

# CADASTRO - 1
@app.route('/doador', methods=['GET'])
def doador():
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


@app.route('/doador', methods=['POST'])
def doador_post():
    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE E_MAIL = ?", (e_mail,))

    if cursor.fetchone():
        return jsonify("Doador já cadastrado!")

    cursor.execute("INSERT INTO USUARIO(NOME, E_MAIL, SENHA) VALUES (?, ?, ?)",
                   (nome, e_mail, senha))

    con.commit()
    cursor.close()

    return jsonify({
        'message': "Doador cadastrado com sucesso!",
        'usuario': {
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha
        }
    })

@app.route('/doador/<int:id>', methods=['PUT'])
def doador_put(id):
    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha from usuario WHERE id_usuario = ?", (id,))
    doador_data = cursor.fetchone()

    if not doador_data:
        cursor.close()
        return jsonify({"Doador não foi encontrado"})

    data = request.get_json()
    nome = data.get('nome')
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor.execute("UPDATE usuario SET NOME = ?, E_MAIL = ?, SENHA = ? WHERE ID_USUARIO = ?",
                   (nome, e_mail, senha, id))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Registro do Doador atualizado com sucesso!",
        'usuario': {
            'id_usuario': id,
            'nome': nome,
            'e_mail': e_mail,
            'senha': senha
        }
    })

@app.route('/doador/<int:id>', methods=['DELETE'])
def deletar_doador(id):
    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE ID_USUARIO = ?", (id,))
    if not cursor.fetchone():
        cursor.close()
        return jsonify({"error": "Cadastro do Doador não encontrado"}), 404

    cursor.execute("DELETE FROM usuario WHERE ID_USUARIO = ?", (id,))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "Doador excluído com sucesso!",
        'id_usuario': id
    })








@app.route('/ong', methods=['GET'])
def ong():
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


@app.route('/ong', methods=['POST'])
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

    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE E_MAIL = ?", (e_mail,))

    if cursor.fetchone():
        return jsonify("ONG já cadastrada!")

    cursor.execute("INSERT INTO USUARIO(NOME, E_MAIL, SENHA, CNPJ, CATEGORIA, DESCRICAO_DA_CAUSA, CEP, CHAVE_PIX, NUM_AGENCIA, NUM_CONTA, NOME_BANCO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco))

    con.commit()
    cursor.close()

    return jsonify({
        'message': "ONG cadastrada com sucesso!",
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


@app.route('/ong/<int:id>', methods=['PUT'])
def ong_put(id):
    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha, cnpj, categoria, descricao_da_causa, cep, chave_pix, num_agencia, num_conta, nome_banco from usuario WHERE id_usuario = ?", (id,))
    ong_data = cursor.fetchone()

    if not ong_data:
        cursor.close()
        return jsonify({"ONG não foi encontrada"})

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
        'message': "Registro da ONG atualizada com sucesso!",
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


@app.route('/ong/<int:id>', methods=['DELETE'])
def deletar_ong(id):
    cursor = con.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE ID_USUARIO = ?", (id,))
    if not cursor.fetchone():
        cursor.close()
        return jsonify({"error": "Cadastro da ONG não encontrado"}), 404

    cursor.execute("DELETE FROM usuario WHERE ID_USUARIO = ?", (id,))
    con.commit()
    cursor.close()

    return jsonify({
        'message': "ONG excluída com sucesso!",
        'id_usuario': id
    })



# ATIVO
    usuarios = {
        "usuario1": {"senha": "senha123", "tentativas": 0, "ativo": True},
        "usuario2": {"senha": "senha456", "tentativas": 0, "ativo": True}
    }

    if usuario not in usuarios:
        return "Usuário não encontrado."

    usuario_data = usuarios[usuario]

    if not usuario_data["ativo"]:
        return "Usuário bloqueado. Contate o administrador."

    if senha == usuario_data["senha"]:
        usuario_data["tentativas"] = 0  # Zera as tentativas em caso de login bem-sucedido
        return "Login bem-sucedido!"
    else:
        usuario_data["tentativas"] += 1
        if usuario_data["tentativas"] >= 3:
            usuario_data["ativo"] = False
            return "Número de tentativas excedido. Usuário bloqueado."
        return f"Senha incorreta. Tentativas restantes: {3 - usuario_data['tentativas']}"



@app.route('/login_doador/<int:id>', methods=['GET', 'POST'])
def login_doador(id, senha):
    cursor = con.cursor()
    cursor.execute("select id_usuario, nome, e_mail, senha from usuario WHERE id_usuario = ?", (id,))
    login_data = cursor.fetchone()

    if not login_data:
        cursor.close()
        return jsonify({'erro': "Login de Doador não encontrado"}), 400

    senha_hash = senha [0]

    if check_password_hash(senha_hash, senha):
        return jsonify({"message": "Login de Doador realizado com sucesso"}), 200

    data = request.get_json()
    e_mail = data.get('e_mail')
    senha = data.get('senha')

    cursor = con.cursor()

    cursor.execute("SELECT id_usuario, nome FROM Usuario WHERE e_mail = ? AND senha = ?", (e_mail, senha,))
    doador = cursor.fetchone()

    cursor.execute("SELECT senha FROM Usuario WHERE e_mail = ?", (e_mail,))
    senha = cursor.fetchone()
    cursor.close()

    if doador:
        return jsonify({
            'message': "Login de Doador feito com sucesso!"
        })

    else:
        return jsonify({
            'message': "Erro no login do Doador!"
        })
