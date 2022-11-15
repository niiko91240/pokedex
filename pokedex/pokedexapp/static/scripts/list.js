var names = document.getElementsByClassName('pokemon-nom')
var types = document.getElementsByTagName('button')



$(document).ready(function(){
    $("#search").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#listePokemon a").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });