from PIL import Image
import pytesseract


def ler_texto_da_imagem():
    # Carrega driver de ODR
    _carregar_tesseract()
    # Lê imagem e retorna texto contido nela
    texto = _ler_imagem('img/202201/01 - Receita e Despesas - Conta Principal.jpeg')
    # Quebra por linha da imagem por linha
    linhas = texto.split("\n")
    # Lista receitas a serem exibidos
    receitas = [
        'Cotas do Mês Cota do Mês',
        'Juros',
        'Multas',
        'Tarifa bancária',
        'Tarifa bancária Custo do Boleto',
        'Rendimento de Investimentos Rendimentos de Investimentos',
        'Salão de Festas',
    ]
    # Filtrar items da lista de receita
    receitas_com_valores = _filtrar_items(linhas, receitas)
    # Lista despesas a serem exibidos
    despesas = [
        'Salário Limpeza e Conservação',
        'Férias',
        'INSS',
        'FGTS',
        'Energia elétrica',
        'Água e Esgoto',
        'Taxa de administração' 'Telefone',
        'Tarifa Bancária Mensal Tarifa Maxi Conta',
        'Elevador',
        'Materiais de Construção Boia Caixa D\'água',
        'Reparos e Manutenções Manutenção de Equipamentos (Visita Técnica)',
        'Reparos e Manutenções Reparo na Bomba de Recalque'
        'Reparos e Manutenções Troca do HD - sistema de câmeras de segurança',
        'Materiais Elétricos Bateria, Lâmpada LED',
        'Despesas bancárias Sispag',
        'Despesas bancárias Tarifa PIX',
        'Despesas bancárias Tarifa Sispag',
        'Outras Despesas Contador',
        'Outras Despesas Distribuição de Água Potável',
        'Outras Despesas Troca do sistema de interfone',
        'Impostos DARF' 'Impostos DARF (Venc 20/12)',
    ]
    # Filtrar items da lista de despesas
    despesas_com_valores = _filtrar_items(linhas, despesas)

    # Retorna lista com receitas e despesas
    return dict(receitas=receitas_com_valores, despesas=despesas_com_valores)


def _filtrar_items(linhas: list, items: list) -> list:
    """Retorna uma lista com os itens da lista de itens que estão contidos na lista de linhas."""
    return [
        caracteres_linha
        for caracteres_linha in linhas
        if any(item in caracteres_linha for item in items)
    ]


def _ler_imagem(nome_arquivo: str) -> list:
    """Lê a imagem e retorna uma lista com o texto contido nela."""
    return pytesseract.image_to_string(
        Image.open(nome_arquivo),
        lang='por',
    )


def _carregar_tesseract():
    """Carrega o tesseract para que ele possa ler a imagem."""
    pytesseract.pytesseract.tesseract_cmd = (
        r'/home/linuxbrew/.linuxbrew/bin/tesseract'
    )


print(ler_texto_da_imagem())
