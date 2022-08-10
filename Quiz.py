import time

#Listas para guardar perguntas, alternativas e respostas do usuário e gabarito
perguntas = ["(Enem/2013) É preciso ressaltar que, de todas as capitanias brasileiras, Minas era a mais urbanizada. Não havia ali hegemonia de um ou dois grandes centros. "
              "A região era repleta de vilas e arraiais, grandes e pequenos, em cujas ruas muita gente circulava. As regiões da América portuguesa tiveram distintas lógicas de ocupação. "
              "Uma explicação para a especificidade da região descrita no texto está identificada na:"
    ,"(Enem/2016) É hoje a nossa festa nacional. O Brasil inteiro, da capital do Império à mais remota e insignificante de suas aldeolas, congrega-se unânime para comemorar o dia que o tirou dentre as nações dependentes para colocá-lo "
      "entre as nações soberanas, e entregou-lhes seus destinos, que até então haviam ficado a cargo de um povo estranho. As festividades em torno da Independência do Brasil marcam o nosso calendário desde os anos "
      "imediatamente posteriores ao de setembro de 1822. Essa comemoração está diretamente relacionada com:"
             ,"(Enem/2010) Para o Paraguai, portanto, essa foi uma guerra pela sobrevivência. De todo modo, uma guerra contra dois gigantes estava fadada a ser um teste debilitante e severo para uma economia de base tão estreita. "
               "Lopez precisava de uma vitória rápida e, se não conseguisse vencer rapidamente, provavelmente não venceria nunca. A Guerra do Paraguai teve consequências políticas importantes para o Brasil, pois:"
             ,"(Enem/2014) As relações do Estado brasileiro com o movimento operário e sindical, bem como as políticas públicas voltadas para as questões sociais durante o primeiro governo da Era Vargas (1930-1945), são temas amplamente estudados pela academia brasileira em seus vários aspectos. "
               "São também os temas mais lembrados pela sociedade quando se pensa no legado varguista. Durante o governo de Getúlio Vargas, foram desenvolvidas ações de cunho social, dentre as quais se destaca a: "
             ,"(Enem/2018) A rebelião luso-brasileira em Pernambuco começou a ser urdida em 1644 e explodiu em 13 de junho de 1645, dia de Santo Antônio. Uma das primeiras medidas de João Fernandes foi decretar nulas as dívidas que os rebeldes tinham com os holandeses. "
               "Houve grande adesão da “nobreza da terra”, entusiasmada com esta proclamação heroica. O desencadeamento dessa revolta na América portuguesa seiscentista foi o resultado do(a): "
             ,"(Enem/2016) A regulação das relações de trabalho compõe uma estrutura complexa, em que cada elemento se ajusta aos demais. A Justiça do Trabalho é apenas uma das peças dessa vasta engrenagem. "
               "A presença de representantes classistas na composição dos órgãos da Justiça do Trabalho é também resultante da montagem dessa regulação. O poder normativo também reflete essa característica. "
               "Instituída pela Constituição de 1934, a Justiça do Trabalho só vicejou no ambiente político do Estado Novo instaurado em 1937."
             ,"(Enem/2014) A transferência da corte trouxe para a América portuguesa a família real e o governo da Metrópole. Trouxe também, e sobretudo, boa parte do aparato administrativo português. "
               "Personalidades diversas e funcionários régios continuaram embarcando para o Brasil atrás da corte, dos seus empregos e dos seus parentes após o ano de 1808. "
               "Os fatos apresentados se relacionam ao processo de independência da América portuguesa por terem"
             ,"(Enem/2014) O problema central a ser resolvido pelo Novo Regime era a organização de outro pacto de poder que pudesse substituir o arranjo imperial com grau suficiente de estabilidade. "
               "O próprio presidente Campos Sales resumiu claramente seu objetivo: “É de lá, dos estados, que se governa a República, por cima das multidões que tumultuam agitadas nas ruas da capital da União. "
               "A política dos estados é a política nacional”. Nessa citação, o presidente do Brasil no período expressa uma estratégia política no sentido de:"
             ,"(Enem/2017) Após o retorno de uma viagem a Minas Gerais, onde Pedro I fora recebido com grande frieza, seus partidários prepararam uma série de manifestações a favor do imperador no Rio de Janeiro, "
               "armando fogueiras e luminárias na cidade. Contudo, na noite de 11 de março, tiveram início os conflitos que ficaram conhecidos como a Noite das Garrafadas, durante os quais os “brasileiros” apagavam as "
               "fogueiras “portuguesas” e atacavam as casas iluminadas, sendo respondidos com cacos de garrafas jogadas das janelas."
             ,"(Enem/2010) Essa medida, decretada pelo príncipe D. João de Bragança, praticamente eliminou o exclusivo metropolitano sobre o comércio da Colônia, desferindo um golpe mortal no Pacto Colonial luso, além de constituir o primeiro grande passo para a independência "
               "efetiva do Brasil. Trata-se da(o):"
             ,"(Enem/2006) A moderna democracia brasileira foi construída entre saltos e sobressaltos. Em 1954, a crise culminou no suicídio do presidente Vargas. No ano seguinte, outra crise quase impediu a posse do presidente eleito, "
               "Juscelino Kubitschek. Em 1961, o Brasil quase chegou à guerra civil depois da inesperada renuncia do presidente Jânio Quadros. Três anos mais tarde, um golpe militar depôs o presidente João Goulart, e o país viveu durante "
               "vinte anos em regime autoritário. A partir dessas informações, relativas à historia republicana brasileira, assinale a opção correta:"
             ,"(Enem/2012) Diante dessas inconsistências e de outras que ainda preocupam a opinião pública, nós, jornalistas, estamos encaminhando este documento ao Sindicato dos Jornalistas Profissionais no Estado de São Paulo, "
               "para que o entregue à Justiça; e da Justiça esperamos a realização de novas diligências capazes de levar à completa elucidação desses fatos e de outros que porventura vierem a ser levantados. A morte do jornalista Vladimir "
               "Herzog, ocorrida durante o regime militar, em 1975, levou a medidas como o abaixo-assinado feito por profissionais da imprensa de São Paulo. A análise dessa medida tomada indica a: "]

