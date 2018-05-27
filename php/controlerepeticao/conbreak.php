<!DOCTYPE html>
<html>
<head>
	<title>Break|Continue</title>
</head>
<body>
<?php
	echo 'O comando break, serve para interromper a execução de um bloco de códigos, seja ele em for ou while <br><br>';

	for($i = 0; $i < 5; $i++){ //Declarando variável, condição e incrementação
		if($i == 4){ //se $i == 4 então
			break; // terminar comando
		}
		echo($i .' ');// Resultado

	}

	echo('<br><br>'. $i . ' //Valor da variável $i, após incrementação');
?>

</br>
</br>
-------------------------------------------
</br>
<?php
	echo "Continue, complementar ao comando break, avança o código para o próximo ciclo de repetição, sem terminar o ciclo atual. Não encerra o bloco de repetição e acaba avançando para o próximo. <br><br>";

	for($i = 0; $i < 10; $i++){
		if($i == 4){
			continue;
		}

		echo($i .' '); // imprimir resultado do comando
	}

	echo('<br><br>'. $i .' //Imprimir resultado após incrementação');

?>
</body>
</html>