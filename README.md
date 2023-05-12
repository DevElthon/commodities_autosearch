# commodities_autosearch
O mercado de commodities é amplo e está em constante mudança, por isso, investidores precisam estar o tempo todo em contato com os preços para saber o que comprar e o que não comprar. Pensando nisso, criei esse programa em Python pensando em automatizar o processo de pesquisa.

O programa realiza a leitura de uma tabela excel, e após realizar as devidas modificações (modificações de alguns caractéres para evitar erros durante o processo de pesquisa), é realizada uma pesquisa no navagador, para isso utilizei a biblioteca do python "selenium" para automatizar a navegação através do chrome (navegador utilizado para o projeto). Durante a navegação, o programa pesquisa o preço dos produtos cotados na tabela, no site "https://www.melhorcambio.com/{produto}-hoje", e utilizando o xpath dos elementos HTML do site, as informações de preço são passadas de volta ao programa.

Após isso, a tabela será atualizada com os preços atuais e se o preço atual de um determinado produto for menor ou igual ao preço ideal, o mesmo será marcado para ser comprado.
Por fim, uma tabela com os preços atualizados será gerada ao final do programa.
