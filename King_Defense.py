import pygame
from random import randint
from sys import exit
import i_data 
from os.path import join
import math




class w_piece(pygame.sprite.Sprite,):

    def __init__(self,piece_t):
        pygame.sprite.Sprite.__init__(self)

        self.stg = 0 #stage/ Cada ponto da lista é um estagio, quando chega ao final ele é deletado
        self.piece_s = i_data.enemies[piece_t]
        self.speed = int(self.piece_s['speed']*Dyn_spd)
        self.image = pygame.image.load(self.piece_s['image']).convert_alpha()
        self.rect = self.image.get_rect(center=pontos[0])
        self.hp = self.piece_s['hp']
        self.maxhp = self.hp
        self.etapa = 0
        self.charged = False
        self.time = 1
        self.piece_t = piece_t
        global PlayerLife 
        n_inimigos.append(1)



    # O metodo verifica a posição atual e a posterior e verifica se ele precisa aumentar o X ou o Y para atingir o proximo estagio

    def caminhoPeao(self,rect): 
        global PlayerLife 
        #print(self.stg,'__',self.speed,'___',Dyn_spd,'___',fps,'__',self.rect.center)


        if rect == pontos[self.stg]:
                self.stg+=1 

        if self.stg < len(pontos):
            pos=[rect[0],rect[1]]

            difx = pontos[self.stg][0] - pos[0]
            dify = pontos[self.stg][1] - pos[1]

            if pos[0] < pontos[self.stg][0]: 
                if (pos[0] + self.speed) <= pontos[self.stg][0]:
                    pos[0] += self.speed

                else: pos[0] = pos[0] + (difx)

            if pos[0] > pontos[self.stg][0]: 
                if (pos[0] - self.speed) >= pontos[self.stg][0]:
                    pos[0] -= self.speed

                else: pos[0] = pos[0] + (difx)

            if pos[1] < pontos[self.stg][1]:
                if (pos[1] + self.speed) <=pontos[self.stg][1]:
                    pos[1] += self.speed

                else: pos[1] = pos[1] + (dify)

            if pos[1] > pontos[self.stg][1]:
                if (pos[1] - self.speed) >= pontos[self.stg][1]:
                    pos[1] -= self.speed

                else: pos[1] = pos[1] + (dify)
            
            return (pos[0],pos[1])
           
        else:
            self.hp = 0
            PlayerLife -= 20                       
            return(-47,-47)
        
        
    def caminhoTorre(self,rect):
        global PlayerLife 

                
        
        if self.stg < len(pontos_caminho):
            if rect == pontos_caminho[self.stg]:
                self.stg+=1
                self.charged = False
            
        if self.charged == False:
            if self.time < 100:
                self.time += 1*Dyn_spd 
            else:
                self.time = 1 
                self.charged = True
            
        if self.stg < len(pontos):
            if self.charged == True:
                self.speed = self.speed*8
                if self.stg < len(pontos_caminho):
                    
                    pos=[rect[0],rect[1]]

                    difx = pontos_caminho[self.stg][0] - pos[0]
                    dify = pontos_caminho[self.stg][1] - pos[1]

                    if pos[0] < pontos_caminho[self.stg][0]: 
                        
                        if (pos[0] + self.speed) <= pontos_caminho[self.stg][0]:
                            pos[0] += self.speed

                        else: pos[0] = pos[0] + (difx)

                    if pos[0] > pontos_caminho[self.stg][0]:

                        if (pos[0] - self.speed) >= pontos_caminho[self.stg][0]:
                            pos[0] -= self.speed

                        else: pos[0] = pos[0] + (difx)

                    if pos[1] < pontos_caminho[self.stg][1]:

                        if (pos[1] + self.speed) <= pontos_caminho[self.stg][1]:
                            pos[1] += self.speed

                        else: pos[1] = pos[1] + (dify)

                    if pos[1] > pontos_caminho[self.stg][1]:

                        if (pos[1] - self.speed) >= pontos_caminho[self.stg][1]:
                            pos[1] -= self.speed

                        else: pos[1] = pos[1] + (dify)
                    
                    return (pos[0],pos[1])
                else:
                    self.hp = 0
                    n_inimigos.remove(1)
                    PlayerLife -= 20
                    
            else: return self.rect.center
        

            

    def update(self):
        
        if self.etapa == 1:
            

            for y in detect_rect:
                if self.rect.colliderect(y):
                    print('ACHEU')
                    self.hp -= 1
            self.etapa = 0  
            return 0
        
        if self.etapa == 0:
            
            
            
            if self.hp > 1:
                detec_pts.append(self.rect.center)

                #print('POS',self.rect.center)
                #print(detec_pts)

                if self.piece_t == 'p_peao':
                    self.rect.center = self.caminhoPeao(self.rect.center)
                elif self.piece_t == 'p_torre':
                    self.rect.center = self.caminhoTorre(self.rect.center)
                    
                self.life_tab = pygame.Surface((self.hp,10))
                self.redlife_tab = pygame.Surface((self.maxhp,10))
                self.redlife_tab.fill('Red')
                self.life_tab.fill('Green')
                    
                screen.blit(self.redlife_tab,(self.rect.centerx-15,self.rect.centery-50))   
                screen.blit(self.life_tab,(self.rect.centerx-15,self.rect.centery-50))
                    
                    
                self.speed = int(self.piece_s['speed']*Dyn_spd)
                
                self.etapa = 1
            else:

                n_inimigos.remove(1)        
                self.kill()
                
            
      


