document.addEventListener("DOMContentLoaded", function () {
    function handleFormSubmit(event, formId, endpoint) {
        event.preventDefault(); // Предотвращаем перезагрузку страницы

        const form = document.getElementById(formId);
        const formData = new FormData(form);
        const jsonData = Object.fromEntries(formData.entries());

        fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(jsonData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                location.reload(); // Перезагрузка после успешного входа/регистрации
            } else {
                alert("Ошибка: " + data.message);
            }
        })
        .catch(error => console.error("Ошибка:", error));
    }

    // Привязываем обработчики к формам
    const signInForm = document.getElementById("sign-in-form");
    if (signInForm) {
        signInForm.addEventListener("submit", function (event) {
            handleFormSubmit(event, "sign-in-form", "/api/sign-in");
        });
    }

    const regForm = document.getElementById("reg-form");
    if (regForm) {
        regForm.addEventListener("submit", function (event) {
            handleFormSubmit(event, "reg-form", "/api/register");
        });
    }
});