<!DOCTYPE html>
<html>
<head>
	<title>Include</title>
</head>
<body>
<?php
	echo 'Include, serve para centraçização de códigos em arquivos separados, sendo assim podemos criar um arquivo com todas as funções deixando elas centralizadas, não sendo repetidas a cada novo arquivo PHP(deixando o código mais lento)<br><br>';
	/*
	Para importar um arquivo PHP dentro de outro os seguintes comandos estão disponíveis:

	include(arquivo) | Importa e executa o código de um arquivo PHP gerando alertas caso alguma falha ocorra

	include_once(arquivo) | Realiza o mesmo que include, mas caso um mesmo documento seja importado pela segunda vez seu código não seja executado

	require(arquivo) | Importa e executa o código de um arquivo php, gerando um erro fatal e interrompendo a execução do código caso alguma falha ocorra.

	require_once(arquivo) | Realiza o mesmo que 'require', mas caso um mesmo documento seja importado pela segunda vez, seu código não é executado

	*/

	$valor = 'Alemanha'; // Declaramos a variavel valor com value alemanha
	echo($valor.'<br>'); // imprimimos ela

	include 'valor.php'; // chamamos o arquivo php
	echo($valor1.'<br>'); // imprimimos o $valor dentro do arquivo php
?>
</body>
</html>