class grupo_inimigos(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'p_peao':
            self.image = pygame.image.load('Peças/p_peao.png').convert_alpha()
        if type == 'path':
            self.image = pygame.image.load('Graphic/Background/Caminho.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0,0))

        self.path = [(47,239)]


class way(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Graphic/Background/DangerZone.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0,0))
        self.mask = pygame.mask.from_surface(self.image, 0)


class b_piece(pygame.sprite.Sprite):
    def __init__(self,piece_t,pos,vivo,direc):
        super().__init__()

        self.piece_s = i_data.allies[piece_t]
        self.piece_t = piece_t
        self.image = pygame.image.load(self.piece_s['image']).convert_alpha()
        self.initlocal = pos
        self.detec = 0
        self.aux = ()
        self.speed = int(self.piece_s['speed']*Dyn_spd)
        self.detec_p = []
        self.mov_p = []
        
        #print(pontos.index((335,335)))
        self.rect = self.image.get_rect(center = pos)
        

  
    def detec_prox(pontos_detec,pontos_mov):
        #Metodo para detecctar inimigos e iniciar e assim iniciar o movimento das peças
        deteccão = 0
        for y in detec_pts:
            for x in pontos_detec:
                #A peça inicia o metodo com a lista dos pontos que ele vai verificar se há inimigos
                if x == y:
                    

                    deteccão = 1
                    
                    destino = pontos_mov[pontos_detec.index(x)]
                        #quando a cordenada de um inimigo é igual a um ponto de detecção o este metodo ativa o metodo de movimentação
                    return [deteccão,destino]
                
        return [deteccão]
            
    
    def movimentação(rect,destino,inicio,vel):
        #O metodo de movimentação utiliza a posição atual da peça (rect) o ponto de movimentação da peça destino[1] e um valor de 0 ou 1 para
        # informar se um inimigo foi detectado ou não. Se ele foi detectado a variavel destino[0] recebe 1 e o metodo realiza a movimentação da peça 
        # o metodo tambem recebe o ponto que o jogador escolheu pra peça (inicio) permaneçer e a velocidade da peça (vel)
        
        #print('AUX: ',self.aux)
        
        #Como os valores da tupla não podem ser somados eles são transformados em uma lista 
        
        pos = [rect[0],rect[1]]
                
        if (pos[0],pos[1]) == destino[1]:
            destino[1] = inicio
            #Quando a peça chega no ponto de movimentação ele precisa voltar pra posição inicial, então a variavel destino recebe a posição inicial
            #da peça, então o algoritmo de movimentação vai receber a posição inicial como ponto de referencia pra peça mover de frame em frame
            
            print('MOMENTOVIRADA')

        if (pos[0],pos[1]) == inicio and destino[1] == inicio:
            print('FIM')
            destino[0] = 0
            #se o destino 
            
        if destino[0] == 1:
            # Etapa 1
            #quando um inimigo é detectado o metodo inicia a movimentação do personagem
            #como a peça tem que passar exatamente por cada centro do quadrado 
            
            difx = pos[0] - destino[1][0]
            dify = pos[1] - destino[1][1]
            
            # se a cordenada x da peça é maior que a cordenada x do destino e se apos diminuir com o valor da velocidade ele pular a coordenada
            # ao inves de somar com o valor da velocidade ele soma a distancia entre a posição da peça e o ponto. Para que todas peças passem pelo
            # ponto de detecção
            if pos[0] > destino[1][0]:
                if(pos[0] - vel) >= destino[1][0]:
                    pos[0] -= vel
                    print('VAI 1 ',pos[0],pos[1])
                else: pos[0] += difx
                
            if pos[0] < destino[1][0]:
                if(pos[0] + vel) <= destino[1][0]:
                    pos[0] += vel
                    print('VAI 2 ',pos[0],pos[1])
                else: pos[0] += difx
                    
            if pos[1] > destino[1][1]:
                if(pos[1] - vel) >= destino[1][1]:
                    pos[1] -= vel
                    print('VAI 3 ',pos[0],pos[1])
                else: pos[1] += dify              
                
            if pos[1] < destino[1][1]:
                if(pos[1] + vel) <= destino[1][1]:
                    pos[1] += vel
                    print('VAI 4 ',pos[0],pos[1])
                    
                else: pos[1] += dify
                                  
            return (pos[0],pos[1])  
        
        else: return(inicio)
        
        

    def update(self):
        #print(detec_pts)
        
        self.rect.center = self.movimentação(self.rect.center)

        self.speed = int(self.piece_s['speed']*Dyn_spd)
        #                                                                                       S A L V A R  I_DATA

                                
#classe para o peão aliado
class b_peao(pygame.sprite.Sprite):

    def __init__(self,piece_t,pos,vivo,direc):
        super().__init__()

        self.piece_s = i_data.allies[piece_t]
        self.piece_t = piece_t
        self.image = pygame.image.load(self.piece_s['image']).convert_alpha()
        self.initlocal = pos
        self.detec = 0
        self.aux = ()
        self.speed = int(self.piece_s['speed']*Dyn_spd)
        self.detec_p = []
        self.mov_p = []
        self.rect = self.image.get_rect(center = pos)
        self.deteccão = [0,(0,0)]
        
        #Depois que o jogador seleciona o local onde ele quer colocar a peça a classe é instanciada com a posição(self.rect.center) escolhida
        #Cada quadrado da tela possui um centro e a distancia do centro de um quadrado para o centro do outro mais proximo é 96, assim dependendo 
        # da direção escolhida pelo jogador o metodo __init__ cria uma listade dois pontos os quais o peão vai usar como referencia para se 
        # mover de frame em frame até chegar lá. Foi decidido que o peão come pela pelas diagonais esquerda ou direita ou acima ou abaixo
        
        # Para a lista fazer a lista de pontos que vai ser ultilizada para verificar se um inimigo passou por um dos pontos, dependendo da direção
        # dele ele pega um ponto da lista pontos(a lista de todos os centros dos quadrados que formam o caminho) realizando a soma da posição dele
        #e o 96, ja que o centro do peão sempre fica em uma distancia de 96 pixeis do centro de de outro quadrado, o qual este deve estar na lista 
        # pontos
        
        if vivo == True:
            for y in pontos:
                if direc == 0:
                        #ele verifica se o peão os dois pontos onde o peão pode ir estão dentro da lista pontos
                    if (self.rect.center[0]-96,self.rect.center[1]+96) == y:
                        # Quando a direção dele é 0, ou seja a da esquerda um dos pontos que ele deve adicionar na lista de pontos o qual ele vai 
                        # usar como referencia é a cordenada X atual dele mais -96 e a cordenada Y dele mais 96
                        
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                        #Os quadrados de detecção sempre são anteriores a um quadrado de movimentação, então atravez da lista pontos é econtrado o
                        #index do ponto de movimentação e esse index menos 1 é o ponto de detecçção
                        
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]+96))-1]))
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                    if (self.rect.center[0]-96,self.rect.center[1]-96) == y:
                            
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]-96))-1]))
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                if direc == 1:
                        
                    if (self.rect.center[0]-96,self.rect.center[1]+96) == y:
                            
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]+96))-1]))
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                    if (self.rect.center[0]+96,self.rect.center[1]+96) == y:
                            
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]+96))-1]))
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96)) 
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                                
                if direc == 2:
                        
                    if (self.rect.center[0]+96,self.rect.center[1]+96) == y:
                            
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]+96))-1]))
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96)) 
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                    if (self.rect.center[0]+96,self.rect.center[1]-96) == y:
                            
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]-96))-1]))
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                                                    
                if direc == 3:
                        
                    if (self.rect.center[0]+96,self.rect.center[1]-96) == y:                                                       
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]-96))-1]))
                        self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                    if (self.rect.center[0]-96,self.rect.center[1]-96) == y:
                            
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]-96))-1]))
                        self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))   
                        

        
    

        
        

    def update(self):
        

        
        if self.deteccão[0] == 0:
            #enquanto nenhum inimigo for detectado o metodo de verificação vai rodar em cada frame
            self.deteccão = b_piece.detec_prox(self.detec_p,self.mov_p)
            
        if self.deteccão[0] == 1:
            #se um inimigo for detectado ele inicia o metodo de movimentação em cada frame
            self.rect.center = b_piece.movimentação(self.rect.center,self.deteccão,self.initlocal,self.speed)
            
        detect_rect.append(self.rect)

        self.speed = int(self.piece_s['speed']*Dyn_spd)
                        

