<!DOCTYPE html>
<html>
<head>
	<title>Exit</title>
</head>
<body>
<?php
	echo 'Exit(Antigo Die), o comando exit realiza o encerramento da execução do código em questão, geralmente o comando é utilizado depois de um erro ou alguma inconsistência ser encontrado no sistema, como uma conexão não realizada <br><br>';

	//sintaxe
	//exit(motivo)
	echo 'Podemos utilizar o die ao invés do exit<br><br>';

	$arquivo = '/caminho/inexistente'; // Variável do diretório declarada
	$file = fopen($arquivo, 'r') or exit('Problemas ao abrir o arquivo <br><br>'); // arquivo a ser aberto e comando exit chamado

?>
</body>
</html>