<!DOCTYPE html>
<html>
<head>
	<title>Criando funções</title>
</head>
<body>
<?php
	echo 'Criar funçoes serve também para reduzir o código, criar as próprias funções ajuda muito, function.<br><br>';

	//sintaxe
	//function nome(parametro1, parametro_n){
		// código a ser executado
	// [return [valor]];
	//}
	//parametros são opcionais, pode retornar um valor para o código que a invocou ou não retornar nada

	function calculeDobro($valor){
		$dobro = $valor * 2;
		return $dobro;
	}

	$i = 10;
	echo("O dobro de $i é ".calculeDobro($i)."<br>");
	echo("O valor original de \$i é ".$i);

?>
</body>
</html>