class b_bispo(pygame.sprite.Sprite):
    def __init__(self,piece_t,pos,vivo):
        super().__init__()

        self.deteccão = [0,(0,0)]
        self.piece_s = i_data.allies[piece_t]
        self.piece_t = piece_t
        self.image = pygame.image.load(self.piece_s['image']).convert_alpha()
        self.initlocal = pos
        self.detec = 0
        self.aux = ()
        self.speed = int(self.piece_s['speed']*Dyn_spd)
        self.detec_p = []
        self.mov_p = []
        self.rect = self.image.get_rect(center = pos)
        
        if vivo == True:
            for y in pontos:
                    #como o bispo como em todas as diagonais ele verifica todos os centros dos quadrados que fazem diagonal com o bispo
                    #ele usa a propria posição e soma com 96 ou -96 e verifica se o centro daquele quadrado esta na lista pontos
                    #se ele estiver ele é adicionado na lista de pontos que vão ser utilizados como referencia no metodo de movimentação
                if (self.rect.center[0]+96,self.rect.center[1]+96) == y: 
                    self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96))
                    self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]+96))-1]))
                    self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]+96))
                    self.detec_p.append((self.rect.center[0]+96,self.rect.center[1]+96))
                        
                if (self.rect.center[0]+96,self.rect.center[1]-96) == y: 
                    self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                    self.detec_p.append((pontos[pontos.index((self.rect.center[0]+96,self.rect.center[1]-96))-1]))
                    self.mov_p.append((self.rect.center[0]+96,self.rect.center[1]-96))
                    self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                if (self.rect.center[0]-96,self.rect.center[1]+96) == y: 
                    self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                    self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]+96))-1]))
                    self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]+96))
                    self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                        
                if (self.rect.center[0]-96,self.rect.center[1]-96) == y: 
                    self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                    self.detec_p.append((pontos[pontos.index((self.rect.center[0]-96,self.rect.center[1]-96))-1]))
                    self.mov_p.append((self.rect.center[0]-96,self.rect.center[1]-96))
                    self.detec_p.append((self.rect.center[0]-96,self.rect.center[1]-96))  
                    
        else: self.rect = self.image.get_rect(center=(self.piece_s['pos']))                   

    def update(self):
        #print(detec_pts)
        if self.deteccão[0] == 0:
            #enquanto nenhum inimigo for detectado o metodo de verificação vai rodar em cada frame
            self.deteccão = b_piece.detec_prox(self.detec_p,self.mov_p)
        if self.deteccão[0] == 1:
            #se um inimigo for detectado ele inicia o metodo de movimentação em cada frame
            self.rect.center = b_piece.movimentação(self.rect.center,self.deteccão,self.initlocal,self.speed)
            
        detect_rect.append(self.rect)

        self.speed = int(self.piece_s['speed']*Dyn_spd)