gabarito=["D","A","A","C","E","B","B","B","E","A","D","E"]

alternativas = [["A.apropriação cultural diante das influências externas","B.produção manufatureira diante do exclusivo comercial","C.insubordinação religiosa diante da hierarquia eclesiástica",
                 "D.fiscalização estatal diante das particularidades econômicas","E.autonomia administrativa diante das instituições metropolitanas"],
                ["A.a construção e manutenção de símbolos para a formação de uma identidade nacional","B.o domínio da elite brasileira sobre os principais cargos políticos, que se efetivou logo após 1822",
                 "C.os interesses de senhores de terras que, após a Independência, exigiram a abolição da escravidão","D.o apoio popular às medidas tomadas pelo governo imperial para a expulsão de estrangeiros do país",
                 "E.a consciência da população sobre os seus direitos adquiridos posteriormente à transferência da Corte para o Rio de Janeiro"]
                ,["A.representou a afirmação do Exército Brasileiro como um ator político de primeira ordem","B.confirmou a conquista da hegemonia brasileira sobre a Bacia Platina","C.concretizou a emancipação dos escravos negros",
                  "D.incentivou a adoção de um regime constitucional monárquico","E.solucionou a crise financeira, em razão das indenizações recebidas"]
                ,["A.disseminação de organizações paramilitares inspiradas nos regimes fascistas europeus","B.aprovação de normas que buscavam garantir a posse das terras aos pequenos agricultores"
                    ,"C.criação de um conjunto de leis trabalhistas associadas ao controle das representações sindicais","D.implementação de um sistema de previdência e seguridade para atender aos trabalhadores rurais"
                  ,"E.implantação de associações civis como uma estratégia para aproximar as classes médias e o governo"]
                ,["A.fraqueza bélica dos protestantes batavos","B.comércio transatlântico da África ocidental","C.auxílio financeiro dos negociantes flamengos","D.diplomacia internacional dos Estados ibéricos"
                    ,"E.interesse econômico dos senhores de engenho"]
                ,["A.Legitimar os protestos fabris","B.Ordenar os conflitos laborais","C.Oficializar os sindicatos plurais","D.Assegurar os princípios liberais","E.Unificar os salários profissionais"]
                ,["A.incentivado o clamor popular por liberdade","B.enfraquecido o pacto de dominação metropolitana","C.motivado as revoltas escravas contra a elite colonial","D.obtido o apoio do grupo constitucionalista português"
                    ,"E.provocado os movimentos separatistas das províncias"]
                ,["A.governar com a adesão popular","B.atrair o apoio das oligarquias regionais","C.conferir maior autonomia às prefeituras","D.democratizar o poder do governo central"
                    ,"E.ampliar a influência da capital no cenário nacional"]
                ,["A.estímulos ao racismo","B.apoio ao xenofobismo","C.críticas ao federalismo","D.repúdio ao republicanismo","E.questionamentos ao autoritarismo"]
                ,["A.abertura dos Portos Brasileiros às Nações Amigas","B.grito do Ipiranga","C.alvará de Liberdade Industrial","D.elevação do Brasil à categoria de Reino Unido a Portugal e Algarves","E.fundação do Banco do Brasil"]
                ,["A.ao término do governo João Goulart, Juscelino Kubitschek foi eleito presidente da Republica","B.a renúncia de Jânio Quadros representou a primeira grande crise do regime republicano brasileiro"
                    ,"C.apos duas décadas de governos militares, Getúlio Vargas foi eleito presidente em eleições diretas","D.a trágica morte de Vargas determinou o fim da carreira política de João Goulart"
                    ,"E.no período republicano citado, sucessivamente, um presidente morreu, um teve sua posse contestada, um renunciou e outro foi deposto"]
                ,["A.certeza do cumprimento das leis","B.superação do governo de exceção","C.violência dos terroristas de esquerda","D.punição dos torturadores da polícia","E.expectativa da investigação dos culpados"]]

