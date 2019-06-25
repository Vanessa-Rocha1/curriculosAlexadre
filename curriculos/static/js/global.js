
$(function() {
	// Carregamento via AJAX simples
	$('#num_curriculos').load('http://127.0.0.1:8000/quantidadeDeCurriculos/');	
})

$(document).ready(function(){
	
$("#dica1").click(function(){
  $("#hide1").show();
})

$("#dica2").click(function(){
  $("#hide2").show();
})

})


