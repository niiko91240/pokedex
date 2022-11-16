
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
var grid = document.getElementById('container2');

function afficherPokemon(){
    modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function createTeam(){
  grid.innerHTML += '<div class="case"><p>Equipe 1</p><div class="circle" id="add-pokemon" onclick="afficherPokemon();"><img src="/static/images/plus-solid.svg"></div><div class="circle" id="add-pokemon" onclick="afficherPokemon();"><img src="/static/images/plus-solid.svg"></div><div class="circle" id="add-pokemon" onclick="afficherPokemon();"><img src="/static/images/plus-solid.svg"></div><div class="circle" id="add-pokemon" onclick="afficherPokemon();"><img src="/static/images/plus-solid.svg"></div><div class="circle" id="add-pokemon" onclick="afficherPokemon();"><img src="/static/images/plus-solid.svg">></div><img class="trash" src="/static/images/trash-can-regular.svg"></div>'
}

$(document).ready(function(){
    $("#searchTeam").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#listeTeam > div").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

