# library
Sistema de gerenciamento de biblioteca

Back-end
Utilizado Rest Framework para Django.


### Primeiros passos:
*No banco de dados Postgree crie um banco chamado librarydb.

*Na pasta do projeto, abra o arquivo settings.py na pasta library.

*Altere as configurações do banco em DATABASES.

*Abra o terminal e digite python manage.py makemigrations

*Depois digite python manage.py migrate

*Por último digite python manage.py runserver

### Detalhe Sobre o Back-end
O projeto foi feito com o front-end desmembrado do back-end utilizando reactjs para o front.
Para que o react consiga consumir os endpoints da nossa api é necessário permitir o aceso do localhost na porta 3000 (porta que o react roda)
Para isso foi instalado o corsheaders no projeto Django.
