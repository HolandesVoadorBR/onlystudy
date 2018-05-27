<!DOCTYPE html>
<html>
<head>
	<title>Goto</title>
</head>
<body>
<?php
	echo 'Goto, comando que permite direcionar a execução de um código para outra parte do bloco de códigos. Para isso é necessário definir quais são as partes de códigos existentes e disponíveis para essa função, citando seus nomes.<br><br><br>';

	//sintaxe
	// goto nome_do_bloco;

	echo('Código iniciando....<br>');
	goto saindo; // chamando o comando para a parte de bloco saindo

	echo('Código executando....<br>'); // o meio sendo ignorado

	saindo: // parte de bloco saindo sendo executada
		echo('Código encerrando....<br>');
?>
</body>
</html>