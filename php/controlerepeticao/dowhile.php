<!DOCTYPE html>
<html>
<head>
	<title>Do While</title>
</head>
<body>
<?php
	echo 'Quase identico ao while, caractesristica diferente (Sua condição é testada no final da execução de cada bloco o que implica que seu código é executado apenas uma vez independemente de condições e variáveis <br><br>';

	//sintaxe
	//do {
		// código a ser executado
	//} while(condição);

	$i = 0; //declara variavel

	do{ //chama o comando
		echo($i .' '); //imprimir
		$i++; // incrementar
	} while($i < 5); // verificação no final do código

	echo ('<br><br>'. $i . ' //Valor após incrementação');

?>
</body>
</html>