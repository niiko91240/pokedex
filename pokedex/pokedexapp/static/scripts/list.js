var names = document.getElementsByClassName('pokemon-nom')
var types = document.getElementsByTagName('button')
var croix = document.getElementById('croix')
if(document.getElementById('search2').value != ''){
  croix.style.display = 'block'
}


$(document).ready(function(){
    $("#search").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#listePokemon a").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

  $(document).ready(function(){
    $("#search2").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      if(value!=''){
        croix.style.display = 'block'
      } else {
        croix.style.display = 'none'
      }
    });
  });

  function vider(){
    document.getElementById('search2').value = ''
  }