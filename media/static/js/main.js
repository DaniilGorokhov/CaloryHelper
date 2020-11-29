//Кнопка меняет цвет, если поля заполнены
let pass = document.querySelector('.password');
var login = document.querySelector('.login');

if (pass && login) {
    pass.addEventListener('input', changeBackground);
    login.addEventListener('input', changeBackground);
}
function changeBackground() {
    if (pass.value !== '' && login.value !== '') {
        document.querySelector('.reviews__button').style.opacity = '1';
    } else {
        document.querySelector('.reviews__button').style.opacity = '0.6';
    }
}

var place = document.querySelector('.place');

function changeBackground2() {
    if (place.value !== '') {
        document.querySelector('.reviews__button').style.opacity = '1';
    } else {
        document.querySelector('.reviews__button').style.opacity = '0.6';
    }
}

if (place) {
    place.addEventListener('input', changeBackground2);
}



//После загрузки файла меняется надпись
var inputs = document.querySelectorAll( '.inputfile' );
if (inputs) {
    Array.prototype.forEach.call(inputs, function (input) {
        var label = input.nextElementSibling,
            labelVal = label.innerHTML;

        input.addEventListener('change', function (e) {
            var fileName = '';
            fileName = "Изменить";

            if (fileName)
                label.querySelector('span').innerHTML = fileName;
            else
                label.innerHTML = labelVal;
        });
    });
}
