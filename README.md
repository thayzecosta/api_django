## Criação de um projeto Django:

Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:

    python3 -m venv ./venv

Ative seu ambiente virtual com o seguinte comando (MAC e Linux):

    source venv/bin/activate

Em caso de Windows, utilize o comando:

    venv\Scripts\activate.bat

Instale o Django nesse ambiente virtualizado:

    pip install django

Instalações adicionais:
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support

Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:

    django-admin startproject setup .

Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

Para iniciar a aplicação, no terminal integrado, escreva:

    python manage.py startapp escola

Para iniciar o servidor:

    python manage.py runserver

Acesse o endereço "http://localhost:8000". Para parar o servidor, use o atalho "Ctrl + C". Caso ele perguntar se deseja encerrar o processo, basta pressionar "Y" e "Enter".