respostas=[]

#Criar funções
#Função para iniciar novo jogo
def novojogo():
    alt=1
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------")
    print("Teste seus conhecimentos sobre história do Brasil para vestibulares com nosso quiz!")
    print("-------------------------------------------------------------------------------------------------")

    for i in perguntas:
        print("")
        print("")
        print("")
        print("")
        print(i)
        for j in alternativas[alt-1]:
            print("")
            print(j)
        resposta=input("\nDigite alternativa escolhida (A,B,C,D,E): ")
        resposta=resposta.upper()
        respostas.append(resposta)
        alt += 1
    return respostas

#Função para verificar se respostas do usuário estão corretas
def conferir(respostas):
    pontos2=0
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------")
    print("Resultado e Gabarito")
    print("-------------------------------------------------------------------------------------------------")
    print("")
    print("")
    if respostas[0] == gabarito[0]:
        print("Acertou a questão 1")
        pontos2 = pontos2 + 1
    else:
        print("Errou questão 1\nResposta certa para questão 1 era: D \nJustificativa: Por conta da extração do ouro, Minas Gerais sempre foi mais vigiada pelo poder público "
              "a fim de garantir que as riquezas encontradas chegariam à Corte. \nAs outras opções não refletem a realidade histórica da região neste período com exageros como produção manufatureira e autonomia administrativa.")
    print("")
    if respostas[1] == gabarito[1]:
        print("\nAcertou a questão 2")
        pontos2=pontos2 + 2
    else:
        print("\nErrou questão 2\nResposta certa para questão 2 era: A \nJustificativa: Esta é uma questão onde se necessita mais conhecimentos de interpretação que de História. "
              "O uso de símbolos como festas nacionais, bandeira e hino tem como objetivo formar uma comunidade que se identifique com esses emblemas e assim, uma identidade nacional."
              "\nAs demais opções não são corretas. A alternativa b) o domínio da elite brasileira sobre os principais cargos políticos, que se efetivou logo após 1822 poderia nos confundir. "
              "No entanto, o cenário político no Brasil independente era bastante confuso e ainda não havia uma consciência nacional por parte deste elite.")
    print("")
    if respostas[2] == gabarito[2]:
        print("\nAcertou a questão 3")
        pontos2=pontos2 + 1
    else:
        print("\nErrou questão 3\nResposta certa para questão 3 era: A \nJustificativa: O Exército brasileiro saiu fortalecido do conflito e passou a exigir mais participação no cenário político, o que acabaria redundando no golpe republicano."
              "\nAs demais opções não são corretas. Afinal, o Brasil não conquista a hegemonia da Bacia Platina e nem os escravos negros são emancipados.")
    print("")
    if respostas[3] == gabarito[3]:
        print("\nAcertou a questão 4")
        pontos2=pontos2 + 2
    else:
        print("\nErrou questão 4\nResposta certa para questão 4 era: C \nJustificativa: Ao mesmo tempo em que promoveu leis que melhoravam a vida dos trabalhadores, o governo de Getúlio Vargas usou os sindicatos para controlá-los."
              "\nAs demais opções não estão corretas. As opções b) aprovação de normas que buscavam garantir a posse das terras aos pequenos agricultores e d) implementação de um sistema de previdência e seguridade para atender aos "
              "trabalhadores rurais estão erradas porque os direitos trabalhistas não contemplavam os trabalhadores rurais.")
    print("")
    if respostas[4] == gabarito[4]:
        print("\nAcertou a questão 5")
        pontos2=pontos2 + 2
    else:
        print("\nErrou questão 5\nResposta certa para questão 5 era: E \nJustificativa: Atenção! A resposta dessa pergunta já está no texto. Notem que ele menciona a alegria dos luso-brasileiros em terem perdoadas suas dívidas com os holandeses. "
              "Portanto, os senhores de engenho voltariam a apoiar os portugueses por conta desta facilidade econômica.")
    print("")
    if respostas[5] == gabarito[5]:
        print("\nAcertou a questão 6")
        pontos2=pontos2 + 2
    else:
        print("\nErrou questão 6\nResposta certa para questão 6 era: B \nJustificativa: A política trabalhista de Vargas consistia em harmonizar os interesses de patrões e trabalhadores. "
              "Enquanto promulgava leis trabalhistas a fim de garantir o apoio da população, favorecia os grandes empresários. Neste contexto, é criada a Justiça do Trabalho, que seria o órgão máximo para resolver as infrações cometidas.")
    print("")
    if respostas[6] == gabarito[6]:
        print("\nAcertou a questão 7")
        pontos2=pontos2 + 3
    else:
        print("\nErrou questão 7\nResposta certa para questão 7 era: B \nJustificativa: A vinda da administração metropolitana para a América Portuguesa fez com que a elite colonial sentisse que era possível administrar o Estado e dispensar "
              "os portugueses do governo. Também cooperou a igualdade jurídica do Brasil a Portugal em 1815.")
    print("")
    if respostas[7] == gabarito[7]:
        print("\nAcertou a questão 8")
        pontos2=pontos2 + 3
    else:
        print("\nErrou questão 8\nResposta certa para questão 8 era: B \nJustificativa: A questão retrata claramente o poder que os estados, e não o governo central, possuíam no Brasil. "
              "Desta forma, o presidente Campo Sales afirma que precisa do apoio dos governadores para poder governar o Brasil, no fenômeno conhecido como política dos governadores.")
    print("")
    if respostas[8] == gabarito[8]:
        print("\nAcertou a questão 9")
        pontos2=pontos2 + 3
    else:
        print("\nErrou questão 9\nResposta certa para questão 9 era: E \nJustificativa: Com a centralização do poder em Dom Pedro I e a crise dinástica pelo trono português, os brasileiros passaram a questionar as "
              "ações cada vez mais centralizadoras do monarca expressando seu descontentamento com violência. Assim, recebem Dom Pedro I com frieza em Minas Gerais e atacando os portugueses no Rio de Janeiro.")
    print("")
    if respostas[9] == gabarito[9]:
        print("\nAcertou a questão 10")
        pontos2=pontos2 + 1
    else:
        print("\nErrou questão 10\nResposta certa para questão 10 era: A \nJustificativa: A Abertura dos Portos, em 1808, significou o fim do monopólio comercial entre o Brasil e Portugal e, portanto, o término do Pacto Colonial.")
    print("")
    if respostas[10] == gabarito[10]:
        print("\nAcertou a questão 11")
        pontos2=pontos2 + 3
    else:
        print("\nErrou questão 11\nResposta certa para questão 11 era: D \nJustificativa: A resposta já está no enunciado da questão. Em 1954, Getúlio Vargas cometeu suicídio, JK teve que enfrentar uma rebelião antes da posse, "
              "Jânio Quadros renunciou e Jango foi deposto pelos militares.")
    print("")
    if respostas[11] == gabarito[11]:
        print("\nAcertou a questão 12")
        pontos2=pontos2 + 1
    else:
        print("\nErrou questão 12\nResposta certa para questão 12 era: E \nJustificativa: Mais uma questão onde não é preciso conhecimentos históricos para respondê-la, e sim a capacidade de interpretar o texto. "
              "Aqui, os jornalistas esperam que a Justiça - mesmo limitada pela ditadura militar - saiba cumprir o seu papel e investigar a morte de Herzog.")
    return pontos2

