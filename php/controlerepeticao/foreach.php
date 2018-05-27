<!DOCTYPE html>
<html>
<head>
	<title>Foreach: </title>
</head>
<body>
<?php
	echo 'O comando .Foreach. realiza uma função parecida com .FOR.: Porém está ligada com a navegação de posições de um array. <br><br>';
	echo 'Diferente de for, foreach não necessita informação condição nem o parâmetro de incremento, pois sua navegação sempre se dará para todos os registros do array informado <br><br>';

	//sintaxe:
	//foreach(array as variaveis temporarias){
	//código a ser executado
	//}

	$meuarray = array('a', 'b', 'c', 'd'); //declaramos um array(contém varios valores)

	foreach($meuarray as $valor) //chamamos o array e criamos a variavel temporaria valor para seprar
	{
		echo($valor .' '); // imprimimos os resultados da variavel temporaria
	}
?>
</body>
</html>