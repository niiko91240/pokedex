
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
var grid = document.getElementById('container2v');
var idTeam = 0; 

function afficherPokemon(id){
  idTeam = id
  modal.style.display = "block";
}

function selectPokemon(idPokemon){
  console.log(idTeam)
  console.log(idPokemon)
  const csrftoken = getCookie('csrftoken');
  $.ajax({
    type: 'POST',
    url: "/pokedexapp/addPokemon/",
    headers: {'X-CSRFToken': csrftoken},
    data : { 'idTeam': idTeam, 'idPokemon': idPokemon},
    csrfmiddlewaretoken: '{{ csrf_token }}',
    success : function(json) {
        $("#request-access").hide();
        console.log("requested access complete");
    }
  })
  document.location.reload(true)
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$(document).ready(function(){
    $("#searchTeam").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#listeTeam > div").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });


  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

