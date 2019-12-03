$(document).ready(function(){
    var ancho = $(window).width();    
    if (ancho <= 1350){
        $('html').css({
            'background-size': 'cover'
        });
    }

	$(window).scroll(function(){
		var barra = $(window).scrollTop();
		var posicion = barra * 0.10;

		$('html').css({
			'background-position': '0 -' + posicion + 'px'
		});
	});

});