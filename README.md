# Script de Backup para o S3

Este script faz o upload de arquivos de um diretório local para um bucket do Amazon S3. Ele compara o tamanho e a data de modificação de cada arquivo local com o arquivo correspondente no bucket do S3. Se o arquivo local for mais novo ou tiver um tamanho diferente, ele faz o upload do arquivo para o S3. Caso contrário, ele pula o arquivo.

## Pré-requisitos

- Python 3.x
- Biblioteca `boto3`: Instale usando `pip install boto3`

## Configuração

Antes de executar o script, você precisa fornecer os valores de configuração necessários.

1. Defina a variável `BUCKET_NAME` com o nome do seu bucket do Amazon S3.
2. Defina a variável `LOCAL_DIR` com o caminho do diretório local que você deseja fazer backup.
3. (Opcional) Modifique a variável `REMOTE_DIR` se desejar armazenar os arquivos de backup em uma pasta específica dentro do bucket do S3.

## Uso

1. Verifique se você instalou as dependências necessárias e configurou o script corretamente.
2. Execute o script usando o Python: `python backup_script.py`
3. O script percorrerá o diretório local de forma recursiva, comparará os arquivos com os do S3 e fará o upload/atualização conforme necessário.
4. O script exibirá mensagens indicando o status de cada arquivo.

**Observação:** É recomendado testar o script minuciosamente e entender o seu comportamento antes de executá-lo em dados críticos.
