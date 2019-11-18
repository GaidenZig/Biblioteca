$(document).ready(function(){
    var ancho = $(window).width();    
    if (ancho <= 1350){
        $('html').css({
            'background-size': 'initial'
        });
    }

	$(window).scroll(function(){
		var barra = $(window).scrollTop();
		var posicion = barra * 0.15;

		$('html').css({
			'background-position': '0 -' + posicion + 'px'
		});
	});

});