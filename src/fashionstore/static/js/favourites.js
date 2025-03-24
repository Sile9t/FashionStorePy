setSelectOneSizeValue();
hideAddToCartBtns();

function setSelectOneSizeValue(){
    let selects = document.getElementsByTagName('select');
    
    for (let select of selects) {
        if (select.disabled) {
            select.value = 'OneSize';
            let valueText = select.options[select.options.length - 1].innerText;
            select.title = valueText;
        }
    }
}

function hideAddToCartBtns() {
    let btns = document.getElementsByClassName('add-to-cart-btn');

    for (let btn of btns) {
        if (btn.classList.contains('visually-hidden')) {
            let card = btn.parentElement;
            let removeBtn = card.getElementsByClassName('remove-from-cart-btn')[0];
            removeBtn.classList.remove('visually-hidden');
        }
    }
}