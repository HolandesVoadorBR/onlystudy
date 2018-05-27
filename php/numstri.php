<!DOCTYPE html>
<html>
<head>
	<title>Numeros e strings</title>
</head>
<body>
<?php
	echo 'A função number_format serve para formatar números decimais, informando quantas casas devem aparecer e incluindo a vírgula a cada três numeros<br><br>';

	//sintaxe
	//(string) number_format(valor, casas decimais, divisor decimal, divisor milhar)

	$valor = 12345.678;
	$var1 = number_format($valor, 1);
	$var2 = number_format($valor, 2, ',','.');

	echo($valor.' //Meu valor <br><br>');
	echo($var1. ' //Aplicando number_format() <br><br>');
	echo($var2. ' //Aplicando number_format() <br><br>');
?>
</body>
</html>