#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Detecção e traçamento do movimento de objetos em vídeos.

Este código possui uma função de detecção e traçamento do 
movimento de objetos em vídeos. 

O código identifica objetos se movendo e enquadra o objeto com uma
"caixa de entorno". Para cada quadro em que um objeto em movimento,
o número do quadro, junto com os dados dessa caixa de entorno 
(coordenadas horizontal e vertical do canto inferior da caixa e a 
largura e a altura da caixa) são registrados em uma lista. Essa 
lista é retornada pela função ao final da análise.

Isso é implementado por uma única função, que possui outros argumentos
de configuração e funcionalidades:

    * detector_de_movimento: recebe o caminho para um arquivo de video
        que será analisado visando detectar e traçar o movimento de um 
        ou mais objetos. 
        
        Retorna o número de quadros por segundo do video e os dados 
        sobre o andamento da caixa de entorno dos objetos em movimento. 
        
        Dependendo dos argumentos, pode gravar em disco ou exibir
        na tela os videos usados ao longo do processamento. Outras 
        opções ajustam a área mínima para um objeto ser identificado, 
        o nível de corte da escala de cinzas usada na detecção do 
        objeto e os quadros inicial e final para o tratamento.

Para mais informações, veja o `help` da função `detector_de_movimento`.

Também é possível usar o código como um script, a partir da linha de
comando. Veja as informações sobre como passar os argumentos através do
comando de linha
```bash
detector_de_movimento --help
```

Exemplos de uso como script:
    1) Exibindo, na tela do computador, os vídeos de processamento

        $ python movimento.py --video video.mov -e

    2) Alterando alguns parâmetros, gravando o video processado e 
    exibindo os vídeos de processamento:

        $ python movimento.py --video video.mov -o video_tratado.avi
            --area_min 200 --nivel_de_corte 50 -e

O código usa o pacote `opencv` e o módulo `imutils`, além do módulo
padrão `argparse`.

