Python + Cloud + GitHub
Este trabalho demonstra habilidades práticas no uso de Python para tarefas relacionadas à nuvem. É focado em 3 áreas principais:

Consumo de APIs Externas: Interação com as APIs do GitHub e Open-Meteo para buscar dados em tempo real.

Manipulação de Dados: Criação e leitura de um arquivo de dados local no formato JSON.

Criação de um Microserviço: Desenvolvimento de uma API web RESTful com o framework Flask.

Versionamento de código com github

🚀 Tecnologias Utilizadas
Python 3: Linguagem principal do projeto.

Flask: Micro-framework para a construção da API web.

Requests: Biblioteca para a realização de requisições HTTP.

Git & GitHub: Ferramentas para controle de versão e hospedagem.

📂 Scripts em execussão:
1. api_github.py
Conecta à API pública do GitHub pra exibir o nome, a descrição e o número de estrelas do repositório principal da linguagem Python (cpython).

Print da Execução:
<img width="992" height="605" alt="image" src="https://github.com/user-attachments/assets/da3bc64b-7c2c-4b94-9fef-14b25ec70c58" />

2. api_clima.py
Utiliza a API Open-Meteo para consultar e mostrar a temperatura atual e a velocidade do vento para as cidades de Curitiba e São Paulo. O script inclui tratamento de erros para falhas de conexão.

Print da Execução:
<img width="1090" height="234" alt="image" src="https://github.com/user-attachments/assets/f1424d31-330e-4b24-82c7-e952e9da9eae" />

Coloquei com erro usando try/except testei sem conexão a internet:
<img width="1090" height="130" alt="image" src="https://github.com/user-attachments/assets/80e2d687-b11a-44d4-96c8-2d0a80ee82b4" />

3. json_local.py
Manipulação arquivos de dados. Primeiro salva uma lista de alunos (com nome e curso) em um arquivo alunos.json e, em seguida, lê este arquivo para exibir as informações no console.

Print da Execução:

<img width="1090" height="231" alt="image" src="https://github.com/user-attachments/assets/4713fe3a-1aed-462b-bc4d-3010cec03e3c" />


4. api_flask.py
Cria um servidor web local que funciona como uma API RESTful com quatro rotas:

/: boas-vindas para testar se a API está no ar.

<img width="963" height="294" alt="image" src="https://github.com/user-attachments/assets/c5e8e9a2-2308-49e1-9451-ae7834977f0a" />

/alunos: Lista todos os alunos lendo do arquivo alunos.json.

<img width="950" height="442" alt="image" src="https://github.com/user-attachments/assets/8b397077-2f49-4774-afa5-8a47e549a8dd" />

/saudacao/<nome>: Devolve uma saudação personalizada.

<img width="936" height="275" alt="image" src="https://github.com/user-attachments/assets/a223860b-cd79-4c7e-b176-6e418194521c" />

/curso/<curso>: Filtra e exibe os alunos que pertencem a um curso específico.
<img width="1080" height="405" alt="image" src="https://github.com/user-attachments/assets/68f2b3b8-3178-4f1c-adb3-0bdb67e4ff2c" />
<img width="1090" height="443" alt="image" src="https://github.com/user-attachments/assets/7386686c-ab81-412f-b82b-77479770ab50" />


