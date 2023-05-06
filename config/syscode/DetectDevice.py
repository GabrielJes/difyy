import time
import subprocess
import sys
import tqdm

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
        print()
        print('Disk not found! ')
        sys.exit(1) # retorna false para encerrar o programa

def IdentifyFileSystem(): # Verifica qual sistemas de arquivo a pessoa quer formatar o pendrive e retorna o nome .
    print()
    print('Select file system : ')
    print()
    print('Enter the option number: ')
    print(' 1 - ext4 \n 2 - vfat')
    print('-'*40)

    Archive = int(input(''))
    if Archive == 1:
        FileSystem = 'ext4'
        
    elif Archive == 2:
        FileSystem = 'Vfat'
    
    else :
        print('Invalid option')
        sys.exit(1)

    return FileSystem

def Confirm(UserResponse): # Confirma se o usuario ja conectou o pendrive, retorna True caso tenha confirmado
    if UserResponse != 's' and UserResponse != 'y':
        print()
        print('Closing ...')
        sys.exit(1)
    else:
        return True

def ext4Config(localdisk): # Configuracao para opcao de ext4
    FileSystem = 'ext4'
    output = subprocess.check_output(f"sudo mkfs.ext4 /dev/{localdisk}*" , shell=True)
    output = output.decode('utf-8')
        
def vfatConfig(localdisk): # Configuracao para opcao de vfat
    FileSystem = 'vfat'
    output = subprocess.check_output(f"sudo mkfs.ext4 /dev/{localdisk}*" , shell=True)
    output = output.decode('utf-8')
   
def FormatDisk(local,Filesystem): # Formata o disco com sistema de arquivos escolhido
    output = subprocess.Popen(f"sudo umount /dev/{local}1", shell=True) 
    print('Creating file system! \n ')
    output = subprocess.check_output(f"sudo mkfs.{Filesystem} /dev/{local}1", shell=True) 
    output = output.decode('utf-8')
    return True
 
def IsoIdentify():
    image = input('Enter the path of your image: ') 
    time.sleep(0.4)
    print('Creating boot! ')
    time.sleep(5)
    output = subprocess.Popen(f"sudo dd if={image} of=/dev/sdb status=progress && sync", shell=True)
    return True


