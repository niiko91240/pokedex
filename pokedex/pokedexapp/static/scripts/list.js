var names = document.getElementsByClassName('pokemon-nom')
var types = document.getElementsByTagName('button')


function search() {
    var search = document.getElementById('search')
    if(search.value == ""){
        for (let index = 1; index < 152; index++) {
            document.getElementById('case-'+index).style.display = "block"; 
        }
    } else {
        for (let index = 1; index < 152; index++) {
            document.getElementById('case-'+index).style.display = "none"; 
        }
        var tabId = []
        for (const name of names) {
            if(name.textContent.includes(search.value.toLowerCase())){
                tabId.push(name.id)
            }
        }
        for (const type of types) {
            if(type.textContent.includes(search.value.toUpperCase())){
                tabId.push(type.id)
            }
        }
        tabId.forEach(x => {
            document.getElementById('case-'+x).style.display = "block"; 
        });
    }
}