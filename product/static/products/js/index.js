const searchInput = document.getElementById("search_product")
const labelSearch = document.querySelector(".label_search")

searchInput.addEventListener('focus', ()=>{
    labelSearch.style.borderColor = "#007bff";
    labelSearch.style.boxShadow = "0 0 0 3px rgba(38, 143, 255, 0.25)";
})

searchInput.addEventListener('blur', ()=>{
    labelSearch.style.borderColor = "#0c0c0c";
    labelSearch.style.boxShadow = "none";
})


document.querySelectorAll('.category-form').forEach(form => {
    form.addEventListener('click', (event) => {
        event.preventDefault()
        form.submit()
    })
})


// close the side navbar when the modal for login is open
var modalElement = document.getElementById('exampleModal');
var offcanvasElement = document.getElementById('offcanvasRight');

var offcanvas = new bootstrap.Offcanvas(offcanvasElement);

modalElement.addEventListener('show.bs.modal', function () {
    // Verifica se o offcanvas está visível e o fecha
    if (offcanvasElement.classList.contains('show')) {
        offcanvas.hide();
    }
});