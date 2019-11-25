from django.core.management.base import BaseCommand
import psycopg2

from dashboard.core import models


class Command(BaseCommand):

    help = "Pega os dados do Banco antigo e traz para o novo"

    def handle(self, *args, **kwargs):
        conn = psycopg2.connect(host="localhost", database="dashboard", user="postgres", password="postgres")
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM _tbdados')
        registros = cursor.fetchall()
        '''
        1 - avião
        2 - produto
        3 - posto de trabalho
        4 - data incio planejada
        5 - data final planejada
        6 - data inicio real
        7 - data final real
        '''
        cont = 1
        for registro in registros:
            if registro[4] and registro[5]:
                # if not models.Aviao.objects.filter(numero=registro[1]):
                #     aviao = models.Aviao()
                #     aviao.numero = registro[1]
                #     aviao.save()
                #     print(cont)
                #     cont += 1

                # if not models.PostoTrabalho.objects.filter(nome=registro[3]):
                #     posto_trabalho = models.PostoTrabalho()
                #     posto_trabalho.nome = registro[3]
                #     posto_trabalho.save()
                #     print(cont)
                #     cont += 1

                # if not models.Produto.objects.filter(nome=registro[2], aviao=aviao):
                #     produto = models.Produto()
                #     produto.nome = registro[2]
                #     produto.aviao = aviao
                #     produto.save()
                #     print(cont)
                #     cont += 1

                aviao, _ = models.Aviao.objects.get_or_create(numero=registro[1])
                produto, _ = models.Produto.objects.get_or_create(nome=registro[2], aviao=aviao)
                posto_trabalho, _ = models.PostoTrabalho.objects.get_or_create(nome=registro[3])
                if not models.ProdutoPostoTrabalho.objects.filter(
                    produto=produto,
                    posto_trabalho=posto_trabalho,
                ):
                    produto_pt = models.ProdutoPostoTrabalho()
                    produto_pt.produto = produto
                    produto_pt.posto_trabalho = posto_trabalho
                    produto_pt.data_inicio_planejada = registro[4]
                    produto_pt.data_final_planejada = registro[5]
                    if registro[6]:
                        produto_pt.data_inicio_real = registro[6]
                    if registro[7]:
                        produto_pt.data_final_planejada = registro[7]
                    produto_pt.save()
                    # produto.postos.add(produto_pt)
                    print(cont)
                    cont += 1

        print("Sucesso!")
        conn.close()
