import time
import pygame
import os
import sys

def detectJoy(joystick_count):
    if(joystick_count < 1):
        raise Exception("Nenhum joystick detectado, conecte um e executa novamente.")

    print("Joysticks detectados: "+str(joystick_count))

    sel_joy = int(input("Digite a numeracao do joystick que deseja configurar (Ex: 1, 2, 3...): ")) -1
    if((sel_joy >= joystick_count) or (sel_joy < 0)):
        raise Exception("Valor invalido ou joystick inexistente")

    return pygame.joystick.Joystick(sel_joy)

def screen_init():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('PiFBA Configuracao Joystick')
    return screen

def createText(text, h):


    rtext = h.render(text, 1, (10, 10, 10))
    return rtext

def background_init(screen, fonts):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))

    title = createText("PiFBA Configuracao de Joystick", fonts[2])


    background.blit(title, (10,10))
    return background

def getEvents(joystick):
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise Exception("Saindo do programa... a pedido do usuario.")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            raise Exception("Saindo do programa... Tecla ESC Pressionada")

        
        
        
        elif event.type == pygame.JOYBUTTONUP:
            #print ("Joystick '" + joystick.get_name() + "' button" + str(event.button) + "up.")
            return ['is_button', event.button]

    return 0

def salvarCfg(joystick, botoes, cfg):
    # arquivo_filename = "/opt/retropie/configs/fba/fba2x.cfg"
    arquivo_filename = "/home/rafael/retroarch.cfg"
    btn_p1 = ['input_player1_a_btn', 'input_player1_x_btn', 'input_player1_b_btn', 'input_player1_y_btn', 'input_player1_l_btn', 'input_player1_r_btn', 'input_player1_start_btn', 'input_player1_select_btn']
    btn_p2 = ['input_player2_a_btn', 'input_player2_x_btn', 'input_player2_b_btn', 'input_player2_y_btn', 'input_player2_l_btn', 'input_player2_r_btn', 'input_player2_start_btn', 'input_player2_select_btn']
    
    arquivo = open(arquivo_filename, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    if(joystick.get_id() == 0):
        for btn_idx in range(len(btn_p1)):            
            for lin_idx in range(len(linhas)):
                if(linhas[lin_idx].startswith(btn_p1[btn_idx])):
                    linhas[lin_idx] = btn_p1[btn_idx]+"="+str(cfg[btn_idx])+"\n"
                
    else:
        for btn_idx in range(len(btn_p2)):            
            for lin_idx in range(len(linhas)):
                if(linhas[lin_idx].startswith(btn_p2[btn_idx])):
                    linhas[lin_idx] = btn_p2[btn_idx]+"="+str(cfg[btn_idx])+"\n"
    
    arquivo = open(arquivo_filename, "w")
    arquivo.writelines(linhas)
    arquivo.close()
    

# DEFINICAO DO MAIN
def main():
    os.system('cls' if os.name=='nt' else 'clear')
    pygame.init()
    pygame.joystick.init()
    fps = 30

    fonts = [pygame.font.SysFont("Arial", 15), pygame.font.SysFont("Arial", 23), pygame.font.SysFont("Arial", 35)]

    botoes = ['A', 'B', 'C', 'D', 'E', 'F', 'Start', 'Ficha (Coin)']
    cfg = []

    joystick_count = pygame.joystick.get_count()

    print("Configuracao PiFBA Joystick Configuration - Ver: 1.0")

    try:

        joystick = detectJoy(joystick_count)

        joystick.init()
        print("Joystick selecionado: "+str(joystick.get_id()+1)+" - "+joystick.get_name())
        screen = screen_init()

        background = background_init(screen, fonts)
        screen.blit(background, (0, 0))
        pygame.display.flip()
        btn_count = 0

        while 1:
            start = time.time()
            events = getEvents(joystick)





            if(isinstance(events, list)):
                if(events[0] == "is_button"):
                    cfg.append(events[1])
                    #print("eh botao")
                elif(events[0] == "is_axis"):
                    cfg.append(events[1])
                    #print("eh marcha")
                print("Qtde: " + str(len(cfg)))

            if(len(cfg) == 8):
                print(cfg)
                salvarCfg(joystick, botoes, cfg)
                pygame.quit()
                quit()

            background = background_init(screen, fonts)

            txt = createText("Pressione o botao: "+ botoes[len(cfg)] , fonts[2])
            background.blit(txt, (150, 150))
            txt = createText("Ou pressione ESC para sair.", fonts[1])
            background.blit(txt, (160,190))

            screen.blit(background, (0, 0))




            pygame.display.flip()

            # manutencao dos frames
            difference = start - time.time()
            delay = 1.0 / fps - difference
            if delay > 0:
                time.sleep(delay)

    except Exception as exc_det:
        type, value, traceback = sys.exc_info()
        print(type)
        print(value)
        print(traceback)
        print(exc_det.args)
        return


# EXECUCAO DO MAIN
main()
pygame.quit()
exit()

"""
elif event.type == pygame.JOYAXISMOTION:
                    for axis_index in range(joystick.get_numaxes()):
                        axis_status = joystick.get_axis(axis_index)
                        #print(str(axis_status) + " motion.")
                        if axis_status < -0.5:
                            #print("Joystick '" + joystick.get_name() + "' axis" + str(event.axis) + "motion.")
                            continuar = False
                            break

                        elif axis_status > 0.5:
                            #print("Joystick '" + joystick.get_name() + "' axis" + str(event.axis) + "motion.")
                            continuar = False
                            break

"""

