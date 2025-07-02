document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('.file-upload-section');
    const fileInput = document.getElementById('profileImageInput');
    const updateBtn = document.getElementById('updateImageButton');
    const removeBtn = form.querySelector('button[value="remove"]');

    let clickedButton = null;

    form.querySelectorAll('button[type="submit"]').forEach(button => {
        button.addEventListener('click', function () {
            clickedButton = this.getAttribute('value');
        });
    });

    form.addEventListener('submit', function (e) {
        if (clickedButton === 'update') {
            if (!fileInput.files.length) {
                e.preventDefault();
                alert("Please select an image before uploading.");
                return;
            }

            updateBtn.classList.add('waiting');
            updateBtn.innerHTML = `<span class="spinner"></span> Update Image...`;
        }

        if (clickedButton === 'remove') {
            removeBtn.classList.add('waiting');
            removeBtn.innerHTML = `<span class="spinner"></span> Remove Image...`;
        }
    });
});

