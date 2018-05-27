<!DOCTYPE html>
<html>
<head>
	<title>Redirecionamento de requisições (header)</title>
</head>
<body>
<?php
	echo 'O php disponibiliza a função header, que pode definir diversos parametros, entrs os principais redirecionamento automático da requisiçãos. Em deiversas funções como cadastro, alterações, exlcusão de dados, para encaminhar o sucesso ou falha da operação é possível incluir um comando header<br><br>';

	/*
	Sintaxe da função header
	(void) header(string)

	Para redirecionar alguém o parametro location deve ser definido
	(void) header("Location: URL")
	*/
	ob_start(); // interupção de fluxo
	include("dados.txt");
	header("Location: http://google.com.br")
	ob_flush(); // liberação de fluxo de saida
?>
</body>
</html>