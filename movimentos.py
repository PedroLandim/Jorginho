import pygame

pygame.init()

x = 70
y = 520
velocidade = 10

#tamanho da tela
janela = pygame.display.set_mode((800,600))

#nome que aparece em cima da janela
pygame.display.set_caption("Jorginho") #vai mudar o nome do jogo ou vai ser esse mesmo?

janela_aberta = True

#enquanto a janela tiver aberta, vai executar o que ta dentro do while
while janela_aberta:
    pygame.time.delay(50)

    #só fecha a janela quando apertar no botão vermelho do X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    #criação dos comandos de movimento
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT]:
        x += velocidade

    if comandos[pygame.K_LEFT]:
        x -= velocidade
            
    janela.fill((0,0,0))

    #criando o objeto na tela(vai ser o pokemon, mas por enquanto vou colocar um círculo aleatório)
    pygame.draw.circle(janela, (210, 0, 0), (70, 520), 50)
    pygame.display.update()

pygame.quit()