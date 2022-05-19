# Sistema-de-controle-para-inventario
Sistema desenvolvido com a finalidade de realizar o controle de movimentação de placas no setor em questão.

Tal sistema cumpre um papel simples mas de extrema importância para a área de atuação: Monitorar todas os itens (neste caso, placas de perfil) que são estocadas neste setor.

Com o uso das linguagens Python, HTML, CSS (usando o framework TailWind CSS) e o alinhamento com um banco de dados SQL o sistema foi desenvolvido e implementado com eficácia, cumprindo seu papel.

<h2>UTILIZAÇÃO</h2>
  
OBS.: Devido a questões de sigilo emprasarial, tanto as fotos como a exemplificação serão "genéricas" e com fins ilustrativos.

![image](https://user-images.githubusercontent.com/70926962/168914142-35efd2f0-b1ab-4d5c-b199-a7957a6209d9.png)

<p align=center>(interface do sistema)</p>

O sistema possui 4 funcionalidades:

<h3>SAÍDA:</h3>

Realiza a movimentação de saída da placa identificada por um código de referência (GRN), para realizar a sáida é preciso inserir o nome de quem requisitou e para qual linha de produção ela irá.

OBSERVAÇÕES:

Caso o GRN informado não conste no sistema, a movimentação será barrada. Além disso caso a linha digitada não seja uma linha válida (neste exemplo as linhas possiveis são representadas pelos números 1, 2, 3, 4 e 5) a movimentação não será realizada e o usuário recebe uma mensagem informando o erro. O sistema também bloqueia saída de placas que já possuem saída.

<h4>Placa não cadastrada</h4>

![image](https://user-images.githubusercontent.com/70926962/168915841-372278e1-d154-4a6a-9674-279d367d555e.png)

<h4>Linha inválida</h4>

![image](https://user-images.githubusercontent.com/70926962/168916006-56a292b4-c81d-4b00-9c28-535aa1693def.png)

<h4>Placa já possui saída</h4>

![image](https://user-images.githubusercontent.com/70926962/168917374-e3b21bf8-a4f7-405d-898b-0ee53e00b432.png)

<h4>Dados informados OK e saída realizada</h4>

![image](https://user-images.githubusercontent.com/70926962/168916326-6e495e5f-6dbd-419c-b026-45354c974064.png)

<h3>ENTRADA:</h3>

Mesma idéia que a saída, porém agora basta inserir o GRN da placa para realizar a entrada desta.

OBSERVAÇÕES:

Novamente, caso o GRN digitado não esteja cadastrado no sistema uma mensagem de erro será mostrada. O sistema também bloqueia entrada de placas que já possuem entrada.

<h4>Placa não cadastrada</h4>

![image](https://user-images.githubusercontent.com/70926962/168915841-372278e1-d154-4a6a-9674-279d367d555e.png)

<h4>Placa já possui entrada</h4>

![image](https://user-images.githubusercontent.com/70926962/168917300-5295f88c-0c62-4c1a-8dde-68b689e19be4.png)

<h4>GRN válido e entrada realizada</h4>

![image](https://user-images.githubusercontent.com/70926962/168916979-28d49940-3b0b-4284-a2af-e17e48027ff2.png)

<h3>CADASTRO:</h3>

Aqui as placas são cadastradas, bastando apenas digitar qual será o GRN dela. 

OBSERVAÇÕES:

As placas seguem um padrão e (neste cenário ilustrativo), o GRN da placa deve iniciar com "PLACATESTE" e possuir 12 dígitos ficando "PLACATESTEAA" por exemplo. Placas não podem ser re-cadastradas e caso isso ocorra, uma mensagem será mostrada. 

<h4>GRN fora do padrão</h4>

![image](https://user-images.githubusercontent.com/70926962/168921601-474c3697-0819-49c7-a095-9a7b41a233dd.png)

<h4>Placa já cadastrada</h4>

![image](https://user-images.githubusercontent.com/70926962/168921845-c2e14f95-c7e8-4335-af5e-1a169a3262ac.png)

<h4>Cadastro realizado</h4>

![image](https://user-images.githubusercontent.com/70926962/168922163-48754a36-fbc0-497c-9840-1ca0c58ba1b5.png)

<h2>PLACAS CADASTRADAS</h2>

Aqui é possível gerar um relatório de todas as placas cadastradas, mostrando a placa, o local onde ela está, quem requisitou por último a placa, a data da última movimentação e quantas vezes o ciclo saída/entrada foi realizado. Tal relatório é um resultado do banco de dados e é mostrado apartir de um documento em .xlsx (excel).

<h2>INFORMAÇÕES EXTRAS</h2>

- Cada placa só pode ter seu ciclo realizado 10 vezes, depois disso, a placa é bloqueada e não pode ser movimentada.
- A remoção das placas do sistema é realizado apartir de um programa de ADM, onde pode-se ver todas as placas cadastradas e remover apartir de seu GRN.
- Como dito antes, o sistema roda em Python, e apartir da biblioteca CherryPy, é possivel que qualquer computador da rede acesse o endereço do sistema.


