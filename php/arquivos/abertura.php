<!DOCTYPE html>
<html>
<head>
	<title>Abertura de arquivos</title>
</head>
<body>
<?php
	echo 'O PHP Permite a manipulação de arquivos desde que tenha permissão e acesso as pastas e arquivos. Abertura/Leitura/Gravação de arquivos: <br><br>';

	/*
	Anertura de arquivos sintaxe fopen:
	(resource) fopen(arquivo, modo)

	Leitura de arquivos sintaxe fread:
	(string) fread(arquivo_aberto, bytes_a_serem_lidos)

	Gravação de arquivos sintaxe fwrite:
	(int) fwrite(arquivo, string, comprimento) |primeiro o arquivo|opicional tamanho limitado|opcional da funcao
	*/

	//Escrevendo em arquivo
	$file = fopen('dados.txt', 'w');
	fwrite($file, 'Escrevendo ');
	fwrite($file, 'no arquivo. ');
	fclose($file);

	//Lendo o arquivo
	$filepath = "dados.txt";
	$file = fopen($filepath, "r");
	$buffer = fread($file, filesize($filepath));
	fclose($file);

	echo($buffer);

	/*
	É possível ler o arquivo linha por linha com os comandos file e count

	*/
?>
</body>
</html>