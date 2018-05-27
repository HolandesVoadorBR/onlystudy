<!DOCTYPE html>
<html>
<head>
	<title>While</title>
</head>
<body>
<?php
	echo 'Outro comando de repetição, que ultiliza as variaveis do codigo fonte(não necessariamente temporarias como em for), sendo necessária apenas definir sua condição de repetição <br><br>';

	//sintaxe
	//while(condição){
		//código a ser executado
	//}

	$i = 0;

	while($i < 5) // Se $i < 5
	{ //execução do código
		echo($i .' '); //imprimir na tela o resultado
		$i++; //fazer incrementação
	}

	echo('<br><br>'. $i . ' //Imprimindo valor da variavel após incrementação em while');

	echo '<br><br> Devemos cuidar a questão de incrementação caso contrário podemos derrubar o servidor, a variável tem que ser declarada desde o inicio.';
?>
</body>
</html>