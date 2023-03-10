import boto3
import os
from datetime import datetime

# Nome do bucket
BUCKET_NAME = ''

# Diretório local a ser copiado
LOCAL_DIR = ""

# Nome da pasta dentro do bucket para armazenar o backup
REMOTE_DIR = 'backup/'

# Criar um cliente do Amazon S3
s3 = boto3.client('s3')

# Percorrer o diretório local e fazer upload dos arquivos para o Amazon S3
for dirpath, dirnames, filenames in os.walk(LOCAL_DIR):
    for filename in filenames:
        local_path = os.path.join(dirpath, filename)
        relative_path = os.path.relpath(local_path, LOCAL_DIR)
        s3_path = os.path.join(REMOTE_DIR, relative_path).replace('\\', '/')
        
        # Obter informações do arquivo local
        local_file_stats = os.stat(local_path)
        local_file_size = local_file_stats.st_size
        local_file_mtime = datetime.utcfromtimestamp(local_file_stats.st_mtime)
        
        try:
            # Obter informações do arquivo no Amazon S3
            s3_object = s3.head_object(Bucket=BUCKET_NAME, Key=s3_path)
            s3_file_size = s3_object['ContentLength']
            s3_file_mtime = datetime.strptime(s3_object['LastModified'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            
            # Verificar se o arquivo local precisa ser atualizado no Amazon S3
            if local_file_size != s3_file_size or local_file_mtime > s3_file_mtime:
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
                print(f'Arquivo {local_path} atualizado no Amazon S3')
            else:
                print(f'Arquivo {local_path} já está sincronizado no Amazon S3')
        
        # Se o arquivo não existir no Amazon S3, fazer upload do arquivo local
        except s3.exceptions.ClientError as e:
            if e.response['Error']['Code'] == '404':
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
                print(f'Arquivo {local_path} adicionado ao Amazon S3')
            else:
                raise e
