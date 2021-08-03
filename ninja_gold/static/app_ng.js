$(document).ready(function () {
    const acciones = document.getElementById('acciones');
    acciones.scrollTo(0, acciones.scrollHeight);

   valor = int(request.GET["log"])

   if (valor > 0){
       $('.color').css('color','#77FF33')
   }
   else if (valor == 0){
    $('.color').css('color','#33D4FF')
   }
   else{
    $('.color').css('color','#FF333F')
   }



})