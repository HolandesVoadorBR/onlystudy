<!DOCTYPE html>
<html>
<head>
	<title>SuperVariaveis do PHP</title>
</head>
<body>
<?php
	echo 'O PHP disponibilza, algumas supervariaveis que permitem acessar de forma simples valores passados como parametros pelos usuários e requisições HTTP, bem como informações de arquivos e upload, servidor e ambiente de execução. A maior parte consiste em arrays, cujos valores são acessados a partir de chaves(indices)<br><br>';

	/*
	$GLOBALS		| Variáveis de escopo global
	$_SERVER		| "" do servidor
	$_GET			| "" passadas por HTTP pelo método GET
	$_POST			| "" passadas por HTTP pelo método POST
	$_FILES			| "" de upload de arquivos
	$_REQUEST		| "" de URL
	$_SESSION		| "" de sessão
	$_ENV			| "" de ambiente
	$_COOKIE		| "" de cookies
	$php_errormsg	| Exibe a última mensagem de erro ocorrida
	$argc 			| Número de argumentos passados para o script
	$argv 			| Array de argumentos passados para o script

	*/

	echo 'Cada uma das supervariaveis apresenta uma série de varios valores para consulta. <br><br>';

	/*
	SERVER_ADDR 			| Ip do servidor
	SERVER_NAME 			| Nome do dominio em que o servidor está executando
	HTTP_ACCEPT_ENCODING 	| COnteúdo do header accept-encoding configurado para o servidor em que o PHP está executando
	HTTP_USER_AGENT 		| Exibe dados do navegador do usuário que originou a requisição ao servidor
	REMOTE_ADDR 			| Exibe o endereço IP do usuário que originou a requisição ao servidor

	*/

	echo($_SERVER['SERVER_ADDR'].'<br>'); // chamamos a supervariavel e sua função (ip do servidor)

	echo($_SERVER['SERVER_NAME'].'<br>'); // nome do servidor

	echo($_SERVER['HTTP_ACCEPT_ENCODING'].'<br>');

?>
</body>
</html>