document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("form").addEventListener("submit", function() {
        setTimeout(() => {
            document.querySelector("input[name='nama']").value = "";
            document.querySelector("textarea[name='pesan']").value = "";
        }, 100); // Tunggu 100ms sebelum reset
    });
});