#Função para verificar se usuário quer jogar novamente
def jogardenovo():
    print("-------------------------------------------------------------------------------------------------")
    x=input("Quer jogar de novo? (Sim/Não)")
    print("-------------------------------------------------------------------------------------------------")
    x = x.upper()
    if x == "SIM":
        return True
    else:
        return False

#Função para verificar pontuação
def pontuacao(pontos):
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------")
    porcentagem=int((pontos/24)*100)
    print("Sua pontuação foi: {0} pontos de 24 totais ou {1}%".format(pontos,porcentagem))
    if pontos>=19:
        print("Parabéns! Você foi muito bem e está preparado para o vsetibular!")
    elif pontos <19 and pontos>=13:
        print("Está no caminho certo para ir bem no vestibular! Mas ainda precisa estudar um pouco mais!")
    else:
        print("Pontuação um pouco ruim, precisamos estudar mais. Mas não desanime!")


#Função para verificar se tempo para fazer quiz está bom
def ver_tempo(tempo):
    if tempo >= 48:
        print("Levou muito tempo para resolver as questões. Precisamos melhorar isso!")
    elif tempo < 48 and tempo >= 36:
        print("Bom tempo para resolver as questões.Mas podemos melhorar!")
    elif tempo > 15 and tempo < 36:
        print("Excelente tempo! Esse tempo está muito bom para o vestibular!")
    else:
        print("Realizou o quiz muito rapidamente. Tente fazer mais seriamente, sem chutar")


