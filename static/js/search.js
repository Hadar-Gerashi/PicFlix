const input = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");
const searchContainer = document.querySelector('.search-container');
const spinner = document.getElementById("searchSpinner"); // ✅ נוסיף את זה

input.addEventListener("input", function () {
    const query = input.value;
    if (query.length === 0) {
        suggestionsBox.innerHTML = "";
        suggestionsBox.style.display = 'none';
        spinner.style.display = 'none';
        return;
    }

    spinner.style.display = 'block'; // ✅ מציגים את הספינר

    fetch(`/search_users?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            spinner.style.display = 'none'; // ✅ מסתירים את הספינר
            const users = data.users;
            suggestionsBox.innerHTML = "";

            if (users.length === 0) {
                suggestionsBox.innerHTML = '<div class="suggestion-item">No results found</div>';
            } else {
                users.forEach(user => {
                    const div = document.createElement("div");
                    div.classList.add("suggestion-item");

                    div.innerHTML = `
                        <div style="width: 30px; height: 30px; background: linear-gradient(45deg, #ff0050, #ff4080); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">
                            ${user.name.charAt(0)}
                        </div>
                        <div>
                            <div style="font-weight: 500;">${user.name}</div>
                            <div style="font-size: 12px; color: rgba(255,255,255,0.6);">@${user.name.toLowerCase().replace(' ', '_')}</div>
                        </div>
                    `;

                    div.onclick = () => {
                        input.value = user.name;
                        suggestionsBox.innerHTML = "";
                        suggestionsBox.style.display = 'none';
                        window.location.href = `/profile/${user.id}`;
                    };

                    suggestionsBox.appendChild(div);
                });
            }

            suggestionsBox.style.display = 'block';
        })
        .catch(err => {
            spinner.style.display = 'none'; // ✅ במקרה של שגיאה
            console.error("Search error:", err);
            suggestionsBox.innerHTML = '<div class="suggestion-item" style="color: #ff6b6b;">Search error</div>';
            suggestionsBox.style.display = 'block';
        });
});
