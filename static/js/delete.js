function openDeleteModal(videoId, videoUrl) {
    document.getElementById('modalVideoId').value = videoId;
    document.getElementById('modalVideoUrl').value = videoUrl;
    document.getElementById('deleteModal').classList.add('active');
}

function closeDeleteModal() {
    document.getElementById('deleteModal').classList.remove('active');
}


window.addEventListener('click', function (e) {
    const modal = document.getElementById('deleteModal');
    if (e.target === modal) {
        closeDeleteModal();
    }
});

document.getElementById('deleteForm').addEventListener('submit', function () {
    const confirmBtn = document.getElementById('confirmDeleteBtn');
    confirmBtn.disabled = true;
    confirmBtn.innerHTML = `<span class="spinner"></span> Deleting...`;
});