class b_torre(pygame.sprite.Sprite):

    def __init__(self,piece_t,pos,vivo,direc):
        super().__init__()

        self.piece_s = i_data.allies[piece_t]
        self.piece_t = piece_t
        self.image = pygame.image.load(self.piece_s['image']).convert_alpha()
        self.initlocal = pos
        self.detec = 0
        self.aux = ()
        self.speed = int(self.piece_s['speed']*Dyn_spd)
        self.detec_p = []
        self.mov_p = []
        self.rect = self.image.get_rect(center = pos)
        self.deteccão = [0,(0,0)]

        if vivo == True:
            
            #A torre pega uma reta, então dependendo da direção ele soma a cordenada x ,com 96 ou-96, ou a cordenada y com 96 ou -96
            #A direção 0 é a da esquerda então a cordenada x da peça soma com -96, e adiciona na lista de pontos de detecção, então inicia o for que
            # vai pegando os valores da lista de pontes de detecção se um ponto na lista de detecção for igual a um ponto na lista pontos ele
            # adiciona na lista pontos fazendo o for rodar mais uma vez, até que chega no ultimo ponto que vai estar fora do caminho e ele não adiciona
            # então acaba o for, basicamente dependendo da direção ele lança um raio entre dois quadrados que pega todos os centros dos quadrados e
            # adiciona na lista de pontos de detecção
            if direc == 0:
                self.detec_p = [(self.rect.center[0]-96,self.rect.center[1])]
                for y in self.detec_p:
                    for x in pontos:
                        if y == x:
                            self.detec_p.append((y[0]-96,y[1]))
                            
                for y in self.detec_p:
                    self.mov_p.append(self.detec_p[len(self.detec_p)-1])
                    #Na lista de pontos de movimentação é adicionado o ultimo ponto da lista de detecções somado com 96  
                

            if direc == 1:                   
                self.detec_p = [(self.rect.center[0],self.rect.center[1]+96)]
                for y in self.detec_p:
                    for x in pontos:
                        if y == x:
                            self.detec_p.append((y[0],y[1]+96)) 
                                                       
                for y in self.detec_p:
                    self.mov_p.append(self.detec_p[len(self.detec_p)-1])        

            if direc == 2:
                    
                self.detec_p = [(self.rect.center[0]+96,self.rect.center[1])]
                for y in self.detec_p:
                    for x in pontos:
                        if y == x:
                                self.detec_p.append((y[0]+96,y[1]))

                                
                for y in self.detec_p:
                    self.mov_p.append(self.detec_p[len(self.detec_p)-1])  
                    
            if direc == 3:
                self.detec_p = [(self.rect.center[0],self.rect.center[1]-96)]
                for y in self.detec_p:
                    for x in pontos:
                        if y == x:
                            self.detec_p.append((y[0],y[1]-96))
                            
                for y in self.detec_p:
                    self.mov_p.append(self.detec_p[len(self.detec_p)-1])                  
                            
        else: self.rect = self.image.get_rect(center=(self.piece_s['pos']))                    
                            
    def update(self):
        #print(detec_pts)
        if self.deteccão[0] == 0:
            self.deteccão = b_piece.detec_prox(self.detec_p,self.mov_p)
        if self.deteccão[0] == 1:
            self.rect.center = b_piece.movimentação(self.rect.center,self.deteccão,self.initlocal,self.speed)
            
        detect_rect.append(self.rect)

        self.speed = int(self.piece_s['speed']*Dyn_spd)                            
                                            

