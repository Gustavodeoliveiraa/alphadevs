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


// sending the form for delete an produto of Cart Shop
// var deleteButton = document.querySelectorAll('.button-delete-product')
// var formDelete = document.getElementById('form-delete')


// deleteButton.forEach((buttons)=>{
//     buttons.addEventListener('click', (event)=>{
//         event.preventDefault()
        
//         // get the correctly id of form  associated at the button clicked
//         var formId = buttons.getAttribute('data-form-id')
//         var formDelete = document.getElementById(formId)
//         formDelete.submit()
        
//     })
// })

var confirmButtons = document.querySelectorAll('.button-delete-product');

confirmButtons.forEach((button) => {
    button.addEventListener('click', (event)=>{
        console.log(event.currentTarget);
        var formId = event.currentTarget.getAttribute('form-id');
        var form = document.getElementById(formId)
        form.submit()
        
    })
})


