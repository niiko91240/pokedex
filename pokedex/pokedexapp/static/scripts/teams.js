$(document).ready(function(){
    $("#searchTeam").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#listeTeam > div").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });