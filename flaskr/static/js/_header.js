(function(fn) {
	'use strict';
	fn(window.jQuery, window, document);
}(function($, window, document) {
	'use strict';
	
	setFuncToAllExt();
}));

function setFuncToAllExt() {
	let btnsList = document.getElementsByClassName('collapse-btn');
	
	for (btn of btnsList){
		btn.addEventListener('click', () => hideAllExtensionsAndOpenRequired(btn));
	}
}

function hideAllExtensionsAndOpenRequired(clickedBtn) {
	let extList = document.getElementsByClassName('collapse');
	
	for (ext of extList){
		if (ext.classList.contains('show')) {
			let collapse = bootstrap.Collapse.getInstance(ext);
			collapse.hide();
		}
	}
}

let userIsLogged = document.getElementById('userIsLogged').value;
let profileBtn = document.getElementById('profile');
// profileBtn.addEventListener('click', profileBtnClick);
profileBtnClick();

function profileBtnClick() {
	if (userIsLogged === 'true') {
		profileBtn.setAttribute('data-bs-toggle', 'dropdown');
		profileBtn.setAttribute('data-bs-target', '#profileModal');
		profileBtn.getElementsByClassName('text-info')[0].classList.remove('visually-hidden');
	}
}

let signBtn = document.getElementById('sign-in-btn');
let regBtn = document.getElementById('reg-btn');

function showForm(e) {
	let signForm = document.getElementById('sign-in-form');
	let regForm = document.getElementById('reg-form');

	if (e == regBtn) {
		signBtn.classList.remove('selected');
		regBtn.classList.add('selected');
		signForm.classList.add('visually-hidden');
		regForm.classList.remove('visually-hidden');
	}
	else if (e == signBtn) {
		signBtn.classList.add('selected');
		regBtn.classList.remove('selected');
		signForm.classList.remove('visually-hidden');
		regForm.classList.add('visually-hidden');
	}
}