Baseado no script disponível em [Basic motion detection and tracking with Python and OpenCV](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/).
'''

__author__ = "Ricardo M. S. Rosa <rmsrosa@gmail.com>"
__homepage__ = "http://github.com/rmsrosa/jupyterbookmaker"
__license__ = "GNU GPLv3"
__version__ = "0.3.1"
__status__ = "beta"

# importa os pacotes necessários

import argparse

import cv2
from imutils.video import VideoStream
import imutils

def detector_de_movimento(video, width = 512,
                          area_min = 500, 
                          nivel_de_corte = 25,
                          quadro_inicial = 1,
                          quadro_final = -1,
                          video_tracado = None,
                          video_cinza = None,
                          video_pb = None,
                          exibe_videos = False):
    '''
    Detecta e traça o movimento de objetos em vídeos.
    
    Esta função usa um método simples de contraste de cada quadro
    com o quadro inicial para detectar a alteração ocorrida e
    inferir e acompanhar a posição de um objeto que se moveu ou 
    que não estava presente na imagem original. 

    Se o objeto já aparece na imagem inicial e se desloca, um 
    "fantasma" do objeto é constantemente detectado. O ideal é que 
    o objeto não apareça inicialmente no vídeo.

    O algoritmo de detecção é baseado nos seguintes passos:

        - O primeiro quadro do filme é transformado em escala
         de cinza (de 0 a 255, i.e. de preto a branco), gerando 
         um quadro denominado `firstFrame`.

        - Cada quadro subsequente também é transformado em escala 
        de cinza (denominado `gray`) e um novo quadro é formado com 
        a diferença entre esse quadro e o primeiro quadro: 
        `tresh = gray - firstFrame`.

        - Com base em um `nivel_de_cinza`, entre 0 e 255, essa 
        diferença é transformada em uma imagem `tresh` em preto 
        e branco, ficando cada *pixel* preto, se o cinza estiver 
        abaixo desse nível, ou branco, se estiver acima.

        - Curvas de contorno entre as partes em preto e em branco 
        da imagem `tresh` são identificadas pelo `opencv`.

        - Para cada curva envolvendo uma área maior do que uma área 
        mínima `area_min`, uma *caixa de entorno* é registrada.
    
    Entrada:
    --------
        video: string
            Uma string com o nome (incluindo o caminho) do arquivo 
            de vídeo a ser tratado.
        
        area_min: ponto flutuante
            A área mínima (em número de pixels) necessária para 
            que um objeto seja identificado. Por exemplo, um
            pequeno retângulo de 20 por 20 pixels tem 400 pixels
            de área.

        nivel_de_corte: ponto flutuante
            O nível de corte para o contraste, em uma escala de 0 a 255,
            para determinar, em cada pixel da imagem, se há diferente 
            entre o quadro atual e o quadro inicial ou não.
                                            
        video_tracado: string
            Uma string com o nome (incluindo o caminho) do arquivo 
            de vídeo a ser gravado contendo o resultado do 
            processamento. O vídeo inclui textos indicando o número
            de cada quadro, o tempo decorrido, o estado do ambiente
            (se ocupado ou desocupado) e com uma caixa de contorno
            em volta de cada objeto detectado.

        video_cinza: string
            Uma string com o nome (incluindo o caminho) do arquivo 
            de vídeo a ser gravado contendo a diferença (pixel a pixel)
            entre os níveis de cinza entre o quadro atual e o quadro
            inicial, que forma a base para a detecção.
        
        video_pb: string
            Uma string com o nome (incluindo o caminho) do arquivo 
            de vídeo a ser gravado, em preto e branco, contendo 
            a versão "estourada" do `video_cinza` descrito acima.
            O estouro é feito com base no `nivel_de_cinza`. 

        exibe_videos = Boolean
            Se `True`, exibe os vídeos envolvidos no tratamento, a
            saber, um vídeo com o contraste inicial entre o quadro 
            atual e o inicial, um vídeo com esse contraste saturado 
            e um vídeo com o processamento final, descrito na
            opção `video_tracado`.
    
    Saída:
    ------
        fps: ponto flutuante
            O número de quadros por segundo do vídeo.

        num_quadros: ponto flutuante
            O número total de quadros examinados.

        tracado: lista
            Uma lista de listas, onde o primeiro item da lista 
            é a lista de strings ['n', 'x', 'y', 'l', 'h'], o segundo 
            item é a lista de strings `['quadro', 'abscissa(px)', 
            'ordenada(px)', 'largura(px)', 'altura(px)']` e outros 
            itens são listas contenda, no ordem, inteiros indicando
            o número do quadro correspondente, a abscissa e a ordenada
            do cando esquerdo inferior da caixa de entorno do objeto
            identificado no quadro e a largura e a altura dessa caixa
            de entorno.

            Quando mais de um objeto é identificado em um mesmo quadro,
            os dados da caixa de entorno de cada objeto são incluídos
            em itens diferentes da lista `tracado`, contendo o mesmo
            número de quadro.
            
    Exemplos:
    --------
        1) Gravando o vídeo processado:
        
            detector_de_movimento("video.mp4",  
                                  video_tracado = "video_tratado.avi")

        2) Alterando alguns parâmetros e exibindo os vídeos de 
        processamento:

            detector_de_movimento("video.mp4", area_min = 200, 
                                  nivel_de_corte = 50,
                                  exibe_videos = True)
        
    '''

    # carrega o vídeo para leitura pelo opencv
    try:
        vs = cv2.VideoCapture(video)
    except FileNotFoundError:
        pass

    # Lê a taxa de quadros por segundo do video
    fps = vs.get(cv2.CAP_PROP_FPS)

    # define o primeiro quadro inicialmente como None
    firstFrame = None    

    # inicializa tracado

    tracado = [
        ['n', 'x', 'y', 'l', 'h'],
        ['quadro', 'abscissa(px)', 'ordenada(px)', 'largura(px)', 'altura(px)']
    ]

    # inicializa variavel de contagem de quadros
    num_quadro = 0

    # loop para percorrer todos os quadros do vídeo
    while True:

        # incrementa a variável de número do quadro
        num_quadro += 1

        # lê o quadro atual
        frame = vs.read()
        frame = frame[1]

        # se o número do quadro for menor do que o quadro inicial,
        # avança para o próximo quadro
        if num_quadro < quadro_inicial:
            continue

        # define texto a ser gravado na imagem
        text = "Desocupado"

        # Se frame lido é None, chegamos ao final do vídeo 
        # e interrompemos a leitura
        if frame is None or 0 < quadro_final < num_quadro:
            break

        # redimensiona quadro, converte para escala de cinza
        # e embaça a imagem (*blur*)
        frame = imutils.resize(frame, width=width)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Se firstFrame é None, inicializa-o como fundo de referência
        # Inicializa-se o tempo também e lê as dimensões da imagem
        if firstFrame is None:
            firstFrame = gray
            height, width, channels = frame.shape

            # Se tiver sido dada a opção para gravar o video com o
            # traçado, inicializa o arquivo de video de saída.
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')

            if video_tracado is not None:
                out_tracado = cv2.VideoWriter(video_tracado, fourcc, fps, (width,height), 1)
            if video_cinza is not None:
                out_cinza = cv2.VideoWriter(video_cinza, fourcc, fps, (width,height), 0)
            if video_pb is not None:
                out_pb = cv2.VideoWriter(video_pb, fourcc, fps, (width,height), 0)
            
            continue

        # define o `frameDelta` como sendo o quadro com a diferença 
        # absoluta entre o quadro atual e o primeiro quadro
        frameDelta = cv2.absdiff(firstFrame, gray)

        # define o quadro `tresh` saturando o contraste na imagem do
        # frameDelta.
        thresh = cv2.threshold(frameDelta, nivel_de_corte, 255, 
                               cv2.THRESH_BINARY)[1]

        # dilata a imagem em `thresh` para preencher os buracos 
        thresh = cv2.dilate(thresh, None, iterations=2)

        # captura o contorno da imagem em contraste
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # percorre os contornos
        for c in cnts:
            # se o contorno for muito pequeno, ignore-o
            if cv2.contourArea(c) < area_min:
                continue

            # calcula a "caixa de entorno" *(bounding box)* do contorno,
            # desenha a caixa na imagem e atualiza o texto a gravar
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Ocupado"

            # exibe, no console, o tempo decorrido até esse quadro e
            # as informaçõs da caixa de entorno
            tracado.append([num_quadro,x,y,w,h])

        # escreve o texto, o número do quadro e o tempo decorrido
        cor_do_texto = (0,0,220)
        cv2.putText(frame, f"Ambiente: {text}", 
            (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, cor_do_texto, 1)
        quadros_decorridos = num_quadro - quadro_inicial + 1
        tempo_str = f"{int(quadros_decorridos/fps/60):3d}m {int(quadros_decorridos/fps % 60):02d}s {int(1000*(quadros_decorridos/fps % 1)):03d}ms"
        cv2.putText(frame, f"Quadro: {quadros_decorridos}",
            (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, cor_do_texto, 1)
        cv2.putText(frame, f"Tempo: {tempo_str}",
            (frame.shape[1] - 154, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, cor_do_texto, 1)


        # exibe os quadros se essa opção estiver sido escolhida
        #. the frame and record if the user presses a key
        if exibe_videos:
            cv2.imshow("Frame Delta", frameDelta)
            cv2.imshow("Thresh", thresh)
            cv2.imshow("Security Feed", frame)

        # Se tiver sido dada a opção para gravar o video com o
        # traçado, grava mais este quadro
        if video_tracado is not None:
            out_tracado.write(frame)
        if video_cinza is not None:
            out_cinza.write(frameDelta)
        if video_pb is not None:
            out_pb.write(thresh)

        # Se a tecla `q` for pressionada, interrompe o processo
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # libera os arquivos de video e fecha as janelas abertas.
    vs.release()
    if video_tracado is not None:
        out_tracado.release()
    if video_cinza is not None:
        out_cinza.release()
    if video_pb is not None:
        out_pb.release()

    cv2.destroyAllWindows()

    return fps, num_quadro - quadro_inicial + 1, tracado

if __name__ == '__main__':

    # define o *parser* de argumentos
    ap = argparse.ArgumentParser(description="Detecta e traça o movimento de objetos em vídeos.")
    ap.add_argument("video", metavar="VIDEO", type=str,
                    help="caminho para o arquivo de video a ser analisado.")
    ap.add_argument("-a", "--area_min", type=int, default=500, 
                    help="área mínima para a detecção do objeto.")
    ap.add_argument("-n", "--nivel_de_corte", type=int, default=25,
                    help="nível de corte (threshold) para a identificação dos objetos em movimento.")
    ap.add_argument("--quadro_inicial", type=int, default=1,
                    help="número do quadro em que o tratamento do vídeo deve ser iniciado.")
    ap.add_argument("--quadro_final", type=int, default=-1,
                    help="número do quadro em que o tratamento do vídeo deve ser finalizado.")
    ap.add_argument("-o", "--video_tracado", default=None,
                    help="nome do arquivo a ser criado contendo o video processado com a identificação do objeto em movimento.")
    ap.add_argument("--video_cinza", default=None,
                    help="nome do arquivo a ser criado contendo o video processado em níveis de cinza, com a diferença em relação ao primeiro quadro.")
    ap.add_argument("--video_pb", default=None,
                    help="nome do arquivo a ser criado com o video processado em preto e branco, com a diferença em relação ao primeiro quadro, estourado de acordo com o nível de corte.")
    ap.add_argument("-e", "--exibe_videos", default=False, 
                    action="store_true", 
                    help="exibe os videos do processamento.")

    # captura os argumentos dados
    args = vars(ap.parse_args())

    # executa a função de detecção de movimento com os argumentos dados
    fps, num_quadros, tracado = detector_de_movimento(**args)
    
    print(f'Número de quadros por segundo: {fps:.2f}')
    print(f'Total de quadros: {num_quadros}')
    print(f'Tempo tratado de video: {int(num_quadros/fps/60):3d}m {int(num_quadros/fps % 60):02d}s {int(1000*(num_quadros/fps % 1)):03d}ms')