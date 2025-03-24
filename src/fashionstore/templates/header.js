document.addEventListener("DOMContentLoaded", function () {
    function handleFormSubmit(event, formId, endpoint) {
        event.preventDefault(); // ������������� ������������ ��������

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
                location.reload(); // ������������ ����� ��������� �����/�����������
            } else {
                alert("������: " + data.message);
            }
        })
        .catch(error => console.error("������:", error));
    }

    // ����������� ����������� � ������
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