class Buttton():
    #Classe para os botões do jogo
    def __init__(self,x,y,type,case):
        
        self.type = i_data.inteface[type]
        self.case = case
        self.image = pygame.image.load(self.type['image'][0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        print(self.rect.center)
        self.clicked = 0
        self.action = False
        self.timer = 0
    
    def SetPos(self,Pos):
        #muda a posição dos botoes
        self.rect.center = Pos
        
    def draw (self):
        
        pos = pygame.mouse.get_pos()
        
        
        if self.case == 'list': 
            count = 0
            
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:

                    
                    if count > 3:
                        count += 1
                    else: count = 0
                    
                    self.clicked = 1
                    self.image = pygame.image.load(self.type['image'][1]).convert_alpha()
                    
                    self.action = True
                
                if pygame.mouse.get_pressed()[0] == 0:
                    
                    self.clicked = 2
                    
                    screen.blit(self.type['CaseList'][count],(self.rect.midright[0]+200,self.rect.midright[1]))
                    self.image = pygame.image.load(self.type['image'][0]).convert_alpha()        
        
        

        if self.case == 'boolean': 
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    #quando o botão é presionado muda a imagem dele pra dar um efeito de profundidade
                    self.clicked = 1
                    self.image = pygame.image.load(self.type['image'][1]).convert_alpha()
                    self.action = True
                    
                
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = 2
                    self.image = pygame.image.load(self.type['image'][0]).convert_alpha()
            
        
        screen.blit(self.image,(self.rect.x,self.rect.y))
        print('PRINT')
        print(self.rect.center)
        #quando o botão é pressionado inicia um timer e então o botão realiza sua ação
        if self.action == True:
            self.timer += 1*Dyn_spd
            print(self.timer)
            if self.timer > 25:
                self.timer = 0
                self.action = False
                return True


        



pygame.init()


#Variaveis
font = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()

start_time = pygame.time.get_ticks() 
 
Level = 0

Levels_disp = [1,0,0,0]
ResolutionValues = [800,600]
GameState = False 
Menu = False
LevelSelection = False
InitScreen = True
Options = False
Pause = False
GameOver = False
global PlayerLife 
global coins
coins = 40
PlayerLife = 100
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
LifeScore = test_font.render(f'{PlayerLife}',False,(64,64,64))
LifeRect = LifeScore.get_rect(center = (1200,150))
start_time = 0

Win = False




n_inimigos = [1]
w_pos = ()
v = 0
mouse1 = False

r = 0


#Variaveis Complexas
Pontos_Fora = []

def PontosFora(v):
    #Adiciona todos os pontos que nao fazem parte do caminho para ser utilizado no metodo pt_mais_prox_ms
    for c in i_data.total_pontos:

        for y in pontos:

            if c == y:
                v = 0
                break
        if v == 1:
            Pontos_Fora.append(c)
        v = 1


    #Numericas



sw=False
o=0

previa=False
Dyn_spd = 1

ContadorHorda = 0

#eventos
clock = pygame.time.Clock()
spawn = pygame.USEREVENT +1
pygame.time.set_timer(spawn,500)
pygame.time.set_timer(spawn,10)



#Instancia das classes Classes
window = pygame.display.set_mode((1366,768))
StartButton = Buttton(672,400,'ButtonPlay','boolean')
OptButton = Buttton(672,600,'ButtonOpt','boolean')
B_Level01 = Buttton(572,500,'B_Level01','boolean')
B_Level02 = Buttton(772,500,'B_Level02','boolean')
B_Level03 = Buttton(672,400,'B_Level03','boolean')
B_Level04 = Buttton(672,400,'B_Level04','boolean')
QuitButtom = Buttton(672,600,'ButtonQuit','boolean')
MenuButtom = Buttton(672,400,'ButtonMenu','boolean')
screen =  pygame.Surface((1366,768)) #pygame.FULLSCREEN)
LockedLevel = pygame.image.load('Graphic\Background\Locked.png')
Winmsg = pygame.image.load('Graphic\Background\WinMsg.png')
LoseMsg = pygame.image.load('Graphic\Background\LoseMsg.png')



way1 = pygame.sprite.GroupSingle(way())
inimigos = pygame.sprite.Group()
aliados = pygame.sprite.Group()
enemie_group = pygame.sprite.Group()
peoes = pygame.sprite.Group()
bispos = pygame.sprite.Group()
torres = pygame.sprite.Group()
allies_group = pygame.sprite.Group()

inimigos.add(grupo_inimigos('path'))



selec_s = pygame.Surface((200,768))
selec_p = False
test = pygame.image.load(join('Peças','p_peao.png'))
surf_setas = pygame.image.load(join('Peças','seta.png')).convert_alpha()
selec_s.fill('Black')
LevelScreen = pygame.image.load(join('Graphic','Background','LevelSelection.png')).convert_alpha()
InitialScreen = pygame.image.load(join('Graphic','Background','init.png')).convert_alpha()
PauseScreen = pygame.Surface((1366,800))
PauseScreen.fill('Gray')
PauseScreen.set_alpha(10)
GrayScreen = pygame.Surface((1366,800))
GrayScreen.fill((43,43,43))
GrayScreen.set_alpha(10)
WinScreen = False



#Função

def pt_mais_prox_ms():
    #esse metodo faz a o efeito de sobreposição quando seleciona a peça para isso ele usa a lista Pontos_fora
    #que contem todos os centros dos quadrados menos o dos quadrados do caminho e a localização do mouse naquele frame
    #então ele verifica qual quadrado esta mais proximo das cordenadas x e y do mouse
    
    miny=0
    minx=0
    i=0
    dist_msx = 10000
    dist_msy = 10000

    while i < len(Pontos_Fora):
        #Busca linear para encontrar o ponto mais proximo ao mouse
        
        #print(i,end=" | ")
        if abs(Pontos_Fora[i][0] - pygame.mouse.get_pos()[0]) < dist_msx or abs(Pontos_Fora[i][1] - pygame.mouse.get_pos()[1]) < dist_msy:
            dist_msx = abs(Pontos_Fora[i][0] - pygame.mouse.get_pos()[0])
            minx = Pontos_Fora[i][0]

            dist_msy = abs(Pontos_Fora[i][1] - pygame.mouse.get_pos()[1])
            miny = Pontos_Fora[i][1]
            
            #print(dist_msx,minx,dist_msy,miny)
        #print(' ')
        i+=1

    #print('AKI',minx,miny) 
    #print('blit',minx,miny)
    return(minx,miny)

while True:
    
    #Tela inicial do jogo
    if InitScreen == True:
        
        #fechar o jogo se o usuario apertar o X na janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
                
            #Sair da teka inicial e ir para o Menu   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('BACKSPACE')
                    InitScreen = False
                    Menu = True        
        
        print('Init')
        screen.blit(InitialScreen,(0,0))
                 
    if Menu == True:
        #metodo para posicionar um botão
        StartButton.SetPos((672,400))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Volta pra tela inicial se apertar esc
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    InitScreen = True
                    Menu = False     
                   
        print('MENU')
        screen.fill((40,40,40))
        #metodo para desenhar o botão na tela que retorna um valor pra saber se o botão foi apertado
        #se o motão StartButton for selecionado Sai da tela de menu e vai para a seleção de niveis
        if StartButton.draw() == True:
            LevelSelection = True
            Menu = False
            
        if OptButton.draw() == True:
            Options = True
            Menu = False
    
    if LevelSelection == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.blit(LevelScreen,(0,0))
        #Botão do nivel 1
        if B_Level01.draw() == True:
            #configura a fase para o nivel 1
            PlayerLife = 100
            ContadorHorda = 0
            Level = 1                
            background = pygame.image.load(join('Graphic','Background','Mapa01.png')).convert_alpha()
            GameState = True
            pontos_caminho = i_data.pontos_caminho1
            pontos = i_data.pontos1
            
            PontosFora(v)
            LevelSelection = False
         
        if Levels_disp[1] == 2:   
            #Se o nivel dois estiver disponivel vai aparecer o botão 
            if B_Level02.draw() == True:
                #configura a fase para o nivel 2
                PlayerLife = 100
                ContadorHorda = 0
                Level = 2                
                background = pygame.image.load(join('Graphic','Background','Mapa02.png')).convert_alpha()    
                GameState = True
                pontos_caminho = i_data.pontos_caminho2
                pontos = i_data.pontos2
                PontosFora(v)
                LevelSelection = False
        
        else:
            screen.blit(LockedLevel,(700,421))
    
    if Options == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                    
        screen.fill((40,40,40))
 
    if Pause == True:
        #Se o nivel começar e o jogador apertar esc o jogo pausa e vai pra tela de pause

        StartButton.SetPos((672,200))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameState = True
                    Pause = False    
                    
        if StartButton.draw() == True: 
            #se apertar o StartButton o jogo continua
            GameState = True
            Pause = False 
            
        if QuitButtom.draw() == True:
            #se apertar o QuitButtom o jogo fecha
                pygame.quit()
                exit()
                
        if MenuButtom.draw() == True:
            #se apertar o MenuButton volta pro menu
            Menu = True
            Pause = False
                
        screen.blit(PauseScreen,(0,0))  
        
    if GameOver == True:
        #se a vida do jogador chegar a zero a tela de gameover aparece
        
        MenuButtom.SetPos((672,500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

                             
        screen.blit(GrayScreen,(0,0))
        screen.blit(LoseMsg,(590,100))
        
        if MenuButtom.draw() == True:
            Menu = True
            GameOver = False     
                                   
        
    if Win == True:
        #se o jogador ficar vivo até o fim aparece a tela de vitoria
        MenuButtom.SetPos((672,500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

                             
        screen.blit(GrayScreen,(0,0))
        screen.blit(Winmsg,(590,100))
        
        if MenuButtom.draw() == True:
            Menu = True
            Win = False        
            
    
    if GameState == True:
        detec_pts = []
        detect_rect = []
        #print(detec_pts,'/')
        
        if PlayerLife < 1:
            
            PlayerLife = 100
            GameOver = True
            GameState = False
                
    #Algoritmo para que a velocidade não se altere dependendo da taxa de frames

        fps = int(clock.get_fps())

        if fps > 0:
            Dyn_spd = (math.ceil((60/fps)*100)/100) 

        screen.blit(background,(0,0))
        aliados.draw(screen)



    #Laço que Varre todos os eventos(como uma tecla apertada, um timer que eu criei, ...)
        for event in pygame.event.get():

    #Se clicar no X da janela fecha programa encerra

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse1 = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse1 = False


    #Se Apertar Tab o Selec_p se torna true e o retangulo preto aparece (pra selecionar peças)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if r < 3:
                        r += 1
                    else: r = 0
                    surf_setas = pygame.transform.rotate(surf_setas, 90)
                if event.key == pygame.K_TAB:             
                    if selec_p is False:
                        selec_p = True
                    else: selec_p = False
                if event.key == pygame.K_ESCAPE:
                    Pause = True
                    GameState = False

    #Se clicar no Peão o x vira 1 e aparece uma sobreposição na tela mostrando locais onde se pode colocar o peão, se x for 2 aparece torre...

            if selec_p:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (b_peao('b_peao',(1295,50),False,-1).rect).collidepoint(pygame.mouse.get_pos()):
                            if previa == 1:
                                previa = 0
                            else: previa = 1
                        if (b_torre('b_torre',(1195,50),False,-1).rect).collidepoint(pygame.mouse.get_pos()):
                            if previa == 2:
                                previa = 0
                            else: previa = 2
                        if (b_bispo('b_bispo',(0,0),False).rect).collidepoint(pygame.mouse.get_pos()):
                            if previa == 3:
                                previa = 0
                            else: previa = 3
                                                     
        if previa == 1:
            
            w_pos = pt_mais_prox_ms()
            rotacionar = [(w_pos[0]-65,w_pos[1]+82,w_pos[0]-65,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]+37,w_pos[0]+85,w_pos[1]+37),
                        (w_pos[0]+37,w_pos[1]+82,w_pos[0]+37,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]-65,w_pos[0]+85,w_pos[1]-65)
                        ]
            #posicionar as setas antes de colocar a peça

            screen.blit(b_peao('b_peao',(1295,50),False,-1).image,(w_pos[0]-15,w_pos[1]-30))
            print("R",r)
            screen.blit(surf_setas,(rotacionar[r][0],rotacionar[r][1]))   
            screen.blit(surf_setas,(rotacionar[r][2],rotacionar[r][3])) #191

            if mouse1 == True and selec_p == False:
                print('ADD1')
                #adicionar um peão se o esquerdo do mouse for apertado
                peoes.add(b_peao('b_peao',w_pos,True,r))

                previa = 0  

        if previa == 2:

            w_pos = pt_mais_prox_ms()
            rotacionar = [(w_pos[0]-65,w_pos[1]+82,w_pos[0]-65,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]+37,w_pos[0]+85,w_pos[1]+37),
                        (w_pos[0]+37,w_pos[1]+82,w_pos[0]+37,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]-65,w_pos[0]+85,w_pos[1]-65)
                        ]

            screen.blit(b_torre('b_torre',(1195,50),False,-1).image,(w_pos[0]-15,w_pos[1]-30))
            print("R",r)
            screen.blit(surf_setas,(rotacionar[r][0],rotacionar[r][1]))   
            screen.blit(surf_setas,(rotacionar[r][2],rotacionar[r][3])) #191

            if mouse1 == True and selec_p == False:
                print('ADD1')
                torres.add(b_torre('b_torre',w_pos,True,r))

                previa = 0  
                
        if previa == 3:

            w_pos = pt_mais_prox_ms()
            rotacionar = [(w_pos[0]-65,w_pos[1]+82,w_pos[0]-65,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]+37,w_pos[0]+85,w_pos[1]+37),
                        (w_pos[0]+37,w_pos[1]+82,w_pos[0]+37,w_pos[1]-109),
                        (w_pos[0]-110,w_pos[1]-65,w_pos[0]+85,w_pos[1]-65)
                        ]

            screen.blit(b_bispo('b_bispo',(0,0),False).image,(w_pos[0]-15,w_pos[1]-30))
            print("R",r)
            screen.blit(surf_setas,(rotacionar[r][0],rotacionar[r][1]))   
            screen.blit(surf_setas,(rotacionar[r][2],rotacionar[r][3])) #191

            if mouse1 == True and selec_p == False:
                print('ADD1')
                bispos.add(b_bispo('b_bispo',w_pos,True)) 
 
                previa = 0              

            
            
            
            
            
            
            
            if event.type == spawn:
                len(detec_pts) 
                               
            #sistema de nascimento dos inimigos baseado na lista i_data.Hordas, essa lista tem um tipo de inimigo e o tempo que ele demora 
            #para do aparecimento do inimigo anterior, então o algoritmo lê a lista percebe que é uma string e adiciona um inimigo,
            #caso não seja uma string e sim um numero esse é o tempo em milisegundos para aparecer outro inimigo   
                if ContadorHorda >= len(i_data.Hordas)-1:
                    #se o algoritmo ja leu a lista i_data.Hordas inteira, ele dá vitoria ao jogador e dá acesso ao novo nivel
                    Levels_disp[Level] = Level+1
                    print(n_inimigos)
                    if len(n_inimigos) == 1:
                        print(n_inimigos)
                        Win = True
                        GameState = False                     

    
               
                elif isinstance(i_data.Hordas[ContadorHorda], str):
                    print(ContadorHorda,' ',len(i_data.Hordas)-1,' ',i_data.Hordas[ContadorHorda],' ',i_data.Hordas[ContadorHorda+1])
                    enemie_group.add(w_piece(i_data.Hordas[ContadorHorda]))
                    if i_data.Hordas[ContadorHorda+1] > 0:
                        pygame.time.set_timer(spawn,i_data.Hordas[ContadorHorda+1])
                        ContadorHorda += 2
                        
                elif i_data.Hordas[ContadorHorda] == -1:
                    pygame.time.set_timer(spawn,10000)
                    ContadorHorda += 1                    
                    
                

                        
                    
                
                    
    


        if selec_p:
            if pygame.sprite.spritecollide(way1.sprite,aliados,False,pygame.sprite.collide_mask):
                inimigos.draw(screen)   
            screen.blit(selec_s,(1145,0))
            if Level == 1:
                screen.blit(b_peao('b_peao',(1295,50),False,-1).image,(b_peao('b_peao',(1295,50),False,-1).rect))
            if Level == 2:
                screen.blit(b_torre('b_torre',(1195,50),False,-1).image,(b_torre('b_torre',(1195,50),False,-1).rect))
                screen.blit(b_peao('b_peao',(1295,50),False,-1).image,(b_peao('b_peao',(1295,50),False,-1).rect))
            if Level == 3:
                screen.blit(b_bispo('b_bispo',(1295,500),False).image,(b_bispo('b_bispo',(1295,500),False).rect))
                screen.blit(b_torre('b_torre',(1195,50),False,-1).image,(b_torre('b_torre',(1195,50),False,-1).rect))
                screen.blit(b_peao('b_peao',(1295,50),False,-1).image,(b_peao('b_peao',(1295,50),False,-1).rect))
    
    




    #Coisas na tela
    #Metodos de atualização de desenho, eles vão fazer tudo que esta no metodo update das classes e o .draw desenha as classes na tela chamada screen
        enemie_group.update()
        enemie_group.draw(screen)
        aliados.update()
        peoes.update()
        peoes.draw(screen)
        bispos.update()
        bispos.draw(screen)
        torres.update()
        torres.draw(screen)
        enemie_group.update()
        allies_group.update()
        allies_group.draw(screen)

    LifeScore = test_font.render(f'{PlayerLife}',False,(75,255,75))
    screen.blit(LifeScore,LifeRect)
    

    pygame.display.update()


        
    upscaled_canvas = pygame.transform.scale(screen, (1366,768))
    window.blit(upscaled_canvas, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    #print(clock.get_fps())
    clock.tick(75) 
    