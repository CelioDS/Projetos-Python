import os.path
import webbrowser

from fpdf import FPDF
from datetime import datetime


dados_contratante = {
    "razao_social": "EMPRESA MODELO LTDA",
    "cnpj": "12.345.678/0001-99",
    "rua": "das Flores",
    "numero": 123,
    "bairro" : "Centro",
    "cidade": "Campinas",
    "uf": "SP",
    "nome_socio": "João da Silva",
    "cpf_socio": "111.222.333-44",
    "telefone": "(19) 99876-5432",
    "email": "joao.silva@empresamodelo.com"
}

class PFD(FPDF):

    def header(self):
        self.set_font("arial", "B", 12)
        self.cell(0,10,"contrato de prestação",0,1,"C")
        self.ln(10) #pular linha apos cabeçalho

    def footer(self):
        self.set_y(-15) # posição a 1..5 do final
        self.set_font("Arial", "I", 8)
        self.cell(0,1, f"pagina {self.page_no()}", 0, 0, "C")

def gerar_pdf_contrato():
    pdf = PFD()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 14)
    pdf.multi_cell(0,10,'INSTRUMENTO PARTICULAR DE PRESTAÇÃO DE SERVIÇOS', align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 5, "CONTRATANTE", ln=True, align="C", border=1)
    pdf.ln(5)
    pdf.set_font("Arial", 'B',8)
    pdf.cell(100,5,f"Razão Social\n", align="J",)
    pdf.cell(50,5,f"CNPJ", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.cell(100, 5,f"{dados_contratante['razao_social']}", )
    pdf.cell(50, 5, f"{dados_contratante['cnpj']}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", "B", 8)
    pdf.cell(0, 5, "ENDEREÇO", ln=True, align="C", border=1)
    pdf.ln(5)

    pdf.cell(40, 5, f"Rua",    align="j", ln=False)
    pdf.cell(40, 5, f"Numero", align="j", ln=False )
    pdf.cell(40, 5, f"Bairro", align="j", ln=False )
    pdf.cell(40, 5, f"idade", align="j", ln=False)
    pdf.cell(40, 5, f"UF:",    align="j", ln=True)

    pdf.set_font("Arial", '', 11)
    pdf.cell(40, 5, f"{dados_contratante['rua']:<30}",    align="j",   ln=False)
    pdf.cell(40, 5, f"{dados_contratante['numero']:<10}", align="j", ln=False)
    pdf.cell(40, 5, f"{dados_contratante['bairro']:<20}", align="j", ln=False)
    pdf.cell(40, 5, f"{dados_contratante['cidade']:<20}", align="j", ln=False)
    pdf.cell(40, 5, f"{dados_contratante['uf']:<3}\n", align="j", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 5, "Representada neste ato por seu sócio administrador:", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 5,
                   f"Nome do Sócio:\t\t\t {dados_contratante['nome_socio']}\n"
                   f"CPF: {dados_contratante['cpf_socio']}\n"
                   f"Telefone: {dados_contratante['telefone']}\n"
                   f"E-mail: {dados_contratante['email']}"
                   , border=1, align="J")
    pdf.ln(5)
    

    pdf.multi_cell(0, 5,'Resolvem, de comum acordo, celebrar o presente contrato, que se regerá pelas seguintes cláusulas e condições:' )

    clausulas = {
        "PRIMEIRA - DO OBJETO": "O objeto do presente contrato é a prestação de serviços de desenvolvimento de software e consultoria em TI.",
        "SEGUNDA - DO VALOR E DA FORMA DE PAGAMENTO": "Pelos serviços prestados, a CONTRATANTE pagará à CONTRATADA o valor total de R$ 5.000,00 (cinco mil reais), a ser pago via transferência bancária até o 5º dia útil de cada mês.",
        "TERCEIRA - DO PRAZO": "O presente contrato terá a vigência de 12 meses, com início na data de sua assinatura.",
        "QUARTA - DO FORO": "Fica eleito o foro da Comarca de Indaiatuba, Estado de São Paulo, para dirimir quaisquer controvérsias oriundas do presente contrato."
    }
    pdf.ln(5)

    for titulo, texto in clausulas.items():
        pdf.set_font("arial", "B", 11)
        pdf.multi_cell(0, 5, f"CLAUSULA {titulo}")
        pdf.multi_cell(0, 5 , texto)

    pdf.ln(10)

    hoje = datetime.now()
    data_formatada = hoje.strftime("%d de %B de %Y")
    local_e_data = f"Indaiatuba, {data_formatada.replace("September", "Setembro")}."
    pdf.cell(0, 5 , local_e_data, ln=True, align="C")
    pdf.ln(15)

    pdf.cell(0,5, "_________________________________________", ln=True, align="C")
    pdf.cell(0,5, dados_contratante["razao_social"], ln=True, align="C")
    pdf.cell(0,5, f"Por: {dados_contratante["nome_socio"]}", ln=True, align ="C")
    pdf.ln(15)

    nome_arquivo = "contrato_prestacao.pdf"
    pdf.output(nome_arquivo)
    webbrowser.open(f"file://{os.path.abspath(nome_arquivo)}")
    print(f"PDF: {nome_arquivo}, gerado com sucesso!")


if __name__ == "__main__":
    gerar_pdf_contrato()


