let errado=0;
let Ncompletos=0;

window.onload=()=>{
    element=document.getElementById('Contenedor');
    element.className+=" animated flipInX delay-1s";
    element.addEventListener('animationend',function(){
        element.className=element.className.replace(" animated","");
        element.className=element.className.replace(" flipInX","");
        element.className=element.className.replace(" delay-1s","");
    }); 
}

function Animar(){
    if(!event){
        event=window.event;
    }
    var element=(event.target || event.srcElement);
    element.className +=" animated rubberBand faster";
    element.addEventListener('animationend', function() { alTerminar(element)});
}

function alTerminar(element){
    element.className=element.className.replace(" animated","");
    element.className=element.className.replace(" rubberBand","");
    element.className=element.className.replace(" faster","");
}

function mostrarRegistro(){
    var mostrar=$('.Registro');
    mostrar[0].style.display="block";
    var ocultar=$('.Login');
    ocultar[0].style.display="none";
}

async function terminarRegistro(){
    await sleep(900);
    var mostrar=$('.Login');
    mostrar[0].style.display="block";
    $('#formReg')[0].reset();
    var ocultar=$('.Registro');
    ocultar[0].style.display="none";
}

/*Ayudas... */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/* validaciones registro */
function validar(event){
    if (!event) {
        event = window.event;
    }
    var objHtml = (event.target || event.srcElement);
    let palabra1="";
    let palabra2="";

    switch (objHtml.id) {
        case "nombresReg":
            palabra1=objHtml.value.substr(0,objHtml.value.indexOf(" "));
            palabra2=objHtml.value.substr(objHtml.value.indexOf(" "),objHtml.value.length);                            
            if(!objHtml.value.length<=0){
                if((palabra1.length > 3 | palabra2.length > 3)&&(palabra1.length<=15 && palabra2.length<=15)){
                    objHtml.className+=" correcto";
                    Ncompletos+=1;
                    errado-=1;  
                }else{
                    errado+=1;
                }
            }else{
                errado+=1;
            } 
            break;
        case "apellidosReg":
            palabra1=objHtml.value.substr(0,objHtml.value.indexOf(" "));
            palabra2=objHtml.value.substr(objHtml.value.indexOf(" "),objHtml.value.length);                            
            if(!objHtml.value.length<=0){
                if((palabra1.length > 3 | palabra2.length > 3)&&(palabra1.length<=15 && palabra2.length <=15)){
                    objHtml.className+=" correcto";  
                    Ncompletos+=1; 
                    errado-=1;  
                }else{
                    errado+=1;
                }            
            }else{
                errado+=1;
            }
            break;
        case "usuarioReg":
            if(!(objHtml.value.length<=2 | objHtml.value.length>8)){                
                objHtml.className+=" correcto"; 
                Ncompletos+=1;  
                errado-=1;
            }else{
                errado+=1;
            }
            break;
        case "contraseniaReg":
            var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
            var mediumRegex = new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
            if(strongRegex.test(objHtml.value)){
                objHtml.className+=" correcto";
                Ncompletos+=1;  
                errado-=1;
            }else if(mediumRegex.test(objHtml.value)){
                objHtml.className+=" medio";
                Ncompletos+=1; 
                errado-=1; 
            }else{
                errado+=1;
            }
            break;
        case "reContraseniaReg":
                let contrasenia=document.getElementById('contraseniaReg');              
            if(objHtml.value==contrasenia.value){
                objHtml.className+=" correcto";
                Ncompletos+=1;
                errado-=1;  
            }else{
                errado+=1;
            }
            break;
        case "emailReg":
            if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(objHtml.value)){
                objHtml.className+=" correcto";
                Ncompletos+=1;  
                errado-=1;
            }else{
                errado+=1;
            }
        break;
    } 
    /* se suma 1 por que no se ha validado la fecha por el momento. Pero deberían ser 7 Ncompletos
    para poder "enviar" el registro*/
    Ncompletos+=1;
}

function subir(){
    limpiarDeValidacion();
    if(errado > 0 |  Ncompletos < 7){
        alert('Revise lo marcado en rojo...');                
    }else {
        terminarRegistro();
        Animar();        
    }
    errado=0;
    Ncompletos=0;      
}

function limpiarDeValidacion(){
    var elemento=document.getElementById('nombresReg');
    elemento.className=elemento.className.replace("correcto","");

    elemento=document.getElementById('apellidosReg');
    elemento.className=elemento.className.replace("correcto","");

    elemento=document.getElementById('usuarioReg');
    elemento.className=elemento.className.replace("correcto","");

    elemento=document.getElementById('contraseniaReg');
    elemento.className=elemento.className.replace("correcto","");
    elemento=document.getElementById('contraseniaReg');
    elemento.className=elemento.className.replace("medio","");

    elemento=document.getElementById('reContraseniaReg');
    elemento.className=elemento.className.replace("correcto","");

    elemento=document.getElementById('emailReg');
    elemento.className=elemento.className.replace("correcto","");
}