#Código principal
print("################################################################################################")
print("")
print("############    ##        ##    ##    ############")
print("##        ##    ##        ##    ##            ##")
print("##        ##    ##        ##    ##          ##")
print("##   ##   ##    ##        ##    ##        ##")
print("##     ## ##    ##        ##    ##      ##")
print("############    ############    ##    ############")
print("            ##")

print("")
print("##       ##    ##    ############    ############   ############    ############    ##         ####")
print("##       ##    ##    ##                  ##         ##        ##    ##        ##    ##        ##  ##")
print("###########    ##    ############        ##         ##        ##    ############    ##       ##    ##")
print("##       ##    ##              ##        ##         ##        ##    ##    ##        ##      ##########")
print("##       ##    ##              ##        ##         ##        ##    ##      ##      ##     ##        ##")
print("##       ##    ##    ############        ##         ############    ##        ##    ##    ##          ##")

print("")
print("################################################################################################")

#Iniciar contagem de tempo
start = time.time()

#Chamada de funções
x=novojogo()
y=conferir(x)
pontuacao(y)

#Terminar contagem de tempo
end = time.time()
tempo=float(format(end - start))
tempo=tempo/60
print("-------------------------------------------------------------------------------------------------")
print("Tempo de quiz: {:.2f} minutos".format(tempo))

#Verificar se tempo está bom
ver_tempo(tempo)

#Chamada para ver se quer jogar de novo
while jogardenovo():
    start = time.time()

    x = novojogo()
    y = conferir(x)
    pontuacao(y)

    end = time.time()
    tempo = float(format(end - start))
    tempo = tempo / 60
    print("-------------------------------------------------------------------------------------------------")
    print("Tempo de quiz: {:.2f} minutos".format(tempo))
    ver_tempo(tempo)

# Mensagem final
print("Obrigado por jogar. E bons estudos!")
print("-------------------------------------------------------------------------------------------------")
print("Quiz feito por:\nLuis Kinukawa")
print("-------------------------------------------------------------------------------------------------")
