document.addEventListener("DOMContentLoaded", function () {
    const videoForm = document.querySelector('form[action="/upload_video"]');
    const uploadBtn = document.getElementById('uploadBtn');

    if (videoForm && uploadBtn) {
        let clicked = false;

        uploadBtn.addEventListener('click', function () {
            clicked = true;
        });

        videoForm.addEventListener("submit", function (e) {


            const fileInput = videoForm.querySelector('input[type="file"]');
            const selectedCategories = videoForm.querySelectorAll('input[name="category_id[]"]:checked');

            if (!fileInput.files.length) {
                e.preventDefault();
                alert("Please select a video file before uploading.");
                return;
            }

            if (selectedCategories.length === 0) {
                e.preventDefault();
                alert("Please select at least one category.");
                return;
            }


            uploadBtn.classList.add('waiting');
            uploadBtn.innerHTML = `<span class="spinner"></span> Uploading video...`;
        });
    }
});
