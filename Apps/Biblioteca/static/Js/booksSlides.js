function sendBook(titulo){
    window.location="{% url 'Biblioteca:libro' 0 %}".replace(/0/,titulo);

}