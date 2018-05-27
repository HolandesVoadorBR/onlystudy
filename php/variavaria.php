<?php

// Php oferece um recurso de variaveis variaveis ($$) para códigos complexos
// Indicando que além do seu valor informado, ela pode ser acessada de forma alternativa

$variavel = "variavel";
$$variavel = 45;
// Equivalente a $variavel = 45;

//printar
echo("O valor de ".$variavel." é ".$$variavel."");

?>