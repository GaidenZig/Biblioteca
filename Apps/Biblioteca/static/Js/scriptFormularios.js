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

/* validaciones registro */
function validar(event){
    if (!event) {
        event = window.event;
    }
    var objHtml = (event.target || event.srcElement);
    let palabra1="";
    let palabra2="";

    switch (objHtml.id) {
        case "usuarioReg":
            if(!(objHtml.value.length<=2 | objHtml.value.length>8)){
                if(objHtml.classList.contains('errado')){
                    objHtml.className=objHtml.className.replace("errado","correcto");
                }
            }else{
                if(objHtml.classList.contains('correcto')){
                    objHtml.className=objHtml.className.replace("correcto","errado");
                } 
            }
            break;
        case "contraseniaReg":
            var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
            var mediumRegex = new RegExp("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})");
            if(strongRegex.test(objHtml.value)){
                if(objHtml.classList.contains('errado')){
                    objHtml.className=objHtml.className.replace("errado","correcto");
                }else if(objHtml.classList.contains('medio')){
                    objHtml.className=objHtml.className.replace("medio","correcto");
                }
            }else if(mediumRegex.test(objHtml.value)){
                if(objHtml.classList.contains('errado')){
                    objHtml.className=objHtml.className.replace("errado","medio");
                }else if(objHtml.classList.contains('correcto')){
                    objHtml.className=objHtml.className.replace("correcto","medio");
                }
            }else{
                if(objHtml.classList.contains('correcto')){
                    objHtml.className=objHtml.className.replace("correcto","errado");
                }else if(objHtml.classList.contains('medio')){
                    objHtml.className=objHtml.className.replace("medio","errado");
                }
            }
            break;
        case "reContraseniaReg":
                let contrasenia=document.getElementById('contraseniaReg');              
            if(objHtml.value==contrasenia.value){                
                if(objHtml.classList.contains('errado')){
                    objHtml.className=objHtml.className.replace("errado","correcto");
                }
            }else{
                if(objHtml.classList.contains('correcto')){
                    objHtml.className=objHtml.className.replace("correcto","errado");
                } 
            }
            break;
        case "emailReg":
            if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(objHtml.value)){
                if(objHtml.classList.contains('errado')){
                    objHtml.className=objHtml.className.replace("errado","correcto");
                }
            }else{
                if(objHtml.classList.contains('correcto')){
                    objHtml.className=objHtml.className.replace("correcto","errado");
                } 
            }
        break;
    } 

    if(validarInputs()==true){
        document.getElementById('botonReg').disabled=true;
    }else{
        document.getElementById('botonReg').disabled=false;
    }
    console.log(document.getElementById('botonReg').disabled);
}

function subir(){
    Animar();
    reiniciarInputs();
}

function reiniciarInputs(){
    let inputs=document.getElementsByClassName('entrada');
    for(let element of inputs){
        if(element.classList.contains('correcto')){
            element.className=elemento.className.replace("correcto","errado");
        }
        else if(element.classList.contains('medio')){
            element.className=elemento.className.replace("medio","errado");
        }
    }
    document.getElementById('botonReg').disabled=true;
}

function validarInputs(){
    let falla=false;
    let inputs=document.getElementsByClassName('entrada');
    for (let element of inputs){
        let clase=element.classList.contains('errado');
        if(clase){
            falla=true;
        }
    }

    return falla;
}