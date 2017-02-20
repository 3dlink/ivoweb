$(document).ready(function(){

	$('#ivo-boton-menu').on('click', function(){
	  $('.ivo-menu-principal-panel').toggleClass('ivo-menu-principal-mostrar');
	});
	
	$('#ivo-boton-menu-cerrar').on('click', function(){
	  $('.ivo-menu-principal-panel').removeClass('ivo-menu-principal-mostrar');
	});

	$("#ivo-usuario").on('click', function(){
		if($('.ivo-usuario-subMenu').is( ":hidden" )){
	  		$('.ivo-usuario-subMenu').addClass('ivo-subMenu-mostrar');
	  		$("#ivo-usuario").addClass('ivo-subMenu-activo');
	  	}else {
	  		$('.ivo-usuario-subMenu').removeClass('ivo-subMenu-mostrar');
	  		$("#ivo-usuario").removeClass('ivo-subMenu-activo');
	  	}
	});


	$("#ivo-notificaciones").on('click', function(){
		if($('.ivo-notificaciones-subMenu').is( ":hidden" )){
	  		$('.ivo-notificaciones-subMenu').addClass('ivo-subMenu-mostrar');
	  		$('.ivo-notificaciones-triangulo').addClass('ivo-subMenu-mostrar');
	  		$("#ivo-notificaciones").parent().addClass('ivo-subMenu-activo');
	  	}else {
	  		$('.ivo-notificaciones-triangulo').removeClass('ivo-subMenu-mostrar');
	  		$('.ivo-notificaciones-subMenu').removeClass('ivo-subMenu-mostrar');
	  		$("#ivo-notificaciones").parent().removeClass('ivo-subMenu-activo');
	  	}
	});

	$("#ivo-carrito").on('click', function(){

		if($('.ivo-header-carrito-subMenu').is( ":hidden" )){
	  		$('.ivo-header-carrito-subMenu').addClass('ivo-subMenu-mostrar');
	  		$("#ivo-carrito").parent().addClass('ivo-subMenu-activo');
	  	}else {
	  		$('.ivo-header-carrito-subMenu').removeClass('ivo-subMenu-mostrar');
	  		$("#ivo-carrito").parent().removeClass('ivo-subMenu-activo');
	  	}
	});

	$("#ivo-galeria-fotoC").on('click', function(){
	  		$('#ivo-subir-flt').addClass('no-modal');
	  		$('#ivo-galeria-flt').removeClass('no-modal');
	});

	$("#ivo-subir-fotoC").on('click', function(){
	  		$('#ivo-galeria-flt').addClass('no-modal');
	  		$('#ivo-subir-flt').removeClass('no-modal');
	  			});

	$(document).bind("click", function (t) {
        
        var elemento = $(t.target);

        if(!$('.ivo-usuario-subMenu').is( ":hidden" )){
	        if (elemento.parents().hasClass('ivo-usuario-subMenu') || elemento.attr('id')=="ivo-usuario"){
	        }else {	$('.ivo-usuario-subMenu').removeClass('ivo-subMenu-mostrar');
		  		$("#ivo-usuario").removeClass('ivo-subMenu-activo');
	        }
    	}

    	if(!$('.ivo-notificaciones-subMenu').is( ":hidden" )){
	        if (elemento.parents().hasClass('ivo-notificaciones-subMenu') || elemento.attr('id')=="ivo-notificaciones"){
	        }else {	$('.ivo-notificaciones-subMenu').removeClass('ivo-subMenu-mostrar');
	        $('.ivo-notificaciones-triangulo').removeClass('ivo-subMenu-mostrar');
		  		$("#ivo-notificaciones").parent().removeClass('ivo-subMenu-activo');
	        }
    	}

    	if(!$('.ivo-header-carrito-subMenu').is( ":hidden" )){
	        if (elemento.parents().hasClass('ivo-header-carrito-subMenu') || elemento.attr('id')=="ivo-carrito"){
	        }else {	$('.ivo-header-carrito-subMenu').removeClass('ivo-subMenu-mostrar');
		  		$("#ivo-carrito").parent().removeClass('ivo-subMenu-activo');
	        }
    	}

    });


    function stickyScroll(e) {
    	if (window.pageYOffset>20) {
    		$('.ivo-header ').addClass('ivo-header-sticky');
    	}else {
    		$('.ivo-header ').removeClass('ivo-header-sticky');
    	}
	}

	// Scroll handler to toggle classes.
	window.addEventListener('scroll', stickyScroll, false);



	
	$('.filter a').click(function(e) {
	  e.preventDefault();
	  var a = $(this).attr('href');
	  a = a.substr(1);
	  $('.sets a').each(function() {
	    if (!$(this).hasClass(a) && a != 'all')
	      $(this).addClass('hide');
	    else
	      $(this).removeClass('hide');
	  });

	});

	$('.sets a').click(function(e) {
	  e.preventDefault();
	  var $i = $(this);
	  $('.sets a').not($i).toggleClass('pophide');
	  $i.toggleClass('pop');
	});

  
});

function soloNumeros(e) {
    var keynum = window.event ? window.event.keyCode : e.which;
    if ((keynum == 8) || (keynum == 46))
    return true;

    return /\d/.test(String.fromCharCode(keynum));
}

function correoValido(email){
	expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) ){
        return false;
    }
    else{
    	return true;
    }
}
function numeroValido(num){
	expr = /^([0-9])+$/;
	if ( !expr.test(num) )
        return false;
    else
    	return true;
}
function validarForm(form){
	var retorno = true;
	$(form).each(function(){
		var tipo = $(this).attr('type');
        if( $(this).attr('required') &&  $(this).val().trim() == '' && retorno == true && tipo != 'hidden'){
        	alert($(this).attr('mensaje'));
        	retorno = false;
        }
        if(retorno){
        	if (tipo == 'email' && $(this).attr('required')){
				if(!correoValido( $(this).val() )){
	    			alert('Ingrese un correo valido');
	        		retorno = false;		
	    		}
	    	}else if (tipo == 'number' && $(this).attr('required')){
	    		if(!numeroValido( $(this).val() )){
	    			alert('Ingrese solo numeros en el campo '+$(this).attr('name'));
	        		retorno = false;		
	        		
	        	}
	        }	
        }
    });
    return retorno;
}