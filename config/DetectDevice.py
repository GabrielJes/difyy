import time
import subprocess
import sys
import os
import tqdm


def loadingProgress(): # Loading progress . 
    for i in tqdm(range(10)):
        time.sleep(1)

def PendriveDetect(): # Retorna o caminho do disco que foi detectado . 
    # Roda o fdisk para verificar quais sao as opcoes de discos, ignorando a opcao do disco A
    output = subprocess.check_output("sudo fdisk -l | grep sd", shell=True) 
    output = output.decode('utf-8') 
    local1 = 'sdb'  # cada local e um possivel pendrive ou disco plugado 
    local2 = 'sdc'
    local3 = 'sdd'

    if local1 in output:
        # o comando abaixo pesquisa o disk identifier, caso ele nao seja do padrao de um pendrive o programa e encerrado
        output = subprocess.check_output("sudo fdisk -l /dev/sdb | grep identifier" , shell=True)
        output = output.decode('utf-8')
        SerialNumber = output[17:27:1] # Verificando output do comando 
        if len(SerialNumber) == 10: # Um serial number de pendrive tem no maximo 10 caracteres, 
            local = 'SDB'# se todos os checks passarem o pendrive e encontrado
            return local # retorna o local para validar a localizacao do pendrive 
        
    elif local2 in output:
        output = subprocess.check_output("sudo fdisk -l /dev/sdc | grep identifier" , shell=True)
        output = output.decode('utf-8')
        SerialNumber = output[17:27:1]
        if len(SerialNumber) == 10:
            local = 'SDC'
            return local
        
    elif local3 in output:
        output = subprocess.check_output("sudo fdisk -l /dev/sdd | grep identifier" , shell=True)
        output = output.decode('utf-8')
        SerialNumber = output[17:27:1]
        if len(SerialNumber) == 10:
            local = 'SDD'
            return local
    else:
        print('Pendrive não encontrado')
        return False # retorna false para encerrar o programa

def IdentifyFileSystem(): # Verifica qual sistemas de arquivo a pessoa quer formatar o pendrive e retorna o nome .
    print()
    print('Selecione a opcao dos sistema de arquivos: ')
    print()
    print(' 1 - ext4 \n 2 - vfat')
    print('-'*40)

    Archive = int(input(''))
    if Archive == 1:
        FileSystem = 'ext4'
        
    elif Archive == 2:
        FileSystem = 'Vfat'

    else :
        print('Opção inválida')
        sys.exit(1)

    return FileSystem

def Confirm(UserResponse): # Confirma se o usuario ja conectou o pendrive, retorna True caso tenha confirmado
    if UserResponse != 's' and UserResponse != 'y':
        print('Encerrando ...')
        time.sleep(3)
        sys.exit(1)
    else:
        return True

def ext4Config(localdisk):
    FileSystem = 'ext4'
    output = subprocess.check_output(f"sudo mkfs.ext4 /dev/{localdisk}*" , shell=True)
    output = output.decode('utf-8')
    print(output)
    
def vfatConfig(localdisk):
    FileSystem = 'vfat'
    output = subprocess.check_output(f"sudo mkfs.ext4 /dev/{localdisk}*" , shell=True)
    output = output.decode('utf-8')
    print(output)

def FormatDisk(local,Filesystem):
    output = subprocess.Popen(f"sudo umount /dev/{local}1", shell=True) 
    print('Criando sistema de arquivos! ')
    output = subprocess.check_output(f"sudo mkfs.{Filesystem} /dev/{local}1", shell=True) 
    output = output.decode('utf-8')
    print(output)

    


    
    
















# criar script para formatacao do pendrive

# adicione o caminho da imagem

# verificar se existe / foi encontrado

# iniciar processo de boot

# criar barra de progresso

# criar um output de feito ou erro

