$(function(){
	$("#id_tipo_salida").change(function(){
		if ($("#id_tipo_salida").val() == "cliente"){
			$("#id_numero_contrato").show();
			$("label[for='id_numero_contrato']").show();
		}else{
			$("#id_numero_contrato").hide();
			$("label[for='id_numero_contrato']").hide();
		}
	});
});