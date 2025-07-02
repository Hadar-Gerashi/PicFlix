function markHomeForRefresh() {
    sessionStorage.setItem('needHomeRefresh', 'true');
}

document.addEventListener("DOMContentLoaded", function () {
    const profileForm = document.getElementById("profile-text-form");
    const profileTextarea = document.getElementById("profile_text");
    const saveTextBtn = document.getElementById("saveTextButton");
    const textStatus = document.getElementById("text-save-status");
    const textDisplay = document.getElementById("profile_text_display");
    let originalText = profileTextarea.value.trim();

    profileTextarea.addEventListener("input", () => {
        saveTextBtn.disabled = profileTextarea.value.trim() === originalText;
    });

    profileForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const userId = profileForm.dataset.userId;
        const newText = profileTextarea.value.trim();
        saveTextBtn.disabled = true;
        saveTextBtn.innerHTML = `<span class="spinner"></span> Saving...`;

        try {
            const response = await fetch(`/profile/${userId}/update_text`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ profile_text: newText })
            });

            if (!response.ok) throw new Error("Failed to save text");

            originalText = newText;
            saveTextBtn.innerHTML = `<i class="fas fa-save"></i> Save Text`;
            textDisplay.textContent = newText || 'No profile description yet.';
            textDisplay.classList.toggle('placeholder-text', !newText);
            textStatus.style.display = "block";
            setTimeout(() => textStatus.style.display = "none", 3000);
            markHomeForRefresh();
        } catch (err) {
            saveTextBtn.innerHTML = `<i class="fas fa-save"></i> Save Text`;
            alert("Error saving profile text.");
        }
    });


    const categoriesForm = document.getElementById("categories-form");
    const checkboxes = categoriesForm.querySelectorAll('input[type="checkbox"][name="categories"]');
    const saveCategoriesBtn = document.getElementById("saveCategoriesButton");
    const categoriesStatus = document.getElementById("save-status");

    let originalChecks = Array.from(checkboxes).map(cb => cb.checked);

    checkboxes.forEach((cb, i) => {
        cb.addEventListener("change", () => {
            const current = Array.from(checkboxes).map(c => c.checked);
            const changed = current.some((val, idx) => val !== originalChecks[idx]);
            saveCategoriesBtn.disabled = !changed;
        });
    });

    categoriesForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        saveCategoriesBtn.disabled = true;
        saveCategoriesBtn.innerHTML = `<span class="spinner"></span> Saving...`;

        const selected = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.value);

        try {
            const response = await fetch('/update_categories', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ categories: selected })
            });

            if (!response.ok) throw new Error("Failed to update categories");

            originalChecks = Array.from(checkboxes).map(cb => cb.checked);
            saveCategoriesBtn.innerHTML = `<i class="fas fa-save"></i> Save Categories`;
            categoriesStatus.style.display = 'block';
            setTimeout(() => categoriesStatus.style.display = 'none', 3000);
            markHomeForRefresh();
        } catch (err) {
            saveCategoriesBtn.innerHTML = `<i class="fas fa-save"></i> Save Categories`;
            alert("Error saving categories.");
        }
    });



    document.querySelectorAll('form[action="/upload_video"], form[action="/delete_video"], form[enctype="multipart/form-data"]').forEach(form => {
        form.addEventListener('submit', markHomeForRefresh);
    });
});



