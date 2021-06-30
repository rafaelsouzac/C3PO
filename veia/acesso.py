import mariadb


def acesso_sgdb():
    tlp_dados_acesso = ('root', '', 'localhost', 3306)

    try:
        ligado = mariadb.connect(user=tlp_dados_acesso[0], password=tlp_dados_acesso[1],
                                 host=tlp_dados_acesso[2], port=tlp_dados_acesso[3])

        return ligado

    except mariadb.Error as e:
        return e


def finaliza_acesso(acesso):
    acesso.close()