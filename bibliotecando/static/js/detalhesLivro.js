document.addEventListener('DOMContentLoaded', () => {
    const favoritoBtn = document.getElementById("favorito-btn");

    if (favoritoBtn) {
        favoritoBtn.addEventListener("click", () => {
            const favorito = favoritoBtn.getAttribute("data-favorito") === "true";

            fetch("", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: new URLSearchParams({ action: "toggle_favorito" })
            })
            .then(response => response.json())
            .then(data => {
                if (data.favorito) {
                    favoritoBtn.setAttribute("data-favorito", "true");
                    favoritoBtn.querySelector("img").src = "/static/svg/bookmark-filled.svg";
                } else {
                    favoritoBtn.setAttribute("data-favorito", "false");
                    favoritoBtn.querySelector("img").src = "/static/svg/bookmark.svg";
                }
            })
            .catch(error => console.error("Erro ao alternar favorito:", error));
        });